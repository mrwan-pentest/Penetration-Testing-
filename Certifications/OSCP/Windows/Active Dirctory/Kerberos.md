## Overview

**Kerberos** is an authentication protocol used by **Active Directory** to verify the identity of users and provide access to services.

The main idea behind Kerberos is simple:

> Instead of sending your password every time you want to access a service, Kerberos uses **Tickets** to prove that you are authenticated.

For example, imagine a Domain:

```
corp.local
```

And a user:

```
Alice
```

Alice wants to access a file server:

```
\\FILE01\Shared
```

Instead of sending:

```
Username + Password
```

directly to the File Server, Kerberos handles the authentication and provides Alice with a **Ticket** that the File Server can trust.

---

# Why Does Kerberos Use Tickets?

Imagine you log into your Domain in the morning.

During the day, you might access:

- File Servers
- SQL Servers
- LDAP
- Web Applications
- Other Domain Services

It would be inefficient and insecure to send your password to every service.

Kerberos solves this by authenticating you once and then giving you a **TGT**.

The TGT can then be used to request tickets for individual services.

```
Login
  ↓
Get TGT
  ↓
Request Service Ticket
  ↓
Access Service
```

So your password is not repeatedly sent to every service.

---

# Main Components

## KDC

The **KDC (Key Distribution Center)** is the central part of Kerberos.

In an Active Directory environment, the **Domain Controller** runs the KDC.

The KDC contains two important services:

### Authentication Service (AS)

The **AS** handles the initial authentication and provides the user with a:

**TGT (Ticket Granting Ticket)**

### Ticket Granting Service (TGS)

The **TGS** receives a valid TGT and uses it to issue a **Service Ticket** for a specific service.

So:

```
Domain Controller
       │
       └── KDC
            │
            ├── AS
            │
            └── TGS
```

---

# How Kerberos Authentication Works

Let's use a simple example.

We have:

```
User: Alice
Domain: corp.local
Domain Controller: DC01
Service: File Server
```

Alice wants to access the File Server.

---

## Step 1 — User Authentication

Alice logs into the Domain.

Her credentials are verified by the Domain Controller.

After successful authentication, the **Authentication Service (AS)** provides Alice with a:

```
TGT
```

**TGT = Ticket Granting Ticket**

You can think of the TGT as:

> "The Domain has verified Alice, and this ticket proves that she has been authenticated."

The important point is that the TGT is **not a ticket for the File Server specifically**.

It is used to request other tickets.

```
Alice
  ↓
Authentication Service (AS)
  ↓
TGT
```

---

# Step 2 — Request a Service Ticket

Now Alice wants to access:

```
File Server
```

She does not send her password to the File Server.

Instead, she takes her TGT to the:

```
Ticket Granting Service (TGS)
```

and requests a ticket for the File Server.

The TGS checks the TGT.

If everything is valid, the TGS gives Alice a:

**Service Ticket**

```
Alice
  ↓
TGT
  ↓
TGS
  ↓
Service Ticket
```

This ticket is specifically intended for the requested service.

---

# Step 3 — Access the Service

Alice now presents the **Service Ticket** to the File Server.

The File Server validates the ticket.

If it is valid:

```
Access Granted
```

The complete process is therefore:

```
Alice
  │
  │ Authentication
  ↓
  AS
  │
  │ TGT
  ↓
  TGS
  │
  │ Service Ticket
  ↓
File Server
  │
  ↓
Access Granted
```

---

# TGT vs Service Ticket

This distinction is extremely important.

### TGT

**Ticket Granting Ticket**

Its purpose is:

> "I am authenticated and can request tickets for services."

It is not normally used directly to access the File Server.

### Service Ticket

Its purpose is:

> "I am authorized to communicate with this specific service."

For example:

```
TGT
 ↓
Request ticket for SQL
 ↓
SQL Service Ticket
```

Or:

```
TGT
 ↓
Request ticket for File Server
 ↓
File Server Service Ticket
```

So you can think of it like this:

```
TGT
 │
 ├──→ SQL Service Ticket
 │
 ├──→ File Server Service Ticket
 │
 ├──→ LDAP Service Ticket
 │
 └──→ HTTP Service Ticket
```

---

# What Is an SPN?

You will encounter **SPN** frequently when studying Active Directory attacks.

**SPN = Service Principal Name**

An SPN identifies a specific service associated with an account in Active Directory.

For example:

```
MSSQLSvc/SQL01.corp.local:1433
```

This tells us that an SQL Server service is running on:

```
SQL01.corp.local
```

using port:

```
1433
```

Kerberos uses SPNs to determine which account is responsible for a particular service.

---

# Why Are SPNs Important for Pentesting?

SPNs are especially important because they are related to:

## Kerberoasting

Suppose we have a Domain account running a service:

```
SQLService
```

and that account has an SPN.

A normal Domain user can potentially request a Service Ticket for that SPN.

The resulting ticket contains information that can be taken offline and subjected to password cracking.

The general idea is:

```
Domain User
     ↓
Request Service Ticket
     ↓
Kerberos
     ↓
Service Ticket
     ↓
Offline Cracking
     ↓
Potential Service Account Password
```

The important point is:

> **Kerberoasting does not break Kerberos itself. It abuses the normal Kerberos process of requesting Service Tickets.**

---

# Important Kerberos Attacks

You will encounter several Kerberos attacks during Active Directory penetration testing.

### Kerberoasting

Targets accounts associated with **SPNs**.

```
SPN
 ↓
Request TGS
 ↓
Obtain ticket material
 ↓
Offline password cracking
```

### AS-REP Roasting

Targets accounts configured without Kerberos **pre-authentication**.

```
User
 ↓
AS-REP
 ↓
Obtain authentication material
 ↓
Offline cracking
```

### Pass-the-Ticket

Instead of obtaining the user's password, an attacker uses a stolen Kerberos **Ticket**.

```
Stolen Ticket
      ↓
Pass-the-Ticket
      ↓
Authenticate as the ticket's user
```

### Golden Ticket

This is a more advanced attack involving the **KRBTGT** account.

If an attacker obtains the necessary secret associated with `KRBTGT`, they can potentially forge Kerberos TGTs.

---

# Kerberos vs NTLM

You will often see these two together when studying Active Directory:

```
Kerberos
NTLM
```

Both are authentication mechanisms, but they work differently.

### Kerberos

Main concept:

```
Tickets
```

```
Authentication
     ↓
TGT
     ↓
Service Ticket
     ↓
Service
```

### NTLM

Main concept:

```
Challenge → Response
```

This is why you'll encounter different types of attacks:

```
Kerberos → Kerberoasting / AS-REP Roasting / Pass-the-Ticket
```

and:

```
NTLM → NTLM Hashes / Net-NTLMv2 / Pass-the-Hash
```

---

# The Mental Model to Remember

Don't try to memorize every Kerberos detail at once.

Remember this story:

> **I log into the Domain → Kerberos authenticates me → I receive a TGT → I use the TGT to ask the TGS for a ticket → I receive a Service Ticket → I use that ticket to access the service.**


## Key Terms

|Term|Meaning|
|---|---|
|**Kerberos**|Authentication protocol|
|**KDC**|Kerberos server running on the Domain Controller|
|**AS**|Authentication Service|
|**TGS**|Ticket Granting Service|
|**TGT**|Ticket Granting Ticket|
|**Service Ticket**|Ticket used to access a specific service|
|**SPN**|Identifies a service associated with an AD account|
|**KRBTGT**|Special AD account involved in Kerberos ticket issuance|

> **The most important thing for Active Directory pentesting is understanding the relationship: `TGT → TGS → Service Ticket`, and then connecting SPNs to attacks such as Kerberoasting.**
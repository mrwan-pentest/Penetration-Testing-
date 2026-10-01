## Overview

**Kerberoasting** is a **post-authentication Kerberos attack** that targets **Service Accounts associated with SPNs (Service Principal Names)** in an Active Directory environment.

To understand the attack, we first need to understand why **SPNs** are important. An SPN identifies a particular service and is associated with the **Domain Account** that runs that service. For example:

```
MSSQLSvc/SQL01.lab.local:1433
```

This tells Kerberos that the SQL service on `SQL01` is associated with a particular account, such as `sqlservice`.

When a Domain user wants to access a Kerberos-authenticated service, they normally request a **Service Ticket** from the **KDC's Ticket Granting Service (TGS)**. The KDC generates this ticket using information associated with the account that owns the SPN.

This normal Kerberos process is what **Kerberoasting** takes advantage of.

An attacker who already has **valid Domain credentials** can enumerate accounts with SPNs and request **Service Tickets** for those services. The attacker does not need the Service Account's password to request the ticket.

The returned **TGS material** contains encrypted data that can be attacked **offline**. Because the encryption is tied to the secret/key of the Service Account, an attacker can use tools such as **Hashcat** to test password guesses without repeatedly communicating with the Domain Controller.


The important distinction from **AS-REP Roasting** is that Kerberoasting does **not** require the account to have Kerberos Preauthentication disabled.

### Why Service Accounts Are Important

Service Accounts can be particularly interesting targets because they are often used to run applications and network services. In some environments, their passwords may remain unchanged for long periods or may not meet strong password requirements.

If the Service Account's password is weak enough to be cracked, recovering it gives us **valid credentials for that account**. What we can do with those credentials then depends on the permissions assigned to the account and the services or systems it can access.

---

# Lab

## Step 1: Identify Users with SPNs

First, we use **GetUserSPNs** to enumerate accounts that have **SPNs**.

We provide valid Domain credentials because we need to authenticate to the Domain:

```
impacket-GetUserSPNs -dc-ip 192.168.227.139 lab.local/user1:'12345l**'
```

![](../../../../Images/Pasted%20image%2020260928014444.png)

The output shows the accounts associated with SPNs.

These accounts can potentially be targeted for **Kerberoasting**.

---

## Step 2: Request the Service Ticket

Once we identify an account with an SPN, we can request its **Service Ticket** using the `-request` option:

```
impacket-GetUserSPNs -dc-ip 192.168.227.139 lab.local/user1:'12345l**' -request
```

![](../../../../Images/Pasted%20image%2020260928014533.png)

The command requests the **TGS (Service Ticket)** associated with the SPN and returns the material in a format that can be used for offline password cracking.

The important point is that we are not directly requesting the user's password or NTLM hash.

We are requesting a **Service Ticket as a legitimate Kerberos operation**, then using the returned encrypted material for cracking.

---

## Step 3: Crack the Hash

After obtaining the TGS material, we can use **Hashcat** with a wordlist:

```
hashcat hash3 /usr/share/wordlists/rockyou.txt
```

Here, we do not specify the Hashcat mode manually. Hashcat attempts to identify the hash type automatically.

![](../../../../Images/Pasted%20image%2020260928014801.png)

The hash was successfully cracked, giving us the **password of the targeted Service Account**.

---



# rpcclient

`rpcclient` is a tool from the **Samba suite** used for interacting with **Windows RPC services**.

Its main purpose is:

> Enumerate information from Windows systems through RPC (Remote Procedure Call).

It is commonly used during:

- **SMB Enumeration**
- **Windows Reconnaissance**
- **Active Directory Enumeration**

---

# What is RPC?

RPC = **Remote Procedure Call**

It allows a computer to:

```
Request services or information from another computer remotely
```

Windows uses RPC for many administrative tasks such as:

- User management
- Domain information
- System information
- Remote administration

---

# When do we use rpcclient?

Usually after discovering:

```
445/tcp open
```

or:

```
139/tcp open
```

because these ports indicate:

- SMB
- NetBIOS

are running.

Example:

```
nmap -p 139,445 target
```

If they are open, you can try RPC enumeration.

---

# Connecting to a Windows Machine

## 1. Null Session (No Credentials)

```
rpcclient -U "" -N 192.168.1.10
```

### Explanation:

|Part|Meaning|
|---|---|
|`rpcclient`|Run the tool|
|`-U ""`|Empty username|
|`-N`|Do not ask for password|
|IP|Target machine|

This tries anonymous access.

---

## 2. With Username and Password

```
rpcclient -U administrator 192.168.1.10
```

It will ask for the password.

Example:

```
Password:
```

Then you get an RPC shell:

```
rpcclient $
```

---

# Important rpcclient Commands

---

# 1. System Information

```
srvinfo
```

Shows information about the Windows machine.

Example output:

```
OS: Windows 10
Server Name: WORKSTATION01
```

Useful for knowing:

- Operating System
- Hostname
- Server information

---

# 2. Domain Information

```
lsaquery
```

Shows:

- Domain Name
- Domain SID

Example:

```
Domain Name: CORP
Domain SID: S-1-5-21-...
```

Useful during:

- Active Directory enumeration
- SID analysis

---

# 3. Enumerate Users

```
enumdomusers
```

One of the most important commands.

It lists users in the domain.

Example:

```
user:[Administrator] rid:[0x1f4]
user:[Guest] rid:[0x1f5]
user:[john] rid:[0x450]
```

You can discover:

- Usernames
- RIDs

This information can later help with:

- Password attacks
- User enumeration

---

# 4. Enumerate Groups

```
enumdomgroups
```

Lists available groups.

Example:

```
Domain Admins
Administrators
Users
Guests
```

Useful to identify privileged groups.

---

# 5. Get User Information

First get the user's RID:

From:

```
enumdomusers
```

Example:

```
Administrator rid:[0x1f4]
```

Then:

```
queryuser 0x1f4
```

Shows information about that user:

- Username
- Account status
- Last login
- Password information

---

# 6. Find SID of a User

```
lookupnames Administrator
```

Converts:

```
Username → SID
```

Example:

```
Administrator S-1-5-21-...
```

---

# 7. Find Username from SID

```
lookupsids S-1-5-21-...
```

Converts:

```
SID → Username
```

---

# Common Enumeration Workflow

A typical penetration testing workflow:

```
1. Scan ports
```

```
nmap -p 139,445 target
```

↓

```
2. Connect with rpcclient
```

```
rpcclient -U "" -N target
```

↓

```
3. Get system information
```

```
srvinfo
```

↓

```
4. Get domain information
```

```
lsaquery
```

↓

```
5. Enumerate users
```

```
enumdomusers
```

↓

```
6. Enumerate groups
```

```
enumdomgroups
```

---

# Why is rpcclient important for Pentesters?

Because it can reveal:

- Valid usernames
- Domain information
- User IDs (RID/SID)
- System details
- Misconfigured SMB/RPC permissions

This information is useful for:

- Password attacks
- Active Directory attacks
- Lateral Movement
- Privilege Escalation

---

# Quick Cheat Sheet

|Command|Purpose|
|---|---|
|`srvinfo`|System information|
|`lsaquery`|Domain information|
|`enumdomusers`|List users|
|`enumdomgroups`|List groups|
|`queryuser RID`|User details|
|`lookupnames USER`|Username → SID|
|`lookupsids SID`|SID → Username|

**In short:**

`rpcclient` = **A Windows RPC enumeration tool used to gather users, domains, SIDs, and system information through SMB/RPC.**
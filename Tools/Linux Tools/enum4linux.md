# 🔍 enum4linux

`enum4linux` is a tool used during the:

```
SMB Enumeration
```

phase.

Its main purpose is:

> To collect information from Windows machines through the SMB protocol.

Instead of manually using multiple tools like:

- `rpcclient`
- `smbclient`
- `net`

`enum4linux` automates many SMB enumeration tasks in one tool.

---

# Why do we use enum4linux?

Usually after discovering:

```
445/tcp open microsoft-ds
```

or:

```
139/tcp open netbios-ssn
```

with Nmap.

This means:

```
SMB service is running
```

Now we can use:

```
enum4linux TARGET
```

to gather information.

---

# What information can enum4linux collect?

## 1) User Enumeration

It can discover users on the Windows system.

Example:

```
Administrator
Guest
John
Bob
```

Command:

```
enum4linux -U TARGET
```

`-U` means:

```
Enumerate Users
```

---

# 2) Group Enumeration

It can discover Windows groups.

Examples:

```
Administrators
Domain Users
Remote Desktop Users
```

Command:

```
enum4linux -G TARGET
```

`-G` means:

```
Enumerate Groups
```

---

# 3) SMB Share Enumeration

It discovers available SMB shares.

Example:

```
\\TARGET\Public
\\TARGET\Backup
\\TARGET\Admin$
```

Command:

```
enum4linux -S TARGET
```

`-S` means:

```
Enumerate Shares
```

---

# 4) Operating System Information

It can collect information such as:

- Windows version
- Computer name
- Domain name
- Workgroup

Command:

```
enum4linux -o TARGET
```

`-o` means:

```
OS Information
```

---

# 5) Password Policy Enumeration

It can reveal password policies like:

- Minimum password length
- Password complexity requirements
- Account lockout policy

Command:

```
enum4linux -P TARGET
```

---

# 6) Domain Information

If the machine belongs to Active Directory, it can discover:

- Domain name
- Domain SID
- Domain information

---

# Null Session Enumeration

One important SMB technique is:

```
Null Session
```

Meaning:

> Connecting to SMB without providing username and password.

Example:

```
enum4linux -a TARGET
```

Sometimes you can retrieve information without authentication.

---

# The Most Common Option

## `-a`

Means:

```
All Enumeration
```

It runs multiple enumeration checks automatically.

Example:

```
enum4linux -a 192.168.1.10
```

It tries to collect:

- Users
- Groups
- Shares
- Password Policy
- OS Information
- Domain Information

---

# Using Credentials

If you have valid credentials:

```
enum4linux -u administrator -p password123 TARGET
```

Authenticated enumeration usually gives more information.

---

# Important Options

|Option|Function|
|---|---|
|`-a`|Full enumeration|
|`-U`|Enumerate users|
|`-G`|Enumerate groups|
|`-S`|Enumerate SMB shares|
|`-P`|Enumerate password policy|
|`-o`|Get OS information|
|`-u`|Username|
|`-p`|Password|

---

# Practical Example

First, scan the target:

```
nmap -p 139,445 192.168.1.10
```

Result:

```
445/tcp open microsoft-ds
```

Now run:

```
enum4linux -a 192.168.1.10
```

Possible output:

```
Users:
Administrator
john

Shares:
Public
Backup

OS:
Windows Server 2016
```

Now you know:

- Valid usernames
- Available shares
- Operating system version

This information can help with:

- Password attacks
- SMB exploitation
- Lateral movement
- Active Directory enumeration

---

# enum4linux vs smbmap

|Tool|Main Purpose|
|---|---|
|enum4linux|Discover SMB information (Users, Groups, Domain, OS)|
|smbmap|Check SMB shares and permissions|

Simple way to remember:

```
enum4linux = Who is the machine?
```

```
smbmap = What can I access?
```

---

# Summary

`enum4linux` is an SMB enumeration tool used to discover:

```
Users
Groups
Shares
Domains
Operating System Information
Password Policies
```

It is commonly used after finding:

```
139/tcp
445/tcp
```

during:

```
SMB Enumeration
```


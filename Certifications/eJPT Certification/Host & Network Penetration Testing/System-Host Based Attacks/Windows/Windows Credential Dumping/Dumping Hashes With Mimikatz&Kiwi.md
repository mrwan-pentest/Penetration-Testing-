# Mimikatz

## What is Mimikatz?

Mimikatz is a very popular post-exploitation tool used after gaining access to a Windows system.

Its main purpose is:

> Extracting authentication information from Windows systems.

It can be used to:

- Extract passwords
- Extract password hashes
- Extract Kerberos tickets
- Perform Pass-the-Hash attacks
- Perform Token Impersonation
- Access credentials stored in memory

In simple terms:

> Mimikatz searches Windows memory and system databases for authentication data.

---

# How Does Mimikatz Find Passwords?

To understand this, we need to understand:

# What is LSASS?

LSASS stands for:

```
Local Security Authority Subsystem Service
```

It is a Windows process:

```
lsass.exe
```

Responsible for:

- User authentication
- Login verification
- Managing security policies
- Handling NTLM authentication
- Handling Kerberos authentication
- Storing credentials temporarily in memory

Because Windows needs to authenticate users quickly, some credentials may exist temporarily in RAM.

This is where Mimikatz comes in 👀

It attempts to read the memory of:

```
lsass.exe
```

and extract:

- Passwords
- NTLM hashes
- Kerberos tickets

---

# What is SAM?

SAM stands for:

```
Security Account Manager
```

It is a Windows database that stores:

- User accounts
- Password hashes

The location is:

```
C:\Windows\System32\config\SAM
```

However, it cannot normally be accessed while Windows is running because the system locks it.

---

# Difference Between LSASS and SAM

| Component | Function |
|---|---|
| SAM | Stores local user password hashes |
| LSASS | Stores authentication credentials in memory during system operation |

---

# Kiwi

## What is Kiwi?

Kiwi is a Meterpreter extension based on Mimikatz.

Instead of uploading and running:

```
mimikatz.exe
```

you can load it directly inside Meterpreter:

```text
load kiwi
```

After loading Kiwi, Mimikatz functionality becomes available through Meterpreter commands.

---

# Dumping Hashes Using Kiwi

## Method 1

## Step 1: Load Kiwi

Load the Kiwi extension into the current Meterpreter session.

```text
load kiwi
```

![](../../../../../../Images/Pasted%20image%2020260520132134.png)

---

## Step 2: Dump All Hashes

To extract available password hashes:

```text
lsa_dump_sam
```

or:

```text
hashdump
```

![](../../../../../../Images/Pasted%20image%2020260520132156.png)

---

## Step 3: Extract SAM Hashes

To extract hashes stored inside the SAM database:

```text
lsa_dump_sam
```

![](../../../../../../Images/Pasted%20image%2020260520132223.png)

---

# Extracting SysKey

## What is SysKey?

SysKey means:

```
System Key
```

It is an old Windows security mechanism used to protect password hashes.

---

# How Does SysKey Work?

Windows does not store password hashes directly.

Instead:

```
Password Hash
        |
        ↓
Encrypted using SysKey
        |
        ↓
Stored inside SAM
```

---

# Relationship Between SAM, SysKey, and LSASS

## 1) SAM

Contains:

```
Password Hashes
```

---

## 2) SysKey

The encryption key that protects those hashes.

---

## 3) LSASS

The process responsible for:

- Authentication
- Managing credentials in memory

---

# Why Extract SysKey?

Some credential extraction tools require:

- SAM hive
- SYSTEM hive

to decrypt and recover password hashes.

Examples:

```
samdump2
secretsdump.py
```

![](../../../../../../Images/Pasted%20image%2020260520132622.png)

---

# Extracting Clear Text Passwords

After obtaining the required credential information, Mimikatz/Kiwi can attempt to retrieve clear-text passwords from memory.

Example:

```text
creds_all
```

![](../../../../../../Images/Pasted%20image%2020260520132759.png)

---

# Key Takeaways

- Mimikatz is a post-exploitation credential extraction tool.
- It targets two main areas:
  - **LSASS memory** → live credentials
  - **SAM database** → local password hashes
- Kiwi provides Mimikatz functionality inside Meterpreter.
- SysKey protects SAM hashes by encrypting them.
- Extracting credentials usually requires elevated privileges such as Administrator or SYSTEM.
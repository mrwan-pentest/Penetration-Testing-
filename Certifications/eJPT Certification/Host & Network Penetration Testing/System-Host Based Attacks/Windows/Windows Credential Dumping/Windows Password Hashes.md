# Windows Password Storage and Hashes

# Windows usually:

```
Does not store the real password
```

Instead, it stores:

```
Hash
```

---

# What is a Hash?

A Hash is:

```
Converting a password into a fixed-length value
```

For example:

```
password123
```

may become:

```
482c811da5d5b4bc6d497ffa98491e38
```

---

# Where does Windows store Hashes?

Usually inside:

```
SAM Database
```

---

# What is SAM?

SAM stands for:

```
Security Account Manager
```

It contains:

- User accounts
- Password Hashes

---

# Where is it located?

```
C:\Windows\System32\config\SAM
```

---

# Can it be opened directly? ❌

Usually no.

Because Windows locks it while the system is running.

Therefore, an attacker needs:

- SYSTEM privileges
- Or specialized tools

---

# Types of Hashes in Windows

## 1) LM Hash

Very old and weak.

---

# Why is it weak?

Because it:

- Converts characters to Uppercase.
- Splits the password into two parts.
- Is very easy to crack.

---

# Example:

```
PASSWORD
```

---

# Is it still used? ❌ Usually not

Modern systems:

```
Disable it
```

---

# 2) NTLM Hash

The most important and commonly used one.

---

# What is NTLM?

It stands for:

```
NT LAN Manager
```

---

# This is the Hash commonly used in:

- Pass-the-Hash
- SMB Authentication
- WinRM
- PsExec

---

# Example NTLM Hash:

```
b4b9b02e6f09a9bd760f388b67351e2b
```

---

# How does an attacker obtain Hashes?

After gaining access to:

```
Administrator or SYSTEM
```

They use tools such as:

- Mimikatz
- secretsdump
- hashdump
- reg save

---

# The second important source

The important one:

```
NTLM Hash
```

---

# How are Hashes also stolen?

From:

```
LSASS Memory
```

---

# What is LSASS?

It stands for:

```
Local Security Authority Subsystem Service
```

# What is its function?

It is a very important Windows process responsible for:

- Login management
- Authentication
- Password validation
- Security Tokens
- Kerberos
- NTLM
- User Sessions

# In simple words:

LSASS is:

```
The center responsible for managing login and permissions
```

---

# The famous tool

# Mimikatz

---

# Difference Between SAM and LSASS

## SAM

Contains:

```
Stored Hashes
```

---

## LSASS

Contains:

```
Live Credentials stored in memory
```
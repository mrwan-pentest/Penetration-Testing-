# SMB Enumeration Modules (Metasploit)

Metasploit provides several SMB modules that help gather information, enumerate users and shares, and perform authentication attacks.

---

## Identify the SMB Version

### Module

```text
auxiliary/scanner/smb/smb_version
```

This module identifies:

- SMB version
- Operating system
- Hostname
- SMB server information

It is usually the first module you should run during SMB enumeration.

---

## Display Module Information

To view details about the current module, use:

```text
info
```

This displays:

- Module description
- Required options
- Supported targets
- References
- Available actions

---

## Enumerate SMB Users

### Module

```text
auxiliary/scanner/smb/smb_enumusers
```

This module attempts to enumerate user accounts from the target SMB server.

It may reveal:

- Usernames
- Built-in accounts
- Domain users

This information is useful for password attacks and privilege enumeration.

---

## Enumerate SMB Shares

### Module

```text
auxiliary/scanner/smb/smb_enumshares
```

This module lists the shared folders available on the SMB server.

It helps identify:

- Shared directories
- Anonymous access
- Writable shares
- Sensitive file locations

---

## Perform an SMB Brute Force Attack

### Module

```text
auxiliary/scanner/smb/smb_login
```

This module performs an authentication attack against the SMB service.

It attempts multiple username and password combinations to discover valid credentials.

If successful, it returns:

- Valid username
- Valid password
- Authentication status
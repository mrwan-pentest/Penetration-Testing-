# smbmap

## What is smbmap?

`smbmap` is one of the most commonly used tools for:

```
SMB Enumeration
```

It is a lightweight and fast tool that helps penetration testers identify:

- Available SMB Shares
- Share permissions
- Read access
- Write access
- Possible file operations

It can also support some remote actions depending on the available permissions.

---

# What is the Idea Behind smbmap?

Instead of manually connecting to SMB Shares using:

```
smbclient
```

`smbmap` performs SMB Enumeration automatically and presents the results in an organized way.

It allows you to quickly identify:

- Accessible shares.
- Available permissions.
- Potential attack opportunities.

---

# Basic Usage

To perform a basic SMB scan:

```
smbmap -H TARGET
```

Example:

```
smbmap -H 10.10.10.5
```

---

# What Does It Do?

The command attempts to enumerate SMB Shares and discover available resources.

By default, it may attempt access using:

```
Anonymous Authentication
```

if the SMB server allows it.

---

# Understanding smbmap Output

`smbmap` displays the permissions available for each share.

|Permission|Meaning|
|---|---|
|`READ ONLY`|The user can only read files|
|`READ, WRITE`|The user can read and upload/modify files|
|`NO ACCESS`|The user cannot access the share|

---

# Authentication with Username and Password

If valid credentials are available, they can be provided using:

```
smbmap -H TARGET -u admin -p password123
```

Options:

- `-H` → Target IP address or hostname.
- `-u` → Username.
- `-p` → Password.

---

# Pass-the-Hash

`smbmap` supports authentication using NTLM Hashes.

Example:

```
smbmap -H TARGET -u administrator -p HASH
```

Some versions may use:

```
--hashes
```

for specifying hashes.

Pass-the-Hash allows authentication using an NTLM Hash instead of the actual password.

---

# Listing Files Inside a Share

To recursively list files inside a specific SMB Share:

```
smbmap -H TARGET -r public
```

Option:

```
-r
```

means:

```
Recursive listing
```

It displays files and directories inside the selected share.

---

# Downloading Files

To download a file from an SMB Share:

```
smbmap -H TARGET --download "public/passwords.txt"
```

This retrieves the specified file from the SMB Share.

---

# Uploading Files

If the current user has write permissions, files can be uploaded:

```
smbmap -H TARGET --upload shell.exe "public/shell.exe"
```

This uploads:

```
shell.exe
```

to:

```
public/shell.exe
```

inside the SMB Share.

---

# Summary

`smbmap` is a fast SMB Enumeration tool used during Windows and Active Directory assessments.

Common uses:

- Discovering SMB Shares.
- Identifying permissions.
- Finding readable and writable locations.
- Downloading files.
- Uploading files when write access is available.
- Supporting credential-based and Pass-the-Hash authentication.

It is commonly used in the enumeration phase to identify possible SMB attack paths.
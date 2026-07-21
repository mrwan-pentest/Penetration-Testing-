# smbclient

**smbclient** is a command-line tool used to interact with:

```
SMB (Server Message Block)
```

services on Windows/Linux systems.

It works like:

```
FTP client
```

but for:

```
SMB Shares
```

---

# What does smbclient do?

It allows you to:

- Enumerate SMB Shares
- Connect to shared folders
- Upload files
- Download files
- Browse directories
- Access SMB resources

---

# When do we use it?

Usually after finding:

```
445/tcp open
```

or:

```
139/tcp open
```

because these ports are used by SMB.

---

# Basic Syntax

```
smbclient //TARGET/SHARE
```

Example:

```
smbclient //192.168.1.10/public
```

---

# Connect with Username and Password

```
smbclient //192.168.1.10/share -U username
```

Example:

```
smbclient //192.168.1.10/public -U admin
```

It will ask for the password.

---

# Anonymous Login (Null Session)

Sometimes SMB allows access without credentials:

```
smbclient -L //192.168.1.10 -N
```

Explanation:

- `-L` → List available shares
- `-N` → No password

Example output:

```
Sharename
---------
public
backup
IPC$
```

---

# List SMB Shares

```
smbclient -L TARGET
```

Example:

```
smbclient -L 10.10.10.5 -U admin
```

Shows:

- Available shares
- Permissions
- SMB services

---

# Inside smbclient

After connecting:

```
smb: \>
```

You can use commands like:

---

## List Files

```
ls
```

or:

```
dir
```

---

## Change Directory

```
cd folder
```

---

## Download File

```
get filename.txt
```

Example:

```
get passwords.txt
```

Downloads the file to your machine.

---

## Upload File

```
put shell.exe
```

Uploads a file to the SMB share.

---

## Exit

```
exit
```

or:

```
quit
```

---

# Important Options

|Option|Function|
|---|---|
|`-L`|List SMB shares|
|`-U`|Specify username|
|`-N`|Anonymous login (no password)|
|`-p`|Specify port|
|`-m`|Specify SMB protocol version|

---

# Specify SMB Version

Example:

```
smbclient -m SMB2 //10.10.10.5/share
```

Useful when:

- SMB1 is disabled
- Connection problems happen

---

# Common Pentesting Workflow

Example:

### 1. Discover SMB

```
nmap -p445 target
```

---

### 2. Enumerate Shares

```
smbclient -L //target -N
```

---

### 3. Connect to Share

```
smbclient //target/share
```

---

### 4. Search Files

```
ls
```

---

### 5. Download Interesting Files

```
get file.txt
```

---

# In short:

```
smbclient = FTP-like tool for SMB shares
```

Used for:

```
SMB Enumeration
        |
        v
Finding Shares
        |
        v
Accessing Files
        |
        v
Downloading / Uploading Data
```
# SMB (Server Message Block)

## Function
- Shares files, printers, folders, and network resources.
- Primarily used between Windows devices.

## Ports
| Port | Usage |
|------|-------|
| `445` | Direct SMB |
| `139` | NetBIOS SMB |

## Capabilities
- Access Shared Folders
- File Transfer
- Command Execution (in some cases)
- Domain Authentication
---
Lab
## Version Detection

```
 use auxiliary/scanner/smb/smb_version
```
---

## List available SMB shares

```
smbclient -L //ip/ -N
```

- `-L` → list shares
- `-N` → no password (anonymous login)

---

## Access a shared folder

If a share is found, connect to it:

```
smbclient //ip/filename
```

---

## Login with username

If credentials are required:

```
smbclient -L //ip/ -U username
```

---

# SMB Enumeration (Metasploit)

## Brute force login

Module:

```
use auxiliary/scanner/smb/smb_login
```

Used for:

- SMB authentication brute force

---

## Enumerate SMB users

```
use auxiliary/scanner/smb/smb_enumusers
```

Used to:

- Discover valid usernames on SMB

---

## Enumerate SMB shares

```
use auxiliary/scanner/smb/smb_enumshares
```

Used to:

- List available shared folders on SMB

---

## SMB login brute force (again)

```
use auxiliary/scanner/smb/smb_login
```

Used for:

- Password guessing against SMB accounts
# FTP (File Transfer Protocol)

FTP stands for:

```text
File Transfer Protocol
```

It is a protocol used to transfer files between a client and a server.

---

## Default Ports

|Port|Purpose|
|---|---|
|21|Control Channel|
|20|Data Channel|

---

## Common Uses

FTP allows users to:

- Upload files
    
- Download files
    
- Browse directories
    
- Manage files on a remote server
    

---

## Typical Enumeration Goals

During a penetration test, FTP is commonly checked for:

- Anonymous login access
    
- Exposed files and directories
    
- Backup files
    
- Configuration files
    
- Sensitive data leakage
    

---

## Useful Commands

Connect to an FTP server:

```bash
ftp <IP>
```

Anonymous login:

```text
Username: anonymous
Password: anonymous
```

List files:

```bash
ls
```

Download a file:

```bash
get filename
```

Upload a file:

```bash
put filename
```

---

## Nmap Enumeration

Detect FTP service:

```bash
nmap -sV -p21 <IP>
```

Check for anonymous access:

```bash
nmap --script ftp-anon -p21 <IP>
```

---

## Key Point

Misconfigured FTP servers may allow anonymous access, which can expose sensitive files and provide valuable information during the reconnaissance phase.

---
Lab 

## Determine the FTP service version.

```
use auxiliary/scanner/ftp/ftp_version
```
![[Pasted image 20260514010026.png]]


## Perform brute-force attacks against FTP credentials.

```
use auxiliary/scanner/ftp/ftp_login
```


## One of the most commonly used FTP modules in Metasploit.
```
set USER_FILE /usr/share/metasploit-framework/data/wordlists/common_users.txt

set PASS_FILE /usr/share/metasploit-framework/data/wordlists/unix_passwords.txt
```
![[Pasted image 20260514010212.png]]

## Check whether the FTP server allows anonymous login.
```
use auxiliary/scanner/ftp/anonymous
```

![[Pasted image 20260514010340.png]]


## Connect and authenticate to the FTP service.
![[Pasted image 20260514010413.png]]

# Done.
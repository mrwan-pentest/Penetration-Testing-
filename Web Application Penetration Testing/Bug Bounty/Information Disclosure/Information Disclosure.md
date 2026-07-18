
## What is Information Disclosure?

Information Disclosure occurs when an application unintentionally exposes sensitive information to users.

The information may not directly lead to code execution, but it can help an attacker discover valuable details about the target.

---

## Common Examples

### Source Code Disclosure

The application exposes:

```text
.php
.git
.bak
.old
```

files containing source code.

---

### Error Messages

Verbose errors reveal:

- File paths
    
- Database names
    
- Software versions
    
- Server information
    

Example:

```text
C:\xampp\htdocs\login.php
```

---

### Version Disclosure

The application reveals:

- Apache version
    
- Nginx version
    
- PHP version
    
- WordPress version
    
- Drupal version
    

Example:

```text
Apache/2.4.49
```

This helps identify known vulnerabilities.

---

### Directory Listing

The web server allows browsing files:

```text
Index of /
```

Attackers can download sensitive files directly.

---

### Backup Files

Developers sometimes leave:

```text
config.php.bak
db.sql
backup.zip
```

These files may contain credentials.

---

### Git Repository Disclosure

An exposed:

```text
.git
```

directory may reveal:

- Source code
    
- Credentials
    
- Deleted files
    
- Development history
    

---

### Sensitive Documents

Publicly accessible files such as:

```text
employees.xlsx
users.csv
database.sql
```

---

## Why is Information Disclosure Dangerous?

It helps attackers:

- Understand the application
    
- Identify technologies
    
- Discover usernames
    
- Find credentials
    
- Locate hidden functionality
    
- Prepare further attacks
    

---

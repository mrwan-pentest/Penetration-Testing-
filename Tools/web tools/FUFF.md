# FFUF

## What is FFUF?

**FFUF (Fuzz Faster U Fool)** is a fast and flexible web fuzzing tool used during the:

```
Information Gathering
Enumeration
```

phases of a penetration test.

Its primary purpose is to discover hidden resources on a web server by sending a large number of requests using a wordlist.

---

# What does FFUF do?

FFUF can be used to discover:

- Hidden directories
- Hidden files
- Virtual Hosts (VHosts)
- Subdomains
- API endpoints
- Parameters
- Backup files
- Development pages

---

# How does FFUF work?

FFUF replaces the keyword:

```
FUZZ
```

with every entry from a wordlist.

For example:

```
http://target.com/FUZZ
```

If the wordlist contains:

```
admin
login
uploads
backup
```

FFUF will automatically test:

```
http://target.com/admin
http://target.com/login
http://target.com/uploads
http://target.com/backup
```

and display the valid responses.

---

# Installation

FFUF comes pre-installed on Kali Linux.

To verify:

```bash
ffuf -V
```

If it is not installed:

```bash
sudo apt update
sudo apt install ffuf
```

---

# Basic Syntax

```bash
ffuf -u URL -w WORDLIST
```

Example:

```bash
ffuf -u http://target.com/FUZZ -w /usr/share/seclists/Discovery/Web-Content/common.txt
```

---

# Common Use Cases

## Directory Enumeration

```bash
ffuf -u http://target.com/FUZZ -w /usr/share/seclists/Discovery/Web-Content/common.txt
```

Searches for hidden directories and files.

---

## File Enumeration

```bash
ffuf -u http://target.com/FUZZ.php -w wordlist.txt
```

Searches for PHP files.

Example results:

```
login.php
admin.php
backup.php
```

---

## Subdomain Enumeration

```bash
ffuf -u http://FUZZ.example.com -w subdomains.txt -H "Host: FUZZ.example.com"
```

Discovers subdomains.

Example:

```
admin.example.com
dev.example.com
mail.example.com
```

---

## Virtual Host Enumeration

```bash
ffuf -u http://192.168.1.10/ -H "Host: FUZZ.example.com" -w vhosts.txt
```

Discovers hidden Virtual Hosts hosted on the same server.

---

## Parameter Fuzzing

```bash
ffuf -u "http://target.com/index.php?FUZZ=test" -w params.txt
```

Discovers hidden HTTP parameters.

Example:

```
id
page
user
file
debug
```

---

# Useful Options

## -u

Specifies the target URL.

Example:

```bash
-u http://target.com/FUZZ
```

---

## -w

Specifies the wordlist.

Example:

```bash
-w wordlist.txt
```

---

## -mc

Match specific HTTP status codes.

Example:

```bash
-mc 200
```

Show only:

```
200 OK
```

Multiple status codes:

```bash
-mc 200,301,302,403
```

---

## -fc

Filter specific HTTP status codes.

Example:

```bash
-fc 404
```

Hide:

```
404 Not Found
```

---

## -fs

Filter responses by size.

Example:

```bash
-fs 4242
```

Useful when the server returns the same page for every request.

---

## -fw

Filter responses by word count.

Example:

```bash
-fw 120
```

---

## -fl

Filter responses by line count.

Example:

```bash
-fl 45
```

---

## -t

Number of concurrent threads.

Example:

```bash
-t 100
```

Higher values make scanning faster but increase the load on the server.

---

## -e

Specify file extensions.

Example:

```bash
-e .php,.txt,.bak
```

FFUF will test:

```
admin.php
admin.txt
admin.bak
```

---

## -H

Add a custom HTTP header.

Example:

```bash
-H "Authorization: Bearer TOKEN"
```

or

```bash
-H "Cookie: PHPSESSID=abc123"
```

---

## -X

Specify the HTTP method.

Example:

```bash
-X POST
```

---

## -d

Send POST data.

Example:

```bash
-d "username=admin&password=test"
```

---

## -o

Save the output.

Example:

```bash
-o results.json
```

---

# Typical Penetration Testing Workflow

```text
Nmap
      ↓
Identify Web Server
      ↓
WhatWeb
      ↓
Identify Technologies
      ↓
FFUF
      ↓
Discover Hidden Directories & Files
      ↓
Analyze Interesting Resources
      ↓
Exploit Vulnerabilities
```

---

# Advantages of FFUF

- Extremely fast
- Lightweight
- Easy to use
- Supports recursive scanning
- Supports filtering by status code, size, words, and lines
- Supports custom headers, cookies, and authentication
- Supports GET and POST requests
- Ideal for directory, file, parameter, subdomain, and VHost enumeration

---

# Summary

FFUF is a high-performance web fuzzing tool used to discover hidden web resources by replacing the `FUZZ` keyword with entries from a wordlist.

It is commonly used to enumerate:

- Directories
- Files
- Subdomains
- Virtual Hosts
- API Endpoints
- HTTP Parameters

making it one of the most important enumeration tools during Web Application Penetration Testing.
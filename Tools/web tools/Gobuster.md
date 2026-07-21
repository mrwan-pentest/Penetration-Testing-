# Gobuster

`Gobuster` is a fast **Enumeration** tool written in the **Go programming language**.

It is designed to perform automated discovery against web applications and network services by using **Wordlists** to identify hidden resources that are not directly visible to users.

Gobuster is commonly used during the **Enumeration phase** of a penetration test to discover additional attack surfaces.

---

# What is Gobuster Used For?

Gobuster can be used to discover:

- Hidden directories
- Hidden files
- Subdomains
- Virtual Hosts

These resources may contain sensitive information, administrative interfaces, development environments, or misconfigured services.

For example, a website may only expose:

```
http://target.com
```

However, Gobuster may discover hidden resources such as:

```
http://target.com/admin
http://target.com/backup
http://target.com/dev
```

These discovered locations can provide additional targets for security testing.

---

# How Does Gobuster Work?

Gobuster performs automated enumeration by using a **Wordlist** containing possible names.

The workflow:

1. Gobuster reads entries from the provided Wordlist.
2. It generates requests against the target.
3. It analyzes server responses.
4. It displays valid resources that exist on the target.

Example:

A Wordlist may contain:

```
admin
backup
login
uploads
```

Gobuster tests:

```
http://target.com/admin
http://target.com/backup
http://target.com/login
http://target.com/uploads
```

If any of these resources exist, Gobuster reports them.

---

# Directory Enumeration

Directory enumeration is used to discover hidden folders and files on a web server.

## Syntax

```
gobuster dir -u http://target.com -w wordlist.txt
```

---

## Command Options

|Option|Description|
|---|---|
|`dir`|Performs directory and file enumeration|
|`-u`|Specifies the target URL|
|`-w`|Specifies the Wordlist|

---

## Example

```
gobuster dir -u http://demo.ine.local -w /usr/share/wordlists/dirb/common.txt
```

In this example:

- `dir` tells Gobuster to perform directory enumeration.
- `-u` defines the target website.
- `-w` provides the Wordlist used for discovery.

---

# File Extension Enumeration

Many web applications use specific file extensions, such as:

```
.php
.asp
.aspx
.txt
```

Gobuster can search for files with specific extensions using the `-x` option.

---

## Syntax

```
gobuster dir -u http://target.com -w wordlist.txt -x php,txt,html
```

This command attempts to discover files such as:

```
login.php
config.php
backup.txt
index.html
```

---

# Increasing the Number of Threads

Gobuster is already fast, but the number of concurrent requests can be increased using the `-t` option.

## Example

```
gobuster dir -u http://target.com -w wordlist.txt -t 50
```

The option:

```
-t 50
```

means Gobuster will use 50 threads to perform enumeration.

Increasing threads can make scans faster, but excessive values may:

- Increase network traffic
- Trigger security controls
- Overload the target server

---

# Subdomain Enumeration

Gobuster can also discover subdomains using DNS enumeration.

Subdomains are commonly used for:

- Development environments
- Testing servers
- Administrative portals
- Internal applications

---

## Syntax

```
gobuster dns -d target.com -w subdomains.txt
```

---

## Explanation

|Option|Description|
|---|---|
|`dns`|Enables DNS subdomain enumeration|
|`-d`|Specifies the target domain|
|`-w`|Specifies the subdomain Wordlist|

---

## Example Results

Gobuster may discover:

```
mail.target.com
dev.target.com
admin.target.com
vpn.target.com
```

These subdomains may expose additional services or vulnerabilities.

---

# Virtual Host Enumeration

Virtual Hosts allow multiple websites to run on the same web server using the same IP address.

Gobuster can test different hostnames to identify hidden virtual hosts.

This technique is especially important during penetration testing and is commonly encountered in **eJPT labs**.

---

## Syntax

```
gobuster vhost -u http://10.10.10.5 -w hosts.txt
```

---

## Explanation

|Option|Description|
|---|---|
|`vhost`|Enables Virtual Host enumeration|
|`-u`|Specifies the target URL or IP address|
|`-w`|Specifies the hostname Wordlist|

---

## Example Results

Gobuster may discover:

```
admin.target.local
dev.target.local
test.target.local
```

These virtual hosts may contain different applications or hidden functionality.

---

# Common Wordlists

Gobuster relies heavily on Wordlists for effective enumeration.

## Dirb Common Wordlist

Location:

```
/usr/share/wordlists/dirb/common.txt
```

This contains common directory and file names.

---

## SecLists

Location:

```
/usr/share/seclists/
```

If installed, SecLists provides a large collection of specialized Wordlists for:

- Web directories
- Files
- Subdomains
- Usernames
- Passwords
- Fuzzing

---

# Important Gobuster Options

## Directory Enumeration

```
gobuster dir
```

Used to scan for hidden directories and files.

---

## Target URL

```
-u
```

Specifies the target address.

Example:

```
-u http://target.com
```

---

## Wordlist

```
-w
```

Defines the Wordlist used for enumeration.

Example:

```
-w wordlist.txt
```

---

## File Extensions

```
-x php,txt,html
```

Searches for files with specific extensions.

---

## Number of Threads

```
-t 50
```

Controls the number of concurrent requests.

---

## Exclude Status Codes

```
-b 404
```

Ignores specific HTTP response codes.

Example:

```
gobuster dir -u http://target.com -w wordlist.txt -b 404
```

This hides results that return:

```
404 Not Found
```

---

## Subdomain Enumeration

```
gobuster dns
```

Used to discover subdomains.

---

## Virtual Host Enumeration

```
gobuster vhost
```

Used to identify hidden virtual hosts.

---

# Gobuster vs Dirb

|Feature|Gobuster|Dirb|
|---|---|---|
|Language|Go|C|
|Speed|Faster|Slower|
|Directory Enumeration|Yes|Yes|
|Subdomain Enumeration|Yes|No|
|Virtual Host Enumeration|Yes|No|
|File Extension Search|Yes|Yes|

Gobuster is often preferred in modern penetration testing because of its speed and additional enumeration modes.

---

# Summary

`Gobuster` is a powerful and fast Enumeration tool used to discover hidden resources in web applications and DNS environments.

Key points:

- Written in Go and optimized for speed.
- Used during the Web Enumeration phase.
- Supports:
    - Directory enumeration
    - File discovery
    - Subdomain enumeration
    - Virtual Host enumeration
- Uses Wordlists to automate discovery.
- Important options:

```
dir     → Directory enumeration
dns     → Subdomain enumeration
vhost   → Virtual Host enumeration
-u      → Target URL
-w      → Wordlist
-x      → File extensions
-t      → Threads
-b      → Exclude status codes
```

Gobuster is one of the essential tools for web reconnaissance and is commonly used in penetration testing certifications such as eJPT.
# Dirb

`Dirb` is a **Web Content Scanner** used during the **Web Enumeration** phase of a penetration test to discover hidden resources on a web server.

It performs automated requests against a target website using a predefined **Wordlist** to identify hidden content that is not directly linked from the main page.

---

# What is Dirb Used For?

`Dirb` is commonly used to discover:

- Hidden directories
- Hidden files
- Administrative panels
- Backup files
- Configuration files
- Old versions of web applications
- Sensitive resources accidentally exposed on the server

For example, a website may only display:

```
http://target.com
```

However, the server may contain hidden paths such as:

```
http://target.com/admin
http://target.com/backup
http://target.com/config.php
```

These resources may reveal sensitive information or provide additional attack surfaces.

---

# How Does Dirb Work?

`Dirb` works by performing **dictionary-based brute forcing** against a web server.

The process:

1. Dirb reads a Wordlist containing possible directory and file names.
2. It sends HTTP requests to the target website using each word from the list.
3. It analyzes the server responses.
4. It reports discovered resources.

Example:

If the Wordlist contains:

```
admin
backup
uploads
login
```

Dirb will test:

```
http://target.com/admin
http://target.com/backup
http://target.com/uploads
http://target.com/login
```

If one of these paths exists, Dirb will display it.

---

# Basic Usage

To perform a basic directory scan against a target website:

```
dirb http://target.com
```

This uses the default Dirb Wordlist to search for common hidden directories and files.

---

# Using a Custom Wordlist

A custom Wordlist can be provided to improve the discovery process.

```
dirb http://target.com wordlist.txt
```

Example:

```
dirb http://demo.ine.local /usr/share/wordlists/dirb/common.txt
```

In this example:

- `http://demo.ine.local` is the target website.
- `/usr/share/wordlists/dirb/common.txt` contains common directory and file names.

Using different Wordlists can reveal additional hidden content depending on the target technology.

---

# Directory Enumeration with Authentication Credentials

Some websites protect their hidden content behind authentication.

Dirb allows scanning authenticated areas by providing valid credentials.

```
dirb http://target.com wordlist.txt -u username:password
```

Example:

```
dirb http://target.com wordlist.txt -u admin:password123
```

This sends requests using the provided credentials while performing enumeration.

---

# Searching for Specific File Extensions

Web applications often use specific technologies such as:

- PHP
- ASP
- JSP
- Backup files

Dirb can search for files with specific extensions using the `-X` option.

---

## Searching for PHP Files

```
dirb http://target.com -X .php
```

This will test files ending with:

```
.php
```

Example:

```
login.php
config.php
admin.php
```

---

## Searching for Multiple Extensions

Multiple extensions can be specified by separating them with commas.

```
dirb http://target.com -X .php,.txt,.bak
```

This searches for:

```
.php
.txt
.bak
```

This is useful for discovering:

- Source code backups
- Configuration files
- Temporary files

---

# Saving Scan Results

Dirb results can be saved into a file for later analysis.

```
dirb http://target.com -o results.txt
```

The output will be stored inside:

```
results.txt
```

This is useful for:

- Creating penetration testing reports
- Reviewing findings later
- Comparing enumeration results

---

# Common Dirb Wordlists

Dirb includes several default Wordlists.

## Default Wordlist

Location:

```
/usr/share/dirb/wordlists/common.txt
```

This contains common directory and file names and is usually the first Wordlist used during enumeration.

---

## Larger Wordlist

Location:

```
/usr/share/dirb/wordlists/big.txt
```

This contains more entries and can discover additional hidden resources.

---

## SecLists Wordlists

If installed, SecLists provides a large collection of specialized Wordlists.

Location:

```
/usr/share/seclists/
```

It contains Wordlists for:

- Web directories
- Files
- Usernames
- Passwords
- Fuzzing
- Various technologies

---

# Practical Usage in Penetration Testing

During a web penetration test, Dirb is usually used after identifying an HTTP/HTTPS service.

Typical workflow:

1. Identify the web server.

```
nmap -p 80,443 target.com
```

2. Perform directory enumeration.

```
dirb http://target.com
```

3. Analyze discovered resources.

Examples:

```
/admin
/uploads
/backup
/login.php
```

4. Test discovered paths for vulnerabilities.

---

# Summary

`Dirb` is a web content enumeration tool used to discover hidden files and directories on web servers.

Key points:

- Used during the Web Enumeration phase.
- Performs dictionary-based scanning using Wordlists.
- Can discover hidden directories, files, and administrative pages.
- Supports custom Wordlists.
- Supports authenticated scanning.
- Can search for specific file extensions.
- Results can be exported for documentation.

Understanding how to use `Dirb` effectively helps penetration testers identify hidden attack surfaces that may not be visible through normal website browsing.
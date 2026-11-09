# Gobuster

## Overview

**Gobuster** is a command-line brute-forcing tool used for enumeration and discovering hidden resources on web servers and DNS infrastructure.

It supports several modes, including:

- **Directory/File Enumeration:** Discover hidden directories and files.
    
- **DNS Enumeration:** Discover subdomains.
    
- **VHost Enumeration:** Discover virtual hosts.
    
- **Fuzzing:** Discover resources using wordlists.
    
---

## Basic Usage

### 1. Directory Enumeration

```
gobuster dir -u http://TARGET -w wordlist.txt
```

### 2. Specify File Extensions

```
gobuster dir -u http://TARGET -w wordlist.txt -x php,txt,html
```

### 3. DNS Subdomain Enumeration

```
gobuster dns -d example.com -w wordlist.txt
```

### 4. Virtual Host Enumeration

```
gobuster vhost -u http://TARGET -w wordlist.txt
```

### 5. Search for Specific File Extensions

```
gobuster dir -u http://TARGET -w wordlist.txt -x bak,old,zip,conf
```

### 6. Save Results to a File

```
gobuster dir -u http://TARGET -w wordlist.txt -o results.txt
```

## Important Options

|Option|Description|
|---|---|
|`dir`|Directory/file enumeration mode|
|`dns`|DNS subdomain enumeration mode|
|`vhost`|Virtual Host enumeration mode|
|`-u`|Target URL|
|`-d`|Target domain (DNS mode)|
|`-w`|Wordlist path|
|`-x`|File extensions to search for|
|`-t`|Number of concurrent threads|
|`-o`|Save results to a file|
|`-s`|Status codes to include (e.g. `200,204,301,302,403`)|
|`-b`|Status codes to exclude|
|`-k`|Skip TLS certificate verification|
|`-r`|Follow redirects|
|`-a`|Set a custom User-Agent|
|`-H`|Add a custom HTTP Header|
|`-c`|Set a Cookie|
|`-U`|HTTP authentication username|
|`-P`|HTTP authentication password|
|`-q`|Disable progress output|
|`-e`|Print full URLs|

## Useful Examples

### Custom HTTP Header

```
gobuster dir -u http://TARGET -w wordlist.txt -H "Authorization: Bearer TOKEN"
```

### Use a Proxy

```
gobuster dir -u http://TARGET -w wordlist.txt --proxy http://127.0.0.1:8080
```

### Increase Threads

```
gobuster dir -u http://TARGET -w wordlist.txt -t 50
```

### Ignore TLS Certificate Errors

```
gobuster dir -u https://TARGET -w wordlist.txt -k
```

### Follow Redirects

```
gobuster dir -u http://TARGET -w wordlist.txt -r
```

## Default Wordlists

Common SecLists locations:

```
/usr/share/seclists/Discovery/Web-Content/
/usr/share/seclists/Discovery/DNS/
```

Example:

```
gobuster dir -u http://TARGET -w /usr/share/seclists/Discovery/Web-Content/common.txt
```

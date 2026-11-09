# DIRB

## Overview

**DIRB** is a Web Content Scanner used to discover hidden directories and files on a web server by brute-forcing paths with a wordlist.

It sends HTTP requests to the target using different paths and identifies accessible resources.

---

## Basic Usage

### 1. Basic Directory Scanning

```
dirb http://TARGET
```

Uses DIRB's default wordlist.

### 2. Specify a Wordlist

```
dirb http://TARGET /path/to/wordlist.txt
```

### 3. Scan with File Extensions

```
dirb http://TARGET -X .php,.txt,.html
```

### 4. Scan a Specific Directory

```
dirb http://TARGET/admin/
```

### 5. Scan HTTPS

```
dirb https://TARGET
```

### 6. Save Results to a File

```
dirb http://TARGET -o results.txt
```

## Important Options

|Option|Description|
|---|---|
|`-a`|Set a custom User-Agent|
|`-c`|Add a custom Cookie|
|`-H`|Add a custom HTTP Header|
|`-p`|Use an HTTP proxy (`IP:PORT`)|
|`-P`|Set proxy username and password|
|`-z`|Set delay between requests in milliseconds|
|`-r`|Do not search recursively|
|`-S`|Silent mode|
|`-v`|Verbose output|
|`-o`|Save output to a file|
|`-X`|Search for files with specific extensions|
|`-N`|Ignore responses with a specific HTTP status code|
|`-w`|Do not stop on warning messages|

## Useful Examples

### Custom Header

```
dirb http://TARGET -H "Authorization: Bearer TOKEN"
```

### Using a Proxy

```
dirb http://TARGET -p 127.0.0.1:8080
```

### Ignore 403 Responses

```
dirb http://TARGET -N 403
```

### Scan Without Recursive Searches

```
dirb http://TARGET -r
```

## Default Wordlist Location

```
/usr/share/dirb/wordlists/common.txt
```

List available wordlists:

```
ls /usr/share/dirb/wordlists/
```


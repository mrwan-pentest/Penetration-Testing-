# FFUF (Fuzz Faster U Fool)

## Overview

**FFUF** is a fast web fuzzer written in Go, commonly used in penetration testing to discover hidden directories, files, subdomains, virtual hosts, and parameters.

It uses a Wordlist and replaces the `FUZZ` keyword with each entry.

---


## 1. Directory & File Discovery

```
ffuf -u http://TARGET/FUZZ -w /usr/share/seclists/Discovery/Web-Content/common.txt
```

- `-u`: Target URL.
    
- `-w`: Wordlist path.
    
- `FUZZ`: Placeholder replaced by each wordlist entry.
    

### Search for specific file extensions

```
ffuf -u http://TARGET/FUZZ -w wordlist.txt -e .php,.txt,.html
```

- `-e`: Extensions to append to each wordlist entry.
    

## 2. Subdomain Discovery

```
ffuf -u http://FUZZ.example.com -w /usr/share/seclists/Discovery/DNS/subdomains-top1million-5000.txt
```

Replace `FUZZ` with candidate subdomains.

## 3. Virtual Host Discovery (VHost)

```
ffuf -u http://TARGET -H "Host: FUZZ.example.com" -w wordlist.txt
```

Tests different virtual host names through the HTTP Host header.

## 4. Parameter Discovery

```
ffuf -u "http://TARGET/page.php?FUZZ=test" -w wordlist.txt
```

Discovers possible GET parameter names.

### POST Parameter Discovery

```
ffuf -u http://TARGET/login.php -X POST -d "FUZZ=test" -w wordlist.txt
```

Tests possible POST parameter names.

## 5. Important Options

|Option|Description|
|---|---|
|`-u`|Target URL|
|`-w`|Wordlist|
|`-e`|File extensions|
|`-H`|Custom HTTP header|
|`-X`|HTTP method|
|`-d`|POST request data|
|`-mc`|Match HTTP status codes|
|`-fc`|Filter HTTP status codes|
|`-fs`|Filter responses by size|
|`-fw`|Filter responses by word count|
|`-ac`|Automatic calibration|
|`-t`|Number of concurrent threads|
|`-o`|Save results to a file|
|`-of`|Output format|

## 6. Filtering Results

Filter out 404 responses:

```
ffuf -u http://TARGET/FUZZ -w wordlist.txt -fc 404
```

Show only successful responses with status 200:

```
ffuf -u http://TARGET/FUZZ -w wordlist.txt -mc 200
```

Filter responses with a specific size:

```
ffuf -u http://TARGET/FUZZ -w wordlist.txt -fs 1234
```

## 7. Save Results

```
ffuf -u http://TARGET/FUZZ -w wordlist.txt -o results.json -of json
```

Saves the results in JSON format.

## Common Wordlists

From SecLists:

- Directory discovery: `Discovery/Web-Content/common.txt`
    
- Subdomain discovery: `Discovery/DNS/subdomains-top1million-5000.txt`
    
- Passwords: `Passwords/Common-Credentials/`
    

Default Kali path:

```
/usr/share/seclists/
```

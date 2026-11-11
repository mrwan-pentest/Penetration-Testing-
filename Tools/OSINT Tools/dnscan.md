
# Dnscan Tool

## 1. Introduction

Dnscan is a Python-based DNS enumeration tool used to discover subdomains associated with a target domain.

It uses a Wordlist-based approach to test possible subdomain names and identify valid DNS records.

It is useful during the Passive Reconnaissance and DNS Enumeration phases.

rbsec/dnscan · GitHub+1

## 2. Basic Subdomain Enumeration

To scan a domain and discover its subdomains:

```
dnscan -d example.com
```

- `-d`: Specifies the target domain.
    
- `example.com`: The domain being scanned.
    

## 3. Using a Custom Wordlist

We can specify our own Wordlist using `-w`:

```
dnscan -d example.com -w subdomains.txt
```

The tool uses the words in the file to check for possible subdomains.

## 4. Recursive Enumeration

To enable recursive scanning, use `-r`:

```
dnscan -d example.com -r
```

This allows the tool to scan discovered subdomains recursively, looking for additional subdomains.

## 5. Save Results to a File

To save the results:

```
dnscan -d example.com -o results.txt
```

## 6. Important Options

|Option|Description|
|---|---|
|`-d`|Specifies the target domain|
|`-l`|Reads domains from a file|
|`-w`|Specifies a custom Wordlist|
|`-t`|Sets the number of threads|
|`-r`|Enables recursive scanning|
|`-6`|Checks IPv6 records|
|`-z`|Performs DNS Zone Transfer only|
|`-o`|Saves results to a file|
|`-v`|Enables verbose output|
|`-h`|Displays help information|


## 7. Example Workflow

```
dnscan -d example.com -r -o results.txt
```

This command scans the target domain, enables recursive enumeration, and saves the results in `results.txt`.


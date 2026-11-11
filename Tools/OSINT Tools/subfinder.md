# Subfinder Tool

## 1. Introduction

Subfinder is a passive subdomain discovery tool developed by ProjectDiscovery. It is used to discover subdomains associated with a target domain by querying various public sources.

It is commonly used during the Information Gathering and DNS Enumeration phases of penetration testing.

## 2. Basic Subdomain Enumeration

To discover subdomains associated with a domain, use:

```
subfinder -d example.com
```

The `-d` option specifies the target domain.

## 3. Save Results to a File

We can save the discovered subdomains into a text file using `-o`:

```
subfinder -d example.com -o subdomains.txt
```

This stores the results in `subdomains.txt`.

## 4. Silent Mode

If we want to display only the discovered subdomains without additional output, use:

```
subfinder -d example.com -silent
```

## 5. Enumerate Multiple Domains

We can provide a list of domains using `-dL`:

```
subfinder -dL domains.txt
```

The file `domains.txt` should contain one domain per line.

## 6. Additional Options

|Option|Description|
|---|---|
|`-d`|Specifies a target domain|
|`-dL`|Reads multiple domains from a file|
|`-o`|Saves results to a file|
|`-silent`|Displays only discovered subdomains|
|`-all`|Uses all available sources|
|`-recursive`|Enables recursive subdomain discovery where supported|
|`-v`|Enables verbose output|

## 7. Example Workflow

A simple workflow for discovering subdomains and saving the results:

```
subfinder -d example.com -silent -o subdomains.txt
```

We can then use the discovered subdomains as input for further DNS resolution and authorized security testing.


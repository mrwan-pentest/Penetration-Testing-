# Subdomain Enumeration with Sublist3r

## What is Subdomain Enumeration?

Subdomain Enumeration is the process of discovering subdomains associated with a target domain.

For example, a website may have the main domain:

```
example.com
```

But it may also contain multiple subdomains:

```
mail.example.com
admin.example.com
dev.example.com
test.example.com
```

Each subdomain may host different services or applications.

---

# What is Sublist3r?

`Sublist3r` is an OSINT-based reconnaissance tool used to discover subdomains of a target domain.

It is commonly used during:

- Reconnaissance
- Information Gathering
- Attack Surface Discovery

---

# Why Is Subdomain Enumeration Important?

During penetration testing, the main website may be properly secured, while a hidden subdomain may contain security weaknesses.

Example:

```
dev.example.com
```

A development environment may expose:

- Administrative panels
- Testing applications
- Weak configurations
- Unprotected services

Therefore, discovering subdomains helps expand the attack surface.

---

# How Does Sublist3r Work?

Sublist3r gathers subdomain information from multiple public sources, including:

- Search engines
- SSL certificate records
- Public databases
- DNS information sources
- Internet archives

The process is mostly:

```
Passive Reconnaissance
```

Meaning it collects publicly available information without directly attacking the target.

---

# Basic Usage

## Scanning a Domain

Command:

```
sublist3r -d example.com
```

---

# Command Explanation

|Part|Description|
|---|---|
|`sublist3r`|Runs the Sublist3r tool|
|`-d`|Specifies the target domain|
|`example.com`|The target domain|

Meaning:

```
Discover subdomains related to this domain
```

---

# Example Output

The results may include discovered subdomains:

```
admin.example.com
mail.example.com
dev.example.com
api.example.com
```

These subdomains can then be analyzed for:

- Open ports
- Running services
- Vulnerabilities
- Misconfigurations

---

# Important Options

## Saving Results to a File

Command:

```
sublist3r -d example.com -o results.txt
```

Option:

```
-o
```

Means:

```
Output file
```

It saves discovered subdomains into the specified file.

---

# Controlling Threads

Command:

```
sublist3r -d example.com -t 50
```

Option:

```
-t
```

Means:

```
Number of threads
```

Increasing the number of threads can improve scanning speed.

However:

- Higher values consume more resources.
- Excessive requests may create unnecessary network traffic.

---

# Summary

`Sublist3r` is a reconnaissance tool used to discover subdomains related to a target domain.

Main purposes:

- Identify hidden subdomains.
- Expand the attack surface.
- Collect publicly available information.
- Support further enumeration phases.

Typical workflow:

```
Domain → Subdomain Enumeration → Service Discovery → Vulnerability Assessment
```
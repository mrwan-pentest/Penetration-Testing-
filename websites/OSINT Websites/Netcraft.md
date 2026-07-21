(https://www.netcraft.com/?utm_source=chatgpt.com)
# Netcraft

Netcraft is an online tool used for:

```
Website Reconnaissance and Information Gathering
```

It helps you discover information about a website and its infrastructure.

---

# What does Netcraft provide?

Netcraft can collect information such as:

- 🌐 IP Address
- 🖥️ Web Server Type
- 💻 Operating System
- 🧩 Technologies used
- 📍 Hosting Provider
- 🔐 SSL Certificate Information
- 🌍 Domain History
- 📅 Website uptime information

---

# Why is Netcraft useful in Pentesting?

It is used during:

```
Reconnaissance Phase
```

Before attacking a target, you need to understand:

- Where the website is hosted
- What technologies it uses
- What services may be running

---

# Main Features

## 1. Website Technology Detection

Netcraft can identify:

Example:

```
Web Server:
Apache 2.4

Operating System:
Linux

Framework:
PHP
```

This helps you search for possible vulnerabilities.

---

## 2. Hosting Information

It can show:

- Hosting company
- Data center location
- IP address information

Example:

```
example.com

IP:
93.x.x.x

Hosting:
Cloud Provider
```

---

## 3. SSL Certificate Information

It can display:

- Certificate issuer
- Validity dates
- Domain names in certificate

Useful for discovering:

- Related domains
- Subdomains

---

## 4. Site History

Netcraft can show historical information like:

- Previous IP addresses
- Previous hosting providers
- Technology changes

This can reveal old infrastructure.

---

# Example Usage

Search:

```
example.com
```

You may find:

```
IP Address: 192.168.1.10

Server:
nginx

OS:
Linux

Hosting:
Cloud Provider

SSL:
Valid Certificate
```

---

# Netcraft vs Other Recon Tools

|Tool|Purpose|
|---|---|
|Netcraft|Website information and history|
|WhatWeb|Detect web technologies|
|DNSDumpster|DNS and subdomain discovery|
|theHarvester|Emails and OSINT|
|Shodan|Internet-connected devices|

---

# Pentesting Workflow

```
Target Domain
      |
      ↓
Netcraft
      |
      ↓
Find Server + Technology
      |
      ↓
WhatWeb / Nmap
      |
      ↓
Vulnerability Assessment
      |
      ↓
Exploitation
```

---

# Summary

**Netcraft:**

```
A web reconnaissance tool used to gather information
about websites, servers, hosting, SSL certificates,
and technology stack.
```

It is mainly used during the **Information Gathering / Reconnaissance** phase.
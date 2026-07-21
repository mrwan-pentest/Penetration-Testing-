
(https://whois.domaintools.com/)


# Whois

WHOIS is a protocol and database used to retrieve information about:

```
Domain Names and IP Addresses
```

In simple words:

> WHOIS tells you who owns a domain, when it was registered, and information about its DNS and registrar.

---

# Why is WHOIS used?

It is mainly used during:

```
Reconnaissance / Information Gathering
```

Before penetration testing, it helps you collect public information about the target.

---

# What information does WHOIS provide?

## 1. Domain Owner Information

May include:

- Owner name
- Organization
- Contact email

_(Sometimes hidden by privacy protection)_

---

## 2. Registration Information

Shows:

- Creation date

Example:

```
Created:
2020-05-10
```

- Expiration date

```
Expires:
2027-05-10
```

- Last update date

---

## 3. Registrar Information

Shows the company that registered the domain.

Example:

```
Registrar:
Namecheap
GoDaddy
```

---

## 4. Name Servers (DNS)

Shows the DNS servers responsible for the domain.

Example:

```
NS:
ns1.example.com
ns2.example.com
```

Useful for DNS enumeration.

---

## 5. IP Information

For IP WHOIS lookup, it can show:

- ISP
- Organization
- Network range
- Country

---

# Basic Usage

Using Linux:

```
whois example.com
```

Example:

```
whois google.com
```

---

# Example Output

```
Domain Name:
example.com

Registrar:
Example Registrar

Creation Date:
2020-01-01

Name Server:
ns1.example.com
```

---

# Why is it useful for Pentesters?

WHOIS can reveal:

- Company information
- Related domains
- DNS providers
- Registration details
- Possible contacts for social engineering research

---

# Example Recon Workflow

```
Target Domain
      |
      ↓
WHOIS Lookup
      |
      ↓
Find Registrar + Name Servers
      |
      ↓
DNS Enumeration
      |
      ↓
Subdomain Discovery
      |
      ↓
Scanning
```

---

# WHOIS vs DNS Enumeration

|WHOIS|DNS Enumeration|
|---|---|
|Finds registration information|Finds DNS records|
|Owner / Registrar details|IPs / Subdomains|
|Domain metadata|Infrastructure details|

---

# Summary

**WHOIS:**

```
A database lookup service used to find public
registration information about domains and IP addresses.
```

It is one of the first tools used in the **Reconnaissance phase** to gather information about a target.
https://whois.domaintools.com/
# WHOIS Lookup

WHOIS Lookup is a tool/service that allows you to query WHOIS databases and retrieve public information about:

```
Domains
IP Addresses
```

In simple words:

> WHOIS Lookup lets you ask: "Who owns this domain, when was it created, and what infrastructure is related to it?"

---

# What information can WHOIS Lookup provide?

## 1. Domain Information

Shows:

- Domain name
- Domain status
- Registration date
- Expiration date
- Last update date

Example:

```
Domain:
example.com

Created:
2020-01-15

Expires:
2027-01-15
```

---

## 2. Registrar Information

Shows the company responsible for registering the domain.

Example:

```
Registrar:
GoDaddy
Namecheap
Cloudflare
```

---

## 3. Registrant Information

May show:

- Owner name
- Organization
- Email address
- Country

However, many domains use:

```
WHOIS Privacy Protection
```

to hide this information.

---

## 4. Name Servers

Displays DNS servers managing the domain.

Example:

```
Name Servers:

ns1.example.com
ns2.example.com
```

Useful for:

- DNS enumeration
- Finding DNS providers

---

## 5. IP Address Information

For IP WHOIS lookup, you may find:

- ISP
- Organization
- Network range
- Location information

---

# How to use WHOIS Lookup?

Example:

Search:

```
example.com
```

The tool returns information about that domain.

---

# Pentesting Use Case

During reconnaissance:

```
Target Domain
      |
      ↓
WHOIS Lookup
      |
      ↓
Find Registrar + DNS Servers
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

# WHOIS Lookup vs WHOIS Command

## WHOIS Lookup (Website)

- Easy to use
- No installation required
- Good for quick reconnaissance

---

## whois command (Linux)

Example:

```
whois example.com
```

- Command-line based
- Useful in Kali Linux
- Easy to automate

---

# Why is it useful for Pentesters?

It helps discover:

- Domain ownership information
- DNS infrastructure
- Related organizations
- Registration history
- Potential attack surface

---

# Summary

**WHOIS Lookup:**

```
An online service used to retrieve public registration
information about domains and IP addresses.
```

It is commonly used in the **Reconnaissance / Information Gathering phase** before scanning and exploitation.
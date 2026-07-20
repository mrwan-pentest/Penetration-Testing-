# dnsenum

## What is dnsenum?

`dnsenum` is a tool used for:

```
DNS Enumeration
```

It is designed to collect DNS-related information about a target domain.

It is commonly used during:

- Reconnaissance
- Information Gathering
- Enumeration phases of penetration testing

---

# What Does dnsenum Do?

`dnsenum` collects different types of DNS information, including:

- DNS Records
- Name Servers
- MX Records
- Subdomains
- DNS Zone Transfer attempts
- Google Scraping (when available)
- Subdomain brute forcing

---

# Basic Syntax

The basic usage of `dnsenum` is:

```
dnsenum example.com
```

Example:

```
dnsenum zonetransfer.me
```

---

# What Happens When Running dnsenum?

When executed, `dnsenum` performs several enumeration steps automatically.

The process usually includes:

1. Extracting DNS records:
    - A Records
    - NS Records
    - MX Records
2. Attempting:

```
AXFR (Zone Transfer)
```

3. Searching for subdomains.
4. Performing subdomain brute force using wordlists.

---

# DNS Records

## A Record

The A Record maps a domain name to an IP address.

Example:

```
example.com → 192.168.1.10
```

It helps identify the server hosting the domain.

---

## NS Record (Name Server)

The NS Record identifies the DNS servers responsible for managing the domain.

It answers the question:

```
Who manages the DNS records for this domain?
```

---

## MX Record (Mail Exchange)

The MX Record identifies the mail servers responsible for receiving emails for a domain.

Example:

```
Where do emails sent to @example.com go?
```

---

## TXT Record

TXT Records store text-based information and configurations.

They may contain:

- SPF records
- DKIM information
- Verification tokens

Example:

```
dig TXT example.com
```

---

# Practical Example

Command:

```
dnsenum zonetransfer.me
```

Possible output:

```
mail.zonetransfer.me
vpn.zonetransfer.me
dev.zonetransfer.me
```

This reveals discovered subdomains associated with the target domain.

---

# Important Options

## Full Enumeration

Command:

```
dnsenum --enum example.com
```

This performs a complete enumeration process, including:

- DNS record discovery
- Subdomain brute forcing
- Zone Transfer checks

---

# Using a Specific DNS Server

Command:

```
dnsenum --dnsserver ns1.example.com example.com
```

This forces `dnsenum` to use a specific DNS server for queries.

---

# Using a Custom Wordlist

Command:

```
dnsenum -f subdomains.txt example.com
```

Option:

```
-f
```

means:

```
Filename / Wordlist
```

It allows using a custom wordlist for subdomain discovery.

---

# DNS Zone Transfer

## What is Zone Transfer?

A DNS Zone Transfer allows copying DNS records from one DNS server to another.

The DNS query type used is:

```
AXFR
```

---

## Why Is It Important?

If a DNS server is incorrectly configured and allows unauthorized zone transfers, an attacker may obtain:

- All DNS records
- Internal hostnames
- Subdomains
- Server information

---

# Summary

`dnsenum` is a DNS Enumeration tool used to gather information about domains.

Main capabilities:

- Discover DNS records.
- Identify Name Servers.
- Find mail servers.
- Enumerate subdomains.
- Test for DNS Zone Transfer.
- Perform subdomain brute forcing.

Typical workflow:

```
DNS Enumeration → Discover Assets → Identify Attack Surface
```
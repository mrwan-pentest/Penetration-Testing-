# DNSrecon

## What is DNSrecon?

`DNSrecon` is a penetration testing and reconnaissance tool used to gather information about a domain's:

```
DNS Infrastructure
```

In simple terms:

> DNSrecon helps discover what information is exposed behind a website by analyzing its DNS configuration.

It is commonly used during:

- OSINT
- Reconnaissance
- Information Gathering
- Enumeration

---

# What Information Does DNSrecon Collect?

DNSrecon helps identify:

- Subdomains
- IP Addresses
- Mail Servers
- Name Servers
- Additional DNS information about the target infrastructure

---

# DNSrecon Enumeration Techniques

## 1. DNS Records Enumeration

DNSrecon can query different DNS record types.

---

## A Record

The A Record maps a domain name to an IP address.

Example:

```
example.com → 192.168.1.10
```

It helps identify the server hosting the domain.

---

## MX Record

The MX Record identifies mail servers responsible for handling emails.

Example:

```
Where do emails sent to @example.com go?
```

---

## NS Record

The NS Record identifies the DNS servers responsible for the domain.

It shows:

```
Which servers manage DNS for this domain?
```

---

## TXT Record

TXT Records contain additional text-based information.

They may reveal:

- SPF records
- DKIM information
- Domain verification tokens

---

# 2. Subdomain Enumeration

DNSrecon can search for hidden subdomains.

Examples:

```
admin.example.com
mail.example.com
dev.example.com
```

Discovering subdomains can reveal:

- Additional services
- Development environments
- Administrative panels

---

# 3. DNS Zone Transfer

DNSrecon can attempt:

```
AXFR (DNS Zone Transfer)
```

A successful Zone Transfer may expose the complete DNS database of a domain.

If the DNS server is incorrectly configured, it may reveal:

- All subdomains
- IP addresses
- DNS records
- Internal infrastructure details

---

# Basic Usage

## Scanning a Domain

Command:

```
dnsrecon -d example.com
```

---

## Command Explanation

|Part|Description|
|---|---|
|`dnsrecon`|Runs the DNSrecon tool|
|`-d`|Specifies the target domain|
|`example.com`|The target domain|

Meaning:

```
Analyze this domain using DNSrecon
```

---

# 1. Basic Domain Enumeration

Command:

```
dnsrecon -d example.com
```

## Purpose

Collects basic DNS information about the target domain.

---

## Information Collected

The output may include:

- IP Address
- Name Servers (NS)
- Mail Servers (MX)
- TXT Records
- Basic Subdomain information

---

## Concept

This is a general scan used to build an initial understanding of the target's DNS infrastructure.

---

# 2. Subdomain Brute Force

Command:

```
dnsrecon -d example.com -t brt
```

---

## What Does `-t brt` Mean?

Options:

|Option|Meaning|
|---|---|
|`-t`|Specifies the scan type|
|`brt`|Brute Force mode|

---

## What Does It Do?

DNSrecon attempts to discover subdomains by testing common names.

Examples:

```
admin.example.com
test.example.com
mail.example.com
```

---

## Goal

The goal is to discover hidden subdomains that are not publicly advertised.

---

## Concept

This is similar to password brute forcing, but instead of testing passwords, it tests possible subdomain names.

---

# 3. DNS Zone Transfer Attempt

Command:

```
dnsrecon -d example.com -t axfr
```

---

## What Does `axfr` Mean?

```
AXFR = DNS Zone Transfer
```

---

## What Does It Attempt?

It attempts to retrieve all DNS records from the DNS server at once.

---

## If the Server Is Misconfigured

A successful transfer may reveal:

- All subdomains
- All IP addresses
- Complete DNS records

---

## Goal

The goal is to obtain a complete map of the target domain infrastructure.

---

## Concept

It is similar to asking the DNS server:

```
Give me all information you have about this domain
```

---

# Summary

`DNSrecon` is a powerful DNS reconnaissance tool used to discover information about target domains.

Main capabilities:

- DNS Record Enumeration
- Subdomain Discovery
- Mail Server Identification
- Name Server Discovery
- DNS Zone Transfer Testing

Common workflow:

```
DNS Enumeration → Discover Assets → Map Infrastructure → Identify Attack Surface
```
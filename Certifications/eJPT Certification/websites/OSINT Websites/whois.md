
(https://whois.domaintools.com/)

# WHOIS

## Overview

**WHOIS** is a protocol and a publicly accessible database used to retrieve registration information about **domain names** and **IP addresses**.

The term **WHOIS** refers to both:

- The **service** that provides registration information.
- The **tool** used to query the WHOIS database.

---

# Information Provided by WHOIS

A WHOIS lookup can reveal valuable information about a domain or IP address, including:

- Domain Owner (Registrant)
- Registrar
- Registration Date
- Expiration Date
- Name Servers
- Contact Information (when publicly available)

---

## Domain Owner (Registrant)

Displays information about the entity or individual who registered the domain.

Depending on the domain's privacy settings, this may include:

- Name
- Organization
- Address
- Phone Number
- Email Address

> **Note:** Many domains use privacy protection services, so personal information may be hidden.

---

## Registrar

Identifies the company through which the domain was registered.

Examples:

```text
GoDaddy
Namecheap
Cloudflare Registrar
Google Domains
```

---

## Registration Date

Shows the date on which the domain was originally registered.

This information can help estimate the age of a website.

---

## Expiration Date

Displays the date when the domain registration expires.

The domain owner must renew the registration before this date to maintain ownership.

---

## Name Servers

Lists the authoritative DNS servers responsible for the domain.

Examples:

```text
ns1.example.com
ns2.example.com
```

Name Servers determine where the domain's DNS records are hosted.

---

## Contact Information

When privacy protection is not enabled, WHOIS may provide:

- Registrant Name
- Organization
- Email Address
- Phone Number
- Postal Address

---

# Query Targets

WHOIS can be used to query:

- Domain Names

```text
example.com
openai.com
```

- IP Addresses

```text
8.8.8.8
104.21.35.14
```

---

# Importance in Penetration Testing

WHOIS is commonly used during the **Footprinting** and **Reconnaissance** phases to:

- Identify the domain registrar.
- Discover the domain's registration history.
- Determine the domain's age.
- Identify the authoritative Name Servers.
- Collect publicly available ownership information.
- Gather intelligence that may support further reconnaissance.

---

# Summary

WHOIS is a protocol and public database used to obtain registration information about domains and IP addresses.

It can provide information such as:

- Domain Owner
- Registrar
- Registration Date
- Expiration Date
- Name Servers
- Public Contact Information

WHOIS is one of the fundamental OSINT tools used during the reconnaissance phase of a penetration test.
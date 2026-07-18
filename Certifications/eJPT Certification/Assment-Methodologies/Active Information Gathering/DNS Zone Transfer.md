# DNS Zone Transfer

DNS is responsible for translating domain names into IP addresses.

Example:

```text
example.com -> 93.184.216.34
```

Organizations often maintain multiple DNS servers, such as:

- Primary DNS Server
    
- Secondary DNS Server
    

To keep DNS records synchronized between them, a mechanism called:

```text
Zone Transfer (AXFR)
```

is used.

---

## What Is a DNS Zone?

A DNS Zone is a database that contains DNS records associated with a domain.

Examples:

```text
mail.example.com
vpn.example.com
dev.example.com
```

---

## What Is a DNS Zone Transfer?

A Zone Transfer is the process of copying all DNS records from the primary DNS server to a secondary DNS server.

Instead of querying a single record:

```text
www.example.com
```

You may obtain the entire DNS zone.

---

## Why Is It Important During a Penetration Test?

If a DNS server allows unrestricted AXFR requests, an attacker may retrieve all DNS records for the target domain.

This can reveal:

- Subdomains
    
- Internal server names
    
- VPN gateways
    
- Mail servers
    
- Development and staging environments
    

This information is extremely valuable during:

```text
Reconnaissance / Enumeration
```

---

## Common Tool: dnsenum

Basic usage:

```bash
dnsenum example.com
```

### Capabilities

- DNS enumeration
    
- Subdomain discovery
    
- Name server identification
    
- MX record enumeration
    
- Zone transfer testing (AXFR)
    

DNS Zone Transfers are often considered a high-value finding because they can expose a significant amount of infrastructure information in a single request.

---

![[Pasted image 20260510212128.png]]

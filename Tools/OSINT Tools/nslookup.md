#   
DNSLookup Tool

## 1. Introduction

nslookup (Name Server Lookup) is a command-line tool used to query DNS servers and retrieve DNS information about a domain name or IP address.

It is useful during the DNS Enumeration phase to identify IP addresses, mail servers, name servers, and other DNS records.

## 2. Basic DNS Lookup

To retrieve the IP address associated with a domain, use:

```
nslookup example.com
```

This command queries the configured DNS server and displays the DNS response, including the domain's IP address.

## 3. Query Specific DNS Records

We can specify the type of DNS record we want to retrieve.

A Record – IPv4 Address

```
nslookup -type=A example.com
```

AAAA Record – IPv6 Address

```
nslookup -type=AAAA example.com
```

MX Record – Mail Servers

```
nslookup -type=MX example.com
```

NS Record – Name Servers

```
nslookup -type=NS example.com
```

TXT Record – Text Information

```
nslookup -type=TXT example.com
```

CNAME Record – Canonical Name

```
nslookup -type=CNAME example.com
```

## 4. Query a Specific DNS Server

We can specify which DNS server should handle the query:

```
nslookup example.com 8.8.8.8
```

Here, `8.8.8.8` is Google's public DNS server.

We can also combine this with a specific record type:

```
nslookup -type=MX example.com 8.8.8.8
```

## 5. Reverse DNS Lookup

We can perform a reverse DNS lookup to retrieve the domain name associated with an IP address:

```
nslookup 8.8.8.8
```

## 6. Interactive Mode

We can run `nslookup` without specifying a domain to enter interactive mode:

```
nslookup
```

Then enter commands such as:

`> server 8.8.8.8 > set type=MX > example.com`

This allows us to change the DNS server and record type without restarting the tool.

## 7. Important Options

|Option|Description|
|---|---|
|`-type=A`|Queries IPv4 records|
|`-type=AAAA`|Queries IPv6 records|
|`-type=MX`|Queries mail servers|
|`-type=NS`|Queries name servers|
|`-type=TXT`|Queries TXT records|
|`-type=CNAME`|Queries canonical names|

Key Takeaway: `nslookup` is a useful tool for DNS Enumeration. It allows us to query different DNS record types, identify DNS servers, and perform reverse DNS lookups.
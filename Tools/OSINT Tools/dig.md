
# DIG Tool

## 1. Introduction

DIG (Domain Information Groper) is a command-line tool used to query DNS servers and retrieve DNS records associated with a domain name.

It is commonly used during the DNS Enumeration phase of penetration testing.

## 2. Basic DNS Lookup

To retrieve DNS information about a domain, use:

```
dig example.com
```

This command displays the DNS response, including the IP address and other query details.

## 3. Query Specific DNS Records

We can specify the type of DNS record we want to retrieve.

A Record – IPv4 Address

```
dig example.com A
```

AAAA Record – IPv6 Address

```
dig example.com AAAA
```

MX Record – Mail Servers

```
dig example.com MX
```

NS Record – Name Servers

```
dig example.com NS
```

TXT Record – Text Information

```
dig example.com TXT
```

CNAME Record – Canonical Name

```
dig example.com CNAME
```

## 4. Query a Specific DNS Server

We can specify which DNS server should handle the query using `@`:

```
dig @8.8.8.8 example.com
```

Here, `8.8.8.8` is Google's public DNS server.

## 5. Short Output

To display only the answer without additional details, use:

```
dig example.com +short
```

## 6. Reverse DNS Lookup

We can use `-x` to retrieve the domain name associated with an IP address:

```
dig -x 8.8.8.8
```

## 7. Trace DNS Resolution

To trace the DNS delegation path from the root DNS servers to the target domain, use:

```
dig example.com +trace
```

## 8. Useful Options

|Option|Description|
|---|---|
|`+short`|Displays a short response|
|`+noall +answer`|Displays only the answer section|
|`+trace`|Traces the DNS delegation path|
|`-x`|Performs a reverse DNS lookup|
|`@DNS`|Specifies the DNS server|





# theHarvester

## What is theHarvester?

`theHarvester` is an OSINT (Open Source Intelligence) tool used during the reconnaissance phase to collect publicly available information about a target domain.

In simple terms:

> It gathers publicly exposed information about a target from the Internet.

It is commonly used in:

- Information Gathering
- Passive Reconnaissance
- Attack Surface Discovery

---

# What Does theHarvester Collect?

`theHarvester` can collect information such as:

- Email addresses
- Subdomains
- Hosts
- IP addresses
- Names of employees (depending on the data source)
- Publicly available information related to the target

---

# Why Is theHarvester Important?

During penetration testing, information gathering is an important first step.

theHarvester helps testers:

- Identify possible company employees.
- Discover hidden subdomains.
- Find exposed services.
- Build an initial map of the target infrastructure.

This process is performed without directly attacking the target.

---

# Basic Usage

The general syntax is:

```
theHarvester -d DOMAIN -b SOURCE
```

Example:

```
theHarvester -d example.com -b google
```

---

# Command Explanation

|Option|Description|
|---|---|
|`-d`|Specifies the target domain|
|`example.com`|The target website|
|`-b`|Specifies the data source|
|`google`|Uses Google as the information source|

Meaning:

```
Collect information about this domain using Google
```

---

# Practical Example

Command:

```
theHarvester -d ine.com -b all
```

## Purpose

Collects available information about:

```
ine.com
```

from all supported sources.

The results may include:

- Emails
- Subdomains
- Hosts
- Other publicly available information

---

# Data Sources (`-b`)

The `-b` option defines where theHarvester collects information from.

Common sources include:

|Source|Description|
|---|---|
|`google`|Google search results|
|`bing`|Bing search engine|
|`linkedin`|Public LinkedIn information|
|`yahoo`|Yahoo search results|
|`all`|Uses all available sources|

---

# Employee Information Gathering

Example:

```
theHarvester -d target.com -b linkedin
```

This may reveal:

- Employee names
- Email addresses
- Job roles

This information can be useful during:

- Social Engineering assessments
- Phishing simulations
- Organization mapping

---

# Comparison With Similar Tools

|Tool|Main Purpose|
|---|---|
|Sublist3r|Subdomain discovery|
|DNSrecon|DNS analysis and enumeration|
|theHarvester|Emails, subdomains, hosts, and public information gathering|

---

![](../../../../Images/Pasted%20image%2020260510165847.png)

---

# Summary

`theHarvester` is a passive reconnaissance tool used to collect publicly available information about a target domain.

Main capabilities:

- Email discovery
- Subdomain discovery
- Host identification
- Employee information gathering
- OSINT-based reconnaissance

Typical workflow:

```
Target Domain → OSINT Collection → Asset Discovery → Further Enumeration
```
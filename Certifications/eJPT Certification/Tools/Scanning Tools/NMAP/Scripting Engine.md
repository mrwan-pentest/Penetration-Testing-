# Nmap Scripting Engine (NSE)

It is:

```
A scripting system inside Nmap
```

that allows Nmap to perform more than just:

- Port Scanning
- Service Detection

---

# NSE Idea

By default, Nmap can:

- Discover open ports
- Detect services and versions

But with NSE, Nmap can perform additional tasks such as:

- Vulnerability Detection
- Service Enumeration
- Information Gathering
- Configuration Checks
- Exploit Checks

---

# NSE Scripts Location

Nmap scripts are located at:

```
/usr/share/nmap/scripts
```

Each file inside this directory represents a script that Nmap can run.

---

# `-sC`

Means:

```
Run Default NSE Scripts
```

It runs the default set of NSE scripts included with Nmap.

---

# What do these scripts check?

They collect additional information such as:

- Service information
- Banners
- Server configurations
- Protocol information
- Basic vulnerability checks

---

# Example:

```
nmap -sC target
```

Meaning:

Run a normal Nmap scan with:

```
Default NSE Scripts
```

---

# Practical Example:

Without NSE, you may only see:

```
80/tcp open http
```

With NSE, you may get additional information like:

```
HTTP Server: Apache
Page Title
Allowed Methods
SSL Information
```

---

# `--script-help`

Used for:

```
Displaying information and help about NSE scripts
```

---

# Idea

Before running any script, you can check:

- What does it do?
- What is its purpose?
- Which category does it belong to?
- How is it used?
- Does it require specific arguments?

---

# Example:

```
nmap --script-help http-enum
```

This displays information about:

```
http-enum
```

Including:

- Script description
- How it works
- Correct usage
- Required options

---

# Another Example

To view HTTP-related scripts:

```
ls /usr/share/nmap/scripts/http*
```

You may find:

```
http-enum.nse
http-title.nse
http-methods.nse
```

---

# Common NSE Categories

## `auth`

Checks authentication issues.

Example:

```
Authentication checks
```

---

## `discovery`

Used for information gathering.

Examples:

```
Usernames
Shares
Information
```

---

## `vuln`

Searches for vulnerabilities.

Example:

```
Known vulnerabilities
```

---

## `safe`

Scripts designed to perform checks safely without affecting the target.

---

## `exploit`

Scripts that perform exploitation when the required conditions exist.

---

# Common Examples

## SMB Enumeration:

```
nmap --script smb-enum-shares target
```

---

## HTTP Enumeration:

```
nmap --script http-enum target
```

---

## Vulnerability Scanning:

```
nmap --script vuln target
```

---

# Summary

NSE transforms Nmap from:

```
Port Scanner
```

into a tool capable of:

```
Enumeration + Vulnerability Detection + Information Gathering
```

You can run NSE scripts:

- Using default scripts:

```
-sC
```

- Or selecting a specific script:

```
--script script-name
```
# WMAP

## What is WMAP?

WMAP is:

```
Web Vulnerability Scanner inside Metasploit
```

It is a web application scanning framework integrated into Metasploit.

WMAP is used to:

- Scan web applications.
- Identify potential vulnerabilities.
- Run web-related Metasploit Modules automatically.

---

# WMAP Concept

Instead of manually running every web scanning Module individually, WMAP helps automate the process.

It can:

```
Collect and execute suitable Web Modules automatically
```

This makes web application assessment easier during penetration testing.

---

# What Does WMAP Scan?

WMAP can perform checks for:

- SQL Injection
- File Disclosure
- HTTP PUT Methods
- WebDAV vulnerabilities
- Directory Listing
- HTTP Headers
- Common web vulnerabilities

---

# Loading WMAP

Inside Metasploit:

```
load wmap
```

## Purpose

Loads the WMAP extension into the Metasploit Framework.

---

# Display WMAP Commands

To display all available WMAP commands:

```
wmap_commands
```

## Purpose

Shows the available commands for managing:

- Sites
- Targets
- Modules
- Scans
- Results

---

# Adding a Target Website

To add a website to WMAP:

```
wmap_sites -a http://TARGET
```

Example:

```
wmap_sites -a http://192.168.1.10
```

## Purpose

Adds the target website to the WMAP database.

---

# Listing Added Sites

To display all stored websites:

```
wmap_sites -l
```

## Purpose

Shows all websites currently added to WMAP.

---

# Selecting a Target

To define the target that will be scanned:

```
wmap_targets -t http://TARGET
```

Example:

```
wmap_targets -t http://192.168.1.10
```

## Purpose

Selects the website that WMAP will scan.

---

# Listing Current Targets

To display selected targets:

```
wmap_targets -l
```

## Purpose

Shows:

```
Current targets configured for scanning
```

---

# Running WMAP Scans

## Quick Test Scan

Command:

```
wmap_run -t
```

## Purpose

Runs test Modules designed for quick checks.

It usually performs:

- Basic Enumeration
- Information gathering
- Lightweight checks

---

# Full Scan

Command:

```
wmap_run -e
```

## Purpose

Runs all applicable WMAP Modules against the target.

The scan may include checks for:

- Vulnerabilities
- Files
- WebDAV
- HTTP Headers
- Directories
- SQL Injection checks
- Other web security issues

---

# Viewing Results

WMAP results can be viewed using Metasploit commands.

## View Services

```
services
```

## View Discovered Vulnerabilities

```
vulns
```

---

# Practical Example

Start Metasploit:

```
msfconsole
```

Load WMAP:

```
load wmap
```

Add the target:

```
wmap_sites -a http://192.168.1.10
```

Select the target:

```
wmap_targets -t http://192.168.1.10
```

Run the full scan:

```
wmap_run -e
```

---

# Managing WMAP Modules

## Display Available Modules

Command:

```
wmap_modules -l
```

## Purpose

Lists all Modules available for WMAP scanning.

---

# Display Module Information

Command:

```
wmap_modules -i MODULE_NAME
```

## Purpose

Displays information about a specific WMAP Module.

---

# Running a Specific Module

Instead of running the entire scan, you can execute a single Module:

```
wmap_run -m MODULE_NAME
```

Example:

```
wmap_run -m auxiliary/scanner/http/http_header
```

This runs only the specified HTTP Header scanning Module.

---

# Deleting Sites

To remove a website from WMAP:

```
wmap_sites -d ID
```

The `ID` refers to the identifier assigned to the stored site.

---

# Deleting Targets

To remove a target:

```
wmap_targets -d ID
```

---

# Summary

WMAP is a Metasploit extension designed for automated web application scanning.

Main features:

- Web vulnerability scanning.
- Automated execution of web-related Modules.
- Target management.
- Web enumeration.
- Vulnerability discovery.

Common workflow:

```
Load WMAP → Add Site → Select Target → Run Scan → Review Results
```
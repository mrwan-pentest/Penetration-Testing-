# WMAP (Web Assessment Plugin)

WMAP is a **built-in web vulnerability scanner** included with the Metasploit Framework. It automates web application assessment by identifying potential vulnerabilities and executing appropriate Metasploit web modules.

Instead of manually running each web-related module, WMAP organizes and executes them automatically against the target website.

---

# What Can WMAP Detect?

Depending on the available modules, WMAP can identify issues such as:

- SQL Injection (SQLi)
- File Disclosure
- HTTP PUT Method
- WebDAV Misconfigurations
- Directory Listing
- Insecure HTTP Headers
- Default Files
- Web Server Misconfigurations
- Common Web Vulnerabilities

---

# Loading WMAP

Before using WMAP, load the plugin inside Metasploit:

```bash
load wmap
```

---

# Display Available WMAP Commands

```bash
wmap_commands
```

Displays all commands supported by the WMAP plugin.

---

# Add a Website

Register the target website in the WMAP database:

```bash
wmap_sites -a http://TARGET
```

### Example

```bash
wmap_sites -a http://192.168.1.10
```

---

# List Registered Websites

```bash
wmap_sites -l
```

Displays all websites currently stored in the WMAP database.

---

# Select the Target

Specify which website will be scanned:

```bash
wmap_targets -t http://TARGET
```

### Example

```bash
wmap_targets -t http://192.168.1.10
```

---

# List Current Targets

```bash
wmap_targets -l
```

Shows all active targets selected for scanning.

---

# Running a Scan

## Quick Scan

```bash
wmap_run -t
```

Runs a lightweight assessment, typically performing:

- Enumeration
- Basic fingerprinting
- Lightweight security checks

---

## Full Scan

```bash
wmap_run -e
```

Executes all applicable WMAP modules against the target.

This may include:

- SQL Injection checks
- Directory Enumeration
- WebDAV Testing
- HTTP Header Analysis
- File Disclosure
- Server Misconfiguration Checks
- Various Web Vulnerability Modules

---

# Viewing Scan Results

After the scan completes, Metasploit stores the findings in its database.

Display discovered services:

```bash
services
```

Display identified vulnerabilities:

```bash
vulns
```

---

# Managing Websites

## Delete a Website

```bash
wmap_sites -d ID
```

Removes a website from the WMAP database.

---

# Managing Targets

## Delete a Target

```bash
wmap_targets -d ID
```

Removes a target from the current scan list.

---

# Working with WMAP Modules

## List Available Modules

```bash
wmap_modules -l
```

Displays all web modules available to WMAP.

---

## Display Module Information

```bash
wmap_modules -i MODULE_NAME
```

Shows detailed information about a specific module.

---

## Execute a Single Module

```bash
wmap_run -m MODULE_NAME
```

### Example

```bash
wmap_run -m auxiliary/scanner/http/http_header
```

Runs only the specified module instead of executing the complete WMAP scan.

---

# Practical Example

```bash
msfconsole

load wmap

wmap_sites -a http://192.168.1.10

wmap_targets -t http://192.168.1.10

wmap_run -e

services

vulns
```

---

# Lab Walkthrough

## Load the Plugin

```bash
load wmap
```

Loads the WMAP plugin into Metasploit.

---

## Add the Target Website

```bash
wmap_sites -a http://192.157.89.3
```

Adds the website to the WMAP database.

---

## Select the Target

```bash
wmap_targets -t http://192.157.89.3
```

Marks the website as the active target for scanning.

---

## Verify Registered Websites

```bash
wmap_sites -l
```

Displays all websites currently stored.

---

## Verify Active Targets

```bash
wmap_targets -l
```

Displays the targets selected for assessment.

---

## Perform a Quick Scan

```bash
wmap_run -t
```

Performs a lightweight assessment focusing mainly on:

- Enumeration
- Basic Information Gathering
- Initial Security Checks

---

## Perform a Full Scan

```bash
wmap_run -e
```

Runs every compatible WMAP module to perform a comprehensive web application assessment.

---

## Display Available Commands

```bash
wmap_commands
```

Lists all WMAP commands.

---

## List Installed Modules

```bash
wmap_modules -l
```

Shows all modules available for WMAP scanning.

---

## Display Module Details

```bash
wmap_modules -i MODULE_NAME
```

Displays detailed information about a selected module.

---

## Execute a Specific Module

```bash
wmap_run -m auxiliary/scanner/http/http_header
```

Runs only the HTTP Header scanner against the target.

---

# Summary

WMAP is Metasploit's integrated web application scanner. It simplifies web assessments by automatically selecting and executing appropriate web-related auxiliary modules.

### Typical WMAP Workflow

1. Load the plugin.
2. Add the target website.
3. Select the active target.
4. Run either a quick or full scan.
5. Review discovered services and vulnerabilities.
6. Investigate individual findings or execute specific modules as needed.
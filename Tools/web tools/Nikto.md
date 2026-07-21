# Nikto

`Nikto` is an open-source **Web Server Scanner** used to perform security assessments against web servers.

It is designed to identify common security issues, including:

- Sensitive files
- Dangerous web pages
- Misconfigurations
- Outdated software versions
- Known vulnerabilities
- Default directories and files

Nikto is commonly used during the **Web Enumeration** phase of a penetration test to gather information about the target web server and identify potential attack vectors.

---

# What is Nikto Used For?

Nikto performs automated checks against web servers to discover security weaknesses.

It can identify issues such as:

- Exposed administrative pages
- Default files installed by web servers
- Backup files
- Unsafe HTTP headers
- Outdated server software
- Known vulnerable components
- Incorrect server configurations

Example:

A web server may expose files such as:

```
backup.zip
config.old
admin/
```

These resources may reveal sensitive information or provide additional attack opportunities.

---

# How Does Nikto Work?

Nikto uses a database of known vulnerabilities and common web server issues.

The scanning process:

1. Nikto connects to the target web server.
2. It sends HTTP/HTTPS requests.
3. It compares responses against its vulnerability database.
4. It reports discovered issues.

Nikto does not exploit vulnerabilities automatically; instead, it identifies possible weaknesses that require further investigation.

---

# Basic Syntax

```
nikto -h <target>
```

Where:

- `-h` specifies the target host or URL.

---

# Scanning a Website

To scan a web server:

```
nikto -h http://192.168.1.10
```

This performs a general security scan against the target.

Nikto checks for:

- Common vulnerabilities
- Misconfigurations
- Exposed files
- Known server issues

---

# Scanning HTTPS Websites

If the target uses HTTPS:

```
nikto -h https://192.168.1.10
```

Nikto will perform the scan against the HTTPS service.

This is useful when testing:

- Secure web applications
- HTTPS configurations
- SSL-enabled services

---

# Scanning a Specific Port

Web services are not always hosted on the default ports:

```
80  → HTTP
443 → HTTPS
```

A web application may run on another port such as `8080`.

Example:

```
nikto -h 192.168.1.10 -p 8080
```

This scans the web service running on port:

```
8080
```

---

# Scanning Multiple Ports

Nikto can scan multiple web ports by separating them with commas.

Example:

```
nikto -h 192.168.1.10 -p 80,443,8080
```

This checks web services running on:

```
80
443
8080
```

---

# Using SSL Mode

To force Nikto to use HTTPS:

```
nikto -h 192.168.1.10 -ssl
```

This is useful when:

- The service uses SSL/TLS.
- The target does not automatically detect HTTPS.

---

# Saving Scan Results

Nikto results can be exported into a file for later analysis.

Example:

```
nikto -h 192.168.1.10 -o report.txt
```

The scan output will be saved as:

```
report.txt
```

This is useful for:

- Penetration testing reports
- Documentation
- Reviewing findings later

---

# Saving Results as HTML

Nikto can generate reports in HTML format.

Example:

```
nikto -h 192.168.1.10 -o report.html -Format htm
```

This creates a browser-readable report.

HTML reports are useful for:

- Professional security reports
- Sharing findings with clients
- Visual review of scan results

---

# Scanning a Domain Name

Nikto can scan a target using a hostname instead of an IP address.

Example:

```
nikto -h example.com
```

Nikto will perform the scan against:

```
example.com
```

This is common when testing real-world web applications.

---

# Running a Specific Scan Type

Nikto allows selecting specific categories of checks using the `-Tuning` option.

Example:

```
nikto -h target -Tuning 9
```

This performs checks for:

```
Dangerous Files
```

---

# Nikto Tuning Option

The `-Tuning` option allows testers to control which types of checks Nikto performs.

|Value|Scan Type|
|---|---|
|`0`|File Upload|
|`1`|Interesting Files|
|`2`|Misconfiguration|
|`3`|Information Disclosure|
|`4`|Injection|
|`5`|Authentication|
|`6`|Denial of Service|
|`9`|Dangerous Files|

---

## Example: Misconfiguration Scan

```
nikto -h target -Tuning 2
```

This focuses only on:

```
Misconfigurations
```

Examples:

- Incorrect server settings
- Default configurations
- Unsafe options

---

## Example: Dangerous Files Scan

```
nikto -h target -Tuning 9
```

This focuses on finding:

- Backup files
- Sensitive files
- Dangerous default resources

---

# Using Nikto Through a Proxy (Burp Suite)

Nikto traffic can be routed through a proxy such as Burp Suite.

Example:

```
nikto -h target -useproxy http://127.0.0.1:8080
```

This sends all Nikto requests through:

```
Burp Suite Proxy
127.0.0.1:8080
```

---

# Why Use a Proxy During Testing?

Passing Nikto traffic through Burp Suite allows you to:

- Inspect HTTP requests
- Modify requests manually
- Analyze server responses
- Combine automated scanning with manual testing

This is useful for deeper web application assessments.

---

# Nikto in a Penetration Testing Workflow

A common web testing workflow:

## Step 1: Identify the Web Service

First, identify open web ports:

```
nmap -p 80,443 target
```

---

## Step 2: Run Nikto Scan

Perform automated web server enumeration:

```
nikto -h http://target
```

---

## Step 3: Analyze Findings

Review discovered issues such as:

```
- Exposed files
- Outdated versions
- Misconfigurations
- Sensitive directories
```

---

## Step 4: Perform Manual Testing

Use tools such as:

- Burp Suite
- Gobuster
- Dirb
- Manual HTTP testing

to investigate discovered issues further.

---

# Summary

`Nikto` is an open-source Web Server Scanner used to identify common security weaknesses in web servers.

Key points:

- Used during Web Enumeration.
- Detects:
    - Sensitive files
    - Misconfigurations
    - Outdated software
    - Known vulnerabilities
    - Dangerous directories
- Supports:
    - HTTP and HTTPS scanning
    - Custom ports
    - Report generation
    - Scan customization
    - Proxy integration

Important options:

```
-h              → Target host
-p              → Specify port
-ssl            → Use HTTPS
-o              → Save output
-Format htm     → Generate HTML report
-Tuning         → Select scan categories
-useproxy       → Use proxy server
```

Nikto is a valuable first-pass scanner that helps penetration testers quickly identify potential weaknesses before moving to deeper manual analysis.
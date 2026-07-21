# WhatWeb

## What is WhatWeb?

WhatWeb is a web fingerprinting tool used during the **Reconnaissance / Information Gathering** phase to identify the technologies running behind a website.

In simple terms:

> It fingerprints a website to reveal the technologies and software it uses.

---

# What Does WhatWeb Do?

WhatWeb can identify information such as:

- Web Server (Apache, Nginx, IIS, etc.)
- Programming Language or Framework (PHP, ASP.NET, Node.js, Ruby on Rails, etc.)
- Content Management System (CMS) (WordPress, Joomla, Drupal, etc.)
- Security Technologies (such as WAFs or security headers)
- Plugins and third-party components
- Cookies and session technologies
- Software versions (when exposed)

---

# How Does WhatWeb Work?

To scan a website, run:

```bash
whatweb example.com
```

When executed, WhatWeb:

1. Sends HTTP requests to the target website.
2. Analyzes the HTTP responses.
3. Looks for technology fingerprints, including:
   - HTTP headers
   - HTML source code
   - Meta tags
   - Cookies
   - JavaScript files
   - File paths
   - Error messages
4. Compares the collected fingerprints against its built-in database to identify the technologies in use.

---

# Example Output

```text
http://example.com [200 OK]
Apache[2.4.41]
PHP[7.4.3]
WordPress
jQuery[3.5.1]
```

---

# Output Explanation

| Result | Meaning |
|---------|---------|
| Apache | Web server |
| PHP | Server-side programming language |
| WordPress | Content Management System (CMS) |
| jQuery | JavaScript library |

---

# Why is WhatWeb Important?

WhatWeb helps you:

- Understand the target's technology stack.
- Identify outdated software or components.
- Search for known vulnerabilities related to detected versions.
- Choose the most appropriate exploitation tools.
- Build a more effective attack plan during the reconnaissance phase.

For example, if WhatWeb detects:

```text
WordPress 5.2
```

You can continue with tools such as:

```text
WPScan
```

to enumerate:

- Users
- Plugins
- Themes
- Known vulnerabilities

---

# Verbose Mode

To display more detailed information:

```bash
whatweb -v example.com
```

## `-v`

**Verbose Mode**

Displays additional details about detected technologies, including the fingerprints and evidence used during identification.

---

# Useful Options

## Scan Multiple Websites

To scan multiple targets from a file:

```bash
whatweb targets.txt
```

The `targets.txt` file should contain one website per line.

---

## Increase the Aggression Level

```bash
whatweb -a 3 example.com
```

## `-a`

**Aggression Level**

Controls how aggressively WhatWeb fingerprints the target.

Higher levels send more requests and perform deeper analysis.

### Aggression Levels

| Level | Description |
|---------|-------------|
| 1 | Passive and fast |
| 3 | Balanced (commonly used) |
| 4 | More aggressive |
| 5 | Most aggressive (more requests and a higher chance of detection) |

---

## Disable Colored Output

```bash
whatweb --no-colour example.com
```

Useful when redirecting the output to a file.

---

## Save the Results

Save the output directly to a file:

```bash
whatweb example.com > results.txt
```

or

```bash
whatweb -v example.com | tee results.txt
```

---

# Typical Penetration Testing Workflow

```text
whatweb example.com
        │
        ▼
Identify technologies
        │
        ▼
nmap -sV target
        │
        ▼
Identify open services
        │
        ▼
wpscan --url http://example.com
        │
        ▼
(If WordPress is detected)
        │
        ▼
Search for known vulnerabilities and continue enumeration
```

---

# Summary

WhatWeb is a fast and lightweight web fingerprinting tool that helps identify:

- Web servers
- Programming languages
- Frameworks
- CMS platforms
- Plugins
- Security technologies
- Software versions

It is one of the most valuable reconnaissance tools for understanding a target before performing a web application security assessment.
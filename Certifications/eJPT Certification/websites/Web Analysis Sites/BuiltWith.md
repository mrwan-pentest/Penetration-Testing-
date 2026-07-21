
# BuiltWith

## What is BuiltWith?

**BuiltWith** is a **web technology profiling** tool used during the **Reconnaissance (Information Gathering)** phase of a penetration test.

Its primary purpose is to identify the technologies, frameworks, services, and third-party components used by a website.

Unlike vulnerability scanners, BuiltWith focuses on **technology identification**, helping you understand the target's technology stack before beginning deeper enumeration or exploitation.

---

# Why is BuiltWith Important?

As a penetration tester, understanding the technologies behind a website helps you:

- Identify the target's technology stack.
- Discover potential attack surfaces.
- Detect outdated frameworks or libraries.
- Identify CMS platforms.
- Recognize third-party services.
- Choose the appropriate enumeration and exploitation tools.

For example:

If BuiltWith detects:

```text
WordPress
```

You may continue with:

```text
WPScan
```

If it detects:

```text
Drupal
```

You might search for:

```text
Drupalgeddon vulnerabilities
```

---

# What Information Does BuiltWith Provide?

BuiltWith can identify information such as:

- Web Server
- Programming Languages
- CMS Platforms
- JavaScript Libraries
- Frameworks
- Analytics Services
- CDN Providers
- SSL Providers
- Advertising Networks
- Payment Platforms
- Hosting Providers
- DNS Services
- Third-party Widgets
- Security Technologies

---

# Example Information

## Web Server

Examples:

```text
Apache
Nginx
Microsoft IIS
```

---

## Programming Languages

Examples:

```text
PHP
ASP.NET
Node.js
Python
Ruby
Java
```

---

## CMS

Examples:

```text
WordPress
Drupal
Joomla
Magento
Shopify
```

---

## JavaScript Libraries

Examples:

```text
jQuery
React
Vue.js
Angular
Bootstrap
```

---

## CDN

Examples:

```text
Cloudflare
CloudFront
Fastly
Akamai
```

---

## Analytics

Examples:

```text
Google Analytics
Google Tag Manager
Hotjar
Mixpanel
```

---

## Payment Platforms

Examples:

```text
Stripe
PayPal
Square
```

---

## Security Technologies

Examples:

```text
Cloudflare
Sucuri
Imperva
reCAPTCHA
```

---

# Example Workflow

Suppose you analyze a website using BuiltWith.

The results may indicate:

```text
CMS:
WordPress

Web Server:
Apache

Language:
PHP

JavaScript:
jQuery

CDN:
Cloudflare
```

From this information, you can plan your next steps:

- Enumerate WordPress.
- Identify the WordPress version.
- Enumerate plugins and themes.
- Search for known vulnerabilities.
- Check whether Cloudflare is hiding the origin server.

---

# How to Use BuiltWith

BuiltWith is primarily available as a web service.

Simply visit:

```text
https://builtwith.com
```

Then enter the target domain:

```text
example.com
```

The site will analyze the target and display the detected technologies.

---

# Browser Extension

BuiltWith is also available as a browser extension.

Once installed, clicking the extension while visiting a website instantly displays the technologies used by that site.

---

# Installing the Browser Extension

## Google Chrome

1. Open the Chrome Web Store.
2. Search for:

```text
BuiltWith Technology Profiler
```

3. Click:

```text
Add to Chrome
```

4. Confirm by selecting:

```text
Add Extension
```

---

## Microsoft Edge

1. Open the Edge Add-ons Store.
2. Search for:

```text
BuiltWith Technology Profiler
```

3. Click:

```text
Get
```

4. Install the extension.

---

## Firefox

BuiltWith is also available for Firefox through the Firefox Add-ons store.

Search for:

```text
BuiltWith
```

Then install it like any other browser extension.

---

# Typical Penetration Testing Workflow

```text
BuiltWith
        ↓
Identify Technologies
        ↓
WhatWeb
        ↓
Fingerprint Web Server
        ↓
Nmap
        ↓
Identify Open Ports & Services
        ↓
WPScan / CMSmap
        ↓
Enumerate CMS
        ↓
Search for Known Vulnerabilities
        ↓
Exploitation
```

---

# BuiltWith vs WhatWeb

| Feature | BuiltWith | WhatWeb |
|----------|-----------|----------|
| Web-based | ✅ | ❌ |
| Command-line | ❌ | ✅ |
| Browser Extension | ✅ | ❌ |
| CMS Detection | ✅ | ✅ |
| Framework Detection | ✅ | ✅ |
| Plugin Detection | ✅ | ✅ |
| Technology Fingerprinting | ✅ | ✅ |
| Automation | ❌ | ✅ |
| Useful in Scripts | ❌ | ✅ |

---

# Advantages

- Easy to use.
- No installation required when using the website.
- Provides detailed technology information.
- Detects many third-party services.
- Excellent for reconnaissance.
- Browser extension allows quick technology identification.

---

# Limitations

- Does not identify vulnerabilities directly.
- Some advanced features require a paid subscription.
- Detection accuracy depends on publicly exposed technologies.
- Cannot replace active enumeration tools like WhatWeb or Nmap.

---

# Summary

BuiltWith is a web technology profiling tool used during the **Reconnaissance** phase of a penetration test.

It helps identify:

- Web Servers
- Programming Languages
- Frameworks
- CMS Platforms
- JavaScript Libraries
- Analytics Services
- CDN Providers
- Security Technologies
- Third-party Components

Understanding the target's technology stack allows penetration testers to select the most appropriate enumeration and exploitation techniques before attempting to identify vulnerabilities.
# Anthem (TryHackMe)

# Overview

**Anthem** is a beginner-friendly Windows CTF focused on **OSINT, Web Enumeration, Information Disclosure, Windows Access Control, and basic Privilege Escalation**.

Unlike machines that rely heavily on exploitation, Anthem emphasizes the importance of careful observation. Many of the required credentials and hints are hidden in plain sight, rewarding attackers who thoroughly inspect web pages, source code, and system files.

Throughout this machine, we perform:

- Web Enumeration
- robots.txt Enumeration
- CMS Enumeration
- OSINT
- RDP Authentication
- Windows File Permission Abuse
- Administrator Account Compromise

---

# Skills Covered

- Nmap Enumeration
- Web Enumeration
- robots.txt Enumeration
- CMS Discovery
- OSINT
- Information Disclosure
- Source Code Analysis
- RDP Authentication
- Windows File Permissions
- Administrator Compromise


---

# Nmap Scan

We began by scanning the target to identify the exposed services.

![](../Images/Pasted%20image%2020260724234804.png)

The scan revealed two open ports:

```text
80   HTTP
3389 RDP
```

The presence of an HTTP service suggested that the initial attack surface would be the website.

---

# Web Enumeration

We navigated to the website to inspect its content.

![](../Images/Pasted%20image%2020260724235153.png)

One of the first files worth checking during web enumeration is:

```text
robots.txt
```

This file is commonly used to instruct search engines which pages should not be indexed.

Although intended for search engines, it often leaks interesting directories or sensitive information.

---

# robots.txt Enumeration

We browsed to:

```text
/robots.txt
```

![](../Images/Pasted%20image%2020260724235243.png)

Inside the file we discovered:

- Hidden directories
- Sensitive information
- A password
- A reference to an administrative portal

One of the disclosed paths was:

```text
/umbraco
```

---

# Discovering the CMS

Browsing to the Umbraco directory revealed an administrator login page.

![](../Images/Pasted%20image%2020260724235558.png)

## What is Umbraco?

**Umbraco** is an open-source **Content Management System (CMS)** built on Microsoft's .NET platform. It enables administrators to manage website content through a web-based interface.

---

# Domain Enumeration

The first question required identifying the website's domain.

This information was available directly on the homepage.

![](../Images/Pasted%20image%2020260724235701.png)

---

# Username Enumeration

Next, we needed to identify the administrator's username and email address.

From the homepage, we opened the article titled:

```text
READ THIS ARTICLE
```

![](../Images/Pasted%20image%2020260724235927.png)

The article contained a poem.

![](../Images/Pasted%20image%2020260725000120.png)

Rather than ignoring it, we treated it as a potential OSINT clue.

Searching the poem online led us to the identity of its author.

![](../Images/Pasted%20image%2020260725000222.png)

From this, we successfully identified the administrator's username:

```text
Solomon Grundy
```

---

# Email Enumeration

The administrator's email address was still unknown.

While browsing another page, we discovered the following employee information:

```text
Jane Doe
JD@anthem.com
```

![](../Images/Pasted%20image%2020260725000349.png)

This revealed the company's email naming convention:

```text
First Initial + Last Initial
```

Applying the same pattern to the administrator:

```text
Solomon Grundy
```

We inferred the administrator's email address to be:

```text
SG@anthem.com
```

![](../Images/Pasted%20image%2020260725000810.png)

---

# Flag Collection

## First Flag

The first flag was hidden inside the page source.

![](../Images/Pasted%20image%2020260725002420.png)

---

## Second Flag

The second flag was located in the source code of the homepage.

![](../Images/Pasted%20image%2020260725002608.png)

---

## Third Flag

The third flag was found on **Jane Doe's Author Page**.

![](../Images/Pasted%20image%2020260725002754.png)

---

## Fourth Flag

The fourth flag was hidden inside the source code of the **IT Department** page.

![](../Images/Pasted%20image%2020260725003024.png)

---

# RDP Access

At this stage, we had recovered valid credentials.

Since Remote Desktop Protocol was enabled, we attempted authentication via RDP.

![](../Images/Pasted%20image%2020260725001106.png)

The login was successful.

---

# User Flag

After logging in, we located the user flag.

![](../Images/Pasted%20image%2020260725001145.png)

---

# Searching for Administrator Credentials

The challenge hint indicated that the administrator password was **hidden**.

This suggested that we should search for hidden files.

Windows allows hidden files to be displayed through:

```text
View
    ↓
Hidden items
```

![](../Images/Pasted%20image%2020260725001353.png)

After enabling hidden files, we discovered a hidden directory named:

```text
backup
```

![](../Images/Pasted%20image%2020260725001446.png)

Inside was a text file.

However, we did not have permission to read it.

![](../Images/Pasted%20image%2020260725001530.png)

---

# Abusing File Permissions

Instead of giving up, we inspected the file permissions.

From the file properties:

```text
Properties
    ↓
Security
```

We added our own user account:

```text
SG
```

![](../Images/Pasted%20image%2020260725001627.png)

We then granted ourselves Full Control over the file.

![](../Images/Pasted%20image%2020260725001751.png)

After modifying the permissions, we were finally able to open the file.

Inside, we found the administrator password.

![](../Images/Pasted%20image%2020260725001826.png)

---

# Administrator Access

Using the recovered credentials, we logged in as the Administrator via RDP.

![](../Images/Pasted%20image%2020260725001917.png)

The final administrator flag was successfully retrieved.

![](../Images/Pasted%20image%2020260725001941.png)

---

# Summary

This machine demonstrated how **information disclosure and OSINT can be just as valuable as software vulnerabilities**.

Rather than exploiting a technical flaw, the attack relied on carefully collecting small pieces of publicly available information and combining them to compromise the system.

## Skills Practiced

- Nmap Enumeration
- robots.txt Enumeration
- CMS Discovery
- Umbraco Enumeration
- OSINT
- Source Code Inspection
- Information Disclosure
- Email Enumeration
- RDP Authentication
- Windows File Permission Abuse
- Administrator Compromise

# Machine Compromised Successfully ✔
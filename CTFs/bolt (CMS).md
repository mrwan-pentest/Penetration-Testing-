# Bolt CMS

## Overview

**Bolt CMS** is a lightweight **Content Management System (CMS)** used to create and manage dynamic websites. Like **WordPress** and **Drupal**, it provides an administrative interface that allows users to publish and manage website content without developing a website from scratch.

A **CMS** is a category of software designed to simplify website management, while **Bolt** is one specific CMS within that category.

---

## Objective

The objective of this lab was to enumerate the target, recover valid credentials, identify the installed Bolt CMS version, exploit a known vulnerability using Metasploit, and obtain remote access to the target.

---

## Nmap Scan

Performed an Nmap scan to identify the exposed services and open ports.

The scan revealed that the web service was running on **port 8000**.

![](Penetration%20Testing/Images/Pasted%20image%2020260419095204.png)

---

## Credential Discovery

Recovered a valid password.

![](Penetration%20Testing/Images/Pasted%20image%2020260419095350.png)

Recovered a valid username.

![](Penetration%20Testing/Images/Pasted%20image%2020260419095431.png)

---

## Login Page Discovery

Located the Bolt CMS login page using Google search.

Authenticated successfully using the recovered credentials and identified the installed Bolt CMS version.

---

## Vulnerability Research

Searched for publicly available exploits using **SearchSploit**.

A corresponding **Metasploit** module was found for the identified Bolt CMS version.

![](Penetration%20Testing/Images/Pasted%20image%2020260419095842.png)

---

## Exploitation

Executed the Metasploit module to exploit the vulnerability.

Successfully obtained a remote session on the target.

![](Penetration%20Testing/Images/Pasted%20image%2020260419095928.png)

![](Penetration%20Testing/Images/Pasted%20image%2020260419095946.png)

---

## Notes

### Bolt CMS

Bolt CMS is a lightweight Content Management System (CMS) used to build and manage websites through an administrative interface.

### SearchSploit

SearchSploit is an offline utility included with Kali Linux that allows searching the Exploit-DB database locally for publicly available exploits.

### Metasploit

Metasploit is an exploitation framework used to validate vulnerabilities and gain remote access through publicly available exploit modules.
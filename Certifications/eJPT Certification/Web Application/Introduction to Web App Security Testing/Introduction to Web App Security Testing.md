# Web Applications & Web Security

## What is a Web Application?

A **Web Application** is software that runs on a **Web Server** and is accessed through a web browser.

### Examples

- Gmail
- Facebook
- Amazon
- Office 365

---

## How Does It Work?

```text
Browser
   │
HTTP/HTTPS
   │
Web Server
   │
Database
```

The user sends an **HTTP Request**.

The server processes the request and returns an **HTTP Response**.

---

## Front-End Components

### HTML

Builds the structure of the webpage.

### CSS

Controls the design and appearance.

### JavaScript

Adds interactivity and dynamic behavior.

---

## Client-Server Architecture

- **Client:** Web Browser
- **Server:** Web Server

The client sends requests.

The server processes them and returns responses.

---

## Stateless HTTP

HTTP is a **stateless protocol**, meaning it does not remember previous requests.

To maintain user sessions, web applications use:

- Cookies
- Sessions
- Tokens

---

# Web Application Security

The goal of Web Application Security is to protect:

## Confidentiality

Ensuring sensitive information remains private.

---

## Integrity

Preventing unauthorized modification of data.

---

## Availability

Keeping services accessible and operational.

---

## Why Are Web Applications Attractive Targets?

Web applications often store sensitive information such as:

- User Accounts
- Passwords
- Credit Card Information
- Personal Data

Since they are exposed to the Internet, they are common attack targets.

---

# Threat vs Risk

## Threat

Anything capable of causing damage.

### Examples

- Hackers
- Malware
- Phishing Attacks

---

## Risk

The likelihood and impact of a threat exploiting a vulnerability.

```text
Threat + Vulnerability = Risk
```

---

# Common Web Application Threats

## SQL Injection (SQLi)

Injecting SQL statements into an application.

May allow attackers to:

- Read data
- Modify data
- Delete data

---

## Cross-Site Scripting (XSS)

Injecting JavaScript into web pages.

May lead to:

- Cookie theft
- Session hijacking
- Account compromise

---

## Cross-Site Request Forgery (CSRF)

Forcing an authenticated user to perform actions without their knowledge.

### Examples

- Changing passwords
- Updating account settings

---

## Security Misconfiguration

Incorrect or insecure application settings.

### Examples

- Default credentials
- Debug Mode enabled
- Exposed administration pages

---

## Sensitive Data Exposure

Leaking confidential information such as:

- Passwords
- Personal Information
- Payment Data

---

## Brute Force Attacks

Repeatedly attempting passwords until the correct one is found.

---

## Credential Stuffing

Using leaked credentials from previous breaches to access other accounts.

---

## File Upload Vulnerabilities

Uploading malicious files instead of legitimate ones.

May lead to:

```text
Remote Code Execution (RCE)
Web Shell Upload
```

---

## Server-Side Request Forgery (SSRF)

Forcing the server to send requests on behalf of the attacker.

Possible targets include:

- Internal Services
- Cloud Metadata Services
- Internal Networks

---

## Denial of Service (DoS / DDoS)

Overwhelming a server with excessive requests.

### Goal

Disrupt or completely stop the service.

---

## Broken Access Control

Improper authorization controls that allow unauthorized access.

### Example

A regular user can access another user's data or the administrator panel.

---

# Web Application Security Testing

The process of identifying:

- Vulnerabilities
- Weaknesses
- Security Risks

before attackers can exploit them.

---

## Vulnerability Scanning

Automated scanning using specialized tools.

Typically searches for:

- SQL Injection
- Cross-Site Scripting (XSS)
- Security Misconfigurations
- Outdated Software Versions

---

## Penetration Testing

Simulating real-world attacks.

### Goal

Verify whether discovered vulnerabilities can actually be exploited.

---

## Code Review

Reviewing application source code to identify:

- Programming Errors
- Security Vulnerabilities
- Insecure Configurations

---

## Authentication Testing

Testing the application's authentication mechanism.

The main question is:

```text
Are you really who you claim to be?
```

---

## Authorization Testing

Testing user permissions.

The main question is:

```text
Are you authorized to access this resource?
```

---

## Input Validation Testing

Testing how the application handles user input.

Critical for preventing:

- SQL Injection (SQLi)
- Cross-Site Scripting (XSS)

---

## Session Management Testing

Evaluating how user sessions are handled.

Looking for issues such as:

- Session Hijacking
- Session Fixation

---

## API Security Testing

Assessing the security of application APIs.

Primary focus areas include:

- Authentication
- Authorization
- Data Exposure

---

# Security Testing vs Penetration Testing

## Security Testing

### Goal

```text
Finding Vulnerabilities
```

Focuses on identifying security weaknesses.

Can be performed manually or automatically.

---

## Penetration Testing

### Goal

```text
Exploiting Vulnerabilities
```

Focuses on exploiting discovered vulnerabilities to verify their real-world impact.
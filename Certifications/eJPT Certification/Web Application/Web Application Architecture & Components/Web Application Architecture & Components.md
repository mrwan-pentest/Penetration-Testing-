# Web Technologies

As a penetration tester, you will work daily with technologies such as:

- HTML
- JavaScript
- Cookies
- APIs
- Databases
- Web Servers

Therefore, you should understand:

- Where each technology operates.
- What its purpose is.
- How it can potentially be exploited.

---

# Client-Side Technologies

Client-side technologies run inside the user's web browser.

---

## HTML

HTML (**HyperText Markup Language**) is the standard language used to build web pages.

It is used to create:

- Headings
- Buttons
- Forms
- Tables

### Why is HTML important for penetration testers?

HTML pages may contain valuable information such as:

- Hidden Fields
- HTML Comments
- Sensitive Information embedded in the page source

---

## CSS

CSS (**Cascading Style Sheets**) controls the appearance of a web page.

It defines:

- Colors
- Fonts
- Sizes
- Layout and positioning

CSS rarely contains direct vulnerabilities, but it may reveal:

- Hidden files
- Internal paths
- Directory structures

---

## JavaScript

JavaScript is the programming language executed inside the browser.

It is commonly used for:

- User interaction
- Input validation
- Updating web pages without reloading (AJAX)

### Why is JavaScript important?

JavaScript files may expose valuable information, including:

- API Endpoints
- API Keys
- Hidden Functions
- Client-side logic that may be bypassed

---

## Cookies

Cookies are small pieces of data stored by the browser.

They are commonly used for:

- Session Management
- Remembering Users
- Storing User Preferences

### Security Importance

Stealing session cookies may lead to:

- Session Hijacking

---

## Local Storage

Local Storage is browser storage used to save data locally.

### Difference Between Cookies and Local Storage

- Local Storage is **not automatically sent** to the server.
- Data remains stored only within the browser.

It may contain sensitive information such as:

- JWT Tokens
- API Keys

---

# Server-Side Technologies

Server-side technologies execute on the web server.

---

## Web Server

### Examples

- Apache
- Nginx
- IIS

### Responsibilities

- Receiving HTTP Requests
- Serving static content
- Forwarding requests to the application

Think of it as the **front door** of a website.

---

## Application Server

The Application Server runs the application's code.

### Responsibilities

- Executing application logic
- Processing requests
- Communicating with databases

Think of it as the **brain** of the application.

---

## Database Server

The Database Server stores application data.

### Examples

- MySQL
- PostgreSQL
- Microsoft SQL Server (MSSQL)
- Oracle Database

Typical stored information includes:

- Users
- Passwords
- Products
- Orders

### Common Related Vulnerability

```text
SQL Injection (SQLi)
```

---

## Server-Side Languages

These languages execute on the server.

### Common Languages

- PHP
- Python
- Java
- Ruby

Knowing the backend language helps identify:

- File structures
- Error messages
- Potential vulnerabilities

---

# Communication & Data Flow

The typical communication process is:

```text
Browser
    │
HTTP Request
    │
Web Server
    │
Application
    │
Database
    │
HTTP Response
    │
Browser
```

---

# Data Interchange

Data interchange refers to exchanging information between different systems.

### Examples

- A website communicating with PayPal
- An application using Google Maps APIs

Modern web applications constantly exchange data with external services.

---

# API (Application Programming Interface)

API stands for:

```text
Application Programming Interface
```

An API allows different systems and applications to communicate with each other.

### Example

A weather application requests weather information from a weather API.

### Security Perspective

For penetration testers, APIs are primary assessment targets.

---

# Data Formats

## JSON

JSON (**JavaScript Object Notation**) is the most commonly used data format today.

### Advantages

- Lightweight
- Fast
- Human-readable

Widely used in REST APIs.

---

## XML

XML (**eXtensible Markup Language**) is an older and more verbose format.

Commonly used with:

- SOAP Services
- Legacy Applications

### Related Vulnerability

```text
XML External Entity (XXE)
```

---

# REST

REST (**Representational State Transfer**) is the most common architectural style for building web APIs.

REST primarily relies on HTTP methods.

---

## GET

Retrieves data from the server.

---

## POST

Creates or submits new data.

---

## PUT

Updates existing resources.

---

## DELETE

Deletes resources.

---

# SOAP

SOAP (**Simple Object Access Protocol**) is an older protocol based on XML.

Although less common than REST, it is still used in:

- Enterprise Environments
- Legacy Systems

---

# Security Technologies

## Authentication

Authentication verifies a user's identity.

The primary question is:

```text
Who are you?
```

### Examples

- Username
- Password

---

## Authorization

Authorization determines what an authenticated user is allowed to do.

The primary question is:

```text
What are you allowed to access?
```

### Example

Can a normal user access the administrator dashboard?

---

## SSL/TLS

SSL/TLS is responsible for encrypting communications.

It secures:

```text
HTTP → HTTPS
```

SSL/TLS protects:

- Passwords
- Sessions
- Sensitive Data

while they are transmitted across the network.

---

# External Technologies

## CDN (Content Delivery Network)

A CDN is a distributed network of servers located around the world.

### Purpose

- Speed up website loading
- Reduce the load on the origin server

---

## Third-Party Libraries

Developers often rely on external libraries to simplify development.

### Examples

- jQuery
- Bootstrap
- React Packages

### Security Importance

Outdated libraries may contain publicly known vulnerabilities and should always be assessed during penetration testing.
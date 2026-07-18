

## What is Request Manipulation?

Request Manipulation is the process of modifying an HTTP request before it reaches the web server.

Instead of sending the request exactly as the browser creates it, an attacker intercepts and changes parts of the request.

---

## Basic Idea

Normal user request:

```http
POST /change-password

username=john
password=123456
```

Modified request:

```http
POST /change-password

username=admin
password=123456
```

The attacker changes the request and observes how the application responds.

---

## Why Is It Important?

Some applications trust user-supplied data.

If the server does not properly validate requests, an attacker may:

- Access unauthorized data
    
- Modify prices
    
- Change account information
    
- Escalate privileges
    
- Bypass security controls
    

---

## Common Targets

### URL Parameters

Original:

```http
GET /profile?id=10
```

Modified:

```http
GET /profile?id=11
```

---

### POST Parameters

Original:

```http
price=500
```

Modified:

```http
price=5
```

---

### Cookies

Original:

```http
role=user
```

Modified:

```http
role=admin
```

---

### HTTP Headers

Original:

```http
X-Forwarded-For: 192.168.1.5
```

Modified:

```http
X-Forwarded-For: 127.0.0.1
```

---

## Is Request Manipulation a Vulnerability?

No.

Request Manipulation is a technique.

It is used to discover vulnerabilities such as:

- IDOR
    
- Access Control Issues
    
- Business Logic Flaws
    
- Price Manipulation
    
- Privilege Escalation
    
- Authentication Bypass
    

---

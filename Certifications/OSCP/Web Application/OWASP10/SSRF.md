
# Server-Side Request Forgery (SSRF)

## What is SSRF?

**SSRF (Server-Side Request Forgery)** is a web vulnerability that allows an attacker to force the **server** to send HTTP requests to destinations chosen by the attacker.

Instead of the attacker sending the request directly, the vulnerable server sends it on the attacker's behalf.

---

## How Does SSRF Work?

Normally:

```text
Attacker
    │
    ▼
Web Application
    │
    ▼
External Website
```

With SSRF:

```text
Attacker
    │
    ▼
Vulnerable Web Application
    │
    ├──► Internal Server
    ├──► Database
    ├──► Cloud Metadata Service
    └──► Other Internal Resources
```

The attacker controls the URL that the server requests.

---

# Why is SSRF Dangerous?

The server usually has access to resources that attackers cannot reach directly.

An attacker may be able to access:

- Internal applications
- Private APIs
- Internal web servers
- Cloud metadata services
- Localhost services
- Sensitive files (in some cases)

---

# Example

Suppose a website has the following feature:

```text
https://example.com/fetch?url=https://google.com
```

The application downloads the URL provided by the user.

Instead of supplying:

```text
https://google.com
```

An attacker sends:

```text
http://127.0.0.1/admin
```

The server then requests:

```text
http://127.0.0.1/admin
```

Since the request comes from the server itself, it may access resources that are normally inaccessible to external users.

---

# Common SSRF Targets

## Localhost

```text
http://127.0.0.1
```

or

```text
http://localhost
```

---

## Internal Network

```text
http://192.168.1.10
```

```text
http://10.0.0.5
```

```text
http://172.16.0.1
```

---

## Cloud Metadata Services

AWS:

```text
http://169.254.169.254/latest/meta-data/
```

Azure:

```text
http://169.254.169.254/metadata/
```

Google Cloud:

```text
http://169.254.169.254/computeMetadata/v1/
```

These services may expose sensitive information such as temporary credentials if not properly protected.

---

# Typical SSRF Payloads

```text
http://127.0.0.1
```

```text
http://localhost
```

```text
http://169.254.169.254/latest/meta-data/
```

```text
http://192.168.1.1
```

---

# Possible Impacts

An attacker may be able to:

- Access internal applications
- Enumerate internal services
- Read cloud metadata
- Interact with internal APIs
- Bypass firewall restrictions
- In some cases, achieve Remote Code Execution (RCE)

---

# How to Identify SSRF

Look for features where the server fetches user-supplied URLs, such as:

- Import from URL
- Fetch Image
- URL Preview
- Webhooks
- PDF Generation
- Avatar Upload by URL
- RSS Feed Import
- API Integrations

Example:

```text
GET /fetch?url=https://example.com
```

or

```text
POST /download
```

Body:

```text
url=https://example.com/file.pdf
```

---

# Prevention

To prevent SSRF:

- Validate user-supplied URLs.
- Allow requests only to trusted domains (Allowlist).
- Block access to internal IP ranges.
- Block access to localhost.
- Restrict access to cloud metadata services.
- Disable unnecessary outbound connections from the server.
- Use network segmentation and firewalls.

---

# Summary

- **SSRF** allows an attacker to make the **server** send HTTP requests to arbitrary destinations.
- It is commonly used to access **internal systems**, **private APIs**, and **cloud metadata services**.
- SSRF can lead to **information disclosure**, **internal network enumeration**, and sometimes even **Remote Code Execution (RCE)**.
---
# SSRF Lab

## Step 1: Identify the SSRF Vulnerability

First, we intercepted the request using **Burp Suite** after discovering that the vulnerable functionality was the **Check Stock** feature.

![](../../../../Images/Pasted%20image%2020260727230401.png)

---

## Step 2: Identify the Internal IP Range

After analyzing the application, we discovered that the **Admin** interface was only accessible from an internal IP address within the following range:

```text
192.168.0.x
```

![](../../../../Images/Pasted%20image%2020260727230528.png)

---

## Step 3: Discover the Internal Host

Since the last octet (`x`) was unknown, we used **Burp Intruder** to brute-force all possible values.

We sent the intercepted request to **Intruder** and configured the payload to test every IP address in the range:

```text
192.168.0.1 → 192.168.0.255
```

![](../../../../Images/Pasted%20image%2020260727230728.png)

---

## Step 4: Identify the Correct Host

After the attack completed, we analyzed the responses.

Most requests returned error responses, but one request returned:

```text
HTTP Status: 200 OK
```

This indicated that we had successfully discovered the internal server hosting the **Admin Panel**.

![](../../../../Images/Pasted%20image%2020260727231649.png)

---

## Step 5: Access the Admin Panel

After identifying the correct internal IP address, we modified the SSRF payload to target the discovered Admin interface.

The server forwarded our request, allowing us to access the **Admin Panel** successfully.

From there, we deleted the target user and completed the lab.

![](../../../../Images/Pasted%20image%2020260727231842.png)

---

# Summary

1. Intercepted the **Check Stock** request.
2. Identified the internal IP range (`192.168.0.x`).
3. Used **Burp Intruder** to brute-force the last octet.
4. Identified the valid host by observing an **HTTP 200 OK** response.
5. Accessed the internal **Admin Panel** via SSRF.
6. Deleted the target user to complete the lab.
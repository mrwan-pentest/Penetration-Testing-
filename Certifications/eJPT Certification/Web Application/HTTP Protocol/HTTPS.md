# HTTPS (HyperText Transfer Protocol Secure)

## Why Do We Need HTTPS?

The primary weakness of standard HTTP is that it transmits data in **plain text**.

For example:

```http
POST /login HTTP/1.1

username=admin
password=123456
```

Anyone with access to the network traffic can read this information using packet capture or interception tools such as:

- Wireshark
- tcpdump
- Man-in-the-Middle (MITM) attacks

Sensitive information such as usernames, passwords, session cookies, and personal data can therefore be exposed.

---

# What is HTTPS?

HTTPS stands for:

```text
HyperText Transfer Protocol Secure
```

It is the secure version of HTTP that protects communication between:

```text
Browser  ⇄  Web Server
```

HTTPS provides confidentiality, integrity, and authentication by encrypting all HTTP traffic.

---

# How HTTPS Works

With standard HTTP, communication occurs directly between the browser and the web server.

```text
Browser
    │
   HTTP
    │
Web Server
```

With HTTPS, HTTP is encapsulated inside a secure TLS connection.

```text
Browser
    │
HTTP
    │
TLS / SSL
    │
Web Server
```

This additional security layer encrypts all transmitted data before it travels across the network.

---

# What are SSL and TLS?

## SSL (Secure Sockets Layer)

SSL stands for:

```text
Secure Sockets Layer
```

SSL was the original protocol designed to secure network communications.

Today, SSL is considered obsolete due to known security weaknesses.

---

## TLS (Transport Layer Security)

TLS stands for:

```text
Transport Layer Security
```

TLS is the modern successor to SSL and is the protocol currently used to secure HTTPS connections.

Although the term **SSL Certificate** is still widely used, it almost always refers to a **TLS Certificate**.

---

# What Does TLS Provide?

TLS adds three fundamental security properties to HTTP communications:

- Confidentiality
- Integrity
- Authentication

---

# Confidentiality

Confidentiality ensures that transmitted data cannot be read by unauthorized parties.

Before encryption:

```text
password=123456
```

After encryption:

```text
a8f91x0d8f1s0df81...
```

Anyone intercepting the traffic will only see encrypted data that cannot be understood without the appropriate cryptographic keys.

---

# Integrity

Integrity ensures that transmitted data cannot be modified without detection.

For example, suppose the client sends:

```text
amount=100
```

An attacker attempts to modify the request during transmission:

```text
amount=10000
```

TLS performs integrity verification and detects any unauthorized modifications, causing the altered data to be rejected.

---

# Authentication

Authentication verifies that the client is communicating with the legitimate web server rather than an attacker.

Without authentication, an attacker could impersonate a trusted website and steal sensitive information.

To establish trust, HTTPS uses a **Digital Certificate** issued by a trusted Certificate Authority (CA).

The browser validates the certificate before establishing the encrypted connection, ensuring that the server's identity is authentic.
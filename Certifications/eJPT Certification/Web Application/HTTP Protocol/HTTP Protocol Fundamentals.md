# HTTP (HyperText Transfer Protocol)

## What is HTTP?

HTTP stands for:

```text
HyperText Transfer Protocol
```

It is the application-layer protocol responsible for communication between a web client and a web server.

```text
Browser  ⇄  Web Server
```

For example, when you visit:

```text
https://google.com
```

your browser does not directly understand the website.

Instead, it sends an **HTTP Request** to the web server, which processes the request and returns an **HTTP Response**.

---

# What is a Protocol?

A **protocol** is a standardized set of rules that defines how two systems communicate.

It can be thought of as a common language between two devices. If both parties do not follow the same protocol, communication cannot occur successfully.

---

# HTTP Runs on Top of TCP

Within the TCP/IP networking model, HTTP operates at the **Application Layer** and relies on TCP for reliable data transmission.

```text
Application Layer
        │
      HTTP
        │
       TCP
        │
        IP
```

HTTP defines how data is exchanged, while TCP ensures that the data is delivered reliably.

---

# Stateless Communication

One of the most important characteristics of HTTP is that it is **stateless**.

This means that the protocol does not remember previous requests.

For example:

1. A user submits a login request.
2. A second request is sent a few seconds later.

The server treats the second request as completely independent from the first unless additional mechanisms are used.

To maintain user state, modern web applications commonly use:

- Cookies
- Sessions
- Tokens

These mechanisms allow the server to recognize returning users across multiple requests.

---

# Client-Server Model

HTTP follows a **client-server architecture**.

## Client

The client is the application that sends requests to the server.

Common examples include:

- Google Chrome
- Mozilla Firefox
- Microsoft Edge

---

## Server

The server hosts the web application and processes incoming requests.

Examples include:

- Google
- Facebook
- Amazon

---

## Communication Flow

The communication process follows this sequence:

```text
Client
   │
HTTP Request
   │
Server
   │
HTTP Response
   │
Client
```

---

# URL and URI

Every resource available on a web server has an address.

Examples include:

```text
https://site.com/login
```

```text
https://site.com/images/logo.png
```

The server determines which resource the client is requesting based on the URL or URI provided in the request.

---

# HTTP Versions

## HTTP/1.0

HTTP/1.0 is the original widely adopted version of the protocol.

Its primary limitation was that it created a new TCP connection for every request.

---

## HTTP/1.1

HTTP/1.1 is the most widely used version of HTTP.

One of its most significant improvements is support for **Persistent Connections**.

This feature allows multiple HTTP requests to reuse the same TCP connection instead of creating a new one for each request, improving performance and reducing latency.

---

# How HTTP Communication Works

When a user visits a website, the communication process is as follows:

```text
Browser
    │
HTTP Request
    │
Web Server
    │
HTTP Response
    │
Browser
```

---

# HTTP Request

An **HTTP Request** is the message sent by the client to the server.

Example:

```http
GET / HTTP/1.1
Host: site.com
```

Meaning:

> Retrieve the website's home page.

---

# HTTP Response

An **HTTP Response** is the message returned by the server after processing the client's request.

Example:

```http
HTTP/1.1 200 OK
```

The response typically includes resources such as:

- HTML
- CSS
- JavaScript
- Images
- JSON
- Other web content

---

# What is a Resource?

A **resource** is any object that can be requested from a web server.

Examples include:

The home page:

```text
/
```

A login page:

```text
/login
```

An image:

```text
/logo.png
```

An API endpoint:

```text
/api/users
```

---

# Carriage Return and Line Feed

HTTP messages use specific control characters to separate lines.

## Carriage Return (`\r`)

```text
Carriage Return
```

Moves the cursor back to the beginning of the current line.

---

## Line Feed (`\n`)

```text
Line Feed
```

Moves the cursor down to the next line.

---

## Carriage Return + Line Feed (`\r\n`)

```text
\r\n
```

Represents the standard line ending used in HTTP messages.

It functions similarly to pressing the **Enter** key.

Example:

```http
GET /login HTTP/1.1
Host: site.com
User-Agent: Firefox
```

Each line in an HTTP request or response is terminated using:

```text
\r\n
```
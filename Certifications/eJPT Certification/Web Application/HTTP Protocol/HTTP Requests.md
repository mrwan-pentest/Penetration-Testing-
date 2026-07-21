# HTTP Request Components

An HTTP request is typically composed of three main parts:

```text
Request Line
Headers
Body (Optional)
```

Example:

```http
GET /login HTTP/1.1
Host: example.com
User-Agent: Firefox
Cookie: session=123456

username=admin&password=123456
```

---

# 1. Request Line

The **Request Line** is the first line of every HTTP request.

It consists of three components:

```http
GET /login HTTP/1.1
```

---

## HTTP Method

```text
GET
```

Specifies the action that the client wants to perform.

Common HTTP methods include:

- GET
- POST
- PUT
- DELETE
- PATCH

---

## URL / Path

```text
/login
```

Specifies the requested resource or page.

---

## HTTP Version

```text
HTTP/1.1
```

Specifies the version of the HTTP protocol being used.

---

# 2. Request Headers

After the Request Line come the HTTP headers.

Each header follows the format:

```text
Header-Name: Value
```

Example:

```http
Host: google.com
User-Agent: Firefox
```

Headers provide additional information about the request to the web server.

---

# 3. Request Body

The **Request Body** is optional.

It is commonly used with methods such as:

```text
POST
PUT
PATCH
```

Example:

```http
POST /login HTTP/1.1

username=admin&password=123456
```

Everything below the headers represents the request body.

---

# Complete HTTP Request Example

```http
GET / HTTP/1.1
Host: www.google.com
User-Agent: Firefox
Accept: text/html
Accept-Encoding: gzip
Connection: keep-alive
```

---

## Request Breakdown

### Request Line

```http
GET / HTTP/1.1
```

---

### Headers

```http
Host: www.google.com
User-Agent: Firefox
Accept: text/html
Accept-Encoding: gzip
Connection: keep-alive
```

---

### Body

No body is included because **GET** requests typically do not contain one.

---

# HTTP Methods

## GET

Used to retrieve data from the server.

Example:

```http
GET /products
```

Meaning:

> Retrieve the list of products.

### Characteristics

- Read-only operation.
- Does not modify server-side data.

Example:

```http
GET /profile
```

---

## POST

Used to send data to the server.

Example:

```http
POST /login
```

Request Body:

```text
username=admin&password=123456
```

Common use cases:

- Login
- Registration
- File Upload

---

## PUT

Used to completely replace an existing resource.

Example:

```http
PUT /users/1
```

Suppose the current resource is:

```json
{
  "name": "Ali",
  "age": 20
}
```

Sending:

```json
{
  "name": "Ahmed",
  "age": 25
}
```

replaces the entire resource.

---

## PATCH

Used to modify only part of an existing resource.

Example:

```json
{
  "age": 25
}
```

Only the specified field is updated.

---

## DELETE

Used to remove a resource.

Example:

```http
DELETE /users/1
```

Meaning:

> Delete user with ID 1.

---

## HEAD

Similar to **GET**, but returns only the response headers without the response body.

Example:

```http
HEAD /file.zip
```

Useful for checking:

- File size
- Last modification date
- File existence

---

## OPTIONS

Returns the HTTP methods supported by the target resource.

Example:

```http
OPTIONS /api/users
```

Possible response:

```text
GET, POST, PUT, DELETE
```

This method is commonly used during enumeration.

---

# URL / Path

In the following request:

```http
GET /downloads/index.php HTTP/1.1
```

The path is:

```text
/downloads/index.php
```

The root page is always represented by:

```text
/
```

Examples:

```text
/login
/admin
/uploads
/api/users
```

---

# HTTP Protocol Version

In the request:

```http
GET / HTTP/1.1
```

The following component:

```text
HTTP/1.1
```

indicates the HTTP protocol version.

---

# Host Header

One of the most important HTTP headers.

Example:

```http
Host: www.google.com
```

A single web server may host multiple websites on the same IP address.

The **Host** header tells the server which website the client wants to access.

Example:

```text
One IP Address
│
├── google.com
├── mail.google.com
└── maps.google.com
```

The server uses the Host header to determine the correct website.

---

# User-Agent Header

Example:

```http
User-Agent: Firefox
```

The **User-Agent** header identifies:

- Browser type
- Browser version
- Operating system

Real-world example:

```http
User-Agent: Mozilla/5.0 (Windows NT 10.0)
```

---

# Accept Header

Example:

```http
Accept: text/html
```

The **Accept** header tells the server which content types the client can process.

Example:

```http
Accept: text/html
```

Indicates that the client expects HTML content.

---

# Accept-Encoding Header

Example:

```http
Accept-Encoding: gzip, deflate
```

This header informs the server that the client supports compressed responses.

The server may respond using:

```text
gzip
```

instead of uncompressed data.

Benefits include:

- Faster response times
- Reduced bandwidth usage

---

# Connection Header

Example:

```http
Connection: keep-alive
```

The **Connection** header controls whether the TCP connection remains open after the request.

```text
keep-alive
```

Instructs the server to keep the connection open for additional requests instead of closing it immediately.
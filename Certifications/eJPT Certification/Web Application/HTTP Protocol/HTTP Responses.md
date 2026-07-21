# HTTP Response

After a client (such as a web browser) sends an HTTP request, the web server processes it and returns an **HTTP Response**.

For example, the browser sends:

```http
GET / HTTP/1.1
Host: google.com
```

The server responds with:

```http
HTTP/1.1 200 OK
Content-Type: text/html

<html>...</html>
```

This message is known as an **HTTP Response**.

---

# HTTP Response Components

An HTTP response consists of three main parts:

```text
Status Line
Headers
Body
```

Example:

```http
HTTP/1.1 200 OK
Date: Fri, 13 Mar 2015 11:26:05 GMT
Content-Type: text/html
Content-Length: 258

<html>...</html>
```

---

# 1. Status Line

The **Status Line** is the first line of every HTTP response.

Example:

```http
HTTP/1.1 200 OK
```

It consists of three components:

## HTTP Version

```text
HTTP/1.1
```

Indicates the version of the HTTP protocol used by the server.

---

## Status Code

```text
200
```

A numerical code that indicates the outcome of the request.

---

## Status Message

```text
OK
```

A short textual description of the status code.

---

# Common HTTP Status Codes

## 200 OK

```http
200 OK
```

Indicates that the request was processed successfully.

---

## 301 Moved Permanently

```http
301 Moved Permanently
```

Indicates that the requested resource has been permanently moved to a new location.

Example:

```text
http://site.com
        ↓
https://site.com
```

---

## 302 Found

```http
302 Found
```

Indicates a temporary redirect.

The resource is temporarily available at a different location.

---

## 400 Bad Request

```http
400 Bad Request
```

Indicates that the server could not process the request because it was malformed or invalid.

---

## 401 Unauthorized

```http
401 Unauthorized
```

Indicates that authentication is required.

Example:

An API requires an authentication token, but the client did not provide one.

---

## 403 Forbidden

```http
403 Forbidden
```

Indicates that the server understood the request but refuses to authorize it.

Example:

A non-administrative user attempts to access:

```text
/admin
```

---

## 404 Not Found

```http
404 Not Found
```

Indicates that the requested resource does not exist on the server.

This is one of the most common HTTP status codes encountered during web assessments.

---

## 500 Internal Server Error

```http
500 Internal Server Error
```

Indicates that an unexpected error occurred on the server.

A **500** response may be caused by:

- Application bugs
- Unexpected user input
- Server-side exceptions
- Misconfigurations

During penetration testing, unexpected **500** responses may sometimes indicate the presence of a vulnerability.

---

# Response Headers

The response headers appear immediately after the Status Line.

Example:

```http
Date: Fri, 13 Mar 2015 11:26:05 GMT
Content-Type: text/html
Server: Apache
```

Headers provide additional information about the server and the response.

---

# Date Header

Example:

```http
Date: Fri, 13 Mar 2015 11:26:05 GMT
```

The **Date** header indicates when the server generated the response.

---

# Cache-Control Header

One of the most important HTTP response headers.

Example:

```http
Cache-Control: private, max-age=3600
```

This header controls how responses are cached by browsers and intermediary proxies.

Instead of downloading the same content repeatedly, the browser may reuse a cached copy according to the specified policy.

---

## private

```http
Cache-Control: private
```

Indicates that the response is intended for a single user and should not be stored by shared caches.

---

## no-cache

```http
Cache-Control: no-cache
```

Instructs the client to revalidate the cached content with the server before using it.

---

## no-store

```http
Cache-Control: no-store
```

Prevents the response from being stored anywhere.

This directive is commonly used for:

- Banking applications
- Financial services
- Sensitive user accounts

---

## max-age

```http
Cache-Control: max-age=3600
```

Specifies that the response may be cached for **3600 seconds (1 hour)** before it must be refreshed.

---

# Content-Type Header

One of the most important headers during web application testing.

Example:

```http
Content-Type: text/html
```

The **Content-Type** header tells the client what type of data is contained in the response.

Examples include:

```text
text/html
application/json
application/xml
image/png
text/plain
```

---

# Content-Encoding Header

Example:

```http
Content-Encoding: gzip
```

Indicates that the response body has been compressed before transmission.

The browser automatically decompresses the content before displaying it.

Common values include:

```text
gzip
deflate
br
```

Compression improves:

- Response speed
- Bandwidth efficiency

---

# Server Header

Example:

```http
Server: Apache
```

or

```http
Server: nginx
```

or

```http
Server: IIS
```

The **Server** header identifies the web server software handling the request.

This information is valuable during reconnaissance because it helps identify the target's technology stack.

---

# Content-Length Header

Example:

```http
Content-Length: 258
```

Specifies the size of the response body in bytes.

For example:

```http
Content-Length: 50000
```

Indicates that the response body contains:

```text
50000 Bytes
```

---

# Response Body

The **Response Body** is the final section of the HTTP response.

Example:

```http
HTTP/1.1 200 OK
Content-Type: text/html

<html>
    <h1>Welcome</h1>
</html>
```

The following content:

```html
<html>
    <h1>Welcome</h1>
</html>
```

is the **Response Body**, which contains the actual data returned by the server.
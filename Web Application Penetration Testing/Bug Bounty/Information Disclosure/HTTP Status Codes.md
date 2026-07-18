## What Are Status Codes?

HTTP Status Codes are numbers returned by a web server to indicate the result of a request.

When a browser requests a page:

```text
Client → Server
```

the server responds with:

```text
Status Code + Response
```

Example:

```text
HTTP/1.1 200 OK
```

---

# 1xx - Informational

The request was received and processing is continuing.

Example:

```text
100 Continue
```

Rarely encountered during web application testing.

---

# 2xx - Success

The request was successful.

## 200 OK

The page exists and was loaded successfully.

Example:

```text
GET /index.php

Response:
200 OK
```

This is the most common success response.

---

## 201 Created

A new resource was successfully created.

Common in APIs.

Example:

```text
201 Created
```

---

# 3xx - Redirection

The server redirects the client to another location.

## 301 Moved Permanently

The page has permanently moved.

Example:

```text
http://site.com
```

redirects to:

```text
https://site.com
```

---

## 302 Found

Temporary redirect.

The resource exists somewhere else temporarily.

---

# 4xx - Client Errors

The request contains an error.

## 400 Bad Request

The request is malformed.

Example:

```text
Invalid HTTP request
```

---

## 401 Unauthorized

Authentication is required.

Example:

```text
Login required
```

---

## 403 Forbidden

The server understands the request but refuses access.

Example:

```text
/admin
```

exists, but access is denied.

---

## 404 Not Found

The requested resource does not exist.

Example:

```text
/secret-page
```

returns:

```text
404 Not Found
```

Very common during directory enumeration.

---

## 405 Method Not Allowed

The HTTP method is not allowed.

Example:

```text
POST /page
```

when only GET is accepted.

---

# 5xx - Server Errors

The server failed to process the request.

## 500 Internal Server Error

A generic server-side error.

Often indicates:

- Application bugs
    
- Misconfigurations
    
- Unhandled exceptions
    

---

## 502 Bad Gateway

A gateway or proxy received an invalid response.

---

## 503 Service Unavailable

The service is temporarily unavailable.

Often caused by:

- Maintenance
    
- Overload
    
- Crashes
    

---

# Common Status Codes in Pentesting

|Code|Meaning|
|---|---|
|200|Resource exists|
|301|Permanent redirect|
|302|Temporary redirect|
|401|Authentication required|
|403|Access denied|
|404|Resource not found|
|500|Server error|

---


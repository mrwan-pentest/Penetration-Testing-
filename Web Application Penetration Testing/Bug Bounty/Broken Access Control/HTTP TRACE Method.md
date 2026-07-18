## TRACE is an HTTP method used for diagnostic and debugging purposes.

It allows a client to see exactly how its HTTP request is received by the web server.

---

# How Does TRACE Work?

## The client sends a TRACE request to the server.

Example:

```http
TRACE / HTTP/1.1
Host: example.com
```

The server responds by echoing the exact request back to the client.

Example response:

```http
HTTP/1.1 200 OK

TRACE / HTTP/1.1
Host: example.com
User-Agent: Mozilla/5.0
Cookie: session=abc123
```

---

# Why Is TRACE Dangerous?

## If TRACE is enabled, sensitive request headers may be reflected in the response.

For example:

- Cookies
    
- Authorization headers
    
- Custom authentication headers
    

This information may be abused by an attacker.

---

# TRACE and Cross-Site Tracing (XST)

## If TRACE is enabled together with other browser vulnerabilities, an attacker may steal sensitive HTTP headers.

This attack is known as:

```text
Cross-Site Tracing (XST)
```

---

# How to Check if TRACE Is Enabled

## Send a TRACE request using curl:

```bash
curl -X TRACE http://target.com
```

Or use Burp Suite:

- Change the HTTP method to `TRACE`
    
- Send the request
    
- Check the response
    

---

# Secure Configuration

## Most production web servers disable the TRACE method because it is rarely needed.

If the server returns:

```http
405 Method Not Allowed
```

or

```http
501 Not Implemented
```

TRACE is disabled.

---


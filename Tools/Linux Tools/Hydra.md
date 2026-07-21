

## What is Hydra?

Hydra is a tool used for:

```
Password Brute Force / Login Cracking
```

It is designed to test authentication mechanisms by attempting multiple combinations of:

- Usernames
- Passwords

against different network services.

Hydra is commonly used during penetration testing to identify weak credentials.

---

# Supported Services

Hydra supports many authentication services, including:

- SSH
- FTP
- RDP
- SMB
- HTTP
- HTTPS
- Telnet
- MySQL
- PostgreSQL
- VNC

---

# General Syntax

The general Hydra syntax is:

```
hydra [options] service://target
```

---

# SSH Example

Example:

```
hydra -l root -P passwords.txt ssh://192.168.1.10
```

This attempts to authenticate to an SSH service using:

- A single username:
    - `root`
- Passwords from:
    - `passwords.txt`

---

# Username Options

## `-l`

Specifies a single username.

Example:

```
-l admin
```

Hydra uses only the provided username.

---

## `-L`

Specifies a username wordlist.

Example:

```
-L users.txt
```

Hydra reads multiple usernames from the specified file.

---

# Password Options

## `-p`

Specifies a single password.

Example:

```
-p password123
```

Hydra uses only the provided password.

---

## `-P`

Specifies a password wordlist.

Example:

```
-P passwords.txt
```

Hydra tests passwords from the provided file.

---

# Important Hydra Options

## `-t`

Defines the number of parallel threads.

Example:

```
-t 4
```

Increasing the number of threads makes the attack faster, but it may also:

- Trigger account lockout.
- Cause service instability.
- Generate more detectable traffic.

---

## `-V`

Displays every login attempt.

Example:

```
-V
```

Useful for monitoring the attack progress.

---

## `-q`

Reduces output and displays less information.

---

## `-Q`

Runs Hydra in very quiet mode.

---

## `-f`

Stops Hydra after finding the first valid credential.

This is useful because it prevents unnecessary attempts after successful authentication.

---

# Hydra Against Web Applications

Hydra can also attack web authentication mechanisms.

There are two common cases:

1. HTTP Basic Authentication.
2. Web login forms using HTTP POST requests.

---

# HTTP Basic Authentication

## What is HTTP Basic Authentication?

HTTP Basic Authentication is a login mechanism where the browser displays a popup:

```
Username:
Password:
```

The credentials are sent through HTTP authentication headers.

---

# How to Identify Basic Authentication?

You can usually identify Basic Authentication by:

- A browser popup asking for username and password.
- The HTTP response containing:

```
WWW-Authenticate
```

header.

---

# Attacking HTTP Basic Authentication with Hydra

For Basic Authentication, Hydra uses:

```
http-get
```

or:

```
http-head
```

---

# Example

```
hydra -L users.txt -P passwords.txt -s 8080 10.128.163.215 http-get /
```

---

# Explanation

## `http-get`

Indicates that the target uses Basic Authentication through a GET request.

---

## `/`

The path being protected.

---

## `-s`

Specifies the target service port.

Example:

```
-s 8080
```

---

# Hydra Against Login Pages

For normal web login forms, Hydra uses:

```
http-post-form
```

because login forms usually send credentials using HTTP POST requests.

---

# Example

```
hydra -f -V -l username -P /usr/share/wordlists/rockyou.txt 10.82.135.6 http-post-form "/admin/index.php:user=^USER^&pass=^PASS^:Username or password invalid"
```

---

# Understanding HTTP POST Form Syntax

The general format is:

```
"path:parameters:failure_message"
```

---

## Path

Example:

```
/admin/index.php
```

The location of the login page.

---

## Parameters

Example:

```
user=^USER^&pass=^PASS^
```

The parameters sent during login.

Hydra replaces:

```
^USER^
```

with usernames.

and:

```
^PASS^
```

with passwords.

---

## Failure Message

Example:

```
Username or password invalid
```

Hydra uses this message to determine whether the login attempt failed.

If the response does not contain this message, Hydra assumes the credentials may be valid.

---

# Example Login Form Attack

```
hydra -L users.txt -P passwords.txt 10.0.0.5 http-post-form "/login.php:username=^USER^&password=^PASS^:Invalid credentials"
```

---

# Finding Login Parameters

The username and password parameter names can be identified from:

- Burp Suite.
- Browser Developer Tools.
- HTTP request analysis.

Example:

A login request may contain:

```
username=admin&password=test123
```

These parameter names are then used in the Hydra command.

---

# HTTPS Login Forms

If the website uses HTTPS instead of HTTP, use:

```
https-post-form
```

or:

```
https-get
```

Example:

```
hydra -L users.txt -P passwords.txt target https-post-form "/login.php:user=^USER^&pass=^PASS^:Invalid credentials"
```

---

# Summary

Hydra is a powerful credential testing tool used during penetration testing to identify weak authentication.

Important options:

|Option|Purpose|
|---|---|
|`-l`|Single username|
|`-L`|Username wordlist|
|`-p`|Single password|
|`-P`|Password wordlist|
|`-t`|Number of threads|
|`-V`|Show attempts|
|`-f`|Stop after first success|

Hydra supports many protocols and is commonly used for testing SSH, FTP, HTTP authentication, and web login forms.
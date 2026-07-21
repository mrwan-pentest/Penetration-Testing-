# HTTP Enumeration with Metasploit

Metasploit provides several modules that can be used to perform **HTTP enumeration**, helping identify web server information, hidden files and directories, and login pages.

---

# Identifying the Web Server Version

## Module

```text
auxiliary/scanner/http/http_version
```

Displays information about the target web server, including:

- Web Server
- Version
- Banner

![](../../../../../Images/Pasted%20image%2020260514130429.png)

---

# Discovering the robots.txt File

## Module

```text
auxiliary/scanner/http/robots_txt
```

Checks whether the following file exists:

```text
robots.txt
```

This file may reveal:

- Hidden directories
- Administrative pages
- Files or paths that the website owner does not want search engines to index

![](../../../../../Images/Pasted%20image%2020260514130639.png)

---

# Retrieving HTTP Headers

## Module

```text
auxiliary/scanner/http/http_header
```

Retrieves the HTTP response headers to gather information about the server, such as:

- Web server type
- Technologies in use
- Software versions
- Security-related headers

![](../../../../../Images/Pasted%20image%2020260514130731.png)

---

# Discovering Hidden Files and Directories

## Module

```text
auxiliary/scanner/http/dir_scanner
```

Performs directory scanning to identify:

- Admin pages
- Sensitive files
- Hidden directories

![](../../../../../Images/Pasted%20image%2020260514130929.png)

---

# Checking for Directory Listing

## Module

```text
auxiliary/scanner/http/dir_listing
```

Checks whether the web server has **Directory Listing** enabled.

If enabled, it may expose:

- Files
- Directories
- Backup files
- Configuration files

![](../../../../../Images/Pasted%20image%2020260514131042.png)

---

# Checking for HTTP PUT Support

## Module

```text
auxiliary/scanner/http/http_put
```

Tests whether the server allows file uploads using the:

```text
HTTP PUT
```

method.

If misconfigured, it may allow an attacker to upload:

- Web Shells
- Malicious files

![](../../../../../Images/Pasted%20image%2020260514131123.png)

---

# Enumerating Apache User Directories

## Module

```text
auxiliary/scanner/http/apache_userdir_enum
```

Searches for Apache user directories in the following format:

```text
/~username
```

For example:

```text
/~admin
/~john
/~test
```

![](../../../../../Images/Pasted%20image%2020260514131208.png)

---

# Performing Brute Force on Login Pages

## Module

```text
auxiliary/scanner/http/http_login
```

Attempts to authenticate to web login pages using multiple usernames and passwords.

It can be used against:

- Admin pages
- Control panels
- Web applications

![](../../../../../Images/Pasted%20image%2020260514131238.png)
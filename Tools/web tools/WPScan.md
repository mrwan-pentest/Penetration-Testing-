# WPScan

**WPScan** is a specialized tool for:

```
WordPress Security Scanning
```

It is used to scan WordPress websites and discover information and vulnerabilities related to WordPress.

---

# What does WPScan do?

It can:

- Detect WordPress version
- Enumerate Themes
- Enumerate Plugins
- Find WordPress users
- Detect known vulnerabilities
- Perform password auditing (Brute Force)

---

# Basic Usage

Scan a website:

```
wpscan --url http://example.com
```

It can show:

- WordPress version
- Installed plugins
- Installed themes
- General information

---

# Enumerate Users

```
wpscan --url http://example.com --enumerate u
```

Finds WordPress users like:

```
admin
john
editor
```

Useful for:

- Username discovery
- Password auditing

---

# Enumerate Plugins

```
wpscan --url http://example.com --enumerate p
```

Shows:

- Plugin names
- Plugin versions
- Known vulnerabilities

Example:

```
Plugin: contact-form-7
Version: 5.0
Vulnerable: Yes
```

---

# Enumerate Themes

```
wpscan --url http://example.com --enumerate t
```

Finds:

- Active theme
- Installed themes
- Possible vulnerabilities

---

# Vulnerability Database

WPScan can compare discovered versions with its vulnerability database.

You need an API Token:

```
wpscan --url http://example.com --api-token TOKEN
```

It helps find:

- CVEs
- Vulnerable plugins
- Vulnerable themes
- WordPress vulnerabilities

---

# Password Brute Force

Test WordPress login credentials:

```
wpscan --url http://example.com -U users.txt -P passwords.txt
```

Where:

- `-U` → Username list
- `-P` → Password list

---

# Important Options

|Option|Function|
|---|---|
|`--url`|Specify target WordPress site|
|`--enumerate`|Enumerate WordPress information|
|`-u`|Username list|
|`-P`|Password list|
|`--api-token`|Connect to vulnerability database|
|`--plugins-detection`|Control plugin detection method|

---

# Common Enumeration Types

|Option|What it Finds|
|---|---|
|`u`|Users|
|`p`|Plugins|
|`t`|Themes|

Example:

```
wpscan --url http://target.com --enumerate p,t,u
```

This performs:

- Plugin enumeration
- Theme enumeration
- User enumeration

---

# Common Pentesting Usage

## 1. Reconnaissance

Find WordPress information:

```
Version
Plugins
Themes
Users
```

---

## 2. Find Vulnerable Plugins

Example:

```
Old Plugin Version
        |
        ↓
Known CVE
        |
        ↓
Possible Exploitation
```

---

## 3. User Enumeration

Discover valid usernames for further testing.

---

## 4. Password Auditing

Check if users have weak passwords.

---

# In short:

```
WPScan = A WordPress-focused security scanner
```

It helps you answer:

```
What WordPress version is running?
What plugins/themes exist?
Are they vulnerable?
What users exist?
```
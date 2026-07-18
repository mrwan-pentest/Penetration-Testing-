
## What is phpinfo.php?

`phpinfo.php` is a PHP file used to display detailed information about the PHP environment running on a web server.

A common example is:

```php
<?php
phpinfo();
?>
```

When accessed through a browser, it generates a page containing extensive server information.

---

## Example URL

```text
https://target.com/phpinfo.php
```

---

## What Information Does It Reveal?

### PHP Version

Example:

```text
PHP Version 7.4.33
```

Useful for identifying known vulnerabilities.

---

### Operating System

Example:

```text
Linux Ubuntu 20.04
```

or

```text
Windows Server 2019
```

---

### Web Server Information

Example:

```text
Apache/2.4.49
```

or

```text
Nginx/1.18.0
```

---

### Installed PHP Modules

Example:

```text
curl
mysqli
openssl
gd
ldap
```

This helps attackers understand available functionality.

---

### Server Paths

Example:

```text
/var/www/html
```

or

```text
C:\xampp\htdocs
```

---

### Configuration Files

Example:

```text
Loaded Configuration File
/etc/php/7.4/apache2/php.ini
```

---

### Environment Variables

May reveal:

```text
PATH
USERNAME
HOSTNAME
```

and other system information.

---

### Database Information

Sometimes reveals:

- MySQL settings
    
- PostgreSQL settings
    
- Connection details
    

---

## Why is phpinfo.php Dangerous?

It provides attackers with:

- Software versions
    
- System paths
    
- Server details
    
- Installed modules
    
- Configuration information
    

All of which can assist in further attacks.

---

## Information Disclosure Vulnerability

An exposed:

```text
phpinfo.php
```

is considered:

```text
Information Disclosure
```

because it leaks sensitive server information.

---

## How to Find It?

Common filenames:

```text
phpinfo.php
info.php
test.php
php.php
```

Using a browser:

```text
https://target.com/phpinfo.php
```

Or with directory brute-forcing tools:

```text
Gobuster
Dirsearch
Feroxbuster
```

---

## Pentesting Value

If you discover a phpinfo page, always look for:

- PHP Version
    
- Server Version
    
- Document Root
    
- Loaded Modules
    
- File Paths
    
- Temporary Directories
    

These details often help identify the next attack vector.



## What is robots.txt?

`robots.txt` is a text file located in the web root directory.

Example:

```text
https://example.com/robots.txt
```

Its purpose is to tell search engines which pages or directories they should or should not crawl.

---

## Example

```text
User-agent: *
Disallow: /admin
Disallow: /backup
Disallow: /private
```

Meaning:

- Allow search engines to access the website.
    
- Do not index:
    
    - `/admin`
        
    - `/backup`
        
    - `/private`
        

---

## Why is robots.txt Interesting for Pentesters?

Developers often place sensitive paths inside:

```text
robots.txt
```

Thinking search engines will ignore them.

However:

```text
robots.txt is public.
```

Anyone can read it.

---

## Information Commonly Found

### Admin Panels

```text
Disallow: /admin
```

---

### Backup Directories

```text
Disallow: /backup
```

---

### Development Areas

```text
Disallow: /dev
Disallow: /staging
```

---

### Private Files

```text
Disallow: /private
```

---

### Hidden Applications

```text
Disallow: /cms
Disallow: /internal
```

---

## Typical Pentesting Process

### Step 1

Visit:

```text
https://target.com/robots.txt
```

---

### Step 2

Read all disclosed paths.

Example:

```text
User-agent: *
Disallow: /administrator
Disallow: /secret
Disallow: /backup.zip
```

---

### Step 3

Browse to those locations manually.

Examples:

```text
https://target.com/administrator
https://target.com/secret
https://target.com/backup.zip
```

---

## Example of Information Disclosure

robots.txt:

```text
User-agent: *
Disallow: /admin-panel
```

An attacker visits:

```text
https://target.com/admin-panel
```

and discovers the login page.

The file unintentionally disclosed sensitive information.

---


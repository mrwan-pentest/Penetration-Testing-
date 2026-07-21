

What are Google Dorks?

Google Dorks are special search operators used in Google to find information that does not appear in normal search results.



Why are they used?

They are used during Information Gathering and OSINT.

They help in:

- Discovering sensitive files
- Finding admin pages
- Identifying exposed vulnerabilities
- Extracting hidden information from websites

---

Important Google Dorks Examples

Search for specific file types

```
filetype:pdf site:example.com
```

Shows only PDF files within a specific website.

---

Login pages

```
inurl:login site:example.com
```

Finds URLs containing the word login.

---

Admin panels

```
inurl:admin site:example.com
```

Searches for administrative pages.

---

Sensitive files or passwords

```
filetype:txt password
```

Finds text files containing the word password.

---

List all indexed pages of a website

```
site:example.com
```

Displays all pages indexed by Google for that domain.

---

Google Dork: intitle:"index of"

This dork is used to find open directory listings on web servers.

---

Command

```
intitle:"index of"
```

---

Meaning

Search for pages whose title contains Index of.

---

What is Index of?

It appears when a web server exposes directory contents without protection.

Example:

```
Index of /uploads
```

It may contain:

- backup.zip
- database.sql
- images
- config.txt

---

Why does this happen?

- Directory listing is enabled
- Misconfigured Apache or Nginx server
- Security misconfiguration

---

What does it reveal?

It can expose:

- Open directories
- Sensitive files on servers

---

Advanced examples

Search within a specific site

```
site:example.com intitle:"index of"
```

Search for backup files

```
intitle:"index of" backup
```

Search for database files

```
intitle:"index of" database
```

---

Google Dork: cache:example.com

This is used to view a cached version of a website.

---

Command

```
cache:example.com
```

---

Meaning

It shows a saved snapshot of a website stored by Google.

---

What is cache?

A cached page is a stored copy of a website saved by search engines.

Google:

- Visits the site
- Saves a copy
- Shows it even if the site is changed or deleted

---

What you can get from it

- Old versions of web pages
- Deleted content
- Information no longer available on the live site

---

Related tool

Wayback Machine, which provides similar website archiving functionality.

---

Common Google Dorks Operators

|Operator|Function|
|---|---|
|site:|Search within a specific website|
|filetype:|Find specific file types|
|inurl:|Search keywords in URL|
|intitle:|Search keywords in page title|
|cache:|View cached version of a page|

---

## Show all indexed pages of a specific website.

![](../../../../Images/Pasted%20image%2020260510150210.png)



## Search for web pages that include the word “admin” in the URL or content.

![](../../../../Images/Pasted%20image%2020260510150247.png)



## Find and list subdomains related to a target domain.

![](../../../../Images/Pasted%20image%2020260510150351.png)

## Search for pages that contain files with a specific extension such as PDF.

![](../../../../Images/Pasted%20image%2020260510154632.png)

بحث عن كلمة معينه داخل ملف
هنا يعني هذا الامر 
ابحث داخل موقع ine.com  عن pdf  وابحث داخله عن كلمة password

![](../../../../Images/Pasted%20image%2020260510154936.png)

## Search inside a website for files of a specific type (e.g. PDF) that contain a specific keyword.

### Example:  
#### Search within `ine.com` for PDF files that contain the word “password”.

![](../../../../Images/Pasted%20image%2020260510155356.png)

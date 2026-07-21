# HTTrack

`HTTrack` is a website mirroring tool used to create a complete local copy of a website on your machine.

It downloads website resources, including:

- HTML pages
- Images
- CSS files
- JavaScript files
- Other accessible website assets

The downloaded copy can then be browsed:

```
Without an Internet connection
```

---

# What is Website Mirroring?

Website mirroring means creating an offline replica of an entire website.

Instead of accessing:

```
http://example.com
```

every time, HTTrack downloads the website structure and files locally.

The tool also attempts to:

- Rebuild internal links
- Preserve the website structure
- Maintain relationships between downloaded resources

This allows the website to function locally as much as possible.

---

# Why Use HTTrack in Penetration Testing?

During a penetration test, HTTrack can be useful during the **Web Enumeration** and **Information Gathering** phases.

A website may contain information that is not immediately visible during normal browsing, such as:

- Hidden files
- HTML comments
- Old pages
- Backup files
- Configuration files
- Forgotten resources

By creating a local copy of the website, a tester can analyze the downloaded files offline and search for interesting information.

---

# Example Scenario

Assume a website contains hidden files:

```
backup.zip
config.bak
old_page.html
```

These files may not be linked from the main website.

When HTTrack crawls the website, it may discover and download accessible resources, allowing further analysis.

---

# How Does HTTrack Work?

HTTrack works through an automated crawling process.

The workflow:

1. HTTrack accesses the main website page.
2. It analyzes the links inside the page.
3. It follows discovered links.
4. It downloads available resources.
5. It repeats the process recursively.

This process is known as:

```
Crawling
```

---

# Basic Usage

To create a local mirror of a website:

```
httrack http://example.com
```

HTTrack will begin downloading accessible website resources and store them locally.

---

# Output After Running HTTrack

After completion, HTTrack creates a directory containing the downloaded website.

The directory may include:

- HTML files
- Images
- CSS files
- JavaScript files
- Other website resources

Example structure:

```
website/
├── index.html
├── images/
├── css/
├── js/
└── hts-cache/
```

---

# Important Files Created by HTTrack

|File / Directory|Purpose|
|---|---|
|`index.html`|Main website page|
|`hts-log.txt`|Log file containing operation details|
|`hts-cache`|Stores cached information used by HTTrack|
|`cookies.txt`|Stores website cookies when available|

---

# Important Concepts

## Mirror

A **Mirror** means:

```
A complete local copy of a website
```

The goal is to replicate the website structure and resources locally.

---

## Crawling

**Crawling** means:

```
Automatically navigating through website links to discover resources
```

Web crawlers start from a known page and follow available links to find additional content.

---

# Analyzing Downloaded Files

After downloading the website, penetration testers can analyze the collected files.

---

## Listing Downloaded Files

The `find` command can be used to display files inside the downloaded directory.

```
find .
```

This helps identify:

- Hidden files
- Unexpected directories
- Backup files

---

## Searching for Flags

In CTF environments, flags may exist inside downloaded files.

```
grep -R "FL@G" .
```

Explanation:

- `grep` searches for specific text patterns.
- `-R` performs a recursive search through directories.

---

## Searching for HTML Comments

Developers may accidentally leave sensitive information inside HTML comments.

```
grep -R "<!--" .
```

Example:

```
<!-- Temporary admin password: admin123 -->
```

These comments are invisible in the browser but exist inside the source code.

---

## Searching for Sensitive Keywords

To search for possible credentials or sensitive information:

```
grep -Ri "password" .
```

Explanation:

- `-R` searches recursively.
- `-i` ignores uppercase/lowercase differences.

Possible discoveries:

```
password=
passwd=
admin_password=
```

---

# Sensitive Information That May Be Discovered

|Finding|Why It Matters|
|---|---|
|Backup files|May contain source code or credentials|
|HTML comments|Developers may leave sensitive notes|
|JSON APIs|May expose sensitive data|
|Old pages|May reveal outdated functionality|
|Configuration files|May contain Credentials|

---

# HTTrack in a Penetration Testing Workflow

A common workflow:

## Step 1: Identify the Website

First, identify the target web application.

Example:

```
http://target.com
```

---

## Step 2: Create a Local Mirror

Download the website:

```
httrack http://target.com
```

---

## Step 3: Analyze Downloaded Content

Search for interesting information:

```
find .
```

```
grep -Ri "password" .
```

```
grep -R "<!--" .
```

---

# Limitations of HTTrack

Although HTTrack is useful, it has limitations:

- It only downloads publicly accessible content.
- It does not bypass authentication.
- It may not fully capture dynamic content generated by JavaScript.
- It cannot replace specialized web scanners.

For modern web applications, it is usually combined with other enumeration tools such as:

- Gobuster
- Dirb
- Burp Suite
- Nmap

---

# Summary

`HTTrack` is a website mirroring and crawling tool that creates a local copy of a web application.

Key points:

- Downloads website resources for offline analysis.
- Useful during Web Enumeration.
- Can reveal hidden information inside downloaded files.
- Helps analyze:
    - HTML comments
    - Backup files
    - Configuration files
    - Old website resources

Important commands:

```
httrack http://example.com
```

Create a website mirror.

```
find .
```

List downloaded files.

```
grep -R "<!--" .
```

Search for HTML comments.

```
grep -Ri "password" .
```

Search for sensitive keywords.
# Crawling vs Spider

Before performing any web application assessment, one of the first steps is to **discover and enumerate the target website**. Two fundamental concepts in this phase are **Crawling** and **Spidering**.

---

# What is Crawling?

**Crawling** is the process of discovering and collecting web pages, links, and other resources from a website.

In other words, it is **the activity of exploring a website** to understand its structure.

### Example

Suppose you visit:

```text
http://target.com
```

Your goal is to identify every accessible page, directory, and resource within the website.

The process of searching for and collecting these pages is called:

```text
Crawling
```

---

# What is a Spider?

A **Spider** (also called a **Web Crawler**) is the tool or software that performs the crawling process.

Simply put:

```text
Crawling = The Process

Spider = The Tool That Performs the Process
```

---

# How Does a Spider Work?

A spider starts with one or more URLs.

It then:

1. Visits the initial page.
2. Downloads the HTML content.
3. Extracts all available links.
4. Visits the newly discovered links.
5. Repeats the process until no additional pages are found.

This allows the spider to automatically map the website's structure.

---

# Why is Crawling Important?

For penetration testers, crawling helps identify:

- Hidden Pages
- Hidden Directories
- Login Pages
- API Endpoints
- Administrative Panels
- Backup Files
- Downloadable Resources
- Additional Attack Surface

The more pages you discover, the greater your understanding of the target application.

---

# Manual Crawling vs Automated Crawling

## Manual Crawling

The tester manually browses the application.

Examples include:

- Clicking links
- Navigating menus
- Inspecting page source
- Following redirects

### Advantages

- Better understanding of application logic.
- Easier identification of unusual behavior.

---

## Automated Crawling

Performed using specialized tools.

Popular examples include:

- Burp Suite Spider / Crawler
- OWASP ZAP Spider
- Feroxbuster
- Dirsearch
- Gobuster (for directory enumeration)

### Advantages

- Faster
- Discovers large numbers of pages automatically
- Efficient for large applications

---

# Crawling Workflow

```text
Target URL
      │
      ▼
Spider Visits Page
      │
      ▼
Extract Links
      │
      ▼
Visit New Links
      │
      ▼
Repeat Until No More Pages Are Found
```

---

# Summary

| Term | Description |
|------|-------------|
| **Crawling** | The process of discovering and collecting website pages and resources. |
| **Spider** | The tool or program that automatically performs the crawling process. |
| **Purpose** | Enumerate the website, map its structure, and discover potential attack surfaces before further testing. |
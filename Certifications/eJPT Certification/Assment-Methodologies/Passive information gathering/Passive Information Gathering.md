#  Passive Information Gathering

## Definition

Collecting information without directly interacting with the target.

The target is usually unaware that the information is being gathered.

---

## Examples

- Whois lookup
- Google dorking
- LinkedIn search
- DNS records
- Shodan

---

## Advantage

- Quiet method
- Hard to detect

---

## Footprinting

Footprinting means collecting as much information as possible about a target before starting an attack.

It is usually the first phase in:

- Penetration Testing
- Ethical Hacking

---

## robots.txt file

During initial information gathering, one of the first things to check is the robots.txt file.

---

## What is robots.txt?

A file used by websites to instruct search engines (like Google) about:

- Pages allowed to be indexed
- Pages disallowed from crawling

---

## Location

```
https://example.com/robots.txt
```

---

## Example structure

```
User-agent: *Disallow: /adminDisallow: /private
```

---

## Meaning

|Line|Meaning|
|---|---|
|User-agent: *|Applies to all bots|
|Disallow: /admin|Do not access /admin|

---

## Why it is useful in security testing

robots.txt may reveal hidden or sensitive paths such as:

- Admin panels
- Backup files
- Private directories
- Hidden pages

These can sometimes be directly accessible.

---

## Example

```
Disallow: /backupDisallow: /secret-admin
```

Security testers may try accessing these paths directly.

---

## Important note

robots.txt is not a security control.

It is only a request for search engines, not protection.

---

## Why websites hide pages from Google

To avoid clutter in search results and prevent indexing of unnecessary pages such as:

- Login pages
- Search results
- Internal functions

robots.txt is used for search engine optimization and crawling control, not security.

---

## Sitemap.xml

### What is sitemap.xml?

A file (usually XML) created by website owners to help search engines understand the structure of the website and index pages efficiently.

---

## Security value of sitemap.xml

For penetration testers, it can reveal:

- Full list of website pages
- Hidden or forgotten pages
- File types used in the website (php, pdf, zip, xml)

---

## Why developers use it

To ensure search engines discover all important pages, especially in large websites.

It acts as a complete list of URLs submitted to search engines for faster indexing.

---

## Crawling concept

### Definition

Crawling is the process where search engines use automated bots (spiders) to explore websites.

---

### How it works

- A bot visits a web page
- Reads its content
- Extracts all links
- Follows those links recursively

---

### Simple analogy

Like reading a large encyclopedia page by page, following references to new pages.

---

### Purpose

To collect data and build the search engine index.

---

### Relation with robots.txt

robots.txt instructs bots where they are allowed or not allowed to crawl.

---

### Relation with sitemap.xml

sitemap.xml provides a structured map of all important pages to help bots crawl efficiently.

---

## Summary

Crawling is the core process used by search engines to discover, analyze, and index web pages.
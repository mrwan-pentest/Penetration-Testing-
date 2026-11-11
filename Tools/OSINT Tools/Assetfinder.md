# Assetfinder Tool

## 1. Introduction

Assetfinder is a command-line tool used to discover subdomains associated with a target domain.

It collects information from public sources and helps identify additional assets that may belong to the target organization.

It is commonly used during the Passive Reconnaissance and Subdomain Enumeration phases of penetration testing.

## 2. Basic Subdomain Enumeration

To discover subdomains associated with a domain, use:

```
assetfinder example.com
```

This command searches for assets related to `example.com` and displays the discovered domains and subdomains.

## 3. Find Only Subdomains Related to the Target

To limit the results to subdomains belonging to the specified domain, use:

```
assetfinder --subs-only example.com
```

This helps filter out unrelated domains that may appear in the results.

## 4. Save Results to a File

We can save the discovered subdomains into a text file using output redirection:

```
assetfinder --subs-only example.com > subdomains.txt
```

The results will be stored in `subdomains.txt`.

## 5. Remove Duplicate Results

We can use `sort -u` to sort the results and remove duplicate entries:

```
assetfinder --subs-only example.com | sort -u
```

To save the clean results:

```
assetfinder --subs-only example.com | sort -u > subdomains.txt
```

## 6. Useful Commands

|Command|Description|
|---|---|
|`assetfinder example.com`|Finds related domains and subdomains|
|`assetfinder --subs-only example.com`|Displays only subdomains of the target|
|`> subdomains.txt`|Saves output to a file|
|`sort -u`|Sorts results and removes duplicates|

## 7. Example Workflow

A simple command to discover subdomains, remove duplicates, and save the results:

```
assetfinder --subs-only example.com | sort -u > subdomains.txt
```

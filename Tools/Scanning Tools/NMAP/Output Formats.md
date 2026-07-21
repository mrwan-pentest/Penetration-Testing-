# `-oN`

Save the results as:

```
Normal text output
```

It saves the Nmap scan results in a regular readable text file.

Example:

```
nmap -oN scan.txt target
```

The output will be saved in:

```
scan.txt
```

Useful when you want:

- A simple report
- Human-readable results
- Documentation

---

# `-oX`

Save the results as:

```
XML format
```

XML is useful for:

- Other security tools
- Automated analysis
- Importing scan results into platforms

Example:

```
nmap -oX scan.xml target
```

Example of using it with Metasploit:

The Nmap scan is saved as XML:

```
nmap -oX scan.xml target
```

Then it can be imported into Metasploit:

```
db_import scan.xml
```

This allows Metasploit to use the discovered:

- Hosts
- Services
- Ports
- Vulnerabilities

without scanning again.

---

# `-oG`

Means:

```
Grepable Output
```

---

# Idea

It saves the output in a format that is:

```
Easy to search using grep
```

Example:

```
nmap -oG scan.gnmap TARGET
```

---

# Why is it useful?

Because you can process the results using Linux tools like:

```
grep
awk
cut
```

Example:

```
grep open scan.gnmap
```

This extracts lines containing:

```
open ports
```

---

This format is:

```
Less commonly used today
```

because:

```
XML output is more powerful and widely supported
```

---

# `-oA`

Means:

```
All Formats
```

---

# What does it do?

It saves the scan results in all major formats at the same time:

- Normal
- XML
- Grepable

Example:

```
nmap -oA fullscan TARGET
```

---

# It creates three files:

|File|Format|
|---|---|
|`fullscan.nmap`|Normal Output|
|`fullscan.xml`|XML Output|
|`fullscan.gnmap`|Grepable Output|

---

# Why use `-oA`?

Because during penetration testing you often need:

- A readable report (`.nmap`)
- A file for tools like Metasploit (`.xml`)
- A file for command-line processing (`.gnmap`)

So instead of running Nmap multiple times:

```
nmap -oA scan TARGET
```

saves everything in one scan.
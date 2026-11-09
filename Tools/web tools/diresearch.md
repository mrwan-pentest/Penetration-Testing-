# dirsearch

## What is dirsearch?

dirsearch is an open-source command-line tool written in Python that discovers hidden directories and files on web servers. It sends a large number of HTTP requests based on a wordlist and analyzes the responses to work out which paths exist on the target.

## Purpose

Web servers often contain content that is not linked anywhere in the application. dirsearch helps uncover this content during the Enumeration phase.

Typical findings include:

- Admin panels and login pages
- Backup and configuration files
- Hidden directories and development endpoints
- Upload directories
- Forgotten or unlinked files that may expose sensitive information

## Installation

On Kali Linux, dirsearch can be installed directly from the package repositories.

Bash

```
sudo apt install dirsearch
```

It can also be installed with pip.

Bash

```
pip3 install dirsearch
```

Alternatively, the tool can be cloned from its official GitHub repository and run from source.

Bash

```
git clone https://github.com/maurosoria/dirsearch.git
cd dirsearch
python3 dirsearch.py -u http://target.com
```

## Basic Syntax

Only a target URL is required. If no wordlist or extensions are specified, dirsearch uses its built-in wordlist and default extensions.

Bash

```
dirsearch -u <URL> [options]
```

## Common Options

|Option|Description|
|---|---|
|`-u`|Specifies the target URL.|
|`-l`|Loads multiple targets from a file.|
|`-e`|Defines the file extensions to test, separated by commas.|
|`-w`|Specifies a custom wordlist.|
|`-t`|Sets the number of threads.|
|`-r`|Enables recursive scanning of discovered directories.|
|`-R`|Sets the maximum recursion depth.|
|`-i`|Shows only the specified status codes.|
|`-x`|Excludes the specified status codes from the results.|
|`-f`|Forces every extension to be appended to every wordlist entry.|
|`-H`|Adds a custom HTTP header to each request.|
|`--cookie`|Sends a cookie with each request, which is useful for authenticated scans.|
|`--proxy`|Routes the traffic through a proxy such as Burp Suite.|
|`--random-agent`|Uses a random User-Agent for each request.|
|`--delay`|Adds a delay between requests.|
|`-o`|Saves the results to a file.|
|`--format`|Defines the report format, such as plain, json, or csv.|
|`-h`|Displays the help menu.|

Option names may vary slightly between versions. Use the help menu to confirm the options available in your installation.

Bash

```
dirsearch -h
```

## Usage Examples

### Basic Scan

We start with a default scan to get an overview of the accessible directories and files on the target.

Bash

```
dirsearch -u http://10.10.10.10
```

### Scanning for Specific Extensions

If the technology behind the application is known, limiting the scan to relevant extensions makes the results more accurate and the scan faster.

Bash

```
dirsearch -u http://10.10.10.10 -e php,txt,bak
```

### Using a Custom Wordlist

A custom wordlist is useful when the default one finds nothing interesting, or when the target requires a more specific list.

Bash

```
dirsearch -u http://10.10.10.10 -w /usr/share/wordlists/dirb/common.txt
```

### Filtering Status Codes

To reduce noise, we can exclude responses that are not useful, such as 403 and 404.

Bash

```
dirsearch -u http://10.10.10.10 -x 403,404
```

We can also display only the status codes we are interested in.

Bash

```
dirsearch -u http://10.10.10.10 -i 200,301,302
```

### Recursive Scanning

Recursive scanning tells dirsearch to scan inside every directory it discovers. The depth is limited here to keep the scan time reasonable.

Bash

```
dirsearch -u http://10.10.10.10 -r -R 2
```

### Increasing Speed

Increasing the number of threads speeds up the scan. High values may overload the target or trigger security controls.

Bash

```
dirsearch -u http://10.10.10.10 -t 50
```

### Authenticated Scanning

Some content is only accessible after logging in. Supplying a valid session cookie lets dirsearch enumerate these protected areas.

Bash

```
dirsearch -u http://10.10.10.10 --cookie "PHPSESSID=<session_value>"
```

### Routing Traffic Through a Proxy

Sending the requests through Burp Suite lets us inspect and replay them later.

Bash

```
dirsearch -u http://10.10.10.10 --proxy http://127.0.0.1:8080
```

### Saving the Results

Saving the output to a file makes it easier to review the findings and include them in a report.

Bash

```
dirsearch -u http://10.10.10.10 -e php,txt -o results.txt
```


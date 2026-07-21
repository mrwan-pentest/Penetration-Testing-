# Searchsploit

`searchsploit` is a command-line tool included with **Exploit-DB**.

Its purpose:

> Search for publicly available exploits from the Exploit Database directly from your terminal.

In simple words:

After discovering a service/version:

```
Apache 2.4.49
Windows Server 2012
vsFTPd 2.3.4
```

You use `searchsploit` to check:

```
Is there a public exploit for this version?
```

---

# Basic Syntax

```
searchsploit [keyword]
```

---

# 1. Search for an Exploit

Example:

```
searchsploit vsftpd 2.3.4
```

Searches Exploit-DB for exploits related to:

```
vsFTPd version 2.3.4
```

Example result:

```
vsftpd 2.3.4 - Backdoor Command Execution
```

---

# 2. Search by Software Name

Example:

```
searchsploit apache
```

Shows all exploits related to Apache.

---

# 3. Search by Version

Example:

```
searchsploit "Apache 2.4"
```

Useful after:

```
nmap -sV target
```

Because Nmap gives you:

```
Apache httpd 2.4.49
```

Then:

```
searchsploit Apache 2.4.49
```

---

# 4. Exact Match Search

```
searchsploit -e apache 2.4.49
```

`-e`

means:

```
Exact Match
```

Search only for the exact phrase.

---

# 5. Show Exploit Location

```
searchsploit -p ID
```

Example:

```
searchsploit -p 50383
```

Shows the full path of the exploit.

Example:

```
/usr/share/exploitdb/exploits/linux/remote/50383.py
```

---

# 6. Copy Exploit to Current Directory

```
searchsploit -m ID
```

`-m`

means:

```
Mirror
```

Example:

```
searchsploit -m 50383
```

Copies the exploit to your current folder.

Useful because you can:

- Modify it
- Read the source code
- Run it

---

# 7. Display Exploit Details

```
searchsploit -x ID
```

`-x`

means:

```
Examine
```

Example:

```
searchsploit -x 50383
```

Opens the exploit source code.

---

# 8. Update Exploit Database

Exploit-DB database can become outdated.

Update it:

```
searchsploit -u
```

`-u`

means:

```
Update
```

---

# 9. Search Without Extra Information

```
searchsploit -w apache
```

Shows the Exploit-DB website link.

`-w`

means:

```
Show URL
```

---

# Practical Workflow (eJPT Style)

### 1. Find service version

```
nmap -sV target
```

Example:

```
FTP
vsFTPd 2.3.4
```

---

### 2. Search for exploit

```
searchsploit vsftpd 2.3.4
```

---

### 3. Read exploit information

```
searchsploit -x exploit_ID
```

---

### 4. Copy exploit

```
searchsploit -m exploit_ID
```

---

# Important Options Cheat Sheet

|Command|Function|
|---|---|
|`searchsploit keyword`|Search exploits|
|`-e`|Exact search|
|`-x`|View exploit code|
|`-m`|Copy exploit locally|
|`-p`|Show exploit path|
|`-u`|Update database|
|`-w`|Show Exploit-DB URL|

---

**In short:**

`searchsploit` = **A local Exploit-DB search tool used after enumeration to find public exploits for discovered services and versions.**
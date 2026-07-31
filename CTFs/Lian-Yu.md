# Lian-Yu (TryHackMe)

# Overview

**Lian-Yu** is a beginner-friendly Linux CTF that focuses on **Web Enumeration, Directory Fuzzing, Source Code Analysis, Encoding Identification, FTP Enumeration, Steganography, SSH Access, and Linux Privilege Escalation**.

This machine demonstrates how seemingly insignificant clues hidden across a web application can be chained together to obtain valid credentials and eventually compromise the entire system. It emphasizes careful enumeration, hidden file discovery, and the importance of investigating every artifact discovered during the engagement.

Throughout this machine, we perform:

- Web Enumeration
- Directory Fuzzing
- Source Code Analysis
- Base58 Decoding
- FTP Enumeration
- Steganography
- SSH Authentication
- Linux Privilege Escalation using GTFOBins

---

# Skills Covered

- Nmap Enumeration
- Directory Fuzzing
- Source Code Inspection
- Information Disclosure
- Hidden File Discovery
- Base58 Decoding
- FTP Enumeration
- Steganography Analysis
- Credential Discovery
- SSH Authentication
- Linux Enumeration
- Sudo Misconfiguration
- GTFOBins Privilege Escalation

---

# Nmap Scan

We began by performing an Nmap scan to identify the exposed services running on the target.

![](../Images/Pasted%20image%2020260730213003.png)

The scan revealed the available attack surface and confirmed that a web service was accessible.

---

# Directory Enumeration

The next step was to enumerate hidden directories using directory fuzzing.

![](../Images/Pasted%20image%2020260730213144.png)

During the scan, we discovered an interesting directory named:

```
/island
```

![](../Images/Pasted%20image%2020260730213402.png)

---

# Source Code Analysis

After browsing to the newly discovered page, we inspected its HTML source code.

While reading the source, we noticed an interesting keyword that appeared to be either a username or an important clue.

![](../Images/Pasted%20image%2020260730213524.png)

Since no obvious credentials were available, we continued our enumeration.

---

# Enumerating the Island Directory

Hidden directories often contain additional hidden resources.

We launched another directory fuzzing scan against:

```
/island
```

![](../Images/Pasted%20image%2020260730213623.png)

The scan revealed another hidden directory:

```
/island/2100
```

![](../Images/Pasted%20image%2020260730213658.png)

---

# Discovering a Hidden File Extension

After opening the page, we carefully analyzed its content.

The text hinted at a file using the following extension:

```
.ticket
```

![](../Images/Pasted%20image%2020260730213851.png)

Instead of guessing manually, we instructed our fuzzing tool to search specifically for files ending with the **.ticket** extension.

![](../Images/Pasted%20image%2020260730214526.png)

A hidden file was successfully discovered.

![](../Images/Pasted%20image%2020260730214700.png)

---

# Recovering Encoded Credentials

Inside the ticket file, we found what appeared to be an encoded password.

![](../Images/Pasted%20image%2020260730215605.png)

After identifying the encoding as **Base58**, we decoded it.

![](../Images/Pasted%20image%2020260730215723.png)

At this point we had:

- Username obtained from the page source
- Password recovered from the encoded ticket

Recovered credentials:

```
vigilante : !#th3h00d
```

---

# FTP Access

Using the recovered credentials, we authenticated to the FTP service.

![](../Images/Pasted%20image%2020260730220036.png)

The login was successful.

---

# FTP Enumeration

After listing the available files, one file immediately caught our attention:

```
.other_user
```

![](../Images/Pasted%20image%2020260730221117.png)

Reading the file revealed another system username.

![](../Images/Pasted%20image%2020260730221154.png)

To ensure that no important artifacts were missed, we downloaded every file from the FTP server.

```
mget *
```

![](../Images/Pasted%20image%2020260730220135.png)

---

# Steganography Analysis

Among the downloaded files were several images.

We analyzed them using **StegSeek**.

![](../Images/Pasted%20image%2020260730220346.png)

The analysis successfully extracted a hidden compressed archive.

---

# Extracting Sensitive Files

After extracting the archive, two interesting files appeared:

```
passwd
shadow
```

![](../Images/Pasted%20image%2020260730220629.png)

Inspecting the **shadow** file revealed another password.

![](../Images/Pasted%20image%2020260730220713.png)

We now possessed:

- A valid username
- A corresponding password

Making SSH authentication possible.

---

# SSH Access

Using the recovered credentials, we logged into the target through SSH.

We now had interactive shell access to the system.

---

# Privilege Escalation Enumeration

The first privilege escalation step was checking our sudo permissions.

```
sudo -l
```

The output revealed that the following binary could be executed with elevated privileges:

```
pkexec
```

---

# GTFOBins Privilege Escalation

To determine whether **pkexec** could be abused, we searched **GTFOBins**.

GTFOBins provides documented techniques for exploiting legitimate Linux binaries to perform privilege escalation.

The page included a privilege escalation technique for **pkexec**.

After executing the documented commands, we successfully spawned a root shell.

---

# Root Access

Privilege escalation was successful.

We obtained full administrative control over the target system.

---

# Summary

**Lian-Yu** is an excellent beginner-level machine that demonstrates how multiple small discoveries can be chained together into a complete system compromise.

Rather than relying on a single vulnerability, the machine encourages careful enumeration, hidden file discovery, source code inspection, steganography analysis, and Linux privilege escalation techniques.

It also highlights the importance of following every clue uncovered during reconnaissance, as each one contributes to the next stage of the attack.

## Skills Practiced

- Nmap Enumeration
- Directory Fuzzing
- Source Code Analysis
- Hidden Resource Discovery
- Base58 Decoding
- FTP Enumeration
- Steganography Analysis
- Credential Discovery
- SSH Authentication
- Linux Enumeration
- Sudo Misconfiguration Enumeration
- GTFOBins
- Linux Privilege Escalation
- Root Compromise

# Machine Compromised Successfully ✔
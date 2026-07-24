# Sudo Agent (TryHackMe)

# Overview

**Sudo Agent** is a beginner-to-intermediate Linux CTF that combines multiple penetration testing techniques in a single challenge.

Throughout this machine, we perform:

- Web Enumeration
- HTTP Header Manipulation
- FTP Brute Force
- Steganography
- Archive Password Cracking
- Base64 Decoding
- SSH Access
- Linux Privilege Escalation
- Sudo Misconfiguration Exploitation

The challenge demonstrates how seemingly unrelated pieces of information can be chained together to achieve full system compromise.


---

# Nmap Scan

We started by scanning the target to identify the exposed services.

![](../Images/Pasted%20image%2020260724162026.png)

---

# Web Enumeration

Browsing the website revealed the following message:

```text
Use your own codename as user-agent to access the site.
```

![](../Images/Pasted%20image%2020260724162130.png)

The message suggested that access depended on the value of the **User-Agent** HTTP header.

At the bottom of the page, we also noticed the signature:

```text
From
Agent R
```

This hinted that the codename might simply be a single alphabetic character.

---

# User-Agent Brute Force

We generated a wordlist containing all uppercase and lowercase letters.

![](../Images/Pasted%20image%2020260724162453.png)

Next, we intercepted the request using **Burp Suite**.

The request was then sent to **Intruder**.

![](../Images/Pasted%20image%2020260724162808.png)

We placed the payload position inside the **User-Agent** header and loaded our character list.

![](../Images/Pasted%20image%2020260724162908.png)

During the attack, we noticed that every request returned:

```text
HTTP 200
```

except one.

When the letter:

```text
C
```

was used, the response changed to:

```text
HTTP 302
```

This strongly indicated that **C** was the correct codename.

![](../Images/Pasted%20image%2020260724163004.png)

---

# Following the Redirect

We resent the request using:

```text
User-Agent: C
```

and followed the redirect.

![](../Images/Pasted%20image%2020260724163133.png)

The new page disclosed the username:

```text
chris
```

---

# FTP Brute Force

Since the FTP service was available, we attempted a brute-force attack using the discovered username.

Eventually, valid credentials were recovered.

![](../Images/Pasted%20image%2020260724163516.png)

---

# FTP Login

After logging into the FTP server, we downloaded every available file.

```
mget *
```

![](../Images/Pasted%20image%2020260724163715.png)

---

# Hidden Hint

Reading one of the downloaded text files revealed an interesting clue.

It mentioned that one of the images contained hidden login information.

![](../Images/Pasted%20image%2020260724163829.png)

---

# Binwalk Analysis

We analyzed the image using **Binwalk**.

```
binwalk image.jpg
```

Binwalk detected embedded data and extracted an archive.

![](../Images/Pasted%20image%2020260724164039.png)

The output also informed us that the extracted files had been written to:

```
To_agentR.txt
```

![](../Images/Pasted%20image%2020260724164248.png)

---

# Password-Protected Archive

Attempting to extract the ZIP archive prompted for a password.

![](../Images/Pasted%20image%2020260724165108.png)

---

# Cracking the ZIP Password

First, we converted the ZIP archive into a hash using:

```
zip2john archive.zip > hash.txt
```

![](../Images/Pasted%20image%2020260724164731.png)

Next, we cracked the password with **John the Ripper**.

![](../Images/Pasted%20image%2020260724164854.png)

---

# Extracting the Archive

Using the recovered password, we successfully extracted the archive.

![](../Images/Pasted%20image%2020260724165348.png)

---

# Base64 Decoding

The extracted file contained an encoded string.

![](../Images/Pasted%20image%2020260724165505.png)

It appeared to be Base64-encoded.

After decoding it, we obtained what looked like another password.

![](../Images/Pasted%20image%2020260724165603.png)

---

# Steghide Extraction

Next, we examined the second image using **Steghide**.

```
steghide extract -sf image.jpg
```

When prompted, we entered the password recovered from the Base64 string.

![](../Images/Pasted%20image%2020260724165839.png)

Steghide extracted a hidden text file:

```text
message.txt
```

Reading the file revealed valid SSH credentials.

![](../Images/Pasted%20image%2020260724165941.png)

---

# SSH Login

Using the recovered credentials, we logged into the target via SSH.

![](../Images/Pasted%20image%2020260724170104.png)

---

# Privilege Escalation

We checked which commands could be executed with elevated privileges.

```
sudo -l
```

![](../Images/Pasted%20image%2020260724170203.png)

The output contained:

```text
(ALL, !root) /bin/bash
```

This unusual sudo configuration immediately suggested a known privilege escalation vulnerability.

---

# Vulnerability Research

Searching for this sudo misconfiguration led us to a public vulnerability.

![](../Images/Pasted%20image%2020260724170635.png)

The associated CVE was identified.

![](../Images/Pasted%20image%2020260724170722.png)

We reviewed the exploitation technique.

![](../Images/Pasted%20image%2020260724170821.png)

---

# Root Access

After executing the exploit, we successfully obtained a root shell.

![](../Images/Pasted%20image%2020260724170929.png)

---

# Summary

This machine demonstrated how multiple attack techniques can be chained together to compromise a Linux system.

## Skills Practiced

- Nmap Enumeration
- Burp Suite Intruder
- HTTP Header Manipulation
- FTP Brute Force
- File Enumeration
- Binwalk
- ZIP Password Cracking
- John the Ripper
- Base64 Decoding
- Steghide
- SSH Authentication
- Linux Privilege Escalation
- Sudo Misconfiguration Exploitation

# Machine Compromised Successfully ✔
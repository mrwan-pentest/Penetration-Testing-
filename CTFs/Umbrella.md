# Umbrella (TryHackMe)

# Overview

**Umbrella** is a Linux-based CTF that focuses on **Docker Registry Enumeration, Database Enumeration, Password Cracking, SSH Authentication, Node.js Code Review, Remote Code Execution (RCE), Docker Escape concepts, and Linux Privilege Escalation**.

This machine demonstrates that compromising a system is not always about exploiting a single vulnerability. Instead, it requires chaining together multiple weaknesses, beginning with information disclosure in a Docker Registry and ending with privilege escalation on the host operating system.

Throughout this machine we perform:

- Docker Registry Enumeration
- Docker Image Information Disclosure
- Database Enumeration
- Password Cracking
- SSH Access
- Node.js Source Code Review
- Node.js Code Injection
- Reverse Shell
- Docker Escape Concept
- Linux Privilege Escalation

---

# Skills Covered

- Nmap Enumeration
- Docker Registry Enumeration
- Docker Image Analysis
- MySQL Enumeration
- John the Ripper
- Hydra
- SSH Authentication
- Source Code Review
- Node.js Security
- Understanding `eval()`
- Remote Code Execution (RCE)
- Docker Shared Volumes
- Linux Privilege Escalation

---

# Nmap Enumeration

As always, we begin by identifying the attack surface.

A standard Nmap scan revealed several open ports.

![](../Images/Pasted%20image%2020260802155701.png)

To gather additional information, we performed service and version detection using:

```bash
-sVC
```

![](../Images/Pasted%20image%2020260802155849.png)

This immediately revealed something interesting...

Port **5000** appeared to be running a **Docker Registry**.

![](../Images/Pasted%20image%2020260802155930.png)

---

# What is Docker Registry?

Before touching anything, it's always worth understanding what you're attacking.

A **Docker Registry** is a repository used to store Docker images.

Think of it as GitHub...

...but instead of storing source code, it stores complete Docker images.

If a registry is accidentally exposed to the public, attackers may be able to:

- Enumerate images
- Download application layers
- Recover configuration files
- Extract credentials
- Discover secrets

This immediately makes Docker Registry a very attractive attack surface.

---

# Research Before Exploitation

Instead of blindly attacking the service, we spent a few minutes researching Docker Registry enumeration.

One excellent resource is HackTricks:

```
https://hacktricks.wiki/de/network-services-pentesting/5000-pentesting-docker-registry.html
```

![](../Images/Pasted%20image%2020260802160146.png)

Learning how a technology works is often more valuable than memorizing commands.

---

# Docker Registry Enumeration

Following the documentation, we queried the registry using:

```bash
curl -s http://<TARGET-IP>:5000/v2/umbrella/timetracking/manifests/latest
```

![](../Images/Pasted%20image%2020260802160552.png)

Success!

Instead of receiving meaningless JSON, the registry leaked extremely valuable information.

Inside the manifest we discovered:

- Database hostname
- Database username
- Database password
- Database name

This is an excellent example of **Information Disclosure**.

---

# MySQL Access

With valid database credentials available, the next logical step was connecting to MySQL.

![](../Images/Pasted%20image%2020260802161243.png)

During authentication we used:

```bash
--skip-ssl
```

### Why?

Some MySQL servers require SSL negotiation.

When certificates are missing or improperly configured, authentication may fail.

Using:

```bash
--skip-ssl
```

tells the client to disable SSL negotiation and connect using plaintext communication.

---

# Database Enumeration

Once connected, we explored the available tables.

Eventually we located the users table.

![](../Images/Pasted%20image%2020260802161445.png)

Inside we recovered:

- Usernames
- Password hashes

The application had done the hard work for us.

Now it was our turn.

---

# Password Cracking

We exported the hashes into a file and cracked them using John the Ripper.

![](../Images/Pasted%20image%2020260802161707.png)

After several moments...

John successfully recovered multiple plaintext passwords.

---

# SSH Authentication

At this stage we had:

- Usernames
- Passwords

The next question became:

> Can any of these credentials be reused elsewhere?

Rather than manually testing every combination, Hydra handled the work for us.

![](../Images/Pasted%20image%2020260802161851.png)

Eventually Hydra identified valid SSH credentials.

---

# Initial Shell

Using the recovered credentials we authenticated via SSH.

![](../Images/Pasted%20image%2020260802162008.png)

We now had our initial foothold.

---

# Web Application Enumeration

Another service was still waiting for us on port **8080**.

We logged into the application using the same credentials.

![](../Images/Pasted%20image%2020260802162405.png)

After logging in, we noticed a page that accepted user input.

Input fields are always worth investigating...

Especially when we already have shell access to inspect the backend source code.

---

# Source Code Review

Since we already had SSH access, we located the application's source code.

Instead of guessing how the application behaved...

...we simply read the code.

![](../Images/Pasted%20image%2020260802162629.png)

Reviewing source code is one of the most powerful techniques during internal assessments.

It often reveals vulnerabilities that would otherwise remain invisible.

---

# Discovering the Vulnerability

After reviewing the application, we discovered it was written in **Node.js**.

More importantly...

The application was using the dangerous function:

```javascript
eval()
```

---

# Why is eval() Dangerous?

`eval()` executes whatever string it receives as JavaScript code.

Example:

```javascript
eval("2+2")
```

becomes

```javascript
4
```

However...

If an attacker controls that input:

```javascript
eval(userInput)
```

then the attacker controls what the server executes.

This frequently results in:

- Arbitrary JavaScript execution
- Command execution
- Remote Code Execution (RCE)./;

For this reason, using `eval()` on untrusted input is considered a serious security vulnerability.

---

# Achieving Remote Code Execution

Knowing that arbitrary JavaScript execution was possible, we searched for a Node.js reverse shell payload.

![](../Images/Pasted%20image%2020260802163020.png)

Since the application accepted only a single line of input, we converted the payload into a one-liner.

(ChatGPT made that part much easier.)

![](../Images/Pasted%20image%2020260802163156.png)

After starting our listener...

![](../Images/Pasted%20image%2020260802163223.png)

...the payload executed successfully.

![](../Images/Pasted%20image%2020260802163317.png)

A reverse shell was established.

---

# Stabilizing the Shell

The initial shell was unstable.

To obtain a proper interactive terminal we upgraded it using:

```bash
script -qc /bin/bash /dev/null
```

![](../Images/Pasted%20image%2020260802163407.png)

---

# Wait...

## Are We Really Root?

Running:

```bash
id
```

showed that we were root.

Sounds great...

Except...

We were **root inside a Docker container**.

Not on the actual operating system.

This is a very important distinction.

Compromising a container **does not automatically mean** the host has been compromised.

---

# Docker Escape Concept

Now the real challenge began.

How do we move from the container to the host?

Rather than immediately searching for kernel exploits...

we first investigated whether the container shared any directories with the host.

Using:

```bash
df -h
```

we inspected mounted filesystems.

![](../Images/Pasted%20image%2020260802163837.png)

Several shared directories appeared.

One directory immediately caught our attention:

```text
logs
```

---

# Verifying the Shared Volume

Before attempting privilege escalation, we needed proof that the directory was actually shared.

From the container:

We created a simple file.

![](../Images/Pasted%20image%2020260802164429.png)

Then we checked the same directory from the host.

![](../Images/Pasted%20image%2020260802164444.png)

The file appeared.

Perfect.

This confirmed that both systems were accessing the same filesystem.

---

# Why is This Dangerous?

Imagine writing files as **root inside the container**...

Those files also appear on the host.

That means we can potentially create files that the host later executes.

Or...

Create privileged binaries.

This shared volume became our bridge from Docker to the host.

---

# Privilege Escalation

Since we already had root privileges inside the container, we copied Bash into the shared directory.

![](../Images/Pasted%20image%2020260802164641.png)

Next we assigned the SUID permission:

```bash
chmod +s bash
```

![](../Images/Pasted%20image%2020260802164801.png)

When executed from the host...

The SUID bit caused Bash to run with root privileges.

Instantly giving us full root access.

![](../Images/Pasted%20image%2020260802164859.png)

Mission accomplished.

---

# Key Learning Points

This machine teaches several important real-world concepts:

- Exposed Docker Registries can leak sensitive information.
- Docker image metadata may contain hardcoded credentials.
- Password reuse frequently leads to lateral movement.
- Reading application source code is often faster than blind fuzzing.
- Never use `eval()` with untrusted user input.
- Root inside Docker is **not** necessarily root on the host.
- Shared Docker volumes can become a bridge for privilege escalation if misconfigured.

---

# Summary

Umbrella is an excellent example of how multiple small weaknesses can combine into a complete system compromise.

Rather than exploiting a single critical vulnerability, we chained together:

- Information Disclosure
- Database Enumeration
- Password Cracking
- Credential Reuse
- Source Code Review
- Node.js RCE
- Docker Enumeration
- Shared Volume Abuse
- Linux Privilege Escalation

Each step alone was not enough.

Together...

They resulted in full compromise of the target.

---

# Skills Practiced

- Nmap Enumeration
- Docker Registry Enumeration
- Docker Image Analysis
- MySQL Enumeration
- Password Cracking
- Hydra
- SSH Authentication
- Source Code Review
- Node.js Security
- eval() Abuse
- Remote Code Execution
- Docker Escape Concepts
- Linux Privilege Escalation

# Machine Compromised Successfully ✔
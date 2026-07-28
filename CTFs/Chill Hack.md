# Chill Hack (TryHackMe)

# Overview

**Chill Hack** is a Linux-based beginner/intermediate CTF that demonstrates how multiple low-severity weaknesses can be chained together to achieve full system compromise.

The machine combines **Web Enumeration, Command Injection, Reverse Shells, Shell Stabilization, Linux Privilege Escalation, Steganography, Password Cracking, Credential Discovery, and Docker Privilege Escalation**.

Rather than relying on a single vulnerability, the attack requires careful enumeration, bypassing simple input filtering, extracting hidden information from image files, recovering credentials, and finally abusing Docker group membership to obtain root privileges.

Throughout this machine, we perform:

- Web Enumeration
- Directory Fuzzing
- Command Injection
- Filter Bypass
- Reverse Shell
- Shell Stabilization
- Linux Privilege Escalation
- Steganography
- Password Cracking
- SSH Authentication
- Docker Privilege Escalation

---

# Skills Covered

- Nmap Enumeration
- Directory Fuzzing
- Command Injection
- Input Filter Bypass
- Reverse Shell Generation
- TTY Stabilization
- Linux Enumeration
- Sudo Misconfiguration Abuse
- Steganography
- Password Cracking with John the Ripper
- Base64 Decoding
- Hydra Password Validation
- Docker Privilege Escalation

---

# Nmap Scan

We began by scanning the target to identify the exposed services and discover the available attack surface.

![](../Images/Pasted%20image%2020260728161334.png)

The scan revealed the services running on the target, providing the starting point for further enumeration.

---

# Directory Fuzzing

After identifying the web server, we performed directory fuzzing to discover hidden resources.

![](../Images/Pasted%20image%2020260728161604.png)

Among the discovered directories, one immediately stood out:

```
/secret
```

![](../Images/Pasted%20image%2020260728161634.png)

---

# Discovering Command Injection

Browsing to the hidden page revealed an input field capable of executing operating system commands.

![](../Images/Pasted%20image%2020260728161843.png)

This indicated the presence of a **Command Injection** vulnerability, which could potentially be leveraged to obtain **Remote Code Execution (RCE)**.

---

# Bypassing the Input Filter

Basic commands such as:

```
ls
```

were blocked by a simple blacklist.

![](../Images/Pasted%20image%2020260728162003.png)

Instead of executing the command, the application responded with:

```
Are you a hacker?
```

This suggested that the application filtered specific command names rather than safely handling user input.

To bypass the blacklist, we inserted `/` characters between the command letters.

For example:

```
l/s
```

Linux interprets this path correctly while bypassing the application's naive filtering mechanism.

---

# Obtaining Remote Code Execution

With the filter bypassed, the next objective was obtaining a reverse shell.

We generated a Bash reverse shell payload using **Reverse Shell Generator**.

![](../Images/Pasted%20image%2020260728162233.png)

To avoid the blacklist, the payload was slightly modified by prepending the command with `/`.

![](../Images/Pasted%20image%2020260728162341.png)

Before executing the payload, we started a Netcat listener on our attacking machine.

![](../Images/Pasted%20image%2020260728162441.png)

After executing the payload, the target connected back successfully.

![](../Images/Pasted%20image%2020260728162642.png)

![](../Images/Pasted%20image%2020260728162724.png)

---

# Stabilizing the Shell

The initial reverse shell was unstable and lacked full terminal functionality.

![](../Images/Pasted%20image%2020260728163028.png)

To improve interaction, we generated a new Bash reverse shell and established another connection.

![](../Images/Pasted%20image%2020260728163114.png)

![](../Images/Pasted%20image%2020260728163145.png)

![](../Images/Pasted%20image%2020260728163203.png)

Finally, we upgraded the shell to a fully interactive TTY.

![](../Images/Pasted%20image%2020260728163423.png)

---

# Privilege Escalation to User `apaar`

We checked the available sudo permissions.

```
sudo -l
```

![](../Images/Pasted%20image%2020260728164017.png)

The output showed that we could execute a shell script as the user:

```
apaar
```

We inspected the script.

![](../Images/Pasted%20image%2020260728164142.png)

The script accepted user input and printed the supplied value without proper validation.

Instead of providing a normal message, we supplied:

```
/bin/bash
```

Executing the script with this input spawned a Bash shell running as **apaar**.

![](../Images/Pasted%20image%2020260728164228.png)

![](../Images/Pasted%20image%2020260728164253.png)

The shell was then upgraded again to a stable interactive TTY.

![](../Images/Pasted%20image%2020260728164827.png)

---

# Discovering Hidden Images

While enumerating the user's files, we discovered a PHP script.

![](../Images/Pasted%20image%2020260728164905.png)

Inspecting the source code revealed references to two image files.

Since these images were hosted on the target, we downloaded them to our attacking machine for offline analysis.

On the victim machine, an HTTP server was started:

```
python3 -m http.server 8888
```

The images were then downloaded from the attacker machine using:

```
wget http://TARGET_IP/images/002d7e638fb463fb7a266f5ffc7ac47d.gif

wget http://TARGET_IP:8888/images/hacker-with-laptop_23-2147985341.jpg
```

![](../Images/Pasted%20image%2020260728170652.png)

---

# Steganography Analysis

The downloaded images were analysed using **Stegseek**.

One of the JPEG images contained an embedded file.

![](../Images/Pasted%20image%2020260728170822.png)

The extracted file was password protected.

![](../Images/Pasted%20image%2020260728170900.png)

---

# Cracking the Archive Password

The protected archive was converted into a format supported by John the Ripper.

![](../Images/Pasted%20image%2020260728170917.png)

After cracking the hash, the archive password was successfully recovered.

![](../Images/Pasted%20image%2020260728170937.png)

Extracting the archive produced another file:

```
source_code.php
```

![](../Images/Pasted%20image%2020260728171023.png)

---

# Recovering Credentials

Inside the PHP source code we discovered a Base64-encoded password.

![](../Images/Pasted%20image%2020260728171106.png)

After decoding the Base64 string, we recovered the plaintext password.

![](../Images/Pasted%20image%2020260728171202.png)

Although the password was valid, the associated username remained unknown.

---

# Identifying the Correct User

To determine which user owned the recovered password, we created a list of local usernames and used **Hydra** to validate the credentials.

![](../Images/Pasted%20image%2020260728171627.png)

Hydra successfully identified the correct account.

Using the recovered credentials, we authenticated successfully.

![](../Images/Pasted%20image%2020260728171742.png)

---

# Docker Privilege Escalation

After logging in, we inspected the user's group memberships.

```
id
```

![](../Images/Pasted%20image%2020260728173706.png)

The output revealed that the user belonged to the **docker** group.

Membership in the Docker group is effectively equivalent to root privileges because Docker containers can mount the host filesystem and execute commands with elevated permissions.

To identify the appropriate exploitation technique, we consulted **GTFOBins**.

![](../Images/Pasted%20image%2020260728173759.png)

Using the documented Docker escape technique, we mounted the host filesystem inside a privileged container and obtained a root shell.

![](../Images/Pasted%20image%2020260728173832.png)

---

# Summary

This machine demonstrates how seemingly minor security issues can be chained together into a complete system compromise.

The attack began with a hidden web page containing a Command Injection vulnerability, continued through filter bypasses, reverse shell exploitation, and privilege escalation via a misconfigured sudo rule. Further enumeration uncovered hidden data inside images, which ultimately led to valid credentials. Finally, abusing Docker group membership resulted in full root access.

## Skills Practiced

- Nmap Enumeration
- Directory Fuzzing
- Command Injection
- Filter Bypass Techniques
- Remote Code Execution (RCE)
- Reverse Shell Generation
- Shell Stabilization (TTY)
- Linux Enumeration
- Sudo Misconfiguration Abuse
- Steganography Analysis
- Password Cracking
- Base64 Decoding
- Hydra Authentication Testing
- Docker Privilege Escalation
- GTFOBins Enumeration

# Machine Compromised Successfully ✔
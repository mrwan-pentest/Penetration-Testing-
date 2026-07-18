# Web Login Brute Force, SSH Key Recovery, and Privilege Escalation

## Overview

The objective of this lab was to discover a hidden login page, recover valid credentials through a brute-force attack, obtain an SSH private key, crack its passphrase, authenticate via SSH, and escalate privileges to gain root access.

---

## Nmap Scan

Performed an Nmap scan to identify the exposed services.

The scan revealed the following services:

- HTTP
    
- SSH
    

![[Pasted image 20260702000221.png]]

---

## Web Enumeration

Performed directory fuzzing to discover hidden resources on the web server.

A hidden login page was identified.

![[Pasted image 20260702000310.png]]

Inspected the page source code and discovered a valid username.

![[Pasted image 20260702001052.png]]

---

## Brute Force Attack

Performed a brute-force attack against the login page using **Hydra**.

```bash
hydra -f -V -l admin -P /usr/share/wordlists/rockyou.txt 10.82.135.6 http-post-form "/admin/index.php:user=^USER^&pass=^PASS^:Username or password invalid"
```

The POST parameters (`user=^USER^&pass=^PASS^`) were obtained by intercepting the authentication request with **Burp Suite**.

Successfully recovered the user's password.

![[Pasted image 20260702001217.png]]

---

## SSH Private Key Recovery

Authenticated to the web application using the recovered credentials.

Inside the application, discovered an SSH private key.

![[Pasted image 20260702001310.png]]

Saved the private key to a file and adjusted its permissions.

![[Pasted image 20260702001448.png]]

---

## Cracking the Private Key Passphrase

Converted the private key into a format supported by **John the Ripper**.

![[Pasted image 20260702001542.png]]

Cracked the passphrase successfully.

![[Pasted image 20260702001607.png]]

---

## SSH Authentication

Authenticated to the target system using the recovered private key and its passphrase.

![[Pasted image 20260702001948.png]]

---

## Privilege Escalation

Performed local enumeration and executed:

```bash
sudo -l
```

Discovered that the **cat** binary could be executed with elevated privileges.

![[Pasted image 20260702002042.png]]

Since `cat` could be executed as root, it was possible to read any file on the system.

Used it to read the `/etc/shadow` file and extracted the root password hash.

![[Pasted image 20260702002220.png]]

Copied the complete hash into a file and cracked it using **John the Ripper**.

![[Pasted image 20260702002351.png]]

---

## Root Access

After recovering the root password, authenticated as the **root** user.

![[Pasted image 20260702002704.png]]

Successfully obtained root privileges.

---

## Notes

### Burp Suite

Burp Suite was used to intercept the login request and identify the POST parameters required by Hydra.

### SSH Private Key

An SSH private key can optionally be protected with a passphrase. If the key is exposed, the passphrase must be recovered before it can be used for authentication.

### `sudo -l`

The `sudo -l` command lists the commands a user is permitted to execute with elevated privileges. Misconfigured sudo permissions often lead to privilege escalation.

### `/etc/shadow`

The `/etc/shadow` file stores password hashes for local Linux accounts. Reading this file allows an attacker to perform offline password cracking if sufficient privileges are obtained.
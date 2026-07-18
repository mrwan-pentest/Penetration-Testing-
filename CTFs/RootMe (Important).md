# Exploiting a File Upload Vulnerability and Privilege Escalation via SUID

This lab demonstrates how to exploit a **File Upload** vulnerability to obtain a **Reverse Shell**, upgrade it to a fully interactive shell, and finally escalate privileges by abusing a misconfigured **SUID** binary.

---

## Step 1 - Network Enumeration

We began by performing an Nmap scan against the target to identify open ports and running services.

![[Pasted image 20260716171716.png]]

---

## Step 2 - Web Enumeration

Next, we performed directory fuzzing to discover hidden files and directories exposed by the web server.

![[Pasted image 20260716171823.png]]

During the enumeration process, we discovered a **panel** page.

![[Pasted image 20260716171907.png]]

Further exploration revealed an **upload** page where users were allowed to upload files.

![[Pasted image 20260716172013.png]]

At this point, we identified a potential **File Upload** vulnerability.

---

## What is a File Upload Vulnerability?

A **File Upload** vulnerability occurs when a web application allows users to upload files without properly validating their type or content.

If an attacker is able to upload executable files such as PHP, ASPX, or JSP scripts, they may execute arbitrary code on the server, leading to **Remote Code Execution (RCE)**.

Common impacts include:

- Remote Code Execution (RCE)
- Reverse Shell
- Web Shell deployment
- Full server compromise

---

## Step 3 - Preparing a PHP Reverse Shell

To gain remote access, we searched for a publicly available PHP Reverse Shell.

![[Pasted image 20260716172114.png]]

We copied the PHP shell to our attack machine and modified it by replacing the attacker's IP address and listening port with our own.

![[Pasted image 20260716172326.png]]

---

## Step 4 - Bypassing the Upload Filter

Our first attempt was to upload the file with the standard **.php** extension.

The upload failed, indicating that the application was filtering PHP files.

![[Pasted image 20260716172443.png]]

To bypass this restriction, we changed the file extension from **.php** to **.phtml**.

The **.phtml** extension is another valid PHP extension that many web servers execute as PHP code.

![[Pasted image 20260716172545.png]]

After changing the extension, the upload completed successfully.

![[Pasted image 20260716172622.png]]

---

## Step 5 - Obtaining a Reverse Shell

We started a Netcat listener on our attack machine.

![[Pasted image 20260716172652.png]]

Next, we accessed the uploaded shell through the web application.

![[Pasted image 20260716172725.png]]

The shell executed successfully and established a Reverse Shell connection to our listener.

![[Pasted image 20260716172744.png]]

---

## Step 6 - Upgrading the Shell

The initial shell was not fully interactive.

To obtain a proper terminal, we upgraded the shell using Python's `pty` module.

```bash
python3 -c 'import pty; pty.spawn("/bin/bash")'
```

![[Pasted image 20260716172904.png]]

A fully interactive shell greatly improves usability by enabling features such as command history, tab completion, and interactive applications.

---

## Step 7 - Capturing the User Flag

After obtaining a stable shell, we located and retrieved the user flag.

![[Pasted image 20260716173122.png]]

---

## Step 8 - Enumerating SUID Binaries

To identify potential privilege escalation vectors, we searched for files with the **SUID** permission set.

```bash
find / -type f -perm /4000 2>/dev/null
```

This command searches the entire filesystem for files that execute with the permissions of their owner.

![[Pasted image 20260716173306.png]]

Among the results, we discovered that the **Python 2.7** binary had the SUID bit set.

![[Pasted image 20260716173402.png]]

---

## What is SUID?

**SUID (Set User ID)** is a special Linux permission that causes an executable to run with the privileges of its owner instead of the user executing it.

When applied to binaries owned by **root**, the program executes with root privileges.

If a vulnerable or misconfigured binary has the SUID bit set, it may allow an attacker to escalate privileges and obtain root access.

---

## Step 9 - Exploiting the SUID Binary

To determine whether the Python binary could be abused, we searched for it on **GTFOBins**.

GTFOBins documents legitimate Unix binaries that can be abused for privilege escalation under specific configurations.

![[Pasted image 20260716173551.png]]

GTFOBins provided the following payload for spawning a root shell through the SUID Python binary:

```bash
/usr/bin/python2.7 -c 'import os; os.execl("/bin/sh", "sh", "-p")'
```

After executing the command, we successfully obtained a root shell.

![[Pasted image 20260716173649.png]]

---

## Step 10 - Capturing the Root Flag

With root privileges, we accessed the root user's directory and successfully retrieved the root flag.

![[Pasted image 20260716173717.png]]

---

# Summary

In this lab, we successfully compromised the target by exploiting a **File Upload** vulnerability that allowed us to upload and execute a PHP Reverse Shell. After upgrading the shell to a fully interactive TTY, we performed local enumeration and discovered a Python binary with the **SUID** bit set. By leveraging a known privilege escalation technique from **GTFOBins**, we obtained root privileges and captured the final flag.

## Attack Chain

```text
Network Enumeration
        ↓
Directory Fuzzing
        ↓
File Upload Vulnerability
        ↓
Upload PHP Reverse Shell
        ↓
Reverse Shell
        ↓
TTY Upgrade
        ↓
SUID Enumeration
        ↓
GTFOBins
        ↓
Root Shell
        ↓
Capture Root Flag
```
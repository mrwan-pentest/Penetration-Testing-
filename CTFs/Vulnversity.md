# Upload Vulnerability to Root via SUID

## Overview

The objective of this lab was to exploit an insecure **File Upload** functionality to gain initial access to the target system through a PHP Reverse Shell. After obtaining a shell, we enumerated the system, discovered a vulnerable **SUID** binary, and abused it to reset the root password, ultimately gaining full administrative access.

During this engagement, we successfully:

- Enumerated the target with Nmap.
- Identified an insecure file upload functionality.
- Bypassed file extension filtering.
- Uploaded and executed a PHP Reverse Shell.
- Enumerated SUID binaries.
- Exploited a vulnerable SUID binary.
- Reset the root password.
- Logged in as root.

---

# About File Upload Vulnerabilities

A **File Upload** vulnerability occurs when a web application allows users to upload files without properly validating their type or contents.

If an attacker can upload executable files such as PHP scripts, they may achieve **Remote Code Execution (RCE)** by accessing the uploaded file through the web server.

Common bypass techniques include:

- Changing the file extension (`.php` → `.phtml`)
- Double extensions
- MIME type manipulation
- Null byte injection (older PHP versions)

---

# About SUID

**SUID (Set User ID)** is a special Linux permission that allows a program to execute with the permissions of its owner instead of the current user.

If a vulnerable binary has the SUID bit enabled and is owned by **root**, it may be abused to execute commands with root privileges.

SUID binaries can be enumerated using:

```bash
find / -type f -perm /4000 2>/dev/null
```

Many known SUID exploitation techniques are documented on **GTFOBins**.

---

# Initial Enumeration

## Nmap Scan

We began by performing an Nmap scan to identify open ports and running services.

![](../Images/Pasted%20image%2020260717221406.png)

---

## Service Enumeration

Next, we performed version detection and executed Nmap NSE scripts to gather additional information about the discovered services.

![](../Images/Pasted%20image%2020260717221515.png)

The scan revealed an HTTP service running on port **3333**.

---

## Web Enumeration

We performed directory fuzzing against the web server to discover hidden resources.

![](../Images/Pasted%20image%2020260717221648.png)

One of the discovered directories appeared particularly interesting.

![](../Images/Pasted%20image%2020260717221742.png)

---

# Discovering the File Upload Functionality

After accessing the page, we found a feature that allowed users to upload files.

![](../Images/Pasted%20image%2020260717221836.png)

This indicated a potential **File Upload** vulnerability.

---

# Preparing the Reverse Shell

We searched for a PHP Reverse Shell and copied it to our attacker machine.

![](../Images/Pasted%20image%2020260717221936.png)

We modified the payload by replacing the attacker's IP address and listening port.

![](../Images/Pasted%20image%2020260717222044.png)

---

# Bypassing File Extension Filtering

Our first upload attempt failed because the application blocked files with the `.php` extension.

![](../Images/Pasted%20image%2020260717222151.png)

To bypass the filter, we renamed the file using another PHP-supported extension:

```text
.phtml
```

![](../Images/Pasted%20image%2020260717222239.png)

The upload was then accepted successfully.

![](../Images/Pasted%20image%2020260717222302.png)

---

# Locating the Uploaded File

Although the upload succeeded, the application did not reveal where the file was stored.

We therefore performed directory fuzzing against the upload directory itself.

![](../Images/Pasted%20image%2020260717222450.png)

This revealed the directory used to access uploaded files.

We navigated to the uploaded Reverse Shell.

![](../Images/Pasted%20image%2020260717222535.png)

---

# Initial Access

Before executing the payload, we started a Netcat listener.

After opening the uploaded file in the browser, the PHP code executed and connected back to our listener.

![](../Images/Pasted%20image%2020260717222641.png)

We successfully obtained an initial shell on the target.

---

# Privilege Escalation

## Enumerating SUID Binaries

We searched for binaries with the SUID bit enabled.

```bash
find / -type f -perm /4000 2>/dev/null
```

![](../Images/Pasted%20image%2020260717222930.png)

During enumeration, we discovered a binary that could be abused for privilege escalation.

![](../Images/Pasted%20image%2020260717223022.png)

---

## Researching the Exploit

We searched for the binary on **GTFOBins** to identify a known privilege escalation technique.

![](../Images/Pasted%20image%2020260717223326.png)

The published technique demonstrated how the binary could execute a custom **systemd service** as root.

Originally, the example executed the `id` command and redirected its output to:

```text
/tmp/output
```

However, instead of simply printing the current privileges, we modified the service so it would reset the root password.

We replaced the command with:

```ini
ExecStart=/bin/sh -c "echo 'root:Passw@rd123!' | chpasswd"
```

![](../Images/Pasted%20image%2020260407070931.png|544)

This command changes the root password to a value of our choosing.

---

## Obtaining Root

After modifying the payload, we executed the remaining exploitation steps.

![](../Images/Pasted%20image%2020260717223908.png)

The exploit completed successfully and updated the root password.

We then authenticated as the root user using the newly created password.

![](../Images/Pasted%20image%2020260717224108.png)

Root access was successfully obtained.

---

# Summary

In this lab we learned how to:

- Perform service enumeration using Nmap.
- Discover hidden web resources through directory fuzzing.
- Identify insecure file upload functionality.
- Bypass file extension filtering using alternative PHP extensions.
- Upload and execute a PHP Reverse Shell.
- Enumerate SUID binaries.
- Research privilege escalation techniques using GTFOBins.
- Abuse a vulnerable SUID binary to execute privileged actions.
- Reset the root password.
- Obtain full administrative access to the target system.

This lab demonstrates how a combination of an insecure File Upload implementation and a misconfigured SUID binary can be chained together to achieve complete system compromise.
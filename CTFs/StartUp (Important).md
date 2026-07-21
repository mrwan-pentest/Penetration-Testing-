# FTP Anonymous Access to Cron Job Privilege Escalation

## Overview

The objective of this lab is to exploit an FTP server that allows anonymous access, upload a PHP Reverse Shell to gain initial access, extract credentials from a network capture, and finally escalate privileges by abusing a misconfigured script executed by a root Cron Job.

During this engagement, we successfully:

- Gained anonymous access to the FTP server.
- Uploaded and executed a PHP Reverse Shell.
- Retrieved sensitive files from the target.
- Analyzed a packet capture to recover SSH credentials.
- Logged into the target via SSH.
- Abused a writable script executed by a root Cron Job.
- Obtained a Reverse Shell running as root.

---

# About Anonymous FTP

Anonymous FTP allows users to connect to an FTP server without providing valid credentials.

Typically, users authenticate using:

```text
Username: anonymous
Password: anonymous@example.com
```

or simply any password.

If write permissions are enabled, attackers may upload malicious files, making anonymous FTP a serious security risk.

---

# About Cron Jobs

Cron is a Linux scheduling service used to execute commands or scripts automatically at specified intervals.

If a Cron Job runs with root privileges and executes a file that is writable by an unprivileged user, that file can be modified to execute arbitrary commands as root, leading to Privilege Escalation.

---

## Step 1 - Initial Enumeration

We started by performing an Nmap scan to identify open ports and running services on the target machine.

![](../Images/Pasted%20image%2020260716230758.png)

---

## Step 2 - Anonymous FTP Access

We attempted to authenticate to the FTP service using the anonymous account.

The server allowed anonymous authentication without requiring valid credentials.

![](../Images/Pasted%20image%2020260716231128.png)

This indicated that the FTP server was publicly accessible and could potentially allow file uploads.

---

## Step 3 - Web Enumeration

Next, we performed directory enumeration against the web server to discover hidden resources.

![](../Images/Pasted%20image%2020260716231230.png)

The scan revealed a directory named:

```text
/files
```

![](../Images/Pasted%20image%2020260716231312.png)

After accessing this directory, we discovered that it pointed directly to the FTP server's files, meaning any uploaded files could be accessed through the web server.

This made it possible to upload a PHP script via FTP and execute it from the browser.

---

## Step 4 - Preparing a PHP Reverse Shell

We searched for a PHP Reverse Shell.

![](../Images/Pasted%20image%2020260716231656.png)

After downloading the shell, we modified it by configuring our attacker's IP address and listening port.

![](../Images/Pasted%20image%2020260716231947.png)

---

## Step 5 - Uploading the Reverse Shell

Using the anonymous FTP session, we uploaded the PHP Reverse Shell to the server.

![](../Images/Pasted%20image%2020260716232156.png)

---

## Step 6 - Starting the Listener

Before executing the uploaded shell, we started a Netcat listener to receive the incoming Reverse Shell connection.

![](../Images/Pasted%20image%2020260716232032.png)

---

## Step 7 - Gaining Initial Access

We navigated to the uploaded PHP file through the web server.

Executing the file caused the PHP code to run on the server and establish a Reverse Shell.

![](../Images/Pasted%20image%2020260716232249.png)

A successful Reverse Shell connection was established.

![](../Images/Pasted%20image%2020260716232319.png)

---

## Step 8 - Discovering Sensitive Files

During post-exploitation enumeration, we discovered a Wireshark capture file.

![](../Images/Pasted%20image%2020260716232959.png)

To retrieve the file, we copied it into the FTP directory so it could be downloaded from our attacker machine.

![](../Images/Pasted%20image%2020260716233150.png)

We then downloaded the capture file for offline analysis.

![](../Images/Pasted%20image%2020260716233323.png)

---

## Step 9 - Packet Capture Analysis

We opened the capture file using Wireshark.

![](../Images/Pasted%20image%2020260717161229.png)

While analyzing the traffic, we noticed repeated communications involving port **4444**, making it an interesting indicator for further investigation.

![](../Images/Pasted%20image%2020260717161813.png)

Inspecting the suspicious packets revealed plaintext credentials.

![](../Images/Pasted%20image%2020260717162006.png)

These credentials were later used to access the target via SSH.

---

## Step 10 - SSH Access

Using the recovered credentials, we authenticated successfully to the SSH service.

![](../Images/Pasted%20image%2020260717162227.png)

This provided a more stable shell for privilege escalation.

---

## Step 11 - Enumerating for Privilege Escalation

During enumeration, we discovered a directory containing a script executed by the root user.

![](../Images/Pasted%20image%2020260717163017.png)

After examining the script, we found that it executed another file.

![](../Images/Pasted%20image%2020260717163047.png)

We checked the permissions of this secondary file and discovered that our current user had full write permissions.

![](../Images/Pasted%20image%2020260717163130.png)

This represented a classic Cron Job privilege escalation opportunity.

---

## Step 12 - Abusing the Root Cron Job

We generated a Bash Reverse Shell payload from **revshells.com**.

![](../Images/Pasted%20image%2020260717163211.png)

We replaced the contents of the writable script with the Reverse Shell payload.

![](../Images/Pasted%20image%2020260717163330.png)

Before the Cron Job executed, we started a Netcat listener.

![](../Images/Pasted%20image%2020260717163347.png)

Once the scheduled Cron Job ran, it executed our modified script with root privileges, establishing a Reverse Shell as the root user.

![](../Images/Pasted%20image%2020260717163411.png)

---

# Summary

In this lab we learned how to:

- Enumerate services using Nmap.
- Exploit Anonymous FTP access.
- Upload and execute a PHP Reverse Shell.
- Retrieve sensitive files from the compromised system.
- Analyze network traffic with Wireshark.
- Recover plaintext credentials from packet captures.
- Gain stable SSH access.
- Identify an insecure Cron Job configuration.
- Abuse a writable script executed by root.
- Obtain a root Reverse Shell through Cron Job privilege escalation.

This lab demonstrates how multiple small misconfigurations—including anonymous FTP access, exposed sensitive files, plaintext credentials, and insecure Cron Job permissions—can be chained together to achieve full system compromise.
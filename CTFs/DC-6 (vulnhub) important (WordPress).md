# WordPress Reverse Shell & Privilege Escalation

## Overview

This lab demonstrates the process of compromising a vulnerable **WordPress** application to obtain a **Reverse Shell**, perform local enumeration, and escalate privileges to retrieve the **Root Flag**.

The attack chain included service enumeration, WordPress user discovery, credential brute forcing, exploiting a vulnerable plugin to gain remote code execution, and leveraging misconfigured **sudo** permissions to obtain root access.

---

## Objective

The objective of this lab was to identify the target, gain remote access through a vulnerable WordPress application, escalate privileges, and retrieve the root flag.

---

## Network Discovery

Performed a network scan to identify active hosts.

![](../Images/Pasted%20image%2020260428105734.png)

---

## Nmap Scan

Identified the target host along with its open ports.

![](../Images/Pasted%20image%2020260428105846.png)

Performed a detailed Nmap scan against the discovered host.

![](../Images/Pasted%20image%2020260428110019.png)

---

## Web Enumeration

Visited the web application and identified it as a **WordPress** website.

![](../Images/Pasted%20image%2020260428110152.png)

Performed web fuzzing to discover additional resources.

![](../Images/Pasted%20image%2020260428110238.png)

Discovered the WordPress login page.

![](../Images/Pasted%20image%2020260428110324.png)

Added the target domain to the local **hosts** file for proper name resolution.

![](../Images/Pasted%20image%2020260428110512.png)

---

## WordPress User Enumeration

Enumerated valid WordPress usernames.

![](../Images/Pasted%20image%2020260428110548.png)

Successfully identified multiple users.

![](../Images/Pasted%20image%2020260428110618.png)

---

## Credential Attack

Based on the challenge hint, extracted passwords containing **k01** into a separate wordlist.

![](../Images/Pasted%20image%2020260428110744.png)

Saved the discovered usernames into a dedicated user list.

![](../Images/Pasted%20image%2020260428110934.png)

Performed a brute-force attack using the generated username and password lists.

![](../Images/Pasted%20image%2020260428111048.png)

Successfully recovered valid credentials.

![](../Images/Pasted%20image%2020260428111258.png)

---

## Vulnerability Research

Accessed the vulnerable application using the recovered credentials.

![](../Images/Pasted%20image%2020260428111506.png)

Searched for publicly available exploits using **SearchSploit**.

![](../Images/Pasted%20image%2020260428111645.png)

Copied the exploit to the local machine.

![](../Images/Pasted%20image%2020260428111734.png)

Reviewed the exploit source code to understand how it achieves **Remote Code Execution** through a crafted HTTP request.

![](../Images/Pasted%20image%2020260428111916.png)

The exploit documentation showed that modifying the request would allow execution of arbitrary commands, making it possible to obtain a **Reverse Shell**.

![](../Images/Pasted%20image%2020260428112023.png)

---

## Reverse Shell

Prepared Burp Suite to intercept the vulnerable HTTP request.

![](../Images/Pasted%20image%2020260428112418.png)

Intercepted the request.

![](../Images/Pasted%20image%2020260428112458.png)

Modified the payload to execute a reverse shell and forwarded the request.

![](../Images/Pasted%20image%2020260428112754.png)

Started a Netcat listener and successfully received a reverse shell.

![](../Images/Pasted%20image%2020260428112826.png)

---

## Local Enumeration

Performed local enumeration and recovered additional credentials.

![](../Images/Pasted%20image%2020260428115434.png)

Discovered a binary that could be executed as another user.

![](../Images/Pasted%20image%2020260428115543.png)

Executed the binary to switch to the higher-privileged user.

![](../Images/Pasted%20image%2020260428123811.png)

---

## Privilege Escalation

Enumerated the user's **sudo** privileges.

![](../Images/Pasted%20image%2020260428124710.png)

Discovered that **Nmap** could be executed with **root** privileges.

Older versions of Nmap included an interactive mode that could be abused to spawn a shell. However, the installed version no longer supported this feature.

Searched **GTFOBins** for an alternative privilege escalation technique and executed the following commands:

```bash
echo 'os.execute("/bin/sh")' > /tmp/root.nse
sudo nmap --script=/tmp/root.nse
```

Successfully obtained a root shell.

![](../Images/Pasted%20image%2020260428124835.png)

---

## Flags

Successfully located and read the **Root Flag**.

![](../Images/Pasted%20image%2020260428125242.png)

---

## Notes

### SearchSploit

SearchSploit is an offline utility that allows searching the Exploit-DB database directly from Kali Linux.

### Reverse Shell

A Reverse Shell forces the target machine to initiate a connection back to the attacker's listener, providing remote command execution.

### GTFOBins

GTFOBins is a collection of Unix binaries that can be abused to bypass security restrictions and perform privilege escalation when executed with elevated privileges.
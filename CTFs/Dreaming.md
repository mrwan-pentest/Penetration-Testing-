# Web Exploitation, Database Abuse, and Cron-Based Privilege Escalation

## Overview

The objective of this lab was to enumerate the target web application, exploit a vulnerable service to obtain an initial shell, abuse a database-backed application to move laterally between users, and finally achieve root access through a vulnerable Python script executed by **Cron**.

---

## Nmap Scan

Performed an Nmap scan to identify the exposed services running on the target.

![](../Images/Pasted%20image%2020260502210127.png)

---

## Web Enumeration

Performed directory fuzzing to discover hidden resources.

![](../Images/Pasted%20image%2020260502210159.png)

Discovered the following directory.

![](../Images/Pasted%20image%2020260502210222.png)

---

## Default Credentials

Accessed the login page and successfully authenticated using the default credentials.
(password)

![](../Images/Pasted%20image%2020260502210358.png)

---

## Vulnerability Research

Identified the application version and searched for publicly available exploits.

![](../Images/Pasted%20image%2020260502210459.png)

Found a Python exploit targeting the application.

![](../Images/Pasted%20image%2020260502210551.png)

![](../Images/Pasted%20image%2020260502210620.png)

Reviewed the exploit documentation to understand its usage.

![](../Images/Pasted%20image%2020260502210706.png)

Executed the exploit successfully and obtained an initial shell.

![](../Images/Pasted%20image%2020260502211729.png)

---

## Shell Stabilization

Navigated to the appropriate directory.

![](../Images/Pasted%20image%2020260502211752.png)

The initial shell was unstable, so it was upgraded to a fully interactive TTY.

![](../Images/Pasted%20image%2020260502212751.png)

---

## Lateral Movement

Discovered credentials belonging to another user.

Based on the recovered password, identified the corresponding username.

![](../Images/Pasted%20image%2020260502212839.png)

Authenticated via SSH using the recovered credentials.

![](../Images/Pasted%20image%2020260502213010.png)

---

## Database Enumeration

During local enumeration, discovered database credentials.

![](../Images/Pasted%20image%2020260502213754.png)

Also found a binary that could be executed as another user.

![](../Images/Pasted%20image%2020260502213904.png)

After analyzing its behavior, it became clear that the binary processed user records stored in the database.

![](../Images/Pasted%20image%2020260502214042.png)

Authenticated to the database.

![](../Images/Pasted%20image%2020260502214629.png)

Inserted a malicious record containing a payload that spawned a shell when processed by the application.

![](../Images/Pasted%20image%2020260502220150.png)

The payload executed successfully, providing a shell as the target user.

Since the shell was non-interactive, modified the user's file permissions to allow other users to read the password file.

![](../Images/Pasted%20image%2020260502220301.png)

Returned to the previous user account and read the exposed password.

```
mementoMORI666
```

![](../Images/Pasted%20image%2020260502220344.png)

Authenticated as the newly compromised user.

![](../Images/Pasted%20image%2020260502220424.png)

---

## Privilege Escalation

Discovered a Python script on the system.

![](../Images/Pasted%20image%2020260503144213.png)

The script imported another Python module.

![](../Images/Pasted%20image%2020260503144236.png)

Inspected the imported module and discovered that it was writable.

![](../Images/Pasted%20image%2020260503144322.png)

Modified the module by inserting a Python reverse shell payload.

![](../Images/Pasted%20image%2020260503144410.png)

Initially, the reverse shell executed with the same user privileges.

Exited the session, started a listener, and after a short period received a new connection with **root** privileges.

![](../Images/Pasted%20image%2020260503144530.png)

The behavior strongly indicates that the vulnerable Python script was executed automatically by a **Cron job** running as the root user. When Cron executed the modified module, the injected payload established a reverse shell as **root**.

---



### Cron

**Cron** is the Linux task scheduler used to execute commands or scripts automatically at scheduled intervals.

If a root-owned Cron job executes a writable script or imports a writable Python module, modifying that file can result in **Privilege Escalation** to the root user.
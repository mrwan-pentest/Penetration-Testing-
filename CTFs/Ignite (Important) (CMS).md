# Lab Overview

**Objective:** Exploit a vulnerable **FUEL CMS** installation by identifying a known vulnerability, achieving **Remote Code Execution (RCE)**, obtaining a reverse shell, and extracting the database credentials from the CMS configuration files.

---

# Nmap Scan

We began by performing an Nmap scan to identify the open ports on the target.

![](../Images/Pasted%20image%2020260401163404.png)

---

# Service Enumeration

Next, we enabled **version detection** and executed the default Nmap scripts to gather additional information about the running services.

![](../Images/Pasted%20image%2020260401163435.png)

The scan revealed that the target was running the **FUEL CMS**.

---

# Directory Enumeration

We performed directory fuzzing against the web application to discover hidden files and directories.

![](../Images/Pasted%20image%2020260401163421.png)

---

# Searching for a Known Exploit

Since the target was running **FUEL CMS**, we searched for publicly available exploits affecting this version and downloaded the exploit to our attacking machine.

![](../Images/Pasted%20image%2020260401163520.png)

---

# Exploiting the CMS

We executed the exploit against the target.

The exploit successfully demonstrated that the application was vulnerable to **Remote Code Execution (RCE)**, allowing arbitrary system commands to be executed.

![](../Images/Pasted%20image%2020260401163557.png)

![](../Images/Pasted%20image%2020260401163624.png)

---

# Obtaining a Reverse Shell

We started a listener on our attacking machine and executed a reverse shell payload through the RCE vulnerability.

After triggering the payload, we successfully obtained a reverse shell on the target.

![](../Images/Pasted%20image%2020260401163644.png)

---

# Stabilizing the Shell

To improve the shell's usability, we upgraded it to a fully interactive TTY shell using `stty`.

![](../Images/Pasted%20image%2020260401163656.png)

---

# Locating the CMS Configuration Files

By reviewing the CMS documentation and directory structure, we identified the location where **FUEL CMS** stores its configuration files.

We navigated to the configuration directory.

![](../Images/Pasted%20image%2020260401163717.png)

---

# Extracting Database Credentials

After reading the database configuration file, we recovered the database credentials, including the **MySQL root username and password**.

![](../Images/Pasted%20image%2020260401163738.png)
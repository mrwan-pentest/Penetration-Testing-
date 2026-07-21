# Objective

The objective was to enumerate the target, gain initial access through a vulnerable WordPress installation, and escalate privileges to obtain root access.

---

# Nmap Scan

Performed an Nmap scan to identify the available services and open ports.

![](../Images/Pasted%20image%2020260419063333.png)

---

# Update Hosts File

Added the target domain to the local **hosts** file for proper name resolution.

![](../Images/Pasted%20image%2020260419063559.png)

---

# Identify the Web Application

Discovered that the target was running **WordPress**.

![](../Images/Pasted%20image%2020260419064530.png)

![](../Images/Pasted%20image%2020260419064523.png)


---

# Web Fuzzing

Performed web fuzzing to discover hidden files and directories.

![](../Images/Pasted%20image%2020260419064838.png)

---

# WordPress User Enumeration

Enumerated WordPress users using the **-u** option.

![](../Images/Pasted%20image%2020260419064951.png)

The following usernames were successfully identified.

![](../Images/Pasted%20image%2020260419065036.png)

---

# Brute Force Attack

Performed a brute-force attack against the discovered users.

![](../Images/Pasted%20image%2020260419065151.png)

Successfully recovered valid credentials.

![](../Images/Pasted%20image%2020260419070401.png)

---

# Identify the WordPress Version

Determined the WordPress version running on the target.

![](../Images/Pasted%20image%2020260419070605.png)

---

# Vulnerability Research

Searched for publicly available exploits targeting the identified version.

![](../Images/Pasted%20image%2020260419070643.png)

---

# SearchSploit

Verified that a Metasploit module was available for the vulnerability using **SearchSploit**.

![](../Images/Pasted%20image%2020260419070824.png)

---

# Metasploit

Located the corresponding exploit module within Metasploit.

![](../Images/Pasted%20image%2020260419070916.png)

Executed the exploit successfully.

![](../Images/Pasted%20image%2020260419071129.png)

---

# Obtain a Shell

Successfully obtained a shell on the target system.

![](../Images/Pasted%20image%2020260419071608.png)

---

# Inspect the WordPress Configuration

Opened the WordPress configuration file.

![](../Images/Pasted%20image%2020260419071635.png)

Recovered the database username and password.

![](../Images/Pasted%20image%2020260419071754.png)

---

# MySQL Access

Logged into the MySQL database using the recovered credentials.

![](../Images/Pasted%20image%2020260419072010.png)

After enumeration, no useful information was found that could be leveraged for further exploitation.

---

# Privilege Escalation

Searched for SUID binaries and discovered a custom executable named **checker**.

![](../Images/Pasted%20image%2020260419073038.png)

To exploit the binary, the following commands were executed:

```bash
file /usr/bin/checker
ltrace /usr/sbin/checker
export admin=1
/usr/sbin/checker
```

This successfully resulted in root privileges.

![](../Images/Pasted%20image%2020260419074618.png)

---

# Command Explanation

|Command|Description|
|---|---|
|`file /usr/bin/checker`|Identifies the file type (ELF, script, architecture, etc.).|
|`ltrace /usr/sbin/checker`|Monitors library calls made by the binary during execution.|
|`export admin=1`|Creates an environment variable required by the binary.|
|`/usr/sbin/checker`|Executes the vulnerable binary while using the controlled environment variable.|

---

# Notes

## file

The **file** command determines the type of a file.

It identifies whether the file is:

- ELF executable
    
- Script
    
- 32-bit or 64-bit binary
    
- Shared object
    
- Text file
    

---

## ltrace

**ltrace** is a Linux utility used to monitor the **library function calls** made by a program during execution.

It helps analysts understand how a binary behaves internally and is particularly useful during privilege escalation when analyzing custom SUID binaries.
# EternalBlue (MS17-010)

## Overview

**EternalBlue (MS17-010)** is a critical vulnerability in the **SMBv1 (Server Message Block version 1)** protocol that allows an unauthenticated attacker to execute arbitrary code remotely.

It affects several legacy Microsoft Windows operating systems, including:

- Windows 7
    
- Windows Server 2008
    
- Other outdated and unpatched Windows versions
    

---

## Impact

Successful exploitation may allow an attacker to:

- Remote Code Execution (RCE)
    
- Full system compromise
    
- Privilege escalation to **NT AUTHORITY\SYSTEM**
    
- Worm-like propagation across vulnerable hosts
    

---

# Objective

The objective of this lab was to identify a vulnerable SMB service, exploit the **EternalBlue (MS17-010)** vulnerability, obtain a Meterpreter session, dump password hashes, and retrieve all challenge flags.

---

# Nmap Scan

Performed an Nmap scan to identify the exposed services and open ports.

![](../Images/Pasted%20image%2020260412094911.png)

---

# SMB Enumeration

Executed the Nmap SMB vulnerability detection scripts located in:

```text
/usr/share/nmap/scripts
```

The scan confirmed that the target was vulnerable to **MS17-010 (EternalBlue)**.

![](../Images/Pasted%20image%2020260412094957.png)

![](../Images/Pasted%20image%2020260412095025.png)

---

# Metasploit

Searched for the appropriate EternalBlue exploit module within Metasploit.

![](../Images/Pasted%20image%2020260412095123.png)

---

# Exploitation

Configured the exploit and selected the appropriate payload.

![](../Images/Pasted%20image%2020260412095223.png)

Successfully exploited the vulnerability and obtained an initial shell.

---

# Upgrade to Meterpreter

Backgrounded the current session using:

```text
CTRL + Z
```

Loaded the following Metasploit post-exploitation module to upgrade the shell:

```text
use post/multi/manage/shell_to_meterpreter
```

This module converts a standard shell into a fully interactive **Meterpreter** session.

![](../Images/Pasted%20image%2020260412095515.png)

---

# Meterpreter Session

After executing the module, two sessions became available.

Interacted with **Session 2**, which contained the upgraded Meterpreter session.

![](../Images/Pasted%20image%2020260412095605.png)

---

# Session Migration

Migrated the Meterpreter session into a stable process to improve reliability and reduce the risk of losing access.

![](../Images/Pasted%20image%2020260412095639.png)

---

# Dump Password Hashes

Extracted the Windows password hashes from the target system.

![](../Images/Pasted%20image%2020260412095701.png)

---

# Crack the Password Hashes

Cracked the recovered password hashes to obtain valid credentials.

![](../Images/Pasted%20image%2020260412095745.png)

---

# Flags

## Flag 1

Located in:

```text
C:\
```

---

## Flag 2

Located in:

```text
C:\Windows\System32\config
```

---

## Flag 3

Located in:

```text
C:\Users\<User>\Documents
```
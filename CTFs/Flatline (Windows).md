# RDP Exploitation and Remote Administration

## Overview

The objective of this lab was to identify a vulnerable network service, exploit it to obtain a reverse shell, and leverage administrative privileges to gain full access to the target system.

---

## Nmap Scan

Performed an Nmap scan to identify the exposed services.

The scan revealed an additional service running on **RDP (Remote Desktop Protocol)**.

![](Penetration%20Testing/Images/Pasted%20image%2020260411131324.png)

Executed Nmap NSE scripts to gather additional information about the exposed services.

![](Penetration%20Testing/Images/Pasted%20image%2020260411131437.png)

---

## Vulnerability Research

Researched the identified service to determine whether any public exploits were available.

Discovered a publicly available vulnerability that could be exploited either manually or through Metasploit.

I exploited **manually**.

![](Penetration%20Testing/Images/Pasted%20image%2020260411131545.png)

Reviewed the exploit documentation to understand how it should be used.

![](Penetration%20Testing/Images/Pasted%20image%2020260411131639.png)

---

## Exploitation

Modified the exploit by replacing the original command with a **Reverse Shell** payload.

![](Penetration%20Testing/Images/Pasted%20image%2020260411131701.png)

Executed the exploit and successfully obtained a reverse shell.

![](Penetration%20Testing/Images/Pasted%20image%2020260411131734.png)

---

## Post-Exploitation

The obtained shell had **Administrator** privileges.

Although administrative access was available, the target flag could not be accessed directly.

To obtain more reliable remote access, changed the Administrator password and prepared to authenticate remotely.

---

## Enabling SMB Access

SMB was not accessible even though it would normally be available on Windows systems.

This suggested that Windows Firewall was blocking SMB traffic.

Disabled the firewall using PowerShell:

```powershell
Set-NetFirewallProfile -Profile Domain,Public,Private -Enabled False
```

Added the Administrator account to the **Remote Desktop Users** group.

![](Penetration%20Testing/Images/Pasted%20image%2020260411132350.png)

---

## Enabling the Administrator Account

Attempted to authenticate through SMB but discovered that the Administrator account was disabled.

![](Penetration%20Testing/Images/Pasted%20image%2020260411132513.png)

Enabled the account.

![](Penetration%20Testing/Images/Pasted%20image%2020260411132607.png)

![](Penetration%20Testing/Images/Pasted%20image%2020260411132625.png)

---

## Remote Authentication

Authenticated successfully using **Impacket**.

![](Penetration%20Testing/Images/Pasted%20image%2020260411132839.png)

Obtained full SYSTEM-level access to the target.

![](Penetration%20Testing/Images/Pasted%20image%2020260411132907.png)

---

## Notes

### RDP

**Remote Desktop Protocol (RDP)** is Microsoft's remote administration protocol and typically operates on **TCP port 3389**.

### SMB

**Server Message Block (SMB)** is commonly used for remote administration and file sharing on Windows systems. Administrative accounts can authenticate remotely through SMB when the service is accessible.

### Impacket

**Impacket** is a collection of Python tools used for interacting with Windows network protocols. It provides utilities for remote authentication, command execution, credential extraction, and many other post-exploitation tasks.
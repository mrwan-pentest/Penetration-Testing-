# Lab Overview

**Objective:** Identify a vulnerable service, exploit it using **Metasploit**, obtain an initial Meterpreter session, escalate privileges to **SYSTEM**, and demonstrate **Pass-the-Hash (PtH)** using the extracted NTLM hash.

---

# Nmap Scan

We began by performing a standard Nmap scan to identify the open ports and running services.

![](Penetration%20Testing/Images/Pasted%20image%2020260707163153.png)

---

# Service Enumeration

Next, we ran Nmap version detection and scripts against **port 8000** to gather additional information about the service.

![](Penetration%20Testing/Images/Pasted%20image%2020260410071811.png)

The results indicated that the service was vulnerable and that a Metasploit exploit module was available.

![](Penetration%20Testing/Images/Pasted%20image%2020260410071903.png)

---

# Searching for the Exploit

Inside Metasploit, we searched for the corresponding exploit module.

![](Penetration%20Testing/Images/Pasted%20image%2020260410072005.png)

---

# Exploiting the Target

After selecting the appropriate module, we configured it and launched the exploit.

![](Penetration%20Testing/Images/Pasted%20image%2020260410072034.png)

The exploitation was successful, and we obtained a **Meterpreter session**.

![](Penetration%20Testing/Images/Pasted%20image%2020260410072105.png)

---

# Initial Privilege Escalation Attempt

Our first attempt to elevate privileges was unsuccessful.

![](Penetration%20Testing/Images/Pasted%20image%2020260410072135.png)

---

# Finding Privilege Escalation Vulnerabilities

To identify possible local privilege escalation vulnerabilities, we used the following post-exploitation module:

```text
post/multi/recon/local_exploit_suggester
```

![](Penetration%20Testing/Images/Pasted%20image%2020260410072202.png)

The module suggested several potential local exploits.

---

# Trying a Suggested Exploit

We backgrounded the current Meterpreter session and attempted one of the suggested privilege escalation modules.

![](Penetration%20Testing/Images/Pasted%20image%2020260410072341.png)

![](Penetration%20Testing/Images/Pasted%20image%2020260410072409.png)

Unfortunately, this exploit failed to provide a privileged session.

---

# Successful Privilege Escalation

We then tried another Metasploit local exploit:

```text
exploit/windows/local/bypass_eventvwr
```

![](Penetration%20Testing/Images/Pasted%20image%2020260410072456.png)

This exploit successfully elevated our privileges, giving us a **SYSTEM** Meterpreter session.

![](Penetration%20Testing/Images/Pasted%20image%2020260410072532.png)

---

# Viewing Running Processes

To inspect the processes running on the target system, we used:

```text
ps
```

![](Penetration%20Testing/Images/Pasted%20image%2020260410072607.png)

---

# Process Migration

To improve session stability and reduce the likelihood of losing the Meterpreter session, we migrated into the **lsass.exe** process.

```text
migrate -N lsass.exe
```

![](Penetration%20Testing/Images/Pasted%20image%2020260410072620.png)

---

# Dumping NTLM Hashes

After obtaining SYSTEM privileges, we dumped the Windows password hashes using:

```text
hashdump
```

From the output, we copied only the **second value**, which is the **NTLM hash**.

![](Penetration%20Testing/Images/Pasted%20image%2020260410075734.png)

---

# Verifying the Hash

Using **NetExec (nxc)**, we verified whether the extracted NTLM hash could be used for authentication.

![](Penetration%20Testing/Images/Pasted%20image%2020260410075816.png)

The successful authentication confirmed that the target was vulnerable to a **Pass-the-Hash (PtH)** attack.

---

# Cracking the NTLM Hash

Although Pass-the-Hash does not require recovering the plaintext password, we also demonstrated how to crack the NTLM hash using **Hashcat**.

![](Penetration%20Testing/Images/Pasted%20image%2020260410080704.png)

![](Penetration%20Testing/Images/Pasted%20image%2020260410080718.png)

---

# Dumping Hashes with NetExec

As an alternative to Meterpreter's `hashdump`, NetExec can dump the local SAM database directly using:

```text
--sam
```

![](Penetration%20Testing/Images/Pasted%20image%2020260410080942.png)

---

# Pass-the-Hash Attack

Finally, we used **Impacket** to authenticate directly with the NTLM hash.

Instead of using the user's password, Impacket authenticated using the **NTLM hash**, allowing us to obtain a fully interactive shell on the target system.

![](Penetration%20Testing/Images/Pasted%20image%2020260410082231.png)
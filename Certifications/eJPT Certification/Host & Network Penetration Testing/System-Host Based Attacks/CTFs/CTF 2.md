# CTF Walkthrough

## Scenario

This challenge required exploiting multiple Linux services to obtain flags from two target machines.

The techniques used included:

- Network Enumeration
- Directory Enumeration
- Shellshock Exploitation
- SSH Authentication Bypass
- Linux Privilege Escalation via SUID

---

# Target 1

# Enumeration

## Network Enumeration

We began by performing an Nmap scan against the target to identify open ports, running services, and potential attack vectors.

![[Pasted image 20260521133644.png]]

---

## Directory Enumeration

Next, we performed directory enumeration to discover hidden resources exposed by the web server.

![[Pasted image 20260521133703.png]]

During enumeration, we noticed that one of the discovered resources redirected requests to a **CGI** script.

![[Pasted image 20260521133804.png]]

Since CGI scripts are a common attack surface for **Shellshock (CVE-2014-6271)**, this became the primary attack vector.

---

# Exploitation

## Verifying the Shellshock Vulnerability

We used an Nmap NSE script to verify whether the CGI endpoint was vulnerable to Shellshock.

The scan confirmed that the target was vulnerable.

![[Pasted image 20260521133912.png]]

---

## Obtaining Remote Code Execution

After confirming the vulnerability, we searched for a suitable exploitation method capable of establishing a Reverse Shell.

![[Pasted image 20260521133939.png]]

![[Pasted image 20260521133958.png]]

The exploit successfully executed, providing remote shell access to the target.

---

# Flag 1

After obtaining shell access, we explored the root directory (`/`) and located the first flag.

![[Pasted image 20260521134034.png]]

---

# Flag 2

The next objective instructed us to inspect the Apache web root located at:

```
/opt/apache/htdocs/
```

After carefully exploring the directory, we located the second flag.

![[Pasted image 20260521134121.png]]

---

# Target 2

# Enumeration

## Network Enumeration

We performed an Nmap scan against the second target.

The scan revealed an SSH service.

![[Pasted image 20260521134316.png]]

---

## Identifying the SSH Vulnerability

The SSH version appeared to be vulnerable.

We searched for publicly available exploits using **Searchsploit**.

![[Pasted image 20260521134459.png]]

A search revealed a known authentication bypass vulnerability:

```
libssh_auth_bypass
```

---

## Reviewing the Exploit

We reviewed the available exploit to understand its usage.

![[Pasted image 20260521134532.png]]

---

# Exploitation

## Establishing a Reverse Shell

We modified the exploit to execute a Reverse Shell payload.

![[Pasted image 20260521134600.png]]

The exploit successfully provided remote shell access.

![[Pasted image 20260521134621.png]]

---

# Flag 3

After gaining shell access, we explored the user's home directory and located the third flag.

![[Pasted image 20260521134650.png]]

---

# Privilege Escalation

## Enumerating SUID Binaries

To obtain root privileges, we searched for SUID binaries.

Two custom binaries were identified.

One of them had the **SUID** permission enabled.

Further analysis showed that this binary executed the second binary internally.

![[Pasted image 20260521134827.png]]

---

## Exploiting the SUID Binary

Since the executed binary could be modified, we removed it and replaced it with a symbolic link to:

```
/bin/bash
```

After executing the vulnerable SUID binary, it launched a root shell.

![[Pasted image 20260521134917.png]]

---

# Flag 4

With root privileges obtained, we navigated to the `/root` directory and successfully retrieved the final flag.

![[Pasted image 20260521135026.png]]

---

# Summary

This challenge demonstrated several common penetration testing techniques across two Linux targets.

The attack chain included:

1. Performing network enumeration with Nmap.
2. Discovering CGI resources through directory enumeration.
3. Identifying and exploiting the Shellshock vulnerability.
4. Obtaining a Reverse Shell and retrieving the first two flags.
5. Identifying a vulnerable SSH service on the second target.
6. Exploiting the **libssh Authentication Bypass** vulnerability to gain remote access.
7. Enumerating SUID binaries.
8. Exploiting an insecure SUID binary by replacing its executed binary with `/bin/bash`.
9. Escalating privileges to root and retrieving the final flag.

This walkthrough illustrates how multiple vulnerabilities—including outdated services, remote code execution flaws, and insecure SUID configurations—can be chained together to achieve complete system compromise.
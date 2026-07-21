# FTP to SSH Privilege Escalation Walkthrough

## Scenario

The objective of this lab is to exploit an exposed FTP service to gather sensitive information, use the discovered credentials to gain SSH access, and finally escalate privileges through a misconfigured sudo permission assigned to Vim.

---

# Enumeration

## Nmap Scan

We began by performing an Nmap scan to identify the open ports and running services on the target machine.

![](../Images/Pasted%20image%2020260330090032.png)

---

## Nmap Script Scanning

After identifying the available services, we used Nmap NSE scripts to collect additional information that could assist during the enumeration phase.

![](../Images/Pasted%20image%2020260330090146.png)

![](../Images/Pasted%20image%2020260330090200.png)

---

# FTP Enumeration

## Anonymous FTP Access

The scan revealed that the FTP server allowed anonymous authentication. This misconfiguration allowed us to access the FTP service without providing valid credentials.

![](../Images/Pasted%20image%2020260330090335.png)

---

## Downloading Files from the FTP Server

After accessing the FTP server, we discovered several useful files.

We downloaded all available files using the following command:

```
mget * ..>> To download all files
mget file name
```

The `mget` command downloads multiple files from the FTP server in a single operation, making it useful for collecting all accessible files during enumeration.

![](../Images/Pasted%20image%2020260330090427.png)

---

# Gaining Initial Access

## Password Brute Force with Hydra

The downloaded FTP files contained a valid username.

We used Hydra to perform a brute-force attack against the SSH service using the discovered username.

![](../Images/Pasted%20image%2020260330090755.png)

---

## Connecting to a Non-Standard SSH Port

During enumeration, we discovered that the SSH service was running on port **2222** instead of the default SSH port (**22**).

After recovering valid credentials, we authenticated to the SSH service using the custom port.

![](../Images/Pasted%20image%2020260330090855.png)

---

# Initial Access

Successfully authenticated to the target and obtained a low-privileged shell.

---

# Privilege Escalation

## Enumerating Sudo Permissions

The first step after obtaining a shell was to identify which commands could be executed with elevated privileges.

We used:

```
sudo -l
```

This command lists all commands that the current user is allowed to execute with `sudo`.

---

## Privilege Escalation via Vim

The output revealed that **Vim** could be executed with root privileges.

![](../Images/Pasted%20image%2020260716203120.png)

### Why is Vim Dangerous?

Vim is not just a text editor. It also supports executing shell commands from within the editor. If it can be executed through `sudo`, it may allow an attacker to spawn a root shell, making it a common Privilege Escalation vector.

---

## Using GTFOBins

To determine the appropriate exploitation method, we searched for **Vim** on **GTFOBins**, a well-known resource that documents legitimate Unix binaries that can be abused for Privilege Escalation.

![](../Images/Pasted%20image%2020260716203602.png)

We executed the recommended GTFOBins command and successfully obtained a root shell.

![](../Images/Pasted%20image%2020260716203616.png)

---

# Summary

This machine was compromised by chaining together several common penetration testing techniques:

1. Performed service enumeration using Nmap.
2. Identified anonymous FTP access.
3. Downloaded sensitive files from the FTP server.
4. Extracted a valid username from the downloaded files.
5. Performed an SSH brute-force attack using Hydra.
6. Logged into the target through SSH on the non-standard port (**2222**).
7. Enumerated sudo permissions using `sudo -l`.
8. Discovered that Vim could be executed with root privileges.
9. Used the GTFOBins technique to abuse Vim and spawn a root shell.
10. Successfully obtained full administrative access to the target system.
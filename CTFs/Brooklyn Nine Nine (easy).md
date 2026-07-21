# FTP Enumeration, SSH Access, and Privilege Escalation

## Overview

The objective of this lab was to enumerate the FTP service, extract useful information, recover valid user credentials through brute force, authenticate via SSH, and escalate privileges to obtain root access.

---

## Nmap Scan

Performed an Nmap scan to identify the exposed services running on the target.

![](Penetration%20Testing/Images/Pasted%20image%2020260401113044.png)

---

## FTP Enumeration

Connected to the FTP server using **anonymous login** and enumerated the available files.

![](Penetration%20Testing/Images/Pasted%20image%2020260401113133.png)

During the enumeration, discovered a valid username.

![](Penetration%20Testing/Images/Pasted%20image%2020260701225623.png)

---

## Brute Force Attack

Performed a brute-force attack against the discovered user account and successfully recovered its password.

![](Penetration%20Testing/Images/Pasted%20image%2020260401113200.png)

---

## SSH Authentication

Authenticated to the target through SSH using the recovered credentials.

![](Penetration%20Testing/Images/Pasted%20image%2020260701225659.png)

---

## Privilege Escalation

Executed `sudo -l` to identify commands that could be run with elevated privileges.

Discovered a binary that could be abused for privilege escalation.

![](Penetration%20Testing/Images/Pasted%20image%2020260701225736.png)

Searched **GTFOBins** for the binary and obtained the appropriate exploitation technique.

![](Penetration%20Testing/Images/Pasted%20image%2020260701225811.png)

Executed the provided commands and successfully obtained root privileges.

![](Penetration%20Testing/Images/Pasted%20image%2020260701225902.png)

---

## Notes

### Anonymous FTP

Anonymous FTP allows users to access an FTP server without authentication. Misconfigured anonymous access may expose sensitive files that assist during further enumeration.

### SSH

SSH (Secure Shell) provides encrypted remote access to a system and is commonly targeted after valid credentials have been obtained.

### `sudo -l`

The `sudo -l` command displays the programs a user is permitted to execute with `sudo`. Misconfigured sudo permissions are a common privilege escalation vector.

### GTFOBins

GTFOBins is a curated collection of Unix binaries that can be abused to bypass security restrictions, escalate privileges, or obtain interactive shells when executed with elevated permissions.
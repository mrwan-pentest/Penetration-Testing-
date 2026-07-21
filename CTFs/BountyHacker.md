
## The objective is to gather useful information from the FTP service, use the recovered credentials to gain SSH access, and then escalate privileges to obtain root access.

---
# Nmap Enumeration

## Performed an Nmap scan to identify the open ports and running services on the target.

![](../Images/Pasted%20image%2020260331094255.png)



# Service Enumeration

## Used Nmap NSE scripts and version detection to gather additional information about the discovered services.

![](../Images/Pasted%20image%2020260331094323.png)


# Anonymous FTP Access

## Discovered that the FTP service allowed anonymous authentication.

![](../Images/Pasted%20image%2020260331094343.png)

# FTP Enumeration

## Logged into the FTP server and collected useful information.

![](../Images/Pasted%20image%2020260626164427.png)


# Credential Discovery

## Recovered usernames and passwords from files stored on the FTP server.
![](../Images/Pasted%20image%2020260331094417.png)

# Source Code Review

## Examined the application's source code and discovered additional usernames.

![](../Images/Pasted%20image%2020260331094554.png)

# SSH Brute Force

## Used Hydra to perform a brute-force attack against the SSH service using the discovered usernames and passwords.

![](../Images/Pasted%20image%2020260331094659.png)

# SSH Authentication

## Successfully authenticated to the SSH service using the recovered credentials.

![](../Images/Pasted%20image%2020260626163642.png)



# Privilege Escalation Enumeration

## Enumerated sudo permissions using the following command:

sudo -l

![](../Images/Pasted%20image%2020260626163739.png)


# Sudo Misconfiguration

## Identified a binary that could be abused for privilege escalation.

![](../Images/Pasted%20image%2020260626164729.png)


# GTFOBins

## Used GTFOBins to find a privilege escalation technique for the allowed binary.


![](../Images/Pasted%20image%2020260626163842.png)


# Root Access

## Executed the GTFOBins Command and successfully obtained root privileges.

![](../Images/Pasted%20image%2020260626163927.png)
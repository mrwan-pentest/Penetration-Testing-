
## The objective is to gather useful information from the FTP service, use the recovered credentials to gain SSH access, and then escalate privileges to obtain root access.

---
# Nmap Enumeration

## Performed an Nmap scan to identify the open ports and running services on the target.

![[Pasted image 20260331094255.png]]



# Service Enumeration

## Used Nmap NSE scripts and version detection to gather additional information about the discovered services.

![[Pasted image 20260331094323.png]]


# Anonymous FTP Access

## Discovered that the FTP service allowed anonymous authentication.

![[Pasted image 20260331094343.png]]

# FTP Enumeration

## Logged into the FTP server and collected useful information.

![[Pasted image 20260626164427.png]]


# Credential Discovery

## Recovered usernames and passwords from files stored on the FTP server.
![[Pasted image 20260331094417.png]]

# Source Code Review

## Examined the application's source code and discovered additional usernames.

![[Pasted image 20260331094554.png]]

# SSH Brute Force

## Used Hydra to perform a brute-force attack against the SSH service using the discovered usernames and passwords.

![[Pasted image 20260331094659.png]]

# SSH Authentication

## Successfully authenticated to the SSH service using the recovered credentials.

![[Pasted image 20260626163642.png]]



# Privilege Escalation Enumeration

## Enumerated sudo permissions using the following command:

sudo -l

![[Pasted image 20260626163739.png]]


# Sudo Misconfiguration

## Identified a binary that could be abused for privilege escalation.

![[Pasted image 20260626164729.png]]


# GTFOBins

## Used GTFOBins to find a privilege escalation technique for the allowed binary.


![[Pasted image 20260626163842.png]]


# Root Access

## Executed the GTFOBins Command and successfully obtained root privileges.

![[Pasted image 20260626163927.png]]
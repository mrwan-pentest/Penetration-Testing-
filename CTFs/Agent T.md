# Exploiting a Known Vulnerability

## The objective is to identify a known vulnerability in the target service and exploit it to gain remote access.
---

# Nmap Enumeration

## Performed an Nmap scan to identify the services running on the target host.

![[Pasted image 20260403162704.png]]

# Vulnerability Research

## Searched for a matching public exploit using SearchSploit.

![[Pasted image 20260403162801.png]]


# Exploitation

## Used the available exploit to compromise the target and gain initial access.

![[Pasted image 20260403162838.png]]


# Initial Shell

## Obtained a non-interactive shell after successful exploitation.

![[Pasted image 20260403162920.png]]

# Upgrading the Shell

## Started a listener to upgrade the connection 

![[Pasted image 20260628000919.png]]

# Full Shell Access

## Executed the command and successfully established a fully interactive shell on the target.


![[Pasted image 20260626161753.png]]


## obtain a fully interactive shell.

![[Pasted image 20260628001711.png]]

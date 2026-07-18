# Network Discovery with Metasploit

## Overview

This lab demonstrates how to use Metasploit auxiliary modules to discover hosts and services within an internal network.

The process includes adding a target network range, performing a TCP port scan, and identifying services listening on UDP ports.

---

## Objective

The objective of this lab was to configure the target network, perform port scanning, and enumerate both TCP and UDP services.

---

## Configure the Target Network

Configured the internal network range that would be scanned by the Metasploit module.

![[Pasted image 20260524014057.png]]

---

## TCP Port Scan

Executed a TCP port scan against the configured network to identify active hosts and open ports.

![[Pasted image 20260524014127.png]]

---

## UDP Port Scan

Performed a UDP scan to identify services running over the UDP protocol.

![[Pasted image 20260524014231.png]]

---

## Notes

### TCP Port Scanning

TCP scans are commonly used to identify:

- Live hosts
    
- Open TCP ports
    
- Running network services
    

### UDP Port Scanning

Unlike TCP, UDP is a connectionless protocol, making UDP scanning slower and less reliable.

However, many important services operate over UDP, including:

- DNS (53)
    
- DHCP (67/68)
    
- SNMP (161)
    
- NTP (123)
    
- TFTP (69)
    

Enumerating UDP services is an important step during network reconnaissance, as they may expose additional attack surfaces not visible through TCP scanning alone.
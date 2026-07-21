# SNMP (Simple Network Management Protocol)

## Overview

**SNMP (Simple Network Management Protocol)** is a network management protocol used to monitor, configure, and collect information from network devices.

It allows administrators to remotely monitor the health and status of devices connected to a network.

---

# Common Devices That Use SNMP

SNMP is widely implemented on:

- Routers
- Switches
- Printers
- Servers
- Firewalls
- Network Appliances
- IoT Devices

---

# Why Is SNMP Used?

Network administrators use SNMP to:

- Monitor device health
- Collect system information
- Monitor bandwidth usage
- Detect hardware failures
- Receive automatic alerts
- Troubleshoot network issues

---

# Security Issue

Many organizations leave SNMP with its default configuration.

Common mistakes include:

- Default Community Strings
- Weak Community Strings
- Publicly accessible SNMP service
- Running outdated SNMP versions (v1/v2c)

Typical default values include:

```text
public
private
```

These values are well-known and are frequently targeted during penetration tests.

---

# What Is a Community String?

A **Community String** is similar to a password used by SNMP for authentication.

Depending on the configured permissions, it may allow reading information from the device or even modifying its configuration.

---

# Common Community Strings

| Community String | Permission |
|------------------|------------|
| public | Read Only |
| private | Read & Write |

---

# SNMP Ports

| Port | Purpose |
|-------|---------|
| UDP 161 | SNMP Queries |
| UDP 162 | SNMP Traps |

---

# What Is an SNMP Trap?

An SNMP Trap is an unsolicited notification sent automatically by the device to the monitoring server.

Examples include:

- High CPU usage
- Interface failure
- Device reboot
- Low disk space
- Hardware failure

Unlike normal SNMP requests, traps are initiated by the device itself.

---

# SNMP Components

## 1. SNMP Manager

The management system that sends requests to network devices.

Examples:

- Kali Linux
- Monitoring Server
- SolarWinds
- PRTG

---

## 2. SNMP Agent

A service running on the target device that responds to SNMP requests.

The agent collects information from the operating system and hardware and returns it to the manager.

---

## 3. MIB (Management Information Base)

The **Management Information Base (MIB)** is a database that stores information about the device.

Examples of stored information:

- Hostname
- System description
- Network interfaces
- Running processes
- Users
- Installed software
- Network statistics

---

# What Is an OID?

Each piece of information inside the MIB is identified by a unique **Object Identifier (OID)**.

Example:

```text
1.3.6.1.2.1.1.5
```

This OID commonly represents the device hostname.

---

# SNMP Enumeration with snmpwalk

The most common enumeration tool is:

```bash
snmpwalk
```

`snmpwalk` queries an SNMP-enabled device and recursively retrieves information from the MIB.

Instead of requesting a single value, it walks through the entire tree and collects all available data.

This is why the tool is called **snmpwalk**.

---

# Basic Usage

```bash
snmpwalk -v1 -c public 192.168.1.10
```

### Parameters

| Option | Description |
|---------|-------------|
| snmpwalk | SNMP enumeration tool |
| -v1 | SNMP Version 1 |
| -c public | Community String |
| 192.168.1.10 | Target IP |

---

# Query a Specific OID

```bash
snmpwalk -v1 -c public 192.168.1.10 1.3.6.1.2.1.1.5
```

Retrieves the hostname of the target.

---

# Retrieve System Information

```bash
snmpwalk -v1 -c public 192.168.1.10 1.3.6.1.2.1.1.1
```

Returns system information such as:

- Operating System
- Kernel Version
- Device Description

---

# Enumerate Users (Windows)

Some Windows systems expose user information through SNMP.

```bash
snmpwalk -v1 -c public 192.168.1.10 1.3.6.1.4.1.77.1.2.25
```

Depending on the configuration, this may reveal usernames.

---

# SNMP Enumeration with Nmap

Nmap provides several NSE scripts that can automate SNMP enumeration.

Example:

```bash
nmap -sU -p161 --script snmp-* TARGET_IP
```

These scripts can retrieve:

- Hostname
- System Description
- Running Services
- Installed Software
- User Accounts
- Network Interfaces
- Routing Information
- Community Strings (in some cases)

---

# Lab

## Step 1 – Identify the SNMP Service

Performed an Nmap scan against UDP port **161** to verify that the SNMP service was running on the target.

![](../../../../../Images/Pasted%20image%2020260522010753.png)

Performed another scan specifically targeting UDP port **161** for additional verification.

![](../../../../../Images/Pasted%20image%2020260522010817.png)

---

## Step 2 – Discover Community Strings

Used an SNMP brute-force tool to identify valid Community Strings that could be used to query the target.

![](../../../../../Images/Pasted%20image%2020260522010942.png)

Once valid credentials were identified, they were used during the enumeration phase.

---

## Step 3 – Enumerate the Target with snmpwalk

Used **snmpwalk** together with the discovered Community String to retrieve information from the target.

Although data was returned successfully, much of the output was difficult to interpret directly.

![](../../../../../Images/Pasted%20image%2020260522011039.png)

---

## Step 4 – Perform Comprehensive Enumeration with Nmap

Executed the Nmap SNMP NSE scripts to perform a more complete enumeration of the target.

The results were saved to a file for easier analysis.

![](../../../../../Images/Pasted%20image%2020260522011212.png)

---

## Step 5 – Enumerate User Accounts

The enumeration results revealed several usernames configured on the target system.

These usernames were extracted and saved into a wordlist for use in password guessing attacks.

![](../../../../../Images/Pasted%20image%2020260522011237.png)

![](../../../../../Images/Pasted%20image%2020260522011249.png)

![](../../../../../Images/Pasted%20image%2020260522011257.png)

---

## Step 6 – Initial Access

After identifying valid credentials, authentication was performed successfully using Metasploit.

A Meterpreter session was established on the target system.

![](../../../../../Images/Pasted%20image%2020260522011337.png)

![](../../../../../Images/Pasted%20image%2020260522011346.png)

---

# Summary

- SNMP is a protocol used to monitor and manage network devices.
- Devices authenticate using **Community Strings**.
- Weak or default Community Strings such as **public** and **private** are common security risks.
- **snmpwalk** is one of the most widely used tools for SNMP enumeration.
- Nmap NSE scripts can automate extensive SNMP reconnaissance.
- Information gathered through SNMP may include usernames, system details, network interfaces, installed software, and other valuable reconnaissance data.
- The discovered information can often be leveraged to obtain valid credentials or facilitate further attacks during a penetration test.
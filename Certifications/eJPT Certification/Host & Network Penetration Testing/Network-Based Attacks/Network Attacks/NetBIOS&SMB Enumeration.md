# SMB (Server Message Block) & NetBIOS

Windows networks rely on several protocols to share resources such as files, printers, folders, and user information. Two of the most important protocols are **SMB** and **NetBIOS**.

Although they are closely related, they serve different purposes within a Windows network.

---

# What is SMB?

**SMB (Server Message Block)** is a network protocol primarily used for sharing files, printers, and other resources between systems.

It enables users to remotely access shared folders and files across the network.

For example, when accessing a network share such as:

```text
\\192.168.1.10\share
```

the communication is typically performed using the SMB protocol.

---

# SMB Capabilities

SMB allows clients to:

- Read shared files.
- Write or upload files.
- Access shared folders.
- Use shared printers.
- Communicate through IPC (Inter-Process Communication).
- Authenticate users to network resources.

---

# Important SMB Ports

| Port | Purpose |
|------|---------|
| 445 | SMB over TCP (Modern Windows) |
| 139 | SMB over NetBIOS (Legacy Systems) |

---

# What is NetBIOS?

**NetBIOS (Network Basic Input/Output System)** is an older networking technology used by Windows systems.

Unlike SMB, NetBIOS is **not responsible for file sharing**.

Instead, it provides services that allow devices to locate and communicate with one another on a local network.

Its primary responsibilities include:

- Hostname resolution.
- Network discovery.
- Session establishment.
- Broadcasting system information.

For example, instead of connecting to:

```text
192.168.1.20
```

you can connect using the computer name:

```text
WORKSTATION-PC
```

This name resolution is one of NetBIOS's functions.

---

# NetBIOS Services

| Service | Port |
|----------|------|
| Name Service | 137 |
| Datagram Service | 138 |
| Session Service | 139 |

---

# Relationship Between SMB and NetBIOS

Historically, SMB operated **on top of NetBIOS**.

```
NetBIOS
      │
      ▼
SMB Protocol
      │
      ▼
Shared Files & Resources
```

In this architecture:

- NetBIOS handled device discovery and session management.
- SMB handled file and printer sharing.

Modern versions of Windows typically use SMB directly over **TCP port 445**, making NetBIOS optional.

However, NetBIOS is still supported for compatibility with legacy environments.

---

# Common SMB Enumeration Tools

| Tool | Purpose |
|------|---------|
| `smbclient` | Browse and interact with SMB shares |
| `smbmap` | Enumerate SMB shares and permissions |
| `enum4linux` | Comprehensive SMB and Windows enumeration |
| `Nmap SMB NSE Scripts` | SMB service and vulnerability enumeration |
| `NetExec (CrackMapExec)` | Authentication, enumeration, and post-exploitation |

---

# Lab Walkthrough

## Nmap Port Scan

The engagement began by performing an Nmap scan to identify the services exposed by the target.

![](Penetration%20Testing/Images/Pasted%20image%2020260522003114.png)

![](Penetration%20Testing/Images/Pasted%20image%2020260522003133.png)

---

## SMB Version Enumeration

Nmap NSE scripts were executed to identify the SMB version and gather additional information about the service.

![](Penetration%20Testing/Images/Pasted%20image%2020260522003217.png)

---

## SMB Security Configuration

The following SMB security enumeration script was executed.

![](Penetration%20Testing/Images/Pasted%20image%2020260522003408.png)

This script checks several SMB security settings, including:

- SMB Signing
- Authentication mechanisms
- Guest or Null Session access

The results indicated:

```text
message_signing: disabled
```

This means SMB Signing is disabled.

When SMB Signing is not enforced, the host may be vulnerable to attacks such as:

- SMB Relay
- NTLM Relay

---

## Anonymous SMB Enumeration

Anonymous access was tested to determine whether any SMB shares were accessible without authentication.

![](Penetration%20Testing/Images/Pasted%20image%2020260522003549.png)

---

## Enumerating SMB Users

Nmap SMB scripts were then used to enumerate valid user accounts from the SMB service.

![](Penetration%20Testing/Images/Pasted%20image%2020260522003643.png)

The discovered usernames were saved into a wordlist for password brute-forcing.

![](Penetration%20Testing/Images/Pasted%20image%2020260522003727.png)

The brute-force attack successfully recovered valid credentials.

![](Penetration%20Testing/Images/Pasted%20image%2020260522003746.png)

---

## Meterpreter Login

The recovered credentials were used to authenticate to the target through Metasploit.

![](Penetration%20Testing/Images/Pasted%20image%2020260522003818.png)

---

# Discovering an Internal Network

After gaining access, a ping test was performed against another internal host.

![](Penetration%20Testing/Images/Pasted%20image%2020260522003942.png)

The successful response confirmed the existence of an internal network that was not directly reachable from the attacker's machine.

---

# Configuring Autoroute

The internal subnet was added to Metasploit's routing table.

The subnet mask identified from the target indicated that a **/20** network should be routed.

![](Penetration%20Testing/Images/Pasted%20image%2020260522004017.png)

Once the route was added, only Metasploit modules could communicate with the internal network.

To access it using external tools such as Nmap, a SOCKS proxy was required.

---

# Configuring SOCKS Proxy

The proxy configuration file was reviewed to determine the listening port.

![](Penetration%20Testing/Images/Pasted%20image%2020260522004203.png)

Metasploit's SOCKS proxy module was then loaded.

```text
use auxiliary/server/socks_proxy
```

![](Penetration%20Testing/Images/Pasted%20image%2020260522004258.png)

The listening port was configured to match the ProxyChains configuration.

![](Penetration%20Testing/Images/Pasted%20image%2020260522004348.png)

---

# Scanning Through ProxyChains

Nmap was executed through the SOCKS proxy.

When scanning through ProxyChains, the following options are recommended:

```bash
-sT -Pn
```

![](Penetration%20Testing/Images/Pasted%20image%2020260522004458.png)

The scan identified another host exposing an SMB service.

---

# Enumerating SMB Shares

The Meterpreter session was used to interact with the newly discovered internal machine.

Available SMB shares were enumerated using:

```cmd
net view
```

![](Penetration%20Testing/Images/Pasted%20image%2020260522004536.png)

Initially, no shares were returned.

![](Penetration%20Testing/Images/Pasted%20image%2020260522004622.png)

---

# Process Migration

The Meterpreter session was migrated into a different process to obtain a more stable security context.

![](Penetration%20Testing/Images/Pasted%20image%2020260522004708.png)

After migration, the SMB shares became accessible.

![](Penetration%20Testing/Images/Pasted%20image%2020260522004737.png)

> **Why did this work?**
>
> A Meterpreter session inherits the security token of the process it is running inside. Migrating into another process can provide a different security context, allowing access to additional network resources that were previously unavailable.

---

# Mapping a Network Share

The discovered SMB share was mapped as a local drive using:

```cmd
net use
```

![](Penetration%20Testing/Images/Pasted%20image%2020260522004928.png)

Mapping the share allows it to be accessed like a local disk, making file browsing much easier.

---

# Enumerating Shared Files

After browsing the mapped drive, several files containing credentials were discovered.

![](Penetration%20Testing/Images/Pasted%20image%2020260522005017.png)

To read their contents more easily, the investigation returned to the Meterpreter session.

![](Penetration%20Testing/Images/Pasted%20image%2020260522005053.png)

---

# Summary

During this lab, the following techniques were demonstrated:

- Enumerating SMB services with Nmap.
- Identifying insecure SMB configurations.
- Discovering anonymous SMB shares.
- Enumerating valid Windows users.
- Performing SMB password brute-forcing.
- Authenticating with the recovered credentials.
- Discovering an internal network.
- Configuring Metasploit Autoroute.
- Creating a SOCKS proxy for pivoting.
- Scanning internal hosts through ProxyChains.
- Enumerating SMB shares.
- Using Meterpreter process migration to obtain additional access.
- Mapping remote SMB shares using `net use`.
- Extracting sensitive files and credentials from internal network shares.
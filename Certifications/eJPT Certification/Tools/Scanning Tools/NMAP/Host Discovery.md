# Nmap Host Discovery Techniques

Before performing port scanning, a penetration tester usually needs to determine which hosts are alive on the network.

Nmap provides several Host Discovery techniques to identify active devices without performing a full port scan.

These techniques help answer:

- Which systems are online?
- Which IP addresses are in use?
- Which hosts should be scanned further?

---

# `-sn` — Host Discovery Only

## Purpose

The option:

```
-sn
```

means:

```
Host Discovery Only
```

It performs:

```
Host Discovery
```

without performing:

- Port Scan
- Service Detection
- Version Detection

---

## Example

```
nmap -sn 192.168.1.0/24
```

---

## What Does It Do?

Nmap checks which devices are alive within the specified network range.

Example output:

```
Host is up
192.168.1.5
192.168.1.20
192.168.1.50
```

---

# `-PS` — TCP SYN Ping

## Purpose

The option:

```
-PS
```

means:

```
TCP SYN Ping
```

---

## How It Works

Instead of using ICMP Ping, Nmap sends:

```
SYN Packet
```

which is similar to the first step of the TCP three-way handshake.

Normal TCP connection:

```
Client → SYN
Server → SYN/ACK
Client → ACK
```

---

## Why Use It?

Some hosts or Firewalls:

- Block ICMP traffic
- Allow TCP traffic

Therefore, TCP SYN Ping can discover hosts that do not respond to normal Ping requests.

---

## Example

```
nmap -PS 192.168.1.0/24
```

---

## Specifying Ports

You can specify target ports:

```
nmap -PS80,443 192.168.1.0/24
```

This sends SYN packets to:

- Port 80
- Port 443

---

## Common Usage

Useful when:

```
TCP traffic is allowed but ICMP is filtered.
```

---

# `--send-ip` — Force Raw IP Packets

## Purpose

This option forces Nmap to use:

```
Raw IP Packets
```

instead of:

```
Ethernet Frames
```

---

## Normal Behavior

Inside a local network (LAN), Nmap usually uses:

```
ARP / Ethernet
```

for host discovery.

---

## With `--send-ip`

Nmap uses:

```
IP Layer
```

directly.

---

## Example

```
nmap --send-ip -sn 192.168.1.0/24
```

---

## Why Use It?

Useful when testing networks where you want to avoid normal Ethernet-based discovery methods.

---

# `-PA` — TCP ACK Ping

## Purpose

The option:

```
-PA
```

means:

```
TCP ACK Ping
```

---

## How It Works

Unlike:

```
-PS
```

which sends:

```
SYN Packet
```

ACK Ping sends:

```
ACK Packet
```

---

## What is ACK?

ACK stands for:

```
Acknowledgment
```

It means:

```
Confirmation of received data
```

---

## Why Send ACK Without an Existing Connection?

This is the interesting part.

When a host receives an unexpected ACK packet, it usually responds with:

```
RST
```

This response tells Nmap:

```
The host exists and is reachable.
```

---

## Example

```
nmap -PA 192.168.1.0/24
```

---

## Specifying Ports

```
nmap -PA80,443 192.168.1.0/24
```

---

## Why Use ACK Ping?

Because some Firewalls may:

- Block ICMP
- Block SYN packets
- Allow ACK traffic

---

# `-PE` — ICMP Echo Ping

## Purpose

The option:

```
-PE
```

means:

```
ICMP Echo Ping
```

---

## How It Works

Nmap sends:

```
ICMP Echo Request
```

which is the same mechanism used by the normal:

```
ping
```

command.

---

## Response

If the host responds with:

```
ICMP Echo Reply
```

Nmap determines:

```
Host is Up
```

---

## Example

```
nmap -PE 192.168.1.0/24
```

---

## Why Use It?

Used for discovering:

```
Live Hosts
```

---

## Limitation

Many:

- Firewalls
- Servers
- Network devices

block ICMP traffic, which can prevent detection.

---

# `-Pn` — Disable Host Discovery

## Purpose

The option:

```
-Pn
```

tells Nmap:

```
Do not perform Ping Discovery
```

---

## How It Works

Nmap assumes the target is:

```
Alive
```

even if it does not respond to Ping.

---

## Example

```
nmap -Pn 192.168.1.10
```

---

## When To Use It?

Useful when:

- Firewalls block Ping
- The host does not respond to ICMP
- You already know the target exists

---

# Summary

|Option|Purpose|
|---|---|
|`-sn`|Host Discovery only without Port Scan|
|`-PS`|TCP SYN Ping|
|`-PA`|TCP ACK Ping|
|`-PE`|ICMP Echo Ping|
|`-Pn`|Skip Host Discovery and assume host is alive|
|`--send-ip`|Force Nmap to use Raw IP packets|

These options are commonly used during the:

```
Reconnaissance and Enumeration
```

phase of a penetration test to identify active systems before deeper scanning.
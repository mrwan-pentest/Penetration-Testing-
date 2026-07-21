# Nmap Firewall Evasion Options

Nmap provides several options that can be used to test how security devices handle scanning traffic, including:

- Firewalls
- IDS (Intrusion Detection Systems)
- IPS (Intrusion Prevention Systems)

These options help penetration testers understand:

- How network traffic is analyzed
- Whether filtering exists
- How scans appear in logs
- Whether security controls have weak configurations

---

# `-sA` — ACK Scan

## Purpose

Used for:

```
Firewall Detection
```

---

## How It Works

In normal TCP communication, the:

```
ACK Flag
```

is sent after a connection has already been established.

Example:

```
Client  → SYN
Server  → SYN/ACK
Client  → ACK
```

However, with ACK Scan:

Nmap sends:

```
ACK Packet
```

without establishing a real connection first.

---

## Why Use It?

The goal is to observe how the target responds and determine:

- Whether a Firewall exists
- Whether filtering is being applied
- How the Firewall handles unexpected packets

---

## Example

```
nmap -sA 192.168.1.10
```

---

# `-f` — Fragment Packets

## Purpose

The option:

```
-f
```

means:

```
Fragment Packets
```

It performs:

```
Packet Fragmentation
```

---

## Basic Idea

Instead of sending one complete packet:

```
Large Packet
```

Nmap splits it into smaller pieces:

```
Small Fragments
```

---

## Why Use It?

Some older security systems may have difficulty inspecting fragmented packets.

It can be used when testing:

- Firewall Evasion
- IDS/IPS Evasion

---

## Example

```
nmap -f 192.168.1.10
```

---

# `--mtu` — Maximum Transmission Unit

## Purpose

Used to manually specify the size of packet fragments.

---

## What Does MTU Mean?

MTU stands for:

```
Maximum Transmission Unit
```

It means:

```
The largest packet size that can be transmitted over a network without fragmentation.
```

---

## Relationship Between `-f` and `--mtu`

Both options use:

```
Packet Fragmentation
```

However:

|Option|Function|
|---|---|
|`-f`|Performs automatic fragmentation|
|`--mtu`|Allows manual fragment size control|

---

## Example

```
nmap -sS --mtu 16 192.168.1.10
```

---

## What Does 16 Mean?

It means:

```
Split packets into fragments of 16 bytes.
```

---

## Note

The MTU value must be:

```
A multiple of 8
```

Examples:

```
8
16
24
32
```

---

## Common Uses

- Firewall Evasion
- IDS/IPS Evasion

---

# `--data-length` — Adding Random Data

## Purpose

This option adds:

```
Random Data
```

to packets.

---

## Concept

Instead of sending packets that are:

```
Small and predictable
```

Nmap adds additional data:

```
Packet + Random Data
```

---

## Why Use It?

It can help with:

- Changing the appearance of scan traffic
- Making packets less predictable
- Testing detection systems

---

## Example

```
nmap --data-length 50 192.168.1.10
```

Meaning:

Add:

```
50 Bytes
```

of random data to each packet.

---

# `-D` — Decoy Scan

## Purpose

The option:

```
-D
```

means:

```
Decoy Scan
```

---

## How It Works

It makes the target believe that the scan is coming from multiple systems instead of only the real attacker.

Nmap sends packets from:

- The real attacker IP
- Fake IP addresses (Decoys)

---

## Example

```
nmap -D 1.1.1.1,8.8.8.8 192.168.1.10
```

---

## Uses

- Testing logging systems
- Evaluating detection capabilities
- Making source identification more difficult

---

# `-g` — Source Port Manipulation

## Purpose

The option:

```
-g
```

allows manually setting the:

```
Source Port
```

---

## Default Behavior

Normally, Nmap chooses:

```
A random source port
```

With `-g`:

```
You specify the source port manually.
```

---

## Example

```
nmap -g 53 192.168.1.10
```

---

## Meaning

This sets:

```
Source Port = 53
```

The traffic will appear as if it is coming from:

```
DNS Service
```

---

## Why Use It?

Some poorly configured Firewalls trust traffic based on source ports.

Examples:

|Port|Service|
|---|---|
|53|DNS|
|80|HTTP|
|20/21|FTP|

The goal is to test whether Firewall rules incorrectly trust specific source ports.

---

# Summary

|Option|Purpose|
|---|---|
|`-sA`|ACK Scan for Firewall Detection|
|`-f`|Packet Fragmentation|
|`--mtu`|Manual Fragment Size Control|
|`--data-length`|Add Random Data to Packets|
|`-D`|Decoy Scan|
|`-g`|Source Port Manipulation|

These options are commonly used during:

```
Network Enumeration
```

to analyze security controls and understand how network defenses respond to scanning activity.
# `-sS`

Means:

```
TCP SYN Scan
```

Also known as:

```
Half-Open Scan
```

---

# How does it work?

Nmap sends:

```
SYN Packet
```

If the port is open, the target replies with:

```
SYN-ACK
```

Then Nmap:

```
Does not complete the connection
```

Instead, it sends:

```
RST
```

to terminate the connection.

---

# Advantages

- Fast
- One of the most commonly used Nmap scans
- Does not complete the TCP handshake, so it may create fewer logs compared to a full connection scan

---

# Example

```
nmap -sS 192.168.1.10
```

---

# Requirement

Requires:

```
Root privileges
```

because Nmap needs to create and send raw packets.

---

# `-sT`

Means:

```
TCP Connect Scan
```

---

# How does it work?

It completes the full:

```
TCP 3-Way Handshake
```

which is:

```
SYN → SYN-ACK → ACK
```

After establishing the connection, Nmap closes it.

---

# Example

```
nmap -sT 192.168.1.10
```

---

# When is it used?

When:

```
You do not have Root privileges
```

Because it uses the operating system's normal TCP connection functions.

---

# Difference from `-sS`

`-sS`:

- Does not complete the handshake
- Faster
- Requires Root

`-sT`:

- Completes the handshake
- Easier to detect in logs
- Works without Root

---

# `-sU`

Means:

```
UDP Scan
```

Used to scan:

```
UDP Ports
```

Examples:

- DNS → Port 53
- SNMP → Port 161

Example:

```
nmap -sU target
```

---

# Why is UDP scanning different?

Because UDP does not have a handshake like TCP.

Nmap sends UDP packets and analyzes the response:

- No response → may be open or filtered
- ICMP Port Unreachable → closed

---

# `-v`

Means:

```
Verbose Mode
```

It displays more details during the scan.

Example:

```
nmap -v target
```

Useful for seeing:

- Scan progress
- Discovered ports
- Additional information

---

# `-F`

Means:

```
Fast Scan
```

It scans only the most common ports.

By default:

```
Top 100 ports
```

instead of scanning thousands of ports.

Example:

```
nmap -F target
```

---

# `-p-`

Means:

```
Scan All Ports
```

It scans:

```
1-65535
```

instead of only the common ports.

Example:

```
nmap -p- target
```

Useful because sometimes services run on unusual ports.

---

# `-sL`

Means:

```
List Scan
```

---

# What does it do?

Nmap:

```
Only lists the targets
```

without performing:

- Port scanning
- Host discovery
- Sending real scan packets

---

# Example

```
nmap -sL 192.168.1.0/24
```

---

# What does Nmap do?

It:

- Calculates all IP addresses inside the range
- Displays them only

---

# Example output:

```
Nmap scan report for 192.168.1.1
Nmap scan report for 192.168.1.2
Nmap scan report for 192.168.1.3
```

---

# When is `-sL` useful?

Useful for:

- Checking the IP range before scanning
- Confirming target list
- Passive reconnaissance

It is considered the quietest Nmap scan because it does not actively probe the targets.
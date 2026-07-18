

## `-sn`

Performs host discovery only.

- Identifies live hosts on the network.
    
- Does **not** perform:
    
    - Port Scanning
        
    - Service Detection
        

Example:

```bash
nmap -sn 192.168.1.0/24
```

---

## `-PS`

Performs a TCP SYN Ping.

Instead of using ICMP Echo Requests, Nmap sends TCP SYN packets to determine whether a host is alive.

Useful when:

- ICMP is blocked.
    
- TCP traffic is allowed.
    

Examples:

```bash
nmap -PS 192.168.1.0/24
```

Specify target ports:

```bash
nmap -PS80,443 192.168.1.0/24
```

This sends SYN packets to:

- Port 80
    
- Port 443
    

TCP Ping can sometimes bypass firewall restrictions that block ICMP traffic.

---

## `--send-ip`

Forces Nmap to use raw IP packets instead of Ethernet frames.

Default behavior on a local network:

- ARP
    
- Ethernet Frames
    

With `--send-ip`:

- Raw IP packets are used.
    

Example:

```bash
nmap --send-ip -sn 192.168.1.0/24
```

---

## `-PA`

Performs a TCP ACK Ping.

Instead of sending SYN packets, Nmap sends ACK packets.

If the host is alive, it commonly responds with:

```text
RST
```

This indicates that the host exists and is reachable.

Examples:

```bash
nmap -PA 192.168.1.0/24
```

Specify target ports:

```bash
nmap -PA80,443 192.168.1.0/24
```

Useful when:

- ICMP is blocked.
    
- SYN packets are filtered.
    
- ACK packets are allowed through the firewall.
    

---

## `-PE`

Performs an ICMP Echo Ping.

Nmap sends:

```text
ICMP Echo Request
```

Similar to the standard `ping` command.

If the target replies with:

```text
ICMP Echo Reply
```

The host is considered alive.

Example:

```bash
nmap -PE 192.168.1.0/24
```

Commonly used for:

- Live Host Discovery
    

Note:

Some hosts and firewalls block ICMP traffic, making this method unreliable in certain environments.
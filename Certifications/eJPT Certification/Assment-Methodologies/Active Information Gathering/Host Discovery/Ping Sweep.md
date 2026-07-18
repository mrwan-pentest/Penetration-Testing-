

A Ping Sweep is used to identify live hosts within a network range.

## How Does It Work?

A Ping Sweep sends:

```text
ICMP Echo Request
```

If a host responds with:

```text
ICMP Echo Reply
```

The host is considered:

```text
Alive
```

---

## Common Tools for Ping Sweeps

- ping
    
- fping
    
- nmap
    
- netdiscover
    

---

# fping

`fping` is a fast host discovery tool designed to ping multiple hosts simultaneously.

It is more efficient than the traditional `ping` command when scanning large networks.

### Advantages

- Fast network-wide host discovery
    
- Scans multiple targets in parallel
    
- Useful during the reconnaissance phase
    

---

## Scan an Entire Subnet

```bash
fping -a -g 192.168.1.0/24
```

Suppress unreachable host messages:

```bash
fping -a -g 10.10.10.0/24 2>/dev/null
```

---

## Options

|Option|Description|
|---|---|
|`-a`|Display only live hosts|
|`-g`|Generate target IPs from a network range|

---

## Example Output

```text
192.168.1.1
192.168.1.10
192.168.1.20
```

Only responsive hosts are displayed when using `-a`.
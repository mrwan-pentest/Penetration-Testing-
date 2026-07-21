# fping Tool

`fping` is a:

```
Fast tool for checking multiple hosts using ping
```

It is an alternative to the normal `ping` command when you need to:

- Scan an entire network
- Check many hosts quickly

---

# Scanning an Entire Network

Example:

```
fping -a -g 192.168.1.0/24
```

Another example:

```
fping -a -g 10.10.10.0/24 2>/dev/null
```

---

# Option Explanation

|Option|Function|
|---|---|
|`-a`|Display only live hosts|
|`-g`|Generate a range of IP addresses from the network|

---

# How it works

Instead of manually running:

```
ping 192.168.1.1
ping 192.168.1.2
ping 192.168.1.3
```

`fping` automatically generates all IP addresses in the range and checks them.

Example:

```
fping -a -g 192.168.1.0/24
```

It scans:

```
192.168.1.1
192.168.1.2
192.168.1.3
...
192.168.1.254
```

and displays only hosts that respond.

---

# Why is `fping` useful in penetration testing?

During the:

```
Host Discovery Phase
```

it helps you quickly identify:

- Active machines
- Live hosts
- Potential targets

before moving to:

- Port Scanning
- Service Enumeration
- Vulnerability Assessment

---

# Difference between ping and fping

|ping|fping|
|---|---|
|Checks one host at a time|Checks multiple hosts simultaneously|
|Slower for large networks|Faster for network discovery|
|Manual IP input|Supports IP ranges|

---

# Example workflow

First discover live hosts:

```
fping -a -g 192.168.1.0/24
```

Then scan discovered targets:

```
nmap -sS target
```

So `fping` is mainly used for:

```
Fast Host Discovery
```
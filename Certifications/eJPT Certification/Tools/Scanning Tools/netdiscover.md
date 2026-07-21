# Netdiscover

`netdiscover` is a network discovery tool used to identify active devices within a Local Area Network (LAN).

It primarily relies on:

```
ARP Requests
```

Because ARP operates at the local network level, `netdiscover` is especially useful during the **Enumeration** phase of a penetration test to discover live hosts connected to the same network segment.

---

# Purpose

The main purpose of `netdiscover` is to identify devices that are currently active on the local network.

It can discover information such as:

- IP Address
- MAC Address
- Hardware vendor (manufacturer) based on the MAC address prefix
- Active hosts within the same LAN

This information helps penetration testers understand the network structure and identify potential targets for further enumeration.

---

# How Does Netdiscover Work?

`netdiscover` uses the **Address Resolution Protocol (ARP)** to communicate with devices on the local network.

The process works as follows:

1. The tool sends ARP requests to IP addresses within a specific range.
2. Active devices respond with ARP replies.
3. The tool collects information from these responses.
4. The discovered devices are displayed with their IP and MAC addresses.

Because ARP requests are only forwarded inside the local network, `netdiscover` is mainly effective against hosts that exist in the same broadcast domain.

---

# Information Collected

During a scan, `netdiscover` can reveal:

|Information|Description|
|---|---|
|IP Address|The network address assigned to the device|
|MAC Address|The physical hardware address of the network interface|
|Vendor|The device manufacturer identified from the MAC prefix|

---

# Usage in Penetration Testing

During the initial **Enumeration** phase, a penetration tester may not know which devices exist inside the target network.

`netdiscover` helps answer questions such as:

- Which hosts are currently online?
- What IP addresses are in use?
- Are there unknown devices connected to the network?
- What type of hardware may exist in the environment?

This information can be used as a starting point for further activities such as:

- Port scanning
- Service enumeration
- Vulnerability assessment

---

![](../../../../Images/Pasted%20image%2020260511161631.png)

---

# Summary

`netdiscover` is a lightweight network discovery tool that uses ARP requests to identify live hosts inside a local network.

Key points:

- Works mainly inside LAN environments.
- Uses ARP instead of traditional ICMP ping.
- Can discover IP addresses and MAC addresses.
- Commonly used during the Enumeration phase of penetration testing.
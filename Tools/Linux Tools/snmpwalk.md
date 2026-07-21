# snmpwalk

## What is snmpwalk?

`snmpwalk` is a tool used to query devices that have:

```
SNMP (Simple Network Management Protocol)
```

enabled.

It retrieves large amounts of information from the device by walking through the:

```
MIB (Management Information Base)
```

Instead of sending a single SNMP query, `snmpwalk` automatically traverses available SNMP objects and collects multiple pieces of information.

The name comes from:

```
walk = move through / traverse
```

because the tool walks through the SNMP information tree.

---

# What is SNMP?

SNMP is a protocol used for:

- Network device management
- Monitoring systems
- Collecting device information

It is commonly found on:

- Routers
- Switches
- Servers
- Printers
- Network appliances

---

# Basic Usage

The general syntax:

```
snmpwalk -v <version> -c <community_string> <target>
```

Example:

```
snmpwalk -v 1 -c public 192.168.1.10
```

---

# Command Explanation

|Option|Description|
|---|---|
|`snmpwalk`|The SNMP enumeration tool|
|`-v 1`|Specifies the SNMP version|
|`-c public`|Specifies the SNMP Community String|
|IP Address|The target device|

---

# Querying Specific OIDs

SNMP information is organized using:

```
OID (Object Identifier)
```

An OID identifies a specific piece of information inside the MIB.

Example:

```
snmpwalk -v1 -c public 192.168.1.10 1.3.6.1.2.1.1.5
```

This queries a specific SNMP object instead of walking through the entire MIB.

---

# Common SNMP Enumeration Examples

## System Information

To retrieve general system information:

```
snmpwalk -v1 -c public 192.168.1.10 1.3.6.1.2.1.1.1
```

This may reveal information such as:

- Operating system
- Device type
- System description
- Hardware details

---

## System Name

To retrieve the device hostname:

```
snmpwalk -v1 -c public 192.168.1.10 1.3.6.1.2.1.1.5
```

This can reveal:

- Hostname
- Device name

---

## User Enumeration

In some cases, SNMP may expose user information.

Example:

```
snmpwalk -v1 -c public 192.168.1.10 1.3.6.1.4.1.77.1.2.25
```

This may reveal:

- Local users
- Account information

The availability of this information depends on the SNMP configuration and permissions.

---

# Security Considerations

SNMP can expose sensitive information if it is improperly configured.

Common security issues include:

- Default community strings such as:

```
public
```

- Excessive information exposure.
- Weak SNMP permissions.
- Using insecure SNMP versions.

SNMPv1 and SNMPv2c transmit community strings without encryption, making them less secure compared to:

```
SNMPv3
```

which supports authentication and encryption.

---

# Useful Resources

A useful SNMP enumeration cheatsheet:

[https://github.com/mivang/cheatsheets/blob/master/snmpwalk](https://github.com/mivang/cheatsheets/blob/master/snmpwalk)

It contains examples and references related to `snmpwalk` and other SNMP techniques.
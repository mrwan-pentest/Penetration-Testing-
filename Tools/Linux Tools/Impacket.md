# Impacket

## What is Impacket?

Impacket is:

```
A collection of Python-based tools and scripts
```

used to interact with Windows protocols and services.

It provides the ability to communicate with and perform operations against protocols such as:

- SMB
- NTLM
- Kerberos
- LDAP
- MSRPC
- Other Windows-related protocols

Impacket is widely used during penetration testing, Active Directory assessments, and post-exploitation activities.

---

# What Does Impacket Provide?

Impacket contains scripts and libraries that support many offensive security techniques, including:

- Pass-the-Hash
- Remote Execution
- SMB Enumeration
- Kerberos Attacks
- Hash Extraction
- Lateral Movement

---

# Common Impacket Scripts

|Script|Function|
|---|---|
|`psexec.py`|Execute commands remotely through SMB|
|`smbclient.py`|Access SMB Shares|
|`wmiexec.py`|Execute commands through WMI|
|`secretsdump.py`|Extract password hashes and secrets|
|`GetNPUsers.py`|Perform AS-REP Roasting|
|`GetUserSPNs.py`|Perform Kerberoasting|
|`atexec.py`|Execute commands through Task Scheduler|
|`lookupsid.py`|Perform SID Enumeration|

---

# Impacket Command Format

When using Impacket tools, the command name usually starts with:

```
impacket-
```

Example:

```
impacket-psexec
```

The same applies to other scripts:

```
impacket-smbclient
impacket-wmiexec
impacket-secretsdump
```

---

# psexec.py

## Purpose

`psexec.py` is used to execute commands remotely on Windows machines through SMB.

It can provide a remote shell if valid credentials are available.

---

## Basic Usage

```
psexec.py administrator:password@IP
```

After successful authentication, it provides:

```
Shell on the target machine
```

---

# Pass-the-Hash with psexec.py

Instead of using a password, `psexec.py` can authenticate using an NTLM Hash.

Example:

```
psexec.py administrator@IP -hashes LMHASH:NTHASH
```

This technique is known as:

```
Pass-the-Hash
```

It allows authentication using the NTLM Hash without knowing the original password.

---

# secretsdump.py

## Purpose

`secretsdump.py` is used to extract password hashes and security secrets from Windows systems.

---

## Basic Usage

```
secretsdump.py administrator:pass@IP
```

The tool may extract:

- SAM Hashes
- LSA Secrets
- Cached Credentials

---

# smbclient.py

## Purpose

`smbclient.py` is used to connect to SMB Shares on Windows systems.

---

## Basic Usage

```
smbclient.py user:pass@IP
```

It allows interaction with SMB resources using valid credentials.

---

# wmiexec.py

## Purpose

`wmiexec.py` executes commands remotely through:

```
Windows Management Instrumentation (WMI)
```

Unlike file-based execution methods, it can execute commands remotely without uploading an executable file.

---

## Basic Usage

```
wmiexec.py administrator:pass@IP
```

After successful authentication, commands can be executed on the remote Windows system
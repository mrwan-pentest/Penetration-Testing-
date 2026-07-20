# User Account Control (UAC)

## What is UAC?

UAC stands for:

```
User Account Control
```

It is a Windows security feature responsible for controlling the execution of applications that require elevated privileges.

The well-known Windows prompt appears as:

```
Do you want to allow this app to make changes?
```

---

# Why Does UAC Exist?

Even if a user belongs to the:

```
Administrators
```

group, Windows does not automatically provide full administrative privileges.

Instead, Windows runs the user with:

```
Limited privileges
```

until the user approves the UAC prompt.

This prevents unauthorized applications from performing administrative actions without user approval.

---

# Important Concept: Administrator vs Elevated Administrator

Windows separates administrator accounts into two different security contexts.

## Administrator

A user who belongs to the:

```
Administrators Group
```

However, the user may still be running with restricted privileges because of UAC.

---

## Elevated Administrator

An Administrator account running with:

```
Fully elevated privileges
```

This means the process has obtained a high integrity level and can perform administrative operations.

---

# Example Scenario

Sometimes inside a Meterpreter session, running:

```
getuid
```

may show:

```
WIN-XXX\Administrator
```

However, when attempting actions such as:

- Disable Windows Defender
- Dump SAM database
- Perform SYSTEM-level actions

The actions may fail.

---

# Why Does This Happen?

Because:

```
UAC is still protecting the system
```

The user is an Administrator, but the session is not elevated.

---

# What is UAC Bypass?

UAC Bypass is the process of:

```
Bypassing the UAC security prompt and obtaining an Elevated Session
```

without requiring the user to manually click:

```
Yes
```

The goal is to execute code with elevated Administrator privileges.

---

# What is UACMe?

## Overview

UACMe is a project that contains:

```
Multiple methods for bypassing UAC
```

It provides different techniques that abuse Windows trusted behaviors to achieve privilege elevation.

---

# UACMe Techniques

UACMe includes techniques based on:

- AutoElevate
- DLL Hijacking
- Mock Directories
- COM Hijacking
- Scheduled Tasks
- Other Windows elevation mechanisms

---

# Why Are There Multiple UAC Bypass Methods?

Microsoft continuously patches discovered bypass techniques.

However, security researchers may discover new methods.

Therefore:

```
Microsoft fixes one technique, and researchers discover another.
```

---

# UACMe Repository

The official repository:

[https://github.com/hfiref0x/UACME](https://github.com/hfiref0x/UACME)

![[Pasted image 20260519015121.png]]

---

# Selecting a UAC Bypass Method

UACMe provides information about which methods work against specific Windows versions.

You can check the available techniques from the documentation.

![[Pasted image 20260519015200.png]]

---

# Downloading UACMe

The tool can be downloaded from the official repository.

![[Pasted image 20260519015232.png]]

---

# Privilege Escalation with UACMe

## Step 1: Verify Administrator Group Membership

First, we verify that the current user belongs to the Administrators group.

![[Pasted image 20260519020307.png]]

---

## Step 2: Create a Temporary Directory

We create a temporary directory to store the UACMe tool and the payload.

Example:

```
cd C:\Users\admin\AppData\Local\Temp
```

![[Pasted image 20260519020410.png]]

---

## Step 3: Upload UACMe Tool

We upload the UACMe executable to the target system.

![[Pasted image 20260519020436.png]]

---

## Step 4: Upload the Payload

After uploading the tool, we transfer the payload that will be executed after the UAC bypass.

![[Pasted image 20260519020459.png]]

---

## Step 5: Start the Listener

Before executing the bypass technique, we start a Listener to receive the incoming session.

![[Pasted image 20260519020602.png]]

---

## Step 6: Execute UACMe

We execute the UACMe tool.

The number:

```
23
```

represents the specific UAC bypass method that will be used.

Each method targets specific Windows versions and configurations.

![[Pasted image 20260519020659.png]]

---

## Step 7: Obtain Elevated Session

After successful execution, we obtain a Meterpreter session with elevated privileges.

---

# UAC Bypass Using Metasploit

Metasploit also contains modules for performing UAC bypass.

To search for available modules, use:

```
search bypassuac
```

This displays available UAC bypass modules.

However, UACMe is often preferred because it provides a large collection of techniques and supports multiple Windows versions.
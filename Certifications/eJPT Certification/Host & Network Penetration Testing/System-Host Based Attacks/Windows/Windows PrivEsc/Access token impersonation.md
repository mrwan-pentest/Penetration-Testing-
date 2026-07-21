# Access Token

## What is Access Token?

In Windows, when a user successfully logs into the system, Windows creates an object called:

```
Access Token
```

The Access Token represents the user's identity and permissions inside the operating system.

It works as a security object that tells Windows:

- Who the user is.
- What permissions the user has.
- Which groups the user belongs to.
- What actions the user is allowed to perform.

---

# What Does an Access Token Contain?

An Access Token contains information such as:

- Username
- Security Identifier (SID)
- User groups:
    - Administrators
    - Users
    - Other security groups
- Privileges
- Permission level

---

# What is Token Impersonation?

Token Impersonation is the process of using another user's Access Token to perform actions with that user's privileges.

Instead of running commands with your current user permissions, you use the Access Token of another user who has higher privileges.

For example:

A low-privileged user may obtain an Administrator Token and execute commands with Administrator privileges.

---

# Types of Tokens

## 1. Impersonation Token

An Impersonation Token allows a process or thread to temporarily act as another user.

It is commonly used to perform actions on behalf of another user.

---

## 2. Primary Token

A Primary Token is used to run a complete process under another user's security context.

---

# Common Token Impersonation Tools

## Inside Metasploit

```
incognito
```

The Incognito extension allows attackers to list available Tokens and impersonate users with higher privileges.

---

## Outside Metasploit

Common Token Impersonation tools include:

- JuicyPotato
- RoguePotato
- PrintSpoofer
- GodPotato

---

# Privilege Escalation with Metasploit

## Method 1: Using Incognito

### Loading the Incognito Extension

After obtaining a Meterpreter session, we first load the Incognito extension.

![](Penetration%20Testing/Images/Pasted%20image%2020260519132904.png)

---

### Listing Available Tokens

We enumerate the available Tokens that can be impersonated.

![](Penetration%20Testing/Images/Pasted%20image%2020260519132938.png)

---

### Impersonating an Administrator Token

After identifying a privileged Token, we impersonate the Administrator Token.

![](Penetration%20Testing/Images/Pasted%20image%2020260519133022.png)

---

### Verify the Privileges

After successful Token impersonation, we gain access using the privileges of the impersonated user.

![](Penetration%20Testing/Images/Pasted%20image%2020260519133038.png)

---

# Privilege Escalation with PrintSpoofer

## Method 2: Manual Token Impersonation

PrintSpoofer is a tool that abuses Windows privilege mechanisms to obtain elevated privileges by impersonating privileged Tokens.

---

# Step 1: Upload the Tool

First, upload the PrintSpoofer executable to the target machine.

Example:

```
PrintSpoofer.exe
```

---

# Step 2: Execute PrintSpoofer

Run the following command:

```
PrintSpoofer.exe -i -c cmd
```

This creates an interactive command shell with elevated privileges.

---

# PrintSpoofer Options

## -i

```
Interactive
```

Creates an interactive shell session.

---

## -c

Specifies the command that should be executed.

Example:

```
PrintSpoofer.exe -i -c powershell.exe
```

This launches an interactive PowerShell session using elevated privileges.
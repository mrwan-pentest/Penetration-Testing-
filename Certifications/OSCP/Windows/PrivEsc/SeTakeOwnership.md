# SeTakeOwnership

## What is SeTakeOwnershipPrivilege?

`SeTakeOwnershipPrivilege` is a Windows privilege that allows a user to **take ownership of files and other objects**, even when the user would not normally have permission to modify them.

This privilege can become useful for Privilege Escalation because becoming the owner of an object gives the user control over its security settings. Once we become the owner, we can modify the object's **DACL (Discretionary Access Control List)** and grant ourselves additional permissions.

A very important distinction is:

> **Ownership does not automatically mean Full Control.**

The attack therefore happens in multiple stages:

```
SeTakeOwnershipPrivilege
        ↓
Take ownership of a protected object
        ↓
Become the object's owner
        ↓
Modify its DACL
        ↓
Grant ourselves Full Control
        ↓
Modify or replace the object
        ↓
Find a privileged execution path
        ↓
Privilege Escalation
```

In this lab, the target is `Utilman.exe`, a Windows utility that is executed with **SYSTEM privileges** from the Windows lock screen.

---

# Lab

## Initial Access

We started by logging into the Windows machine using the `THMTakeOwnership` user.

Although the user is not actually an Administrator, we opened **Command Prompt using the "Run as administrator" option**.

This can be confusing because the window is an elevated Command Prompt, but that does **not** mean that the `THMTakeOwnership` account has become the Administrator account.

The purpose of doing this is to obtain an **elevated token** for the existing user so that the `SeTakeOwnershipPrivilege` privilege is available for use.

In other words:

```
THMTakeOwnership
        ↓
Run Command Prompt as Administrator
        ↓
Elevated token for THMTakeOwnership
        ↓
SeTakeOwnershipPrivilege becomes available
```

This is different from logging in as the built-in Administrator account.

---

## Step 1 — Enumerate Our Privileges

Before attempting anything, we need to verify which Windows privileges are available to our current security token.

We use:

```
whoami /priv
```

This displays the privileges associated with the current user token.

In the lab, we can see:

```
SeTakeOwnershipPrivilege
```

with the privilege initially shown as `Disabled`.

![SeTakeOwnership privilege](../../../../Images/Pasted%20image%2020260926213636.png)

### What does `Disabled` mean?

`Disabled` does **not** mean that the privilege is unavailable.

It means that the privilege exists in the current token but is not currently enabled for use.

This is one reason why opening the Command Prompt through **Run as administrator** is important in this lab: Windows provides an elevated token containing the necessary privilege.

The important thing to identify during enumeration is therefore:

```
SeTakeOwnershipPrivilege
```

---

# Step 2 — Understand the Target: Utilman.exe

Our target is:

```
C:\Windows\System32\Utilman.exe
```

`Utilman.exe` is a built-in Windows application associated with **Ease of Access** features.

It can be launched directly from the Windows lock screen using the **Ease of Access** button.

![Utilman](../../../../Images/Pasted%20image%2020260926213930.png)

The important security property for this lab is that `Utilman.exe` is executed by Windows in a **SYSTEM security context**.

This gives us a potential Privilege Escalation path.

The idea is not simply to modify an arbitrary system file.

Instead, we want to modify a program that:

1. We can obtain control over.
2. We can cause Windows to execute.
3. Is normally executed with SYSTEM privileges.

Therefore, if we can replace `Utilman.exe` with another executable, the replacement executable can inherit the privileged execution context when Windows launches it.

The intended execution flow is:

```
Windows Lock Screen
        ↓
Ease of Access
        ↓
Utilman.exe
        ↓
SYSTEM
```

Our goal is to turn it into:

```
Windows Lock Screen
        ↓
Ease of Access
        ↓
Modified Utilman.exe
        ↓
cmd.exe
        ↓
SYSTEM
```

---

# Step 3 — Take Ownership of Utilman.exe

Normally, our user should not be able to modify:

```
C:\Windows\System32\Utilman.exe
```

This is where `SeTakeOwnershipPrivilege` becomes useful.

We take ownership of the file with:

```
takeown /f C:\Windows\System32\Utilman.exe
```

The `/f` option specifies the file for which we want to take ownership.

After successful execution, the ownership of the file changes to our current user.

Conceptually:

```
Before:

Owner
  ↓
Trusted system account

User
  ↓
No ownership
```

After `takeown`:

```
Owner
  ↓
THMTakeOwnership
```

However, this is an important point:

> **Taking ownership does not automatically give us Full Control over the file.**

We have changed the **Owner**, but the existing DACL can still prevent us from modifying the file.

Therefore, we need another step.

---

# Step 4 — Grant Our User Full Control

Now that `THMTakeOwnership` owns the file, we can modify its security permissions and grant ourselves Full Control.

We use:

```
icacls C:\Windows\System32\Utilman.exe /grant THMTakeOwnership:F
```

`icacls` is a Windows utility used to view and modify file and directory permissions.

The important part of this command is:

```
/grant THMTakeOwnership:F
```

This means:

```
THMTakeOwnership → Full Control
```

The `F` represents **Full Control**.

![Granting Full Control](../../../../Images/Pasted%20image%2020260926214205.png)

Our privilege escalation path has now reached this point:

```
SeTakeOwnershipPrivilege
        ↓
Take ownership of Utilman.exe
        ↓
Become the owner
        ↓
Modify the DACL
        ↓
Grant THMTakeOwnership Full Control
```

We can now modify the executable.

---

# Step 5 — Replace Utilman.exe with cmd.exe

The next step is to replace the contents of `Utilman.exe` with a copy of `cmd.exe`.

We use:

```
copy cmd.exe utilman.exe
```

This does not make `cmd.exe` itself a SYSTEM program.

Instead, we are taking advantage of **who launches the program**.

Normally:

```
Windows
   ↓
Utilman.exe
   ↓
SYSTEM
```

After the replacement:

```
Windows
   ↓
Utilman.exe
   ↓
Actually contains cmd.exe
   ↓
SYSTEM
```

![Replacing Utilman](../../../../Images/Pasted%20image%2020260926214601.png)

This distinction is extremely important.

The privilege escalation does **not** happen because `cmd.exe` is inherently privileged.

It happens because **Windows launches the replacement executable using the same privileged execution context that it normally uses for Utilman**.

---

# Step 6 — Trigger Utilman from the Lock Screen

Normally, when Windows is at the lock screen, pressing the **Ease of Access** button launches:

```
C:\Windows\System32\Utilman.exe
```

![Ease of Access](../../../../Images/Pasted%20image%2020260926214916.png)

However, we have already replaced the original executable with `cmd.exe`.

Therefore, the execution chain has changed.

### Original behavior

```
Lock Screen
     ↓
Ease of Access
     ↓
Utilman.exe
     ↓
SYSTEM
```

### Modified behavior

```
Lock Screen
     ↓
Ease of Access
     ↓
Modified Utilman.exe
     ↓
cmd.exe
     ↓
SYSTEM
```

This is the critical moment of the attack.

---

# Step 7 — Obtain a SYSTEM Shell

When we trigger **Ease of Access**, Windows launches the modified `Utilman.exe`.

Because the process is launched in the SYSTEM security context, the `cmd.exe` replacement also runs with SYSTEM privileges.

![SYSTEM Shell](../../../../Images/Pasted%20image%2020260926214952.png)

We can verify our current security context with:

```
whoami
```

The expected result is:

```
nt authority\system
```

At this point, the Privilege Escalation is complete.

---

# Understanding the Complete Attack Chain

The entire technique can be understood as a sequence of abusing **ownership**, **permissions**, and **privileged execution**.

```
THMTakeOwnership
        |
        | Elevated Command Prompt
        ↓
SeTakeOwnershipPrivilege
        |
        | Take ownership
        ↓
Utilman.exe
        |
        | Become Owner
        ↓
Modify DACL
        |
        | Grant Full Control
        ↓
THMTakeOwnership → Full Control
        |
        | Replace executable
        ↓
Utilman.exe = cmd.exe
        |
        | Trigger from Lock Screen
        ↓
Windows launches Utilman
        |
        | SYSTEM execution context
        ↓
cmd.exe
        |
        ↓
NT AUTHORITY\SYSTEM
```

---

# Ownership vs. Permissions vs. Privileges

This lab is particularly useful because it demonstrates three concepts that are easy to confuse.

## Privilege

A **Privilege** is a capability assigned to a Windows security token.

Example:

```
SeTakeOwnershipPrivilege
```

It allows the user to take ownership of objects.

---

## Ownership

**Ownership** identifies which security principal owns an object.

For example:

```
Owner: THMTakeOwnership
```

Being the owner does not automatically mean that the user has Full Control.

However, ownership gives the owner the ability to manage the object's security permissions, allowing the owner to modify the DACL and grant appropriate permissions.

---

## Permission

Permissions are defined through the object's **DACL**.

For example:

```
THMTakeOwnership → Full Control
SYSTEM            → Full Control
Users             → Read & Execute
```

In this lab, we use our ownership of `Utilman.exe` to modify its DACL and grant ourselves:

```
Full Control
```

The relationship is therefore:

```
Privilege
    ↓
Take Ownership
    ↓
Ownership
    ↓
Modify DACL
    ↓
Permissions
    ↓
Modify Protected File
```

---

# Why This Leads to SYSTEM

The most important question is:

> Why does modifying `Utilman.exe` result in SYSTEM?

Because the file is not just an arbitrary executable.

Windows is designed to launch `Utilman.exe` from the lock screen using a privileged security context.

We abuse this trusted execution path.

The original relationship is:

```
Windows
   ↓
Utilman.exe
   ↓
SYSTEM
```

We change only the executable:

```
Windows
   ↓
Utilman.exe
   ↓
cmd.exe
   ↓
SYSTEM
```

Therefore, the key idea is:

> **We do not make cmd.exe privileged. We replace a privileged executable with cmd.exe and let Windows execute it through an already privileged execution path.**

---

# Important Lesson

Having `SeTakeOwnershipPrivilege` does **not** automatically mean:

```
SeTakeOwnershipPrivilege = SYSTEM
```

The privilege only gives us the ability to take ownership.

We still need to find an object that can provide a path to higher privileges.

The general methodology is:

```
1. Identify a privileged Windows privilege.
2. Determine what objects we can affect with it.
3. Take ownership of a useful object.
4. Modify its permissions if necessary.
5. Modify or replace the object.
6. Find a way to make Windows execute or use it.
7. Obtain execution in a higher-privileged context.
```

In this lab:

```
Useful privilege:
SeTakeOwnershipPrivilege

Target:
Utilman.exe

Privileged execution context:
SYSTEM

Modification:
Replace Utilman.exe with cmd.exe

Trigger:
Ease of Access from the Lock Screen

Result:
SYSTEM shell
```

---

# Key Takeaways

- `SeTakeOwnershipPrivilege` allows a user to take ownership of protected Windows objects.
- **Ownership and permissions are not the same thing.**
- After becoming the owner, we can modify the object's DACL and grant ourselves additional permissions.
- `icacls` was used to grant `THMTakeOwnership` **Full Control** over `Utilman.exe`.
- `Utilman.exe` is associated with the Windows **Ease of Access** functionality on the lock screen.
- Windows launches Utilman in a **SYSTEM context**.
- Replacing `Utilman.exe` with `cmd.exe` causes Windows to launch `cmd.exe` through that privileged execution path.
- The resulting shell runs as:

```
NT AUTHORITY\SYSTEM
```

- The important concept is not the specific `Utilman` trick. The broader Windows Privilege Escalation technique is:

```
Obtain control over something privileged
        ↓
Modify it
        ↓
Cause the privileged component to execute/use it
        ↓
Inherit the privileged execution context
```

This is why **SeTakeOwnershipPrivilege** can be valuable during Windows Privilege Escalation enumeration.
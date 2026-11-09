# Insecure Service Permissions

## Insecure Service Permissions — Overview

Insecure Service Permissions is a Windows Privilege Escalation weakness that occurs when a low-privileged user has excessive permissions over a Windows Service configuration.

A Windows Service contains important settings such as:

- The executable it runs through `binPath`.
    
- The account used to run it through `obj`.
    
- Its startup behavior.
    
- Other service-related configuration options.
    

Normally, regular users should not be able to modify these settings. However, if the Service DACL grants users permissions such as `SERVICE_CHANGE_CONFIG` or `SERVICE_ALL_ACCESS`, they may be able to reconfigure the Service.

The important idea is:

> We may not be able to modify the original Service executable, but we may be able to change which executable the Service runs.

For example, a Service may originally be configured like this:

```
Service: THMService
Executable: C:\Program Files\THM\service.exe
Account: LocalSystem
```

If a low-privileged user can modify the Service configuration, they may change it to:

```
Service: THMService
Executable: C:\Users\thm-unpriv\rev-svc3.exe
Account: LocalSystem
```

When the Service is restarted, Windows executes the new executable using the Service's configured account. If that account is `LocalSystem`, the new process may run with SYSTEM privileges.

### What must be true for exploitation?

An exploitable situation usually requires:

1. The user can modify the Service configuration.
    
2. The user can change the executable path or another useful setting.
    
3. The Service runs with higher privileges, such as `LocalSystem`.
    
4. The replacement executable can be accessed and executed by the Service.
    
5. The Service can be restarted or otherwise triggered.
    

### Important distinction

Do not confuse these two permissions:

```
Service Executable Permissions
```

and:

```
Service Configuration Permissions
```

- Executable permissions determine who can modify the actual `.exe` file.
    
- Service configuration permissions determine who can change the Service settings, including its executable path.
    

Therefore, a Service executable may be well protected while the Service itself remains vulnerable because users can modify its configuration.

### Main enumeration tools

Common tools for identifying this weakness include:

- `AccessChk`
    
- `PowerUp`
    
- `winPEAS`
    
- `SharpUp`
    

The manual verification process usually involves:

```
AccessChk
   ↓
Inspect Service DACL
   ↓
Identify excessive permissions
   ↓
sc qc
   ↓
Check Service configuration and execution account
   ↓
Validate the potential impact
```

In short: Insecure Service Permissions happen when a low-privileged user can control a privileged Windows Service's configuration. By changing its executable path and restarting it, the user may cause Windows to execute a chosen program with the Service's higher privileges.

---


# Lab

## Step 1: Enumerate Service Permissions

We first inspected the Service and checked which users or groups had permissions to modify its configuration.

![Service Permissions](../../../../Images/Pasted%20image%2020260925000612.png)

The goal of this step is to determine whether our current low-privileged user has sufficient permissions over the Service.

The results showed that regular users had permissions over the Service.

![Service DACL](../../../../Images/Pasted%20image%2020260925000632.png)

This indicated that the Service configuration could potentially be modified by users who should not normally have this level of control.

## Step 2: Generate the Payload

We then generated a Windows Service-compatible reverse shell Payload.

![Payload Generation](../../../../Images/Pasted%20image%2020260925000751.png)

The Payload will later be assigned as the Service's executable. When the Service starts, Windows will execute the configured executable using the Service's configured account.

## Step 3: Transfer the Payload

After generating the Payload, we transferred it to the target machine and placed it at the location we intended to use as the new Service executable.

![Payload Transfer](../../../../Images/Pasted%20image%2020260925000831.png)

The Payload was stored at:

```
C:\Users\thm-unpriv\rev-svc3.exe
```

## Step 4: Configure Payload Permissions

We granted `Everyone` Full Control over the Payload:

```
icacls C:\Users\thm-unpriv\rev-svc3.exe /grant Everyone:F
```

This ensures that the Service can access and execute the Payload.

Here:

- `icacls` manages Windows file and directory permissions.
- `/grant` adds permissions to the specified account or group.
- `Everyone:F` grants `Everyone` `Full Control`.

## Step 5: Modify the Service Configuration

The most important step was changing the Service's executable path and execution account:

```
sc config THMService binPath= "C:\Users\thm-unpriv\rev-svc3.exe" obj= LocalSystem
```

This changes two important properties of `THMService`.

### `binPath`

```
binPath= "C:\Users\thm-unpriv\rev-svc3.exe"
```

This changes the executable that Windows launches when the Service starts.

Instead of the original Service executable, Windows will now execute our Payload.

### `obj`

```
obj= LocalSystem
```

This specifies the account under which the Service runs.

`LocalSystem` is a highly privileged Windows account, so the Payload will execute within the Service's privileged security context.

![Modified Service Configuration](../../../../Images/Pasted%20image%2020260925001052.png)

### Important `sc.exe` Syntax

When using `sc.exe`, pay close attention to the spaces after the equals signs:

```
binPath= "..."
obj= LocalSystem
```

The space after `=` is significant to the syntax expected by `sc.exe`.

## Step 6: Start the Listener

Before restarting the Service, we started a Listener on the attacker's machine.

![Listener](../../../../Images/Pasted%20image%2020260925001139.png)

The Listener waits for the Reverse Shell connection generated when the Payload executes.

## Step 7: Restart the Service

We then stopped and started the Service to trigger the new configuration.

![Restart Service](../../../../Images/Pasted%20image%2020260925001213.png)

Stopping the Service ensures that the previous process is terminated, while starting it again causes Windows to read the modified configuration and execute the new Payload.

## Step 8: Obtain the Shell

The Service executed the Payload successfully, and the Listener received the incoming connection.

![Shell](../../../../Images/Pasted%20image%2020260925001240.png)

We successfully obtained a Shell through the modified Service.

# Key Takeaways

- A Service can be vulnerable even when its executable file itself is properly protected.
- The weakness may exist in the **Service DACL**, allowing unauthorized users to modify the Service configuration.
- `icacls` can be used to inspect and modify Windows file permissions.
- `sc config` can modify Service properties such as `binPath` and `obj`.
- `binPath` determines which executable the Service launches.
- `obj` determines the account under which the Service runs.
- A Service running as `LocalSystem` can provide a path to significant **Privilege Escalation** if an unprivileged user can modify its configuration.
- The critical distinction is between **executable permissions** and **Service configuration permissions**: a protected executable does not necessarily make the Service secure.
---
### Service DACL vs Executable DACL

- **Service DACL:** Controls who can modify or control the **Service itself**, such as changing its `binPath` or starting/stopping the Service.
- **Executable DACL:** Controls who can modify or replace the **executable file** used by the Service.

**Example:**

```
Service → C:\Program Files\MyService\service.exe
```

- Weak **Service DACL** → You may be able to change the `binPath` and point the Service to your own Payload.
- Weak **Executable DACL** → You may be able to modify or replace `service.exe` itself.

**Key Difference:**

> **Service DACL = Control over the Service**  
> **Executable DACL = Control over the Service's executable**

This distinction is important during Windows Privilege Escalation because you need to identify **what exactly the low-privileged user can control**.
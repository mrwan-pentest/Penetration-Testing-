
# Windows Credential Hunting

Credential Hunting is the process of searching a compromised Windows machine for **stored credentials** that may allow access to another user, service, or system.

Passwords may be stored in many places because of:

- Poor security practices by users.
- Automated Windows installations.
- PowerShell command history.
- Saved Windows credentials.
- Application configuration files.
- Registry entries.
- Web server configuration.
- Third-party applications.

The general methodology is:

```
Compromised Windows Machine
        ↓
Search common credential locations
        ↓
Find username / password / hash / token
        ↓
Validate the credential
        ↓
Use it for authentication or further Privilege Escalation
```

---

# 1. Unattended Windows Installation Files

During automated Windows deployments, administrator credentials may accidentally be stored in configuration files.

### Important Locations

These are the paths I would memorize:

```
C:\Unattend.xml
C:\Windows\Panther\Unattend.xml
C:\Windows\Panther\Unattend\Unattend.xml
C:\Windows\System32\sysprep.inf
C:\Windows\System32\sysprep\sysprep.xml
```

These files may contain credentials such as:

```
<Credentials>
    <Username>Administrator</Username>
    <Domain>thm.local</Domain>
    <Password>MyPassword123</Password>
</Credentials>
```

### Key Idea

> **Whenever you find an unattended installation file, inspect it for credentials.**

---

# 2. PowerShell History

PowerShell stores previously executed commands in a history file.

This can become interesting if a user previously typed a password directly into a command.

### Location

```
%USERPROFILE%\AppData\Roaming\Microsoft\Windows\PowerShell\PSReadLine\ConsoleHost_history.txt
```

From `cmd.exe`:

```
type %userprofile%\AppData\Roaming\Microsoft\Windows\PowerShell\PSReadline\ConsoleHost_history.txt
```

From PowerShell, use:

```
Get-Content "$Env:userprofile\AppData\Roaming\Microsoft\Windows\PowerShell\PSReadLine\ConsoleHost_history.txt"
```

### Important Difference

`%userprofile%` is a **CMD environment variable syntax**.

PowerShell uses:

```
$Env:userprofile
```

### Key Idea

> **Always check PowerShell history because users may have accidentally entered credentials directly into commands.**

---

# 3. Saved Windows Credentials

Windows can store credentials for use with other systems.

First, enumerate saved credentials:

```
cmdkey /list
```

This does **not** display the actual passwords.

However, it may reveal useful stored credentials or targets.

If an appropriate saved credential exists, Windows may allow authentication using:

```
runas /savecred /user:admin cmd.exe
```

The important concept is:

```
Saved Credentials
       ↓
Enumerate with cmdkey
       ↓
Identify useful account
       ↓
Authenticate using stored credentials
```

### Key Idea

> `cmdkey /list` tells you what Windows credentials are stored, but it does not simply dump their plaintext passwords.

---

# 4. IIS `web.config`

If IIS is installed, always remember:

```
web.config
```

This is an important configuration file for ASP.NET/IIS applications.

It may contain sensitive information such as:

- Database connection strings
- Database usernames
- Database passwords
- Authentication configuration

### Common Locations

```
C:\inetpub\wwwroot\web.config
```

and:

```
C:\Windows\Microsoft.NET\Framework64\v4.0.30319\Config\web.config
```

To search for connection strings:

```
type C:\Windows\Microsoft.NET\Framework64\v4.0.30319\Config\web.config | findstr connectionString
```

### Key Idea

> **If you find an IIS application, look for `web.config`. Configuration files frequently contain credentials or other sensitive information.**

---

# 5. PuTTY

PuTTY stores information about saved sessions in the Windows Registry.

The relevant Registry path is:

```
HKEY_CURRENT_USER\Software\SimonTatham\PuTTY\Sessions\
```

You can search for proxy-related credentials with:

```
reg query HKEY_CURRENT_USER\Software\SimonTatham\PuTTY\Sessions\ /f "Proxy" /s
```

PuTTY does **not normally store the SSH session password itself**, but proxy configuration can contain authentication credentials.

### Important

`SimonTatham` is the name of PuTTY's creator and part of the Registry path.

It is **not the username whose credentials you are retrieving**.

---

# 6. Other Software

The bigger lesson is not to memorize only PuTTY.

Many applications can store credentials or sensitive configuration information.

Examples include:

```
Browsers
Email Clients
FTP Clients
SSH Clients
VNC
PuTTY
Database Clients
VPN Software
```

Each application has its own method and storage location.

Therefore, during credential hunting:

```
What software is installed?
        ↓
Does it store credentials?
        ↓
Where does it store them?
        ↓
Can those credentials be recovered?
```

---

# Credential Hunting Cheat Sheet

This is the part I recommend keeping as a **quick-review section** in your notes.

|Target|Location / Command|What to Look For|
|---|---|---|
|Unattended Install|`C:\Unattend.xml`|Administrator credentials|
|Unattended Install|`C:\Windows\Panther\Unattend.xml`|Credentials|
|Unattended Install|`C:\Windows\Panther\Unattend\Unattend.xml`|Credentials|
|Sysprep|`C:\Windows\System32\sysprep.inf`|Credentials|
|Sysprep|`C:\Windows\System32\sysprep\sysprep.xml`|Credentials|
|PowerShell History|`%USERPROFILE%\AppData\Roaming\Microsoft\Windows\PowerShell\PSReadLine\ConsoleHost_history.txt`|Commands/passwords|
|Saved Credentials|`cmdkey /list`|Stored credential targets|
|IIS|`web.config`|DB credentials / connection strings|
|PuTTY|`HKCU\Software\SimonTatham\PuTTY\Sessions\`|Proxy credentials|
|Other Software|Application-specific locations|Stored credentials|
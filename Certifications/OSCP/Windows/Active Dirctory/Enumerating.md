# Active Directory Enumeration with PowerView

## Overview

**PowerView** is a PowerShell script from **PowerSploit** that can be used for **Active Directory enumeration**.

It provides commands for discovering information about the Domain, Domain Controllers, Users, Groups, Policies, and other AD objects.

---

## Step 1: Download PowerView

Download `PowerView.ps1` directly from GitHub:

```
curl.exe -L "https://raw.githubusercontent.com/PowerShellMafia/PowerSploit/master/Recon/PowerView.ps1" -o PowerView.ps1
```

The `-L` option follows redirects, while `-o` saves the downloaded file as `PowerView.ps1`.

---

## Step 2: Start PowerShell with Execution Policy Bypass

```
powershell -ep bypass
```

`-ep bypass` starts a new PowerShell process with the **Execution Policy** set to `Bypass`, allowing scripts to run without being blocked by the policy.

---

## Step 3: Load PowerView

Use dot sourcing to load the script into the current PowerShell session:

```
. .\PowerView.ps1
```

The first `.` means **dot sourcing**, which makes the functions defined in `PowerView.ps1` available in the current PowerShell session.

After loading the script, PowerView commands can be executed directly.

---

# Common PowerView Enumeration Commands

## Get Domain Information

To identify the current Active Directory domain:

```
Get-NetDomain
```

This displays information about the current domain, such as its name and other domain-related properties.

---

## Enumerate Domain Controllers

To retrieve information about the Domain Controllers:

```
Get-NetDomainController
```

This can provide information such as the Domain Controller's hostname, domain, and other properties.

---

## Enumerate Domain Users

To retrieve information about domain users:

```
Get-DomainUser
```

This returns information about the users stored in Active Directory.

If you only want to display the users' Common Names (`cn`):

```
Get-DomainUser | select cn
```

---

## Enumerate Domain Policy

To retrieve the domain's security policy information:

```
Get-DomainPolicy
```

This can provide information about policies configured for the domain, such as password and account-related policies.

---

# Built-in Windows Commands

Some basic Active Directory enumeration can also be performed using built-in Windows commands.

### Enumerate Domain Users

```
net users /domain
```

This displays the users in the domain.

### Enumerate Domain Groups

```
net group /domain
```

This displays the groups in the domain.

---

## Quick Reference

|Command|Purpose|
|---|---|
|`Get-NetDomain`|Domain information|
|`Get-NetDomainController`|Domain Controller information|
|`Get-DomainUser`|Domain user information|
|`Get-DomainUser \| select cn`|Display user names|
|`Get-DomainPolicy`|Domain policy information|
|`net users /domain`|List domain users|
|`net group /domain`|List domain groups|
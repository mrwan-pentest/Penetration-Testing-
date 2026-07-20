# CrackMapExec (CME)

## What is CrackMapExec?

CrackMapExec (CME) is a popular penetration testing tool mainly used for:

- SMB Enumeration
- Active Directory assessments
- Pass-the-Hash attacks
- Lateral Movement

It is designed to interact with Windows machines across a network quickly and efficiently.

---

# Main Purpose

CrackMapExec is mainly used for:

```
Quick interaction with Windows systems inside a network
```

It helps penetration testers perform enumeration and authentication testing against Windows environments.

---

# Capabilities of CrackMapExec

CrackMapExec can perform tasks such as:

- SMB enumeration
- Username and password testing
- Pass-the-Hash authentication
- Remote command execution
- SAM database dumping
- Network enumeration
- Session enumeration
- Share enumeration
- User discovery

---

# Common CrackMapExec Usage

## SMB Enumeration

To check SMB information on a target:

```
crackmapexec smb 192.168.1.10
```

This identifies SMB-related information about the target system.

---

## Testing Username and Password

To test credentials against SMB:

```
crackmapexec smb IP -u admin -p password
```

Options:

- `-u` specifies the username.
- `-p` specifies the password.

---

## Pass-the-Hash

CrackMapExec supports authentication using NTLM Hashes.

Example:

```
crackmapexec smb IP -u administrator -H HASH
```

This allows authentication without knowing the user's actual password.

---

## Remote Command Execution

To execute a command on the target:

```
crackmapexec smb IP -u admin -p pass -x whoami
```

The `-x` option executes a command remotely.

Example command:

```
whoami
```

returns the current user context on the target machine.

---

## Enumerating Shares

To display available SMB Shares:

```
crackmapexec smb IP -u admin -p pass --shares
```

This lists accessible network shares using the provided credentials.

---

# NetExec (NXC)

## What is NetExec?

NetExec (NXC) is:

```
The modern successor to CrackMapExec
```

It provides similar functionality with additional improvements and continued development.

---

# Why Was NetExec Created?

CrackMapExec development slowed down for a period of time.

Because of this, the community created:

```
NetExec (nxc)
```

as a modern alternative.

---

# NetExec Usage

## SMB Enumeration

To scan SMB information:

```
nxc smb IP
```

---

## Authentication Testing

To authenticate using credentials:

```
nxc smb IP -u admin -p pass
```

---

## Pass-the-Hash

Authenticate using an NTLM Hash:

```
nxc smb IP -u administrator -H HASH
```

---

## Remote Command Execution

Execute commands remotely:

```
nxc smb IP -u admin -p pass -x whoami
```

The `-x` option executes the specified command on the target.

---

# Supported Protocols in NetExec

NetExec supports multiple protocols, including:

- SMB
- WinRM
- SSH
- FTP
- RDP
- MSSQL
- LDAP

---

# Common Uses of CrackMapExec and NetExec

Both tools are commonly used during:

- Active Directory Enumeration
- Password Spraying
- Pass-the-Hash attacks
- Lateral Movement
- SMB Enumeration

---

# Listing Available Modules

NetExec provides modules that extend its functionality.

To display available SMB modules:

```
nxc smb IP -u admin -p pass -L
```

This lists available modules that can be used for additional enumeration and actions.

---

# Enabling RDP

NetExec can be used to enable Remote Desktop Protocol (RDP) on a target machine.

Example:

```
nxc smb IP -u admin -p pass -M rdp -o ACTION=enable
```

Options:

- `-M rdp` specifies the RDP module.
- `-o ACTION=enable` enables the RDP service.

This is useful during authorized penetration tests when assessing remote access configurations.
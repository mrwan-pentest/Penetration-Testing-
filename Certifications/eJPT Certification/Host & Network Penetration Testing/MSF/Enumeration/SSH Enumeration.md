
# SSH (Secure Shell)

SSH stands for:

```text
Secure Shell
```

It is a secure protocol that allows users to remotely access and manage systems over an encrypted connection.

---

# Purpose

SSH enables you to:

- Log in to a remote machine securely.
- Execute commands remotely.
- Transfer files securely.
- Manage servers over a network.

---

# Default Port

```text
22
```

---

# Example Connection

```bash
ssh user@192.168.1.10
```

This command attempts to establish an SSH connection to the remote host using the specified username.

---

# Authentication

SSH supports two common authentication methods:

- Username and Password
- SSH Keys

---

## SSH Keys

Instead of using a password, SSH can authenticate users with key pairs.

A common private key file is:

```text
id_rsa
```

This method is generally more secure than password authentication.

---

# SSH Enumeration with Metasploit

Metasploit provides several modules for gathering information and testing SSH services.

---

## Identify the SSH Version

### Module

```text
auxiliary/scanner/ssh/ssh_version
```

This module retrieves information such as:

- SSH version
- SSH server software
- Banner information

![[Pasted image 20260514150446.png]]

---

## Brute Force SSH Login

### Module

```text
auxiliary/scanner/ssh/ssh_login
```

This module performs an authentication attack by trying multiple username and password combinations.

It is commonly used to:

- Verify credentials
- Perform brute-force attacks
- Test password security

![[Pasted image 20260514150518.png]]

![[Pasted image 20260514150558.png]]

---

## Enumerate SSH Users

### Module

```text
auxiliary/scanner/ssh/ssh_enumusers
```

This module attempts to identify valid usernames on the target SSH server.

![[Pasted image 20260514150740.png]]

Before running the module, set the following option to:

```text
CHECK_FALSE = false
```

This allows the module to continue checking usernames even when the server returns misleading authentication responses.

![[Pasted image 20260514150817.png]]

```
# SSH (Secure Shell)

```
Secure Shell
```

---

# Function

SSH allows you to:

```
Remotely access and control a system securely
```

---

# Default Port

```
22
```

---

# Connection Example

```
ssh user@192.168.1.10
```

---

## Authentication

Login methods:

- Username / Password
- SSH keys

---

## SSH Keys

Files such as:

```
id_rsa
```

are used instead of passwords.

---

# SSH Enumeration with Metasploit

## SSH version detection

```
auxiliary/scanner/ssh/ssh_version
```

Used to:

```
Identify SSH server version
```

---

## SSH login brute force

```
auxiliary/scanner/ssh/ssh_login
```

Used for:

```
Brute force / login attempts against SSH
```

---

## SSH user enumeration

```
auxiliary/scanner/ssh/ssh_enumusers
```

Used to:

```
Find valid usernames on SSH service
```

Note:

- Set enumeration option to `false` if needed for stability
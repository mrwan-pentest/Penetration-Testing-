## What is GPG2John?

`gpg2john` is a tool that comes as part of the John the Ripper suite.

Its main purpose is:

```
Convert GPG/PGP encrypted files into a password hash format
```

that can be understood and attacked by:

```
John the Ripper
```

In other words:

GPG/PGP files are encrypted using a password. John the Ripper cannot directly crack the original GPG file, so `gpg2john` extracts the password-related information and converts it into a hash format that John can process.

---

# What Are GPG and PGP?

Before understanding `gpg2john`, we need to understand the files it works with.

## PGP (Pretty Good Privacy)

PGP is an encryption system used to protect files, emails, and sensitive information.

It provides:

- Encryption
- Data protection
- Digital signatures

---

## GPG (GNU Privacy Guard)

GPG is the open-source implementation of PGP.

It is commonly used on Linux systems to:

- Encrypt files
- Decrypt files
- Manage encryption keys
- Verify digital signatures

Example encrypted file:

```
backup.pgp
```

This file cannot be opened without the correct private key and password.

---

# Why Do We Use gpg2john?

During a penetration test or CTF, you may find:

- Encrypted backup files
- Private GPG key files
- PGP encrypted documents

Example:

```
backup.pgp
private-key.asc
secret.gpg
```

The challenge is that the file is protected with a password.

`gpg2john` helps by extracting the password hash, allowing you to attempt password recovery using John the Ripper.

---

# Basic Workflow

The general process is:

```
Encrypted GPG/PGP File
        |
        |
        v
     gpg2john
        |
        |
        v
   Extracted Hash
        |
        |
        v
 John the Ripper
        |
        |
        v
 Recovered Password
        |
        |
        v
 Import Key and Decrypt File
```

---

# Step 1 — Convert GPG File to Hash

First, use `gpg2john` to extract the hash from the encrypted file.

Example:

```
gpg2john backup.pgp > hash.txt
```

## Explanation

|Part|Description|
|---|---|
|`gpg2john`|Converts GPG/PGP information into John format|
|`backup.pgp`|Encrypted GPG/PGP file|
|`hash.txt`|File containing the extracted hash|

The output file can now be used with John the Ripper.

---

# Step 2 — Crack the Hash Using John

After extracting the hash:

```
john hash.txt
```

John will attempt to recover the original password.

Using a wordlist:

```
john --wordlist=/usr/share/wordlists/rockyou.txt hash.txt
```

After successful cracking, John will display the recovered password.

---

# Step 3 — Import the GPG Key

After obtaining the password, import the GPG key file.

Command:

```
gpg --import filename
```

## Purpose

Imports the private GPG key into the local GPG keyring.

Example:

```
gpg --import private.key
```

---

# Step 4 — Verify Imported Keys

To check the available secret keys:

```
gpg --list-secret-keys
```

## Purpose

Displays private keys stored in the GPG keyring.

Example output:

```
sec   rsa4096
uid   User Name
```

If the key appears, the import was successful.

---

# Step 5 — Decrypt the File

After importing the key, decrypt the encrypted file:

```
gpg --decrypt backup.pgp
```

## Purpose

Decrypts the GPG/PGP encrypted file using the imported private key.

The command will request the password that was recovered earlier.

---

# Common Usage Scenarios

## 1. Recovering Passwords From Encrypted Backups

A common scenario is finding:

```
backup.pgp
```

containing sensitive information.

The process:

1. Extract the hash.
2. Crack the password.
3. Import the key.
4. Decrypt the backup.

---

## 2. CTF Challenges

In Capture The Flag environments, you may find:

- Encrypted documents.
- Private keys.
- Password-protected backups.

`gpg2john` is commonly used to recover the password and access the hidden flag.

---

## 3. Penetration Testing

During authorized assessments, encrypted files may be discovered during:

- Post Exploitation
- File analysis
- Credential discovery

The tester may analyze whether weak passwords protect sensitive encryption keys.

---

# Important Files Related to GPG

|File Type|Description|
|---|---|
|`.gpg`|GPG encrypted file|
|`.pgp`|PGP encrypted file|
|`.asc`|ASCII armored key or encrypted data|
|Private Key|Required for decryption|

---

# Summary

`gpg2john` is a utility included with John the Ripper that converts GPG/PGP encrypted files into crackable hash formats.

Main purpose:

```
Extract GPG password hash → Crack password with John → Import key → Decrypt file
```

Common workflow:

```
gpg2john backup.pgp > hash.txt

john --wordlist=/usr/share/wordlists/rockyou.txt hash.txt

gpg --import private.key

gpg --list-secret-keys

gpg --decrypt backup.pgp
```

It is mainly used in:

- CTFs
- Password recovery
- Authorized penetration testing
- Analysis of encrypted files
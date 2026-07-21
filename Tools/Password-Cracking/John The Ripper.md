# John the Ripper

## What is John the Ripper?

`John the Ripper` (commonly called `John`) is a password auditing and password recovery tool used to test the strength of passwords and recover passwords from password hashes.

The main idea behind John is:

```
Password → Hash
```

John attempts to reverse this process by trying different password candidates until it finds a password that produces the same hash.

Example:

```
Original Password:
Password123

Hash:
5f4dcc3b5aa765d61d8327deb882cf99
```

John tries possible passwords, generates their hashes, and compares them with the target hash.

If the hashes match:

```
Password Found
```

---

# Where Is John Used?

John is commonly used during authorized security assessments after obtaining password hash files.

Examples:

## Linux Password Hashes

```
/etc/shadow
```

The `/etc/shadow` file stores encrypted password hashes for Linux users.

---

## Windows Password Hashes

```
SAM Database
```

The SAM database stores local Windows account password hashes.

---

## Other Hash Sources

John can also work with:

- Extracted database hashes
- Encrypted file hashes
- Application password hashes
- Private key password hashes

---

# Basic Usage

The simplest syntax:

```
john hashes.txt
```

## Purpose

Attempts to crack all password hashes contained in the specified file.

Example:

```
john password_hashes.txt
```

John automatically tries suitable cracking methods based on the detected hash format.

---

# Using a Wordlist

Command:

```
john --wordlist=/usr/share/wordlists/rockyou.txt hashes.txt
```

## Purpose

Uses a password dictionary file to test possible passwords.

Example:

Wordlist:

```
password
admin
letmein
Password123
```

John tests each word against the target hashes.

---

# Displaying Cracked Passwords

Command:

```
john --show hashes.txt
```

## Purpose

Displays passwords that John has already recovered.

Example output:

```
user:Password123
```

---

# Identifying Hash Types

Before cracking a hash, identifying its type is important because each hash algorithm requires the correct cracking format.

Common Linux password hash identifiers:

|Prefix|Hash Type|
|---|---|
|`$1$`|MD5 Crypt|
|`$5$`|SHA256 Crypt|
|`$6$`|SHA512 Crypt|

Example:

```
$6$abc123$........
```

This indicates:

```
SHA512 Crypt
```

---

# Specifying Hash Format Manually

Sometimes John may not automatically identify the hash type.

You can specify it manually:

```
john --format=sha512crypt hashes.txt
```

## Purpose

Forces John to use the specified hash format.

---

# Saving and Restoring Sessions

Password cracking can take a long time.

If you stop John, you can continue from where it stopped.

Command:

```
john --restore
```

## Purpose

Restores the previous cracking session.

---

# John Attack Modes

John supports different attack modes depending on the available information.

---

# 1. Single Crack Mode

Single mode uses information related to the username and account details to generate password guesses.

Command:

```
john hashes.txt
```

John may use:

- Username information
- Account names
- Common password patterns

Example:

If the username is:

```
john
```

John may try:

```
john123
John2024
johnpassword
```

---

# 2. Wordlist Mode

Wordlist mode uses a predefined password dictionary.

Command:

```
john --wordlist=rockyou.txt hashes.txt
```

## Purpose

Tests passwords from a wordlist against the target hashes.

This is one of the most commonly used methods during penetration testing.

---

# 3. Incremental Mode

Incremental mode performs a brute-force style attack.

Command:

```
john --incremental hashes.txt
```

## Purpose

Attempts all possible character combinations.

Example:

```
a
b
c
aa
ab
ac
...
```

This method can eventually find passwords but is usually very slow because the number of possible combinations increases rapidly.

---

# Common John Workflow

A typical password cracking workflow:

```
Obtain Hashes
      |
      v
Identify Hash Type
      |
      v
Choose Attack Method
      |
      v
Run John
      |
      v
Display Results
```

Example:

```
john --wordlist=/usr/share/wordlists/rockyou.txt hashes.txt

john --show hashes.txt
```

---

# John the Ripper vs Hashcat

|Feature|John the Ripper|Hashcat|
|---|---|---|
|Main Use|Password auditing and recovery|High-performance password cracking|
|Hardware|CPU mainly, supports GPU|Strong GPU acceleration|
|Usage|Simple and automatic|More control over attack methods|
|Best For|Quick cracking and hash analysis|Large-scale cracking|

---

# Summary

`John the Ripper` is a powerful password auditing tool used to recover passwords from hashes.

Main capabilities:

- Crack Linux password hashes.
- Crack Windows password hashes.
- Test password strength.
- Use wordlists.
- Perform brute-force attacks.
- Support multiple hash formats.

Common commands:

```
john hashes.txt

john --wordlist=/usr/share/wordlists/rockyou.txt hashes.txt

john --show hashes.txt
```

John is widely used in:

- Penetration testing
- CTF challenges
- Digital forensics
- Password security assessments
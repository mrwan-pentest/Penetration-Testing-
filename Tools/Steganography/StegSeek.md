
## Overview

**StegSeek** is a fast steganography password cracker and extraction tool designed for **Steghide**.

It is primarily used during:

- CTF Challenges
- Penetration Testing
- Digital Forensics

StegSeek can quickly determine whether a file contains hidden data and recover it by performing a dictionary attack against the embedded password.

Unlike Steghide, which only extracts hidden data when the correct password is known, StegSeek automates the password-cracking process, making it extremely useful during security assessments.

---

# What is Steganography?

**Steganography** is the practice of hiding data inside another file without changing its visible appearance.

For example, a normal image may secretly contain:

- Passwords
- Source code
- ZIP archives
- Private keys
- Text files
- Flags

To anyone viewing the image, it appears completely normal.

---

# Supported File Types

StegSeek works with files created using **Steghide**, which commonly embeds data inside:

- JPEG (.jpg)
- JPEG (.jpeg)
- BMP (.bmp)
- AU Audio (.au)
- WAV Audio (.wav)

---

# Installation

## Debian / Ubuntu / Kali

```bash
sudo apt update
sudo apt install stegseek
```

---

# Verify Installation

```bash
stegseek --help
```

or

```bash
stegseek --version
```

---

# Basic Syntax

```bash
stegseek <image> <wordlist>
```

General format:

```bash
stegseek image.jpg rockyou.txt
```

---

# How StegSeek Works

The process is straightforward:

1. Read the image.
2. Detect whether Steghide data exists.
3. Try passwords from the supplied wordlist.
4. If the correct password is found:
   - Decrypt the hidden content.
   - Extract the embedded file.

---

# Common Usage

## Crack a Steghide Password

```bash
stegseek image.jpg rockyou.txt
```

Example:

```bash
stegseek secret.jpg /usr/share/wordlists/rockyou.txt
```

---

## Extract Hidden Data (Password Known)

If you already know the password, you can specify it directly:

```bash
stegseek image.jpg -p password
```

Example:

```bash
stegseek secret.jpg -p letmein
```

---

## Extract Output to a Specific File

```bash
stegseek image.jpg rockyou.txt -xf output.txt
```

---

## Quiet Mode

Suppress unnecessary output.

```bash
stegseek image.jpg rockyou.txt -q
```

---

# Common Workflow During CTFs

```text
Receive an image
        │
        ▼
Run StegSeek
        │
        ▼
Password Cracked
        │
        ▼
Extract Hidden File
        │
        ▼
Inspect Extracted Content
        │
        ▼
Recover Credentials / Flag / ZIP Archive / Source Code
```

---

# Example

Suppose we have:

```text
secret.jpg
```

Run:

```bash
stegseek secret.jpg /usr/share/wordlists/rockyou.txt
```

Example output:

```text
StegSeek 0.6

Found passphrase: password123

Extracting to "secret.txt".
```

Now:

```text
secret.txt
```

has been extracted successfully.

---

# Difference Between Steghide and StegSeek

| Feature | Steghide | StegSeek |
|----------|----------|----------|
| Hide files | ✅ | ❌ |
| Extract hidden files | ✅ | ✅ |
| Crack password | ❌ | ✅ |
| Dictionary attack | ❌ | ✅ |
| Extremely fast | ❌ | ✅ |

---

# Common Options

| Option | Description |
|---------|-------------|
| `-p` | Specify the password directly. |
| `-xf` | Specify the output filename. |
| `-q` | Quiet mode. |
| `--help` | Display help information. |
| `--version` | Show the installed version. |

---

# Real-World Use Cases

StegSeek is commonly used to:

- Recover hidden files from images.
- Crack Steghide passwords.
- Solve CTF steganography challenges.
- Extract credentials hidden inside images.
- Recover embedded ZIP archives.
- Analyze suspicious media during digital forensic investigations.

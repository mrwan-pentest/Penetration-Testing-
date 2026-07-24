
# Binwalk

## What is Binwalk?

**Binwalk** is an open-source firmware analysis tool used to identify, extract, and analyze embedded files and data inside binary files.

It is widely used during:

- Firmware Analysis
- Reverse Engineering
- Digital Forensics
- Embedded Device Security
- IoT Security Assessments
- CTF Challenges

---

# What Can Binwalk Detect?

Binwalk can identify embedded:

- ZIP archives
- GZIP files
- TAR archives
- SquashFS
- CramFS
- JFFS2
- UBI Images
- Kernel Images
- Bootloaders
- Executables
- Certificates
- Compressed data
- File signatures

---

# Typical Use Cases

- Analyze router firmware
- Analyze IoT devices
- Extract hidden files
- Recover embedded files
- Discover compressed data
- Reverse engineer firmware images
- CTF Steganography & Forensics challenges

---

# Installation

## Debian / Ubuntu / Kali Linux

```bash
sudo apt update
sudo apt install binwalk
```

---

# Verify Installation

```bash
binwalk --version
```

---

# General Syntax

```bash
binwalk [OPTIONS] <file>
```

---

# Scan a File

```bash
binwalk firmware.bin
```

## Function

Scans the binary file and identifies known file signatures.

Example output:

```
DECIMAL       HEXADECIMAL     DESCRIPTION

0             0x0             uImage Header
65536         0x10000         SquashFS filesystem
```

---

# Extract Embedded Files

```bash
binwalk -e firmware.bin
```

## Function

Automatically extracts detected embedded files.

A new directory is created:

```
_firmware.bin.extracted/
```

containing all extracted files.

---

# Scan Recursively

```bash
binwalk -Me firmware.bin
```

## Function

Performs recursive extraction.

If extracted files contain additional embedded files, Binwalk extracts them automatically.

This is one of the most commonly used options during firmware analysis.

---

# Show Entropy Graph

```bash
binwalk -E firmware.bin
```

## Function

Displays the entropy of the binary file.

High entropy usually indicates:

- Compression
- Encryption

Low entropy often indicates:

- Plain text
- Uncompressed data

Useful for identifying hidden or encrypted sections.

---

# Extract Specific Signature

```bash
binwalk -D 'zip archive:zip' firmware.bin
```

## Function

Extracts only ZIP archives found inside the binary.

---

# Search for Strings

```bash
strings firmware.bin
```

Although not a Binwalk command, it is commonly used alongside Binwalk to discover:

- Passwords
- URLs
- API Keys
- Usernames
- Interesting text

---

# Analyze a Firmware Image

```bash
binwalk firmware.bin
```

↓

```bash
binwalk -Me firmware.bin
```

↓

Navigate to:

```bash
cd _firmware.bin.extracted
```

↓

Inspect the extracted files.

---

# Common Options

| Option | Description |
|----------|-------------|
| `-e` | Extract embedded files |
| `-M` | Recursive scan |
| `-eM` | Extract recursively |
| `-E` | Entropy analysis |
| `-D` | Extract only specific signatures |
| `-B` | Signature scan only |
| `-v` | Verbose output |
| `--help` | Show help menu |

---

# Typical Workflow

1. Scan the firmware

```bash
binwalk firmware.bin
```

2. Extract embedded files

```bash
binwalk -e firmware.bin
```

3. If nested archives exist

```bash
binwalk -Me firmware.bin
```

4. Inspect extracted directories

```bash
ls
```

```bash
cd _firmware.bin.extracted
```

5. Analyze the contents

---

# Example

Firmware image:

```
router_firmware.bin
```

Scan it:

```bash
binwalk router_firmware.bin
```

Extract everything:

```bash
binwalk -Me router_firmware.bin
```

Browse extracted files:

```bash
cd _router_firmware.bin.extracted
```

---

# Advantages

- Extremely fast
- Supports hundreds of file signatures
- Automatic extraction
- Recursive extraction
- Excellent for firmware analysis
- Ideal for IoT penetration testing
- Commonly used in CTF challenges

---

# Limitations

- Does not decrypt encrypted data
- Cannot analyze unknown proprietary formats without plugins
- Some extracted files may require manual analysis

---

# Related Tools

- Foremost
- Steghide
- Stegseek
- ExifTool
- Strings
- File
- Hexdump
- xxd

---

# Notes

- `binwalk -Me` is the most commonly used command during firmware analysis.
- Always inspect the extracted directory after running Binwalk.
- Combine Binwalk with `strings`, `file`, and `hexdump` for deeper analysis.
- Binwalk is considered one of the essential tools for Firmware Analysis, IoT Security, Reverse Engineering, and Digital Forensics.
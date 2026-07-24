# Steghide

## What is Steghide?

**Steghide** is an open-source steganography tool used to hide or extract data inside image and audio files without noticeably changing the original file.

It is commonly used during:

- CTF challenges
- Digital Forensics
- Steganography challenges
- Red Team and Penetration Testing labs

---

# Supported File Formats

Steghide supports embedding data into:

- JPEG (.jpg)
- BMP (.bmp)
- WAV (.wav)
- AU (.au)

---

# Installation

## Debian / Ubuntu / Kali Linux

```bash
sudo apt update
sudo apt install steghide
```

---

# Verify Installation

```bash
steghide --version
```

---

# General Syntax

```bash
steghide [OPTIONS]
```

---

# Embed a File

Hide a secret file inside an image.

```bash
steghide embed -cf image.jpg -ef secret.txt
```

### Options

| Option | Description |
|---------|-------------|
| `embed` | Embed data into a carrier file |
| `-cf` | Cover file (image or audio) |
| `-ef` | File to hide |

---

# Embed Without Encryption

```bash
steghide embed -cf image.jpg -ef secret.txt -e none
```

---

# Extract Hidden Data

```bash
steghide extract -sf image.jpg
```

### Options

| Option | Description |
|---------|-------------|
| `extract` | Extract hidden data |
| `-sf` | Stego file |

If a passphrase was used during embedding, Steghide will prompt you to enter it.

---

# Display Embedded Information

```bash
steghide info image.jpg
```

This command displays:

- Whether hidden data exists
- Embedded file name
- File size
- Encryption algorithm
- Compression algorithm

---

# Specify Output Directory

```bash
steghide extract -sf image.jpg -xf output.txt
```

---

# Common Options

| Option | Description |
|---------|-------------|
| `embed` | Hide a file |
| `extract` | Extract hidden data |
| `info` | Show embedded information |
| `-cf` | Cover file |
| `-ef` | File to embed |
| `-sf` | Stego file |
| `-xf` | Extracted output file |
| `-e none` | Disable encryption |

---

# Typical Workflow

1. Inspect the image

```bash
steghide info image.jpg
```

2. Extract hidden data

```bash
steghide extract -sf image.jpg
```

3. Enter the passphrase (if required)

4. Read the extracted file

```bash
cat secret.txt
```

---

# Example

Embed a text file:

```bash
steghide embed -cf cat.jpg -ef flag.txt
```

Extract it later:

```bash
steghide extract -sf cat.jpg
```

---

# Use Cases

- CTF Challenges
- Steganography Challenges
- Digital Forensics
- Malware Analysis
- Red Team Assessments

---

# Advantages

- Easy to use
- Supports encryption
- Supports compression
- Does not noticeably alter image quality
- Widely available on Linux distributions

---

# Limitations

- Supports only a limited number of file formats
- Cannot detect hidden files automatically
- Requires the correct passphrase if encryption is enabled
- Less effective against heavily compressed or modified files

---

# Related Tools

- Stegseek
- Zsteg
- Binwalk
- ExifTool
- Foremost
- Strings

---

# Notes

- Always check images with `steghide info` during CTFs.
- If extraction requests a passphrase, try common passwords or use tools such as **Stegseek** for dictionary attacks.
- Steghide is one of the most frequently encountered steganography tools in Capture The Flag competitions.
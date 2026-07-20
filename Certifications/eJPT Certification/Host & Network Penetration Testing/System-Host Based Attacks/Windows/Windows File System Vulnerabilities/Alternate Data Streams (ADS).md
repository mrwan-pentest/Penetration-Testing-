# Alternate Data Streams (ADS)

## What is ADS?

Alternate Data Streams (ADS) is a feature in the NTFS file system that allows a single file to contain additional hidden data streams.

This means a file is not limited to storing only one piece of content.

---

# The Concept

Normally, you have a regular file:

```
note.txt
```

Containing:

```
hello
```

However, in NTFS, additional hidden content can be attached to the same file:

```
note.txt:hidden
```

This hidden stream does not appear when using:

```
dir
```

---

# Why Is ADS Important from a Security Perspective?

Attackers can use ADS to:

- Hide Payloads
- Hide scripts
- Hide data
- Establish Persistence

inside files that appear normal.

---

# Is ADS a New File?

No.

ADS is not a separate file.

It is a hidden stream attached to an existing file.

---

# Where Does ADS Work?

ADS works only on:

```
NTFS
```

---

# Does ADS Work on FAT32?

No.

ADS is not supported by the FAT32 file system.

---

# Checking the File System Type

To determine whether a drive uses NTFS, run:

```
fsutil fsinfo volumeinfo C:
```

The output will show:

```
File System Name : NTFS
```

---

# Creating an ADS

## Step 1: Create a Normal File

Create a regular file:

```
echo hello > file.txt
```

---

## Step 2: Create a Hidden Stream

Create an additional hidden stream:

```
notepad file.txt:hidden.txt
```

Windows will ask:

```
Do you want to create?
```

Select **Yes**.

---

## Step 3: Add Hidden Content

Write any content.

Example:

```
this is hidden
```

Then save the file.

---

# What Happened?

Now we have:

```
file.txt
```

but it contains a hidden stream.

---

# Normal File Listing

If we check the directory normally:

```
dir
```

The hidden stream will not appear.

The output will only show:

```
file.txt
```

---

# Reading ADS Content

To read the hidden stream:

```
notepad file.txt:hidden.txt
```

or:

```
more < file.txt:hidden.txt
```

---

# Detecting ADS

## Using dir /r

To display Alternate Data Streams:

```
dir /r
```

The output will show:

```
file.txt:hidden.txt:$DATA
```

---

# What is $DATA?

`$DATA` represents the main data stream type used by the NTFS file system.

---

# Hiding a File Inside ADS

## Step 1: Create a Test Payload

Example:

```
calc.exe
```

---

## Step 2: Copy the File into an ADS

Store the payload inside a hidden stream:

```
type calc.exe > file.txt:calc.exe
```

---

# Result

The payload is now hidden inside:

```
file.txt
```

---

# Executing a Payload from ADS

Older Windows systems allowed execution using:

```
start .\file.txt:calc.exe
```

---

# Modern Windows Behavior

In modern Windows versions, many direct ADS execution techniques are blocked.

Therefore, ADS is now commonly used for:

- Hiding files
- Persistence techniques
- Basic bypass techniques
- Forensic evasion techniques

rather than direct payload execution.
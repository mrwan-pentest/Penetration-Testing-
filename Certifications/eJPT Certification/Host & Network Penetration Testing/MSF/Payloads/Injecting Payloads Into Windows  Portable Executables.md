# Embedding a Payload into a Legitimate Program

A payload can be embedded into a legitimate application, such as:

- PuTTY
- VLC
- 7-Zip
- PDF Reader

This technique attempts to make the payload appear as part of a normal executable.

---

# What is a Portable Executable (PE)?

A **Portable Executable (PE)** is the standard executable file format used by Windows.

Examples include:

- `.exe`
- `.dll`

---

# Practical Example

The **`-x`** option specifies the executable file into which the payload will be embedded.

There is also the **`-k`** option, which attempts to preserve the original program's functionality so that it continues to run normally on the victim's machine after the payload is executed.

> **Note:** The `-k` option does not work reliably with every application and may not be compatible with all executable files.

![[Pasted image 20260525011137.png]]
# xfreerdp

## What is xfreerdp?

`xfreerdp` is a Linux-based Remote Desktop client that allows users to:

```
Connect to Windows RDP services
```

It provides functionality similar to:

```
Remote Desktop Connection
```

on Windows, but it can be used from Linux systems such as Kali Linux.

---

# Basic Usage

The general syntax is:

```
xfreerdp /u:username /p:password /v:IP
```

Example:

```
xfreerdp /u:administrator /p:password123 /v:192.168.1.10
```

Options:

|Option|Description|
|---|---|
|`/u`|Specifies the username|
|`/p`|Specifies the password|
|`/v`|Specifies the target IP address or hostname|

---

# Pass-the-Hash with xfreerdp

`xfreerdp` supports authentication using an NTLM Hash instead of a password.

This technique is known as:

```
Pass-the-Hash
```

---

## Example

```
xfreerdp /u:administrator /pth:HASH /v:TARGET
```

Options:

|Option|Description|
|---|---|
|`/u`|Username|
|`/pth`|NTLM Hash authentication|
|`/v`|Target Windows machine|

This allows authentication using the NTLM Hash without knowing the original password.

---

# Ignoring RDP Certificate Warnings

Sometimes RDP connections fail because of certificate validation issues.

To ignore certificate errors:

```
xfreerdp /u:username /p:password /v:IP /cert:ignore
```

Option:

```
/cert:ignore
```

allows the client to ignore certificate verification problems.

---

# Full Screen Mode

To open the RDP session in full-screen mode:

```
xfreerdp /u:username /p:password /v:IP /f
```

Option:

```
/f
```

enables full-screen display.

---

# Setting Screen Resolution

To specify a custom resolution:

```
xfreerdp /u:username /p:password /v:IP /size:1920x1080
```

Option:

```
/size
```

defines the display resolution.

---

# Dynamic Resolution

To enable automatic resizing when changing the window size:

```
xfreerdp /u:username /p:password /v:IP /dynamic-resolution
```

Option:

```
/dynamic-resolution
```

allows the RDP session resolution to adapt dynamically.

---

# Summary

`xfreerdp` is a powerful Linux RDP client commonly used during Windows penetration testing and administration.

Important features:

- Remote Desktop access to Windows systems.
- Password-based authentication.
- Pass-the-Hash authentication.
- Certificate bypass options.
- Full-screen mode.
- Dynamic resolution support.

Common syntax:

```
xfreerdp /u:<username> /p:<password> /v:<target>
```
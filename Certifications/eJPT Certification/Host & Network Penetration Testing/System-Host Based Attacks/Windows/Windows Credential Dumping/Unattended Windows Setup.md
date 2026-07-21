# Unattended Windows Setup

# What is Unattended Windows Setup?

It is:

> A feature used to install Windows automatically.

# Why does this happen?

Because companies sometimes need:

```
To install Windows automatically on a large number of devices
```

Instead of:

- Manual installation.
- Entering the settings every time.

# Here comes Unattended Windows Setup

It means:

```
Automated Windows Installation
```

# How does it work?

They create a configuration file that contains:

- Computer name.
- Language.
- User account.
- Sometimes the Administrator password.

Then Windows reads the file and installs itself automatically.

## The Problem

The configuration files may remain after the installation.

## They may contain:

- Username.
- Password.
- Admin Credentials.

## Common Files

```
C:\Windows\Panther\Unattend.xml
```

```
C:\Windows\Panther\Autounattend.xml
```

## The password may be:

```
Base64 encoded
```

and it is not real encryption.

---

# Lab

After obtaining a:

```
Meterpreter Session
```

we search for:

```
unattend.xml
```

![](Penetration%20Testing/Images/Pasted%20image%2020260519161909.png)

We found it, accessed the path, and transferred it to our machine.

![](Penetration%20Testing/Images/Pasted%20image%2020260519161942.png)

We read the file and noticed that the password was:

```
Base64
```

encoded.

![](Penetration%20Testing/Images/Pasted%20image%2020260519162014.png)

We decoded the password:

![](Penetration%20Testing/Images/Pasted%20image%2020260519162034.png)

Then we logged in using:

```
psexec
```

![](Penetration%20Testing/Images/Pasted%20image%2020260519162052.png)
# SUID

## What is SUID?

Linux provides standard file permissions:

|Permission|Description|
|---|---|
|`r`|Read|
|`w`|Write|
|`x`|Execute|

In addition to these standard permissions, Linux also provides special permissions.

One of them is:

# SUID

---

## What Does SUID Do?

Simply put:

> SUID allows a program to run with the permissions of the file owner rather than the user who executes it.

---

## Example Without SUID

Suppose you are a regular user:

```
student
```

When you execute a program:

↓

The program runs only with **your own privileges**.

---

## Example With SUID

Suppose a program is owned by:

```
root
```

and the SUID permission is enabled.

↓

Any user who executes the program

↓

The program runs with **root privileges** instead of the user's privileges.

---

## Why Does Linux Provide SUID?

Some programs require root privileges to perform specific tasks.

A common example is the `passwd` command.

When a regular user changes their password:

```
passwd
```

The program must modify:

```
/etc/shadow
```

Since `/etc/shadow` is only writable by root, the `passwd` binary is configured with the SUID permission so it can perform the required operation securely.

---

# Finding SUID Binaries

During Linux Privilege Escalation, one of the first enumeration steps is searching for SUID binaries.

Common commands include:

```
find / -perm -4000 2>/dev/null
```

```
find / -user root -perm /4000 2>/dev/null
```

```
find / -user root -perm -u=s 2>/dev/null
```

```
find / -type f -perm /4000 2>/dev/null
```

---

# Lab

After searching for SUID binaries, we discovered two executable files.

One of them could not be accessed directly, while the second binary was owned by **root** and had the **SUID** permission enabled.

![](Penetration%20Testing/Images/Pasted%20image%2020260521014249.png)

---

Next, we used the `strings` command to inspect readable strings embedded inside the SUID binary.

![](Penetration%20Testing/Images/Pasted%20image%2020260521014428.png)

---

The output revealed that the binary attempts to execute another executable that we were unable to access directly.

![](Penetration%20Testing/Images/Pasted%20image%2020260521014513.png)

---

We then removed the original executable and replaced it with our own binary that spawns a shell.

Since the `welcome` binary executes this program internally while running with **root** privileges through SUID, our malicious binary was executed as **root**.

![](Penetration%20Testing/Images/Pasted%20image%2020260521014628.png)

---

Finally, we used the `cp` command to replace the original executable with our modified version.

When the `welcome` binary was executed, it launched our replacement binary, resulting in a **root shell** and successful Privilege Escalation.
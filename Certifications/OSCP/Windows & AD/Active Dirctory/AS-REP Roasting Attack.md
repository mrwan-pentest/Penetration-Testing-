## Overview

**AS-REP Roasting** is a **Kerberos attack** that targets Active Directory accounts where **Kerberos Preauthentication** is disabled.

Normally, before the Domain Controller returns an **AS-REP** response, the user must prove knowledge of their password through Kerberos Preauthentication.

However, if the account has:

```
Do not require Kerberos preauthentication
```

enabled, the Domain Controller can return an **AS-REP response without requiring preauthentication**.

This response contains encrypted data that can be extracted as an **AS-REP hash** and then attacked **offline** using a password-cracking tool such as **Hashcat**.

The important point is that we do **not** need the user's password to request the AS-REP. We only need a valid username and a Domain Controller.

---

# Lab

## Step 1: Identify the Domain

First, we identify the target's **Domain**.

We can use **NetExec (`nxc`)** to enumerate the SMB service:

```
nxc smb 192.168.227.139
```

![](../../../../Images/Pasted%20image%2020260928004045.png)

The output provides information about the target, including the **Domain**.

---

## Step 2: Identify a Vulnerable User

After identifying the Domain, we need to obtain a valid username through enumeration or another method.

If the user account has the following setting enabled:

```
Do not require Kerberos preauthentication
```

the account may be vulnerable to **AS-REP Roasting**.

The reason is that the Domain Controller will allow us to request an **AS-REP response without providing Kerberos Preauthentication**.

We can then extract the returned encrypted material and use it for offline password cracking.

---

## Step 3: Obtain the AS-REP Hash

We use the **GetNPUsers** script from **Impacket** to request the AS-REP response.

```
impacket-GetNPUsers -dc-ip 192.168.227.139 lab.local/user1 -no-pass
```

Here:

- `-dc-ip` — Specifies the IP address of the Domain Controller.
- `lab.local/user1` — Specifies the Domain and username.
- `-no-pass` — Performs the request without providing a password.

If the account does not require Kerberos Preauthentication, we can receive an **AS-REP hash**.

![](../../../../Images/Pasted%20image%2020260928004332.png)

The returned hash can now be saved and used for **offline password cracking**.

---

## Step 4: Crack the Hash

After obtaining the AS-REP hash, we attempt to crack it using **Hashcat**.

For **AS-REP Roasting**, Hashcat uses mode:

```
18200
```

We can then use a wordlist such as `rockyou.txt` to attempt to recover the user's password.

![](../../../../Images/Pasted%20image%2020260928004424.png)

The important concept here is that the cracking happens **offline**.

We are no longer communicating with the Domain Controller while testing passwords. Hashcat performs the password guesses locally against the obtained hash.

---

# If We Don't Know the Username

If we do not have a known username, we can provide **GetNPUsers** with a wordlist containing possible usernames.

```
impacket-GetNPUsers -dc-ip 192.168.227.139 lab.local/ -usersfile /usr/share/metasploit-framework/data/wordlists/unix_users.txt -no-pass
```

`-usersfile` tells **GetNPUsers** to test the usernames contained in the specified wordlist.

The goal is to find a valid Domain account that has **Kerberos Preauthentication disabled**.

![](../../../../Images/Pasted%20image%2020260928004631.png)

If a vulnerable account is found, **GetNPUsers** can return its AS-REP hash, which can then be passed to Hashcat for offline cracking.

---

# Attack Flow

```
Identify Domain
      ↓
Obtain / Enumerate Usernames
      ↓
Find Account with Preauthentication Disabled
      ↓
GetNPUsers
      ↓
Obtain AS-REP Hash
      ↓
Hashcat (18200)
      ↓
Attempt to Recover Password
```

## Key Takeaway

**AS-REP Roasting** abuses accounts that do not require **Kerberos Preauthentication**.

The attack does not require the user's password initially. We use the username to request an **AS-REP response**, obtain the corresponding hash, and then attempt to crack it **offline**.
# SMTP (Simple Mail Transfer Protocol)

```
Simple Mail Transfer Protocol
```

---

# Function

SMTP is used for:

```
Sending emails
```

between:

- Mail clients
- Mail servers

---

# Common Ports

|Port|Usage|
|---|---|
|25|Standard SMTP|
|465|SMTPS (SSL/TLS)|
|587|SMTP Submission|

---

# Does SMTP receive emails?

Usually **no**.

SMTP is mainly used for:

```
Sending emails only
```

Email receiving is typically handled by:

- IMAP
- POP3

---

# How SMTP works

The client sends commands like:

```
HELOMAIL FROMRCPT TODATA
```

---

# Example

```
MAIL FROM: attacker@test.comRCPT TO: admin@test.com
```

---

# What SMTP can reveal

SMTP servers may leak:

- Valid usernames
- Server information
- Mail configuration
- Open relay misconfigurations
- Active accounts

---

# SMTP Enumeration with Metasploit

## SMTP version detection

```
auxiliary/scanner/smtp/smtp_version
```

Used to:

```
Identify SMTP server version
```

---

## SMTP user enumeration

```
auxiliary/scanner/smtp/smtp_enum
```

Used to:

```
Enumerate valid usernames on the SMTP server
```

![](Penetration%20Testing/Images/Pasted%20image%2020260514160819.png)

## Then we will use it for:

- SSH
- FTP
- Web Login
- Password Attacks

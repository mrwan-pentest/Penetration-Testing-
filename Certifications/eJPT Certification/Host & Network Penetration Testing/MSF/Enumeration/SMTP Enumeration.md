
# SMTP (Simple Mail Transfer Protocol)

SMTP stands for:

```text
Simple Mail Transfer Protocol
```

It is the standard protocol used for sending emails between mail clients and mail servers.

---

# Purpose

SMTP is responsible for:

- Sending emails
- Relaying emails between mail servers

It is **not** typically used to receive emails.

Receiving emails is usually handled by:

- POP3
- IMAP

---

# Common Ports

| Port | Purpose |
|------|---------|
| 25 | Standard SMTP |
| 465 | SMTPS (SMTP over SSL/TLS) |
| 587 | SMTP Submission (Authenticated SMTP) |

---

# How SMTP Works

SMTP communication consists of a sequence of commands exchanged between the client and the mail server.

Common commands include:

```text
HELO
MAIL FROM
RCPT TO
DATA
```

### Example

```text
MAIL FROM: attacker@test.com
RCPT TO: admin@test.com
```

The client identifies the sender, specifies the recipient, and then sends the email content.

---

# Why is SMTP Interesting During Enumeration?

SMTP servers can sometimes disclose useful information, including:

- Valid usernames
- Mail server version
- Server configuration
- Open Relay vulnerabilities
- Existing email accounts

This information can be valuable during the reconnaissance phase of a penetration test.

---

# SMTP Enumeration with Metasploit

## Identify the SMTP Version

### Module

```text
auxiliary/scanner/smtp/smtp_version
```

This module retrieves information about the SMTP service, including:

- SMTP server version
- Banner information
- Mail server software

---

## Enumerate SMTP Users

### Module

```text
auxiliary/scanner/smtp/smtp_enum
```

This module performs:

```text
Username Enumeration
```

It attempts to identify valid usernames by interacting with the SMTP server.

![[Pasted image 20260514160819.png]]

Discovered usernames can later be used in attacks against other services, such as:

- SSH
- FTP
- Web Login
- Password Brute Force Attacks

```
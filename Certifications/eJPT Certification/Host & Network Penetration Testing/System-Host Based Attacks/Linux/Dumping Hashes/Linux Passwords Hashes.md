# Linux Password Hashes

## Overview

In Linux systems, user account information is stored in system files, while passwords are never stored in plaintext. Instead, they are stored as cryptographic hashes to help protect user credentials.

A password hash is a one-way representation of a password. During authentication, the operating system hashes the password entered by the user and compares it to the stored hash rather than comparing the plaintext password itself.

## Where Are Password Hashes Stored?

Linux stores password hashes in the following file:

```text
/etc/shadow
```

This file is accessible only to privileged users and contains the password hashes along with additional password policy information, such as password expiration and account aging.

---

# Lab

## Step 1: Upgrade the Shell to a Meterpreter Session

After obtaining a shell on the target system, we upgraded it to a Meterpreter session to gain access to additional post-exploitation capabilities provided by Metasploit.

```text
sessions -u <SESSION_ID>
```

Alternatively, Metasploit provides a dedicated post-exploitation module for extracting password hashes.

![[Pasted image 20260521022745.png]]

## Step 2: Start the Metasploit Database

Before attempting to crack the collected hashes using Metasploit, the PostgreSQL database service must be running.

We started the database service using:

```bash
service postgresql start
```

## Step 3: Crack the Password Hashes

After starting the database service, we used the appropriate Metasploit module to crack the collected password hashes.

![[Pasted image 20260521022943.png]]
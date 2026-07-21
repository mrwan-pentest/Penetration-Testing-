# Objective

The goal of this lab is to gather information from multiple services, enumerate email accounts through **POP3**, recover several credentials, obtain administrator access to the web application, upload a **Python Reverse Shell**, and finally escalate privileges by exploiting a vulnerable Linux kernel.

---

# Initial Enumeration

We started by scanning the target using **Nmap**.

![](Penetration%20Testing/Images/Pasted%20image%2020260425211121.png)

To gather more information about the exposed services, we performed version detection and executed Nmap scripts.

![](Penetration%20Testing/Images/Pasted%20image%2020260425211316.png)

---

# Analyzing the Website

After visiting the website, we inspected the page source and discovered a JavaScript file.

![](Penetration%20Testing/Images/Pasted%20image%2020260425210025.png)

Inside the JavaScript file, we found:

- A username.
- An encoded password.

The password was HTML encoded, so we searched for an **HTML Decoder** and decoded it.

![](Penetration%20Testing/Images/Pasted%20image%2020260425210202.png)

![](Penetration%20Testing/Images/Pasted%20image%2020260425210215.png)

---

# Accessing the Web Application

We navigated to the login page and authenticated using the recovered credentials.

![](Penetration%20Testing/Images/Pasted%20image%2020260425210350.png)

While reviewing the same JavaScript file, we also discovered another username.

---

# Enumerating the POP3 Service

One of the open ports was running the **POP3** service.

> **POP3 (Post Office Protocol v3)** is a protocol used to retrieve emails from a mail server to a local client.

We performed a brute-force attack against the POP3 service to discover valid credentials.

![](Penetration%20Testing/Images/Pasted%20image%2020260425211011.png)

---

# Reading Emails via POP3

After obtaining valid credentials, we connected to the POP3 service using **Telnet**.

![](Penetration%20Testing/Images/Pasted%20image%2020260425212047.png)

We enumerated the mailbox and inspected the available emails.

![](Penetration%20Testing/Images/Pasted%20image%2020260425212300.png)

One of the emails contained another username and password.

![](Penetration%20Testing/Images/Pasted%20image%2020260425212336.png)

---

# Accessing Another Website

We added the discovered hostname to our **hosts** file.

![](Penetration%20Testing/Images/Pasted%20image%2020260425213951.png)

After accessing the new website, we logged in using the credentials recovered from the email.

![](Penetration%20Testing/Images/Pasted%20image%2020260425213902.png)

Inside the application, we discovered another username.

![](Penetration%20Testing/Images/Pasted%20image%2020260425214103.png)

We also recovered Boris's password.

![](Penetration%20Testing/Images/Pasted%20image%2020260425220427.png)

---

# Enumerating Boris's Mailbox

Using Boris's credentials, we authenticated to the POP3 service again and inspected his mailbox.

![](Penetration%20Testing/Images/Pasted%20image%2020260425220815.png)

The mailbox contained another set of credentials.

![](Penetration%20Testing/Images/Pasted%20image%2020260425221137.png)

---

# Downloading the Attachment

We logged into the newly discovered account.

Inside the mailbox, we found an attachment and downloaded it.

![](Penetration%20Testing/Images/Pasted%20image%2020260425221231.png)

The attachment contained an image.

![](Penetration%20Testing/Images/Pasted%20image%2020260425221517.png)

We opened the image%20in the browser.

![](Penetration%20Testing/Images/Pasted%20image%2020260425221552.png)

After analyzing the image, we extracted a **Base64** string.

![](Penetration%20Testing/Images/Pasted%20image%2020260425221740.png)

Decoding the Base64 string revealed another password.

![](Penetration%20Testing/Images/Pasted%20image%2020260425221845.png)

We tested this password with the **admin** account, and the authentication succeeded.

![](Penetration%20Testing/Images/Pasted%20image%2020260425222525.png)

---

# Uploading a Python Reverse Shell

After obtaining administrator access, we uploaded a Python reverse shell.

![](Penetration%20Testing/Images/Pasted%20image%2020260425223434.png)

We executed the uploaded file.

![](Penetration%20Testing/Images/Pasted%20image%2020260425223527.png)

As a result, we received a reverse shell.

![](Penetration%20Testing/Images/Pasted%20image%2020260425223545.png)

---

# Privilege Escalation

After obtaining an initial shell, we enumerated the system looking for privilege escalation opportunities.

We identified a vulnerable Linux kernel and searched for a matching public exploit.

After transferring the exploit to the target machine, we compiled it.

Since **gcc** was not installed on the target, we used **cc** instead.

Finally, we executed the exploit and successfully obtained **Root** privileges.
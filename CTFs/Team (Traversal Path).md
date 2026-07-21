# Team - TryHackMe Walkthrough

## Overview

The objective of this lab was to exploit a **Path Traversal** vulnerability to obtain sensitive information, recover an SSH private key, gain initial access to the target machine, and finally escalate privileges by abusing a misconfigured **sudo** rule and an insecure **Cron Job** running as root.

During this engagement, we successfully:

- Enumerated the target using Nmap.
- Discovered hidden directories through fuzzing.
- Exploited a Path Traversal vulnerability.
- Retrieved an SSH private key.
- Logged into the target via SSH.
- Escalated privileges to another user using a vulnerable sudo configuration.
- Abused a writable script executed by a root Cron Job.
- Obtained a root shell.

---

# About Path Traversal

**Path Traversal** (also known as **Directory Traversal**) is a vulnerability that allows an attacker to access files outside the intended web directory by manipulating file paths.

For example:

```text
../../../../etc/passwd
```

If the application fails to properly validate user input, an attacker may be able to read sensitive files such as:

- `/etc/passwd`
- `/etc/shadow`
- SSH private keys
- Configuration files
- Application credentials

---


# Initial Enumeration

## Nmap Scan

We started by performing an Nmap scan to identify open ports and running services.

![](Penetration%20Testing/Images/Pasted%20image%2020260717164628.png)

---

## Web Directory Enumeration

Next, we performed directory fuzzing to discover hidden resources.

![](Penetration%20Testing/Images/Pasted%20image%2020260717164640.png)

---

# Discovering the Correct Virtual Host

Browsing to the website displayed the default Apache page.

The source code contained the following note:

```text
Apache2 Ubuntu Default Page: It works! If you see this add 'team.thm' to your hosts
```

![](Penetration%20Testing/Images/Pasted%20image%2020260402115235.png)

This indicated that we needed to configure our local hosts file.

We edited:

```bash
sudo nano /etc/hosts
```

and mapped the target IP address to:

```text
team.thm
```

![](Penetration%20Testing/Images/Pasted%20image%2020260717164939.png)

---

## Fuzzing the New Virtual Host

After adding the virtual host, we repeated directory enumeration against:

```text
team.thm
```

![](Penetration%20Testing/Images/Pasted%20image%2020260402115516.png)

A directory named:

```text
script
```

was discovered.

---

## Discovering Backup Files

We fuzzed this directory again while searching for common backup extensions such as:

- txt
- old
- backup

![](Penetration%20Testing/Images/Pasted%20image%2020260717165416.png)

A text file was discovered.

![](Penetration%20Testing/Images/Pasted%20image%2020260717165450.png)

Its contents included the following note:

```text
# Note to self had to change the extension of the old "script" in this folder, as it has creds in
```

![](Penetration%20Testing/Images/Pasted%20image%2020260717165619.png)

This suggested that an older version of the script still existed.

---

## Recovering the Old Script

We changed the extension to:

```text
script.old
```

and successfully downloaded the file.

![](Penetration%20Testing/Images/Pasted%20image%2020260717165729.png)

Inspecting the script revealed FTP credentials.

![](Penetration%20Testing/Images/Pasted%20image%2020260717165818.png)

---

# FTP Enumeration

We authenticated to the FTP service using the recovered credentials.

Initially, FTP passive mode caused connection issues.

![](Penetration%20Testing/Images/Pasted%20image%2020260717165938.png)

We disabled passive mode using:

```text
passive
```

![](Penetration%20Testing/Images/Pasted%20image%2020260717170139.png)

After connecting successfully, we downloaded the available files.

![](Penetration%20Testing/Images/Pasted%20image%2020260717170231.png)

---

## Discovering Another Virtual Host

One of the downloaded files contained the following message:

```text
I have started coding a new website in PHP for the team to use, this is currently under development. It can be found at ".dev" within our domain.
```

This suggested another virtual host existed.

![](Penetration%20Testing/Images/Pasted%20image%2020260717170400.png)

We added:

```text
dev.team.thm
```

to our hosts file.

![](Penetration%20Testing/Images/Pasted%20image%2020260717173122.png)

---

# Exploiting Path Traversal

After browsing the development site, we found a link that accepted file paths.

![](Penetration%20Testing/Images/Pasted%20image%2020260717171514.png)

Testing the parameter revealed a **Path Traversal** vulnerability.

![](Penetration%20Testing/Images/Pasted%20image%2020260717171619.png)

This allowed arbitrary file reads from the server.

---

## Searching for Sensitive Files

From the previously downloaded note, we knew an SSH private key existed.

We searched for the default SSH configuration paths.

![](Penetration%20Testing/Images/Pasted%20image%2020260615011828.png)

![](Penetration%20Testing/Images/Pasted%20image%2020260717171915.png)

After identifying the correct location, we requested the SSH configuration file through the Path Traversal vulnerability.

![](Penetration%20Testing/Images/Pasted%20image%2020260717172048.png)

The response contained the SSH private key.

![](Penetration%20Testing/Images/Pasted%20image%2020260717172141.png)

Because every line started with a comment character (`#`), we viewed the source using **Ctrl+U** to make the content easier to read.

At the end of the file, we recovered:

- Username: **dale**
- SSH Private Key

![](Penetration%20Testing/Images/Pasted%20image%2020260402115831.png)

---

## Cleaning the Private Key

To restore the private key, we removed the leading `#` characters.

One option was to use **CyberChef** with the **Find and Replace** operation.

![](Penetration%20Testing/Images/Pasted%20image%2020260717172418.png)

We replaced:

```text
#
```

with an empty string.

![](Penetration%20Testing/Images/Pasted%20image%2020260717172536.png)

Alternatively, we could use:

```bash
sed 's/#//' oldfile > newfile
```

After saving the key locally, we restricted its permissions.

![](Penetration%20Testing/Images/Pasted%20image%2020260717172722.png)

---

# Initial Access

Using the recovered private key, we authenticated as user **dale**.

![](Penetration%20Testing/Images/Pasted%20image%2020260717173206.png)

---

# Privilege Escalation

## Sudo Enumeration

We enumerated sudo permissions.

```bash
sudo -l
```

![](Penetration%20Testing/Images/Pasted%20image%2020260717173257.png)

The output showed that we could execute a specific script as another user without requiring a password.

---

## Understanding the Script

Reading the script revealed that it accepted two user-controlled variables before printing them.

![](Penetration%20Testing/Images/Pasted%20image%2020260717173645.png)

One of these variables was passed directly to the **date** command without proper sanitization.

This allowed **command injection**.

We injected:

```text
/bin/bash
```

instead of a valid date argument.

![](Penetration%20Testing/Images/Pasted%20image%2020260717173513.png)

As a result, we obtained a shell as the second user.

---

## Upgrading the Shell

To obtain a fully interactive terminal, we upgraded the shell using:

```bash
python3 -c 'import pty; pty.spawn("/bin/bash")'
```

![](Penetration%20Testing/Images/Pasted%20image%2020260717174053.png)

We successfully obtained the user flag.

![](Penetration%20Testing/Images/Pasted%20image%2020260717174152.png)

---

# Cron Job Privilege Escalation

During post-exploitation enumeration, we reviewed the Bash history.

![](Penetration%20Testing/Images/Pasted%20image%2020260717174819.png)

We discovered a script that appeared to be executed automatically.

![](Penetration%20Testing/Images/Pasted%20image%2020260717174851.png)

Another script confirmed that it was executed every minute by a **Cron Job**.

![](Penetration%20Testing/Images/Pasted%20image%2020260402121031.png)

---

## Checking Permissions

We inspected the permissions of the primary script.

![](Penetration%20Testing/Images/Pasted%20image%2020260717174958.png)

The file was owned by **root**, but members of the **admin** group had full write permissions.

We verified our current groups.

![](Penetration%20Testing/Images/Pasted%20image%2020260717175117.png)

Our user belonged to the **admin** group, meaning we could modify the script executed by root.

---

## Obtaining Root

We generated a Bash Reverse Shell from:

```text
https://www.revshells.com/
```

![](Penetration%20Testing/Images/Pasted%20image%2020260717175222.png)

We replaced the contents of the writable script with the Reverse Shell payload.

![](Penetration%20Testing/Images/Pasted%20image%2020260717175324.png)

Next, we started a Netcat listener.

![](Penetration%20Testing/Images/Pasted%20image%2020260717175345.png)

Approximately one minute later, the Cron Job executed our modified script with root privileges.

We successfully received a Reverse Shell as **root**.

![](Penetration%20Testing/Images/Pasted%20image%2020260717175442.png)

Finally, we obtained the root flag.

![](Penetration%20Testing/Images/Pasted%20image%2020260717175523.png)

---

# Summary

In this lab we learned how to:

- Perform service enumeration with Nmap.
- Discover hidden resources through directory fuzzing.
- Configure custom virtual hosts using `/etc/hosts`.
- Identify and exploit a Path Traversal vulnerability.
- Recover sensitive information from exposed files.
- Extract and repair an SSH private key.
- Authenticate using SSH key-based authentication.
- Abuse insecure sudo configurations.
- Escalate privileges through command injection.
- Identify insecure Cron Jobs.
- Exploit writable scripts executed by root.
- Obtain full root access to the target system.

This room demonstrates how several seemingly minor misconfigurations—including exposed backup files, Path Traversal, weak sudo rules, and insecure Cron Job permissions—can be chained together to achieve complete system compromise.
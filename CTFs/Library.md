# SSH Brute Force to Root Compromise

This lab demonstrates an attack chain that begins with user enumeration, continues with an SSH brute-force attack to obtain valid credentials, and ends with Privilege Escalation through a misconfigured `sudo` rule that allows execution of a Python script as the root user.

# Enumeration

## Step 1 - Network Enumeration

We began by performing an Nmap scan against the target to identify open ports and running services.

![[Pasted image 20260709163048.png]]

## Step 2 - User Enumeration

After accessing the web application, we performed user enumeration and successfully identified a valid username.

![[Pasted image 20260406093000.png]]

# Exploitation

## Step 1 - SSH Brute Force

Using the discovered username, we performed an SSH brute-force attack with **Hydra**.

Hydra is commonly used to test multiple password combinations against network services such as SSH, FTP, HTTP, SMB, and many others.

![[Pasted image 20260709163437.png]]

The attack successfully recovered valid SSH credentials.

## Step 2 - SSH Login

Using the recovered credentials, we authenticated to the target through SSH.

![[Pasted image 20260709163533.png]]

# Privilege Escalation

## Step 1 - Local Enumeration

After obtaining shell access, we performed local enumeration to identify privilege escalation opportunities.

We checked the commands the current user was allowed to execute with sudo privileges.

```bash
sudo -l
```

This command lists all programs that the current user can execute with elevated privileges.

The output revealed that a Python script could be executed as the **root** user.

![[Pasted image 20260406093137.png]]

## Step 2 - Replace the Python Script

Since we had permission to modify the script, we deleted the original Python file and created a new file with the same name containing a Python shell payload.

![[Pasted image 20260406093226.png]]

## Step 3 - Execute the Script as Root

Finally, we executed the Python script using the permitted `sudo` command.

Because the script was executed with root privileges, it spawned a root shell and successfully completed the Privilege Escalation.

![[Pasted image 20260406093402.png]]

# Summary

This attack chain consisted of:

1. Network Enumeration with Nmap.
2. User Enumeration through the web application.
3. SSH brute-force attack using Hydra.
4. SSH authentication with the recovered credentials.
5. Local enumeration.
6. Identifying a Python script that could be executed with `sudo`.
7. Replacing the original script with a Python shell payload.
8. Executing the modified script as root.
9. Successfully obtaining a root shell.
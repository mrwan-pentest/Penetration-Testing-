# Web Application to Root Compromise

This lab demonstrates a complete attack chain that begins with web enumeration, continues with credential discovery from a leaked database backup, gains initial access by uploading a PHP payload, and ends with Privilege Escalation through a misconfigured sudo permission.

# Enumeration

## Step 1 - Network Enumeration

We began by performing an Nmap scan against the target to identify open ports and running services.

![](../Images/Pasted%20image%2020260422065437.png)

## Step 2 - Directory Enumeration

Next, we performed directory fuzzing to discover hidden files and directories exposed by the web server.

![](../Images/Pasted%20image%2020260422065501.png)

During the scan, we discovered a **content** directory.

To continue the enumeration process, we performed another fuzzing scan against this directory.

![](../Images/Pasted%20image%2020260422065530.png)

The second scan revealed a MySQL backup file.

![](../Images/Pasted%20image%2020260422065656.png)

## Step 3 - Credential Discovery

After downloading and inspecting the backup file, we discovered a username and a password hash.

![](../Images/Pasted%20image%2020260422065753.png)

## Step 4 - Hash Identification

Before attempting to crack the hash, we identified its type using **Hash Identifier**.

The tool identified the hash as **MD5**.

Next, we used **Hashcat** to crack the password.

![](../Images/Pasted%20image%2020260422065927.png)

The attack successfully recovered the plaintext password.

![](../Images/Pasted%20image%2020260422065951.png)

# Exploitation

## Step 1 - Login to the Web Application

Using the recovered credentials, we authenticated to the application's administrative dashboard.

## Step 2 - Upload a PHP Payload

After logging in, we uploaded a PHP payload through the dashboard.

![](../Images/Pasted%20image%2020260422070035.png)

## Step 3 - Execute the Payload

To execute the uploaded PHP code, we browsed to its location on the web server.

![](../Images/Pasted%20image%2020260422070104.png)

The payload executed successfully and established a Reverse Shell connection.

# Privilege Escalation

## Step 1 - Check Sudo Permissions

After obtaining shell access, we checked the commands that the current user was allowed to execute with sudo privileges.

```bash
sudo -l
```

This command lists all programs that the current user can run with elevated privileges.

The output revealed a PowerShell script that could be executed as the **root** user.

![](../Images/Pasted%20image%2020260422070304.png)

## Step 2 - Analyze the Script

After reviewing the PowerShell script, we discovered that it executed another file named:

```text
copy.sh
```

Since we had permission to modify this script, we replaced its contents with the following command:

```bash
echo "/bin/bash" > /etc/copy.sh
```

When the privileged PowerShell script executed `copy.sh`, it launched a Bash shell with **root** privileges, successfully completing the Privilege Escalation.

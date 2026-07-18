# WordPress to Root Compromise

This lab demonstrates a complete attack chain, starting with the discovery of a WordPress login page, gaining initial access through credential attacks, uploading a Reverse Shell, pivoting into an internal service using Port Forwarding, exploiting an internal CMS, and finally obtaining root access.

# Enumeration

## Step 1 - Configure Local Name Resolution

Before interacting with the target, we added the target's IP address and hostname to the local hosts file.

```text
/etc/hosts
```

This allows the target to be accessed using its hostname instead of its IP address.

## Step 2 - Network Enumeration

We began by performing an Nmap scan against the target to identify open ports and running services.

![[Pasted image 20260404155938.png]]

## Step 3 - Directory Enumeration

Next, we performed directory fuzzing to discover hidden files and directories exposed by the web server.

![[Pasted image 20260422102016.png]]

During the scan, we discovered a hidden page containing a WordPress login portal.

## Step 4 - Username Enumeration

While testing the login page, we discovered that the username **admin** exists.

The application responded differently when the username was valid, returning an "Incorrect password" message instead of indicating that the user did not exist.

![[Pasted image 20260422102215.png]]

# Exploitation

## Step 1 - Brute Force the WordPress Login

After identifying a valid username, we performed a password brute-force attack using WPScan.

WPScan is a security scanner specifically designed for WordPress and includes modules for user enumeration, plugin detection, vulnerability scanning, and password attacks.

![[Pasted image 20260422102342.png]]

The attack successfully recovered the administrator password.

## Step 2 - Upload a PHP Reverse Shell

Using the recovered credentials, we logged into the WordPress administration panel.

We then navigated to the **Theme Editor**, which allows administrators to modify theme files directly from the dashboard.

![[Pasted image 20260422103033.png]]

We selected the following template file and inserted a PHP Reverse Shell payload.

![[Pasted image 20260422103115.png]]

![[Pasted image 20260422103258.png]]

To execute the uploaded payload, we accessed the modified theme file through its URL.

General format:

```text
http://internal.thm/blog/wp-content/themes/<theme-name>/<template-file>
```

In this lab, we visited:

```text
http://internal.thm/blog/wp-content/themes/twentyseventeen/404.php
```

Executing the page caused the PHP code to run and established a Reverse Shell connection.

We successfully obtained our initial shell.

![[Pasted image 20260422103450.png]]

# Post Exploitation

## Step 1 - Credential Discovery

After obtaining shell access, we searched the system for sensitive files and discovered credentials belonging to another user.

![[Pasted image 20260422104045.png]]

## Step 2 - SSH Access

Using the discovered credentials, we authenticated to the target via SSH.

![[Pasted image 20260422104140.png]]

## Step 3 - Internal Service Discovery

While enumerating the system, we found a note indicating that an internal service was listening on TCP port **8080**.

![[Pasted image 20260422104236.png]]

## Step 4 - Port Forwarding

Since the service was only accessible from the target machine, we created an SSH port forwarding tunnel.

Port forwarding allowed us to access the internal service directly from our attacking machine.

![[Pasted image 20260422104443.png]]

We verified that the forwarded port was now accessible locally.

![[Pasted image 20260422104551.png]]

After opening the forwarded service in a browser, we discovered another login page.

The application was identified as a CMS.

![[Pasted image 20260422104641.png]]

# Internal CMS Exploitation

## Step 1 - Search for Public Exploits

After identifying the CMS, we searched Metasploit for modules targeting the detected software.

![[Pasted image 20260422104754.png]]

A module related to the CMS login functionality was available.

![[Pasted image 20260422104833.png]]

## Step 2 - Password Guessing

We searched online for the CMS's default username.

This provided a starting point for password guessing.

![[Pasted image 20260422105118.png]]

We then began testing password combinations.

![[Pasted image 20260422105307.png]]

Eventually, valid credentials were discovered.

![[Pasted image 20260422105515.png]]

## Step 3 - Uploading a Reverse Shell

After logging into the CMS, we explored its administrative interface.

![[Pasted image 20260422105722.png]]

During the assessment, we discovered functionality that allowed custom script uploads.

![[Pasted image 20260422105739.png]]

We generated a **Groovy Reverse Shell** payload from:

```text
https://www.revshells.com/
```

![[Pasted image 20260707171625.png]]

We pasted the generated Groovy script into the available script execution area.

![[Pasted image 20260422105825.png]]

Once executed, the payload established another Reverse Shell connection.

![[Pasted image 20260422110100.png]]

# Privilege Escalation

After gaining access to the internal server, we performed local enumeration to search for privilege escalation opportunities.

During the enumeration process, we discovered the root user's credentials.

![[Pasted image 20260422110309.png]]

Using the recovered credentials, we authenticated as the root user.

![[Pasted image 20260422110419.png]]


**Congratulations! The target has been fully compromised.**

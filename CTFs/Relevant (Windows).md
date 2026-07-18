# Exploiting IIS via File Upload and Privilege Escalation with SeImpersonatePrivilege

This lab demonstrates how to exploit an **IIS** web server through a **File Upload** vulnerability to obtain a **Reverse Shell**, then escalate privileges to **NT AUTHORITY\SYSTEM** by abusing the **SeImpersonatePrivilege** privilege with **PrintSpoofer**.

---

#

## Step 1 - Network Enumeration

We started by performing an Nmap scan to identify open ports and running services.

The initial scan revealed **SMB** and **HTTP** services.

![[Pasted image 20260410164813.png]]

---

## Step 2 - Web Enumeration

Since the target was running **IIS**, we performed directory fuzzing using the **.aspx** extension, which is commonly used for ASP.NET applications hosted on IIS.

![[Pasted image 20260410165246.png]]

---

## Step 3 - SMB Enumeration

We enumerated the SMB shares and discovered a shared file containing passwords.

We copied the file for further analysis.

![[Pasted image 20260410165447.png]]

After examining the file, we noticed that the passwords were encoded using **Base64**, which is easily recognizable by its character set and the `=` or `==` padding at the end.

We decoded the passwords and saved them into a separate file for later use.

![[Pasted image 20260410165835.png]]

---

## Step 4 - Full Port Scan

To ensure no additional services were missed, we performed a full TCP port scan against the target.

![[Pasted image 20260410170124.png]]

The scan revealed several additional open ports.

![[Pasted image 20260410170518.png]]

---

## Step 5 - Identifying the Upload Directory

The newly discovered web service was also hosted on **IIS**.

We attempted to access the previously discovered **Passwords** directory on the first web server, but access was denied.

However, accessing the same path on the newly discovered web service was successful.

![[Pasted image 20260410171059.png]]

This indicated that the directory was accessible through the second IIS instance.

---

## Step 6 - Exploiting the File Upload Vulnerability

Since the upload directory was accessible, we attempted to exploit a **File Upload** vulnerability.

We searched for an **ASPX Web Shell**, downloaded one, and uploaded it to the server using FTP.

The file was uploaded with the following FTP command:

```text
put shell.aspx
```

![[Pasted image 20260410171332.png]]

After the upload completed successfully, we browsed to the uploaded file to execute the Web Shell.

![[Pasted image 20260410171403.png]]

---

## Step 7 - Obtaining a Reverse Shell

We started a Netcat listener on our attack machine.

Once the uploaded ASPX shell was executed, we received a Reverse Shell from the target.

![[Pasted image 20260410171427.png]]

We successfully accessed the system and obtained the user flag.

![[Pasted image 20260410171534.png]]

---

## Step 8 - Privilege Escalation Enumeration

We enumerated the current user's privileges and discovered that the account possessed the **SeImpersonatePrivilege** privilege.

This Windows privilege allows a process to impersonate another user's security token under specific conditions. If misconfigured, it can be abused to escalate privileges to **NT AUTHORITY\SYSTEM**.

![[Pasted image 20260410171640.png]]

---

## Step 9 - Exploiting SeImpersonatePrivilege

One of the most common tools for abusing **SeImpersonatePrivilege** is **PrintSpoofer**.

After downloading the executable, we started an SMB server on our attack machine to transfer it to the target.

![[Pasted image 20260410172225.png]]

From the target machine, we copied the executable from the SMB share.

![[Pasted image 20260410172246.png]]

We executed **PrintSpoofer**, which successfully elevated our privileges to **NT AUTHORITY\SYSTEM**.

![[Pasted image 20260410172405.png]]

---

## Step 10 - Capturing the Root Flag

With SYSTEM-level privileges, we accessed the Administrator's files and successfully retrieved the root flag.

![[Pasted image 20260410172522.png]]
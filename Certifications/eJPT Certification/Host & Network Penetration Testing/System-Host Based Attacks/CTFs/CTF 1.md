# CTF Walkthrough

## Scenario

The objective of this challenge was to obtain multiple flags by exploiting weak credentials, enumerating exposed services, and accessing sensitive files on the target Windows system.

---

# Enumeration

## Brute-Forcing the Web Server Credentials

The first objective indicated that the user **bob** might have chosen a weak password.

To verify this, we performed a brute-force attack against the web server using **Hydra** with a common Unix password wordlist.

```
hydra -l bob -P /usr/share/metasploit-framework/data/wordlists/unix_passwords.txt target1.ine.local http-get
```

This attack successfully recovered valid credentials for the target web application.

![](../../../../../Images/Pasted%20image%2020260520144829.png)

---

## Directory Enumeration

After obtaining valid credentials, we performed directory enumeration to discover hidden resources exposed by the web server.

![](../../../../../Images/Pasted%20image%2020260520144857.png)

During enumeration, we discovered a **WebDAV** directory.

---

## Testing the WebDAV Service

To determine whether the WebDAV service allowed file uploads, we used **davtest**.

The assessment revealed that the server accepted **ASP** file uploads, providing a potential method for executing code on the target.

---

# Exploitation

## Accessing the WebDAV Share

We connected to the WebDAV share using **cadaver**.

After authenticating with the recovered credentials, we browsed the available files and located the first flag.

![](../../../../../Images/Pasted%20image%2020260520145156.png)

---

# Flag 1

The first flag was obtained by authenticating to the exposed WebDAV share and browsing its contents.

---

# Exploring the File System

## Flag 2 - Exploring Valuable Files on the C: Drive

After confirming that the WebDAV service allowed uploads, we uploaded the required file to the server.

![](../../../../../Images/Pasted%20image%2020260520145244.png)

Once uploaded, we explored the **C:** drive and successfully located the second flag.

![](../../../../../Images/Pasted%20image%2020260520145306.png)

---

# SMB Enumeration

## Flag 3 - SMB Enumeration and Credential Attack

Next, we targeted the SMB service.

A brute-force attack was performed using a Metasploit SMB module to identify valid credentials.

![](../../../../../Images/Pasted%20image%2020260520145421.png)

To obtain a separate session for each successful login, we enabled the appropriate option within the module.

![](../../../../../Images/Pasted%20image%2020260520145445.png)

After successful authentication, we accessed the **Administrator** account.

![](../../../../../Images/Pasted%20image%2020260520145550.png)

We then enumerated the available SMB shares, navigated to the appropriate share, and retrieved the third flag.

![](../../../../../Images/Pasted%20image%2020260520145612.png)

---

# Flag 4 - Searching the Desktop Directory

After gaining access to the Administrator account, we navigated to the user's **Desktop** directory.

There, we found and read the fourth flag.

![](../../../../../Images/Pasted%20image%2020260520145704.png)

![](../../../../../Images/Pasted%20image%2020260520145716.png)

---

# Alternative Approach

Instead of using Metasploit for the SMB credential attack, the same objective can be achieved using **Hydra** to perform a brute-force attack against the SMB service.

After recovering valid credentials, authenticate using **smbclient** and browse the available SMB shares to locate the required flags.

---

# Summary

The challenge was completed by combining several common penetration testing techniques:

1. Brute-forcing weak web credentials with **Hydra**.
2. Enumerating hidden directories to discover an exposed **WebDAV** service.
3. Verifying file upload capabilities using **davtest**.
4. Accessing the WebDAV share with **cadaver** to obtain the first flag.
5. Uploading files and exploring the Windows file system to retrieve the second flag.
6. Performing SMB credential attacks to gain administrative access.
7. Enumerating SMB shares and browsing the Administrator's Desktop to recover the remaining flags.

This walkthrough demonstrates how weak passwords, exposed WebDAV services, and improperly secured SMB resources can be chained together to fully compromise a Windows host and obtain sensitive information.
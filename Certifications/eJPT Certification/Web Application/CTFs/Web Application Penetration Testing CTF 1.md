# CTF Walkthrough

# Enumeration

The objective of this challenge was to retrieve four flags by exploiting multiple vulnerabilities exposed by the target web application.

---

# Flag 1

## Exploiting Local File Inclusion (LFI)

The first hint suggested that an important file named `flag.txt` existed somewhere under the root (`/`) directory.

During the initial assessment, we discovered that the web application was vulnerable to **Local File Inclusion (LFI)**.

By exploiting the LFI vulnerability, we were able to access arbitrary files on the target system, including the first flag.

![](Penetration%20Testing/Images/Pasted%20image%2020260610163129.png)

---

# Flag 2

## Directory Enumeration

The second hint suggested exploring the server's directory structure.

To discover hidden directories and files, we performed directory brute-force enumeration.

During the scan, we discovered an interesting hidden URL.

![](Penetration%20Testing/Images/Pasted%20image%2020260610163339.png)

---

## Accessing the Hidden Directory

After navigating to the discovered path, we found a protected resource containing the second flag.

![](Penetration%20Testing/Images/Pasted%20image%2020260610163506.png)

![](Penetration%20Testing/Images/Pasted%20image%2020260610163510.png)

---

# Flag 3

## Brute Forcing the Login Page

The third hint indicated that the login form might be vulnerable to weak credentials.

Before launching a brute-force attack, we gathered information about the authentication mechanism.

---

## Analyzing the Login Request

We intercepted the login request using **Burp Suite** to identify:

- HTTP request method
- Login endpoint
- Username parameter
- Password parameter

The captured request showed that the application uses the **POST** method for authentication.

![](Penetration%20Testing/Images/Pasted%20image%2020260610163843.png)

---

## Identifying the Failure Message

We also identified the error message returned when authentication fails.

This message is required by Hydra to determine unsuccessful login attempts.

![](Penetration%20Testing/Images/Pasted%20image%2020260610164133.png)

---

## Launching the Brute Force Attack

After collecting the required information, we used Hydra to brute-force the login form.

```bash
hydra -f -V -L /usr/share/seclists/Usernames/top-usernames-shortlist.txt -P /root/Desktop/wordlists/100-common-passwords.txt target.ine.local http-post-form "/login:username=^USER^&password=^PASS^:Invalid username or password"
```

### Command Explanation

- `-f` Stop after finding the first valid credentials.
- `-V` Enable verbose output.
- `-L` Specify the username wordlist.
- `-P` Specify the password wordlist.
- `http-post-form` Use the HTTP POST module.
- `/login:username=^USER^&password=^PASS^:Invalid username or password` Define the login endpoint, POST parameters, and failure message.

---

## Valid Credentials Discovered

Hydra successfully identified valid login credentials.

![](Penetration%20Testing/Images/Pasted%20image%2020260610164410.png)

---

## Retrieving the Third Flag

After logging into the application with the discovered credentials, we successfully obtained the third flag.

![](Penetration%20Testing/Images/Pasted%20image%2020260610164528.png)

---

# Flag 4

## SQL Injection Authentication Bypass

The final hint suggested testing the login form with unexpected input.

We attempted a **SQL Injection** attack against the authentication mechanism to bypass the login page and gain access to the administrator account.

![](Penetration%20Testing/Images/Pasted%20image%2020260610164751.png)

---

## Retrieving the Final Flag

After successfully bypassing authentication, we gained access to the administrator account and obtained the final flag.

![](Penetration%20Testing/Images/Pasted%20image%2020260610164820.png)

---

# Summary

During this challenge, we successfully demonstrated several common web application penetration testing techniques:

- Local File Inclusion (LFI)
- Directory Enumeration
- Login Form Analysis using Burp Suite
- Brute Force Authentication using Hydra
- SQL Injection Authentication Bypass

By combining these techniques, we successfully retrieved all four challenge flags.
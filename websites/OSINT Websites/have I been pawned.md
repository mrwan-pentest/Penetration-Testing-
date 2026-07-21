
[Have I Been Pwned: Check if your email address has been exposed in a data breach](https://haveibeenpwned.com/)
# Have I Been Pwned (HIBP)

Have I Been Pwned is a website used to check whether an email address or password has appeared in known data breaches.

In simple words:

> It tells you if your account information has been leaked in a previous breach.

---

# What does HIBP check?

It checks against databases of leaked data containing:

- 📧 Email addresses
- 🔑 Passwords (in a protected way)
- 💳 Other leaked account information from breaches

---

# Main Features

## 1. Check Email Breaches

You enter an email:

```
user@example.com
```

The website tells you if it appeared in known breaches.

Example result:

```
Pwned in 3 data breaches
```

It may show:

- Breach name
- Date
- Data types exposed

Example:

```
Compromised data:
- Email addresses
- Passwords
- Usernames
```

---

## 2. Check Password Exposure

You can check whether a password has appeared in leaked password databases.

Example:

```
Password123
```

Result:

```
This password has been seen many times before
```

Meaning:

Attackers may already know this password.

---

# Why is it important in Cybersecurity?

For security professionals, it helps with:

- Account security assessment
- Password policy testing
- User awareness
- Incident response

---

# Pentesting Use Case

During an authorized security assessment, a tester may check:

```
Company emails
```

to see if employees' accounts appeared in previous breaches.

Example:

```
john@company.com
```

Result:

```
Found in previous breach
```

This can indicate:

- Password reuse risk
- Possible account compromise
- Need for password reset

---

# How it works?

For password checking, HIBP uses a method called:

```
k-Anonymity
```

The password is not sent directly.

Instead:

1. The password is converted into a hash.
2. Only part of the hash is sent.
3. The service returns matching results.
4. Your full password remains private.

---

# Difference Between HIBP and Exploit-DB

|Tool|Purpose|
|---|---|
|Have I Been Pwned|Check leaked accounts/data breaches|
|Exploit-DB|Find public exploits and vulnerabilities|

---

# Example Workflow

```
Collect Email Addresses
          |
          ↓
Check HIBP
          |
          ↓
Find Breach History
          |
          ↓
Assess Password Risk
          |
          ↓
Recommend Security Improvements
```

---

# Summary

**Have I Been Pwned:**

```
A service that checks whether emails or passwords
have appeared in known data breaches.
```

It is mainly used for:

- Security awareness
- Account protection
- Breach investigation
- Reconnaissance during authorized assessments.
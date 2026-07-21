
[Have I Been Pwned: Check if your email address has been exposed in a data breach](https://haveibeenpwned.com/)
# Have I Been Pwned (HIBP)

## What is Have I Been Pwned?

**Have I Been Pwned (HIBP)** is a free online service that allows users to check whether their personal information has appeared in publicly known **data breaches**.

It is widely used by:

- Security Professionals
- Penetration Testers
- System Administrators
- Individual Users

Simply put:

> It tells you whether your email address or other information has been exposed in a known data breach.

---

# What Does It Check?

Have I Been Pwned can search for:

- Email Addresses
- Passwords (using a separate password search service)
- Data Breaches from compromised organizations and websites

---

# What Happens When You Search an Email Address?

Suppose you search:

```text
user@example.com
```

The website compares the email address against its database of publicly known breaches.

---

## Possible Result 1

```text
Good news — no pwnage found!
```

### Meaning

The email address was **not found** in any known public data breach.

> **Note:** This does **not** guarantee that the account has never been compromised—it only means it does not appear in HIBP's current database.

---

## Possible Result 2

```text
Oh no — Pwned!
```

### Meaning

The email address was found in one or more known data breaches.

The report typically includes:

- The breached organization or website
- The breach date
- The type of exposed information

Examples of leaked data include:

- Email Addresses
- Usernames
- Password Hashes
- Phone Numbers
- Names
- Physical Addresses

---

# Why Is It Important?

From a security perspective, HIBP helps users:

- Determine whether an account has been exposed.
- Change passwords after a breach.
- Enable Multi-Factor Authentication (MFA).
- Avoid password reuse across multiple services.

---

# Importance for Penetration Testers

During **OSINT (Open Source Intelligence)**, HIBP can help identify:

- Accounts previously involved in data breaches.
- Potential targets for **Credential Stuffing** attacks.
- Organizations affected by historical security incidents.

> **Note:** Always use this information ethically and only with proper authorization during security assessments.

---

# Typical Workflow

```text
Email Address
      │
      ▼
Have I Been Pwned
      │
      ├── Search Breach Database
      │
      ▼
Results
      │
      ├── No Known Breaches
      └── One or More Data Breaches
                │
                ▼
Review Exposed Information
```

---

# Summary

| Feature | Description |
|---------|-------------|
| **Purpose** | Checks whether an email address or password has appeared in known data breaches. |
| **Search Targets** | Email Addresses, Passwords, and Public Breach Records. |
| **"No pwnage found"** | The email was not found in HIBP's known breach database. |
| **"Pwned!"** | The email appeared in one or more publicly known data breaches. |
| **Security Benefit** | Helps users identify compromised accounts and improve account security. |
| **Common Use** | OSINT, security awareness, credential exposure verification, and incident response. |
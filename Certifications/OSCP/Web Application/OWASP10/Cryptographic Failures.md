
# Cryptographic Failures

## What are Cryptographic Failures?

**Cryptographic Failures** occur when an application **fails to properly protect sensitive data** using cryptography.

This can happen because:

- Data is not encrypted.
- Weak encryption algorithms are used.
- Encryption keys are poorly managed.
- Sensitive data is exposed during transmission or storage.

---

# Why is it Dangerous?

If cryptography is implemented incorrectly, attackers may be able to:

- Read sensitive information.
- Steal passwords.
- Capture session tokens.
- Access confidential user data.

---

# Common Examples

## 1. Using HTTP Instead of HTTPS

Sensitive information is transmitted in **clear text**.

Example:

```
POST /login HTTP/1.1

username=admin
password=123456
```

An attacker using tools like **Wireshark** can capture the credentials.

---

## 2. Storing Passwords in Plain Text

Instead of storing password hashes:

```
123456
```

The application stores:

```
password123
```

If the database is compromised, all passwords are immediately exposed.

---

## 3. Weak Password Hashing

Using weak algorithms such as:

```
MD5
SHA1
```

Instead of modern algorithms like:

```
bcrypt
Argon2
scrypt
```

Weak hashes can often be cracked quickly using tools like **Hashcat**.

---

## 4. Weak or Outdated Encryption

Using deprecated protocols or algorithms such as:

```
SSL
DES
RC4
```

These are considered insecure and should be replaced with modern alternatives like:

```
TLS 1.2 / TLS 1.3
AES
```

---

## 5. Exposed Sensitive Data

Sensitive information is returned to users or stored without proper protection.

Examples:

- Credit card numbers
- Personal information
- API Keys
- Session Tokens

---

# Prevention

- Always use **HTTPS (TLS)**.
- Store passwords using **bcrypt**, **Argon2**, or **scrypt**.
- Use strong encryption algorithms (e.g., **AES**).
- Protect and securely manage encryption keys.
- Never expose sensitive information unnecessarily.

---

# Summary

**Cryptographic Failures** are security weaknesses caused by **improper use of encryption or inadequate protection of sensitive data**, allowing attackers to read or steal confidential information.
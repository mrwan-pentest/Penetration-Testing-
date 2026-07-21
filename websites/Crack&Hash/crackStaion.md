
## [CrackStation - Online Password Hash Cracking - MD5, SHA1, Linux ...](https://www.bing.com/ck/a?!&&p=cf4f7b191ba9efbf471dd13c43c6cde96d1e8fc764a219c33090d4effcf124deJmltdHM9MTc3NjcyOTYwMA&ptn=3&ver=2&hsh=4&fclid=27df3085-b844-6abc-1d5a-278cb94d6b7b&psq=hashcrack&u=a1aHR0cHM6Ly9jcmFja3N0YXRpb24ubmV0Lw)


# CrackStation

**CrackStation** is an online password hash cracking service used to recover plaintext passwords from hashes.

---

# What is CrackStation?

CrackStation is a:

```
Online Hash Cracking Database
```

It contains a huge database of:

- Common passwords
- Wordlists
- Pre-computed hashes

It uses:

```
Hash Lookup
```

instead of traditional brute-force cracking.

---

# How does it work?

You provide a hash:

Example:

```
5f4dcc3b5aa765d61d8327deb882cf99
```

CrackStation searches its database for a matching hash.

If found, it returns:

```
password
```

---

# Supported Hash Types

CrackStation can crack common hashes such as:

- MD5
- SHA1
- SHA256
- SHA512
- NTLM
- Other common hash formats

---

# How to use it?

1. Copy the hash you want to crack.

Example:

```
5f4dcc3b5aa765d61d8327deb882cf99
```

2. Paste it into CrackStation.
3. Click:

```
Crack Hashes
```

4. If the hash exists in its database, it shows the original password.

---

# When is it useful in Pentesting?

After obtaining password hashes from places like:

- `/etc/shadow`
- Windows SAM Database
- Database dumps
- Application password hashes

Example:

You find:

```
NTLM Hash
```

You can try:

- CrackStation
- John the Ripper
- Hashcat

to recover the password.

---

# Advantages

✅ Very fast  
Because it uses a precomputed database.

✅ Easy to use  
No installation required.

✅ Useful for common passwords.

---

# Limitations

❌ Cannot crack every hash.

It usually fails with:

- Strong random passwords
- New passwords
- Salted hashes
- Custom hashing algorithms

---

# CrackStation vs Hashcat

|CrackStation|Hashcat|
|---|---|
|Online service|Local tool|
|Database lookup|Real password cracking|
|Very fast|Uses CPU/GPU power|
|No setup|Requires configuration|
|Limited to known hashes|Can attack unknown passwords|

---

# In short:

```
CrackStation = Online hash lookup service used to quickly recover passwords from known hashes.
```

Common workflow:

```
Get Hash
   |
   v
Try CrackStation
   |
   v
If failed → Use John/Hashcat
```


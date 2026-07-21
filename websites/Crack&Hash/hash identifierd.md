
## [Hash Type Identifier - Identify unknown hashes](https://www.bing.com/ck/a?!&&p=dc20924410d845666ba9dd4f7fbbefd2426f6281f8f6ac4110048ca0144234feJmltdHM9MTc3NjcyOTYwMA&ptn=3&ver=2&hsh=4&fclid=27df3085-b844-6abc-1d5a-278cb94d6b7b&psq=hash+identifier&u=a1aHR0cHM6Ly9oYXNoZXMuY29tL2VuL3Rvb2xzL2hhc2hfaWRlbnRpZmllcg)

# Hash Identifier Website

Hash Identifier is an online tool used to:

```
Identify the possible type of a hash
```

It helps you know what hashing algorithm may have created a given hash value.

---

# Why use it?

When you find an unknown hash, for example:

```
5f4dcc3b5aa765d61d8327deb882cf99
```

You may not know if it is:

- MD5
- SHA1
- NTLM
- SHA256
- bcrypt
- etc.

You paste the hash into the website, and it suggests possible hash types.

---

# How it works?

It analyzes the:

- Hash length
- Characters used
- Hash format

Example:

Input:

```
5f4dcc3b5aa765d61d8327deb882cf99
```

Result:

```
Possible Hash Type:
MD5
NTLM
```

---

# Pentesting Workflow

Usually:

```
Obtain Hash
      |
      ↓
Hash Identifier
      |
      ↓
Determine Hash Type
      |
      ↓
Use John / Hashcat
      |
      ↓
Crack Password
```

---

# Example

You get a Windows NTLM hash:

```
32ed87bdb5fdc5e9cba88547376818d4
```

Use Hash Identifier:

```
NTLM
```

Then use Hashcat:

```
hashcat -m 1000 hash.txt wordlist.txt
```

because:

```
1000 = NTLM mode
```

---

# Limitations

Hash Identifier is not always 100% accurate because:

- Different hash algorithms can have the same length.
- Some hashes have similar formats.

Example:

A 32-character hexadecimal hash could be:

- MD5
- NTLM
- Other algorithms

So it gives:

```
Possible matches
```

not guaranteed identification.

---


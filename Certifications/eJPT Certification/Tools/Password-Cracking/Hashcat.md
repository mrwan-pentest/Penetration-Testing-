# Hashcat

## What is Hashcat?

`Hashcat` is an advanced password recovery tool used to crack password hashes by using the processing power of:

- CPU
- GPU (Graphics Processing Unit)

It is one of the fastest password-cracking tools available because it can utilize modern graphics cards to perform a huge number of hash calculations per second.

Hashcat is commonly used in:

- Password auditing
- Penetration testing
- Digital forensics
- CTF challenges
- Security assessments

---

# What Does "Cracking a Hash" Mean?

When a system stores passwords, it usually does not store the original password.

Instead, it stores a hash.

Example:

```
cd06ca7c7e10c99b1d33b7485a2ed808
```

This could represent an:

```
NTLM Hash
```

The goal of Hashcat is:

```
Find the original password that created this hash
```

Example:

```
Hash:
cd06ca7c7e10c99b1d33b7485a2ed808

Password:
Password123
```

---

# How Does Hashcat Work?

Hashcat works using a password guessing process.

The general idea:

1. Generate possible passwords.
2. Convert each password into a hash.
3. Compare the generated hash with the target hash.
4. If the hashes match, the original password has been found.

Example:

```
Candidate Password
        |
        v
    Hash Function
        |
        v
Generated Hash
        |
        v
Compare With Target Hash
```

---

# Hashcat Attack Modes

Hashcat supports multiple attack techniques depending on the situation.

---

# 1. Dictionary Attack

A Dictionary Attack uses a wordlist containing possible passwords.

Example:

```
hashcat -m 1000 hash.txt wordlist.txt
```

## How It Works

Hashcat takes every word from the wordlist and tries it as a password.

Example wordlist:

```
password
admin
welcome
Password123
```

Each word is converted into a hash and compared with the target hash.

---

# 2. Brute Force Attack

A Brute Force Attack tries every possible combination of characters.

Example:

```
hashcat -m 1000 hash.txt ?a?a?a?a?a?a
```

The pattern:

```
?a
```

represents all possible characters.

Hashcat tries combinations such as:

```
aaaaaa
aaaaab
aaaaac
...
```

until the correct password is found.

This method is powerful but can become very slow when passwords are long.

---

# 3. Hybrid Attack

A Hybrid Attack combines:

- A wordlist
- Additional characters

Example:

```
hashcat -m 1000 hash.txt wordlist.txt ?d?d
```

If the wordlist contains:

```
password
```

Hashcat will try:

```
password12
password34
password99
```

where:

```
?d
```

represents digits.

---

# 4. Rule-Based Attack

A Rule-Based Attack modifies words from a wordlist using predefined transformations.

Example:

Original word:

```
password
```

Generated possibilities:

```
Password
password1
Password123
P@ssword
```

Command:

```
hashcat -m 1000 hash.txt wordlist.txt -r rules/best64.rule
```

---

# Hashcat Modes (`-m`)

The option:

```
-m
```

defines the hash type Hashcat should crack.

Example:

```
hashcat -m 1000 hash.txt wordlist.txt
```

Here:

```
1000 = NTLM
```

---

# Common Hashcat Modes

|Hash Type|Hashcat Mode|
|---|---|
|MD5|`0`|
|SHA1|`100`|
|NTLM|`1000`|
|bcrypt|`3200`|

The correct mode must be selected before cracking.

---

# Hashcat Rules

## What Are Rules?

Rules are instructions that modify words from a wordlist before Hashcat converts them into hashes.

Instead of manually creating thousands of password variations, rules generate them automatically.

Example:

Original word:

```
password
```

Using rules:

```
Password
password123
P@ssword
```

---

# Why Use Rules?

Many users create passwords using predictable patterns:

- Capitalizing the first letter.
- Adding numbers at the end.
- Replacing characters with symbols.

Rules simulate these common password habits.

---

# Applying Rules

The general syntax:

```
hashcat -m HASH_TYPE hash.txt wordlist.txt -r rule.txt
```

Example:

```
hashcat -m 1000 hash.txt wordlist.txt -r myrules.rule
```

---

# Common Hashcat Rules

## Capitalize First Letter

Rule:

```
c
```

Example:

```
password → Password
```

---

## Convert All Characters to Uppercase

Rule:

```
u
```

Example:

```
password → PASSWORD
```

---

## Convert All Characters to Lowercase

Rule:

```
l
```

Example:

```
PASSWORD → password
```

---

## Add Number at the End

Rule:

```
$1
```

Example:

```
password → password1
```

---

## Add Multiple Numbers

Rule:

```
$1$2$3
```

Example:

```
password → password123
```

---

## Replace Characters

Rule:

```
s a @
```

Example:

```
password → p@ssword
```

Explanation:

```
a → @
```

---

# Creating Custom Rules

You can create your own rule file.

Example:

```
nano myrules.rule
```

Add rules:

```
c $1 $2 $3
c sa@
c $!
```

---

# Running Custom Rules

Command:

```
hashcat -m 1000 hash.txt wordlist.txt -r myrules.rule
```

Hashcat will apply your custom transformations to every word in the wordlist.

---

# Practical Password Cracking Workflow

A common workflow:

```
Obtain Hash
      |
      v
Identify Hash Type
      |
      v
Select Hashcat Mode
      |
      v
Choose Attack Method
      |
      v
Run Hashcat
      |
      v
Recover Password
```

---

# Summary

`Hashcat` is a powerful password recovery tool that uses CPU/GPU power to crack password hashes.

Main features:

- Dictionary attacks.
- Brute force attacks.
- Hybrid attacks.
- Rule-based attacks.
- GPU acceleration.
- Support for hundreds of hash algorithms.

Common usage:

```
hashcat -m <hash_mode> <hash_file> <wordlist>
```

The effectiveness of Hashcat depends mainly on:

- Correct hash identification.
- Attack method selection.
- Wordlist quality.
- Hardware performance.
- Password complexity.
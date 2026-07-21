# MySQL is a:

```
Database Management System (DBMS)
```

used to store and manage data.

In penetration testing, we usually deal with MySQL when we discover:

```
3306/tcp open mysql
```

because it may allow us to:

- Enumerate databases
- Extract information
- Test authentication
- Identify vulnerabilities

---

# What is MySQL?

MySQL is a database server that stores data in:

```
Tables
```

inside:

```
Databases
```

Example:

```
Database
 ├── users table
 │     ├── username
 │     └── password
 │
 └── accounts table
       ├── email
       └── balance
```

---

# Why is MySQL important in Pentesting?

Because databases often contain sensitive information:

- User accounts
- Password hashes
- Customer data
- Application secrets
- Configuration information

If an attacker gains access to MySQL, they may be able to extract valuable data.

---

# Default Port

MySQL usually runs on:

```
3306/tcp
```

Nmap example:

```
nmap -p 3306 TARGET
```

Example output:

```
3306/tcp open mysql
```

This tells us:

```
A MySQL database service is running
```

---

# Connecting to MySQL

The main client is:

```
mysql
```

Basic syntax:

```
mysql -h TARGET -u USERNAME -p
```

Example:

```
mysql -h 192.168.1.10 -u root -p
```

Explanation:

|Option|Meaning|
|---|---|
|`-h`|Target host|
|`-u`|Username|
|`-p`|Ask for password|

---

# Common Default Users

Common MySQL accounts:

```
root
admin
mysql
user
```

The most important one:

```
root
```

because it usually has full database privileges.

---

# Important MySQL Commands

After login:

---

## Show Databases

```
SHOW DATABASES;
```

Displays all databases.

Example:

```
information_schema
wordpress
company
```

---

## Select a Database

```
USE database_name;
```

Example:

```
USE wordpress;
```

---

## Show Tables

```
SHOW TABLES;
```

Example:

```
users
posts
comments
```

---

## Show Table Structure

```
DESCRIBE users;
```

Shows columns:

```
id
username
password
email
```

---

## Extract Data

```
SELECT * FROM users;
```

Example:

```
admin : hash123
john  : hash456
```

---

# MySQL Enumeration with Nmap

Nmap has MySQL scripts.

## Version Detection

```
nmap -sV -p 3306 TARGET
```

Shows:

- MySQL version
- Service information

---

## MySQL Information

```
nmap --script mysql-info -p 3306 TARGET
```

Can reveal:

- Version
- Protocol
- Server information

---

## Checking Authentication

```
nmap --script mysql-empty-password -p 3306 TARGET
```

Checks if:

```
Account has empty password
```

---

# MySQL Password Attacks

If you have usernames and want to test passwords:

Using Hydra:

```
hydra -l root -P passwords.txt mysql://TARGET
```

Meaning:

```
Try passwords against MySQL login
```

---

# Common MySQL Security Issues

## 1. Weak Passwords

Example:

```
root:root
root:password
admin:123456
```

---

## 2. Remote Access Enabled

Bad configuration:

```
MySQL accessible from the Internet
```

Attackers can try login attempts.

---

## 3. Old MySQL Versions

Old versions may contain:

- Authentication vulnerabilities
- Privilege escalation issues

---

## 4. Excessive Privileges

Example:

A normal user has:

```
ALL PRIVILEGES
```

Instead of limited permissions.

---

# MySQL in Web Pentesting

Many websites use:

```
Frontend
    |
    |
Backend
    |
    |
MySQL Database
```

Example:

WordPress uses:

```
MySQL Database
```

If you exploit a web application, you may find:

```
wp_users
wp_options
wp_config.php
```

which can contain database credentials.

---

# Important Files

A common file containing MySQL credentials:

```
wp-config.php
```

Example:

```
define('DB_USER','wordpress');
define('DB_PASSWORD','password123');
define('DB_NAME','wordpress');
```

---

# Useful Tools

|Tool|Purpose|
|---|---|
|`mysql client`|Connect to database|
|`Nmap`|Discover MySQL service|
|`Hydra`|Brute force login|
|`Metasploit`|MySQL modules|
|`SQLMap`|Exploit SQL Injection|

---

# Summary

MySQL is:

```
A database server used to store application data.
```

In penetration testing, after finding:

```
3306/tcp open mysql
```

we usually perform:

1. Version detection
2. User enumeration
3. Authentication testing
4. Database enumeration
5. Data extraction

The main goal is to discover whether the database can expose sensitive information or help gain further access.
# MySQL Enumeration

## Overview

**MySQL** is one of the most widely used relational database management systems (RDBMS). It is commonly deployed alongside web applications such as **WordPress**, **Joomla**, and **Drupal** to store application data, user accounts, and configuration information.

During a penetration test, MySQL enumeration focuses on identifying the server version, obtaining valid credentials, enumerating databases and tables, and assessing whether the database can be leveraged for further exploitation.

---

## Default Port

MySQL typically listens on:

```text
3306/TCP
```

---

## Common MySQL Commands

### Connect to MySQL

```bash
mysql -u root -p
```

---

### List Databases

```sql
SHOW DATABASES;
```

---

### Select a Database

```sql
USE database_name;
```

---

### List Tables

```sql
SHOW TABLES;
```

---

### Display Table Structure

```sql
DESCRIBE users;
```

or

```sql
DESC users;
```

---

### View Table Contents

```sql
SELECT * FROM users;
```

---

### List MySQL Users

```sql
SELECT user FROM mysql.user;
```

---

# MySQL Enumeration with Metasploit

## MySQL Version Detection

Uses the following module to identify the installed MySQL version:

```text
auxiliary/scanner/mysql/mysql_version
```

![[Pasted image 20260514141335.png]]

---

## MySQL Login Scanner

Attempts to authenticate using supplied usernames and passwords or perform brute-force attacks.

```text
auxiliary/scanner/mysql/mysql_login
```

![[Pasted image 20260514141431.png]]

---

## MySQL Enumeration

Collects information about the MySQL server, including:

- Users
    
- Privileges
    
- Server version
    

```text
auxiliary/admin/mysql/mysql_enum
```

![[Pasted image 20260514141535.png]]

---

## Schema Enumeration

Enumerates available databases and tables.

```text
auxiliary/scanner/mysql/mysql_schemadump
```

![[Pasted image 20260514141642.png]]

---

## Execute SQL Queries

Executes arbitrary SQL statements directly against the MySQL server.

```text
auxiliary/admin/mysql/mysql_sql
```

![[Pasted image 20260514141834.png]]

---

## File Enumeration

Searches for files that may be accessible through MySQL.

Examples include:

- config.php
    
- passwd
    
- Backup files
    

```text
auxiliary/scanner/mysql/mysql_file_enum
```

![[Pasted image 20260514141919.png]]

---

## Writable Directory Enumeration

Searches for writable directories that can be abused using:

```sql
SELECT ... INTO OUTFILE
```

This technique may allow attackers to upload files such as web shells.

```text
auxiliary/scanner/mysql/mysql_writable_dirs
```

![[Pasted image 20260514142003.png]]

---

## Password Hash Extraction

Extracts password hashes for MySQL user accounts.

```text
auxiliary/scanner/mysql/mysql_hashdump
```

![[Pasted image 20260514142119.png]]

---

## Notes

### MySQL

MySQL is an open-source relational database management system widely used by web applications to store structured data.

### Enumeration

MySQL enumeration helps identify:

- Server version
    
- Valid credentials
    
- Databases
    
- Tables
    
- User accounts
    
- Privileges
    
- Potential privilege escalation or file write opportunities
    

### Metasploit

Metasploit provides several auxiliary modules for MySQL reconnaissance, authentication testing, schema enumeration, SQL execution, and credential extraction.
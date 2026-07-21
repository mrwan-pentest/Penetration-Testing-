
## Default Port

```text
3306
```

---

## Essential MySQL Commands

### Connect to MySQL

```bash
mysql -u root -p
```

---

### Display All Databases

```sql
show databases;
```

---

### Select a Database

```sql
use database_name;
```

---

### Display Tables

```sql
show tables;
```

---

### Display Table Columns

```sql
describe users;
```

or

```sql
desc users;
```

---

### Display Table Data

```sql
select * from users;
```

---

### Display MySQL Users

```sql
select user from mysql.user;
```
---

# MSF


	auxiliary/scanner/mysql/mysql_version
	

![](Penetration%20Testing/Images/Pasted%20image%2020260514141335.png)

---


	auxiliary/scanner/mysql/mysql_login
	


```
Username/Password
```

(Bruteforce)


![](Penetration%20Testing/Images/Pasted%20image%2020260514141431.png)

---



```
auxiliary/admin/mysql/mysql_enum
```

## Enumerate information like:

### users
### privileges
### versions

![](Penetration%20Testing/Images/Pasted%20image%2020260514141535.png)

---

```
auxiliary/scanner/mysql/mysql_schemadump
```

### Show:

- Databases
- Tables

![](Penetration%20Testing/Images/Pasted%20image%2020260514141642.png)

---
- `auxiliary/admin/mysql/mysql_sql`

```
Excute SQL commands
```

![](Penetration%20Testing/Images/Pasted%20image%2020260514141834.png)

---
- `auxiliary/scanner/mysql/mysql_file_enum`

```
Search for files stored on the target server using MySQL features.
```

يفحص هل ملفات مثل:

- config.php
- passwd
- backups

موجودة ويمكن الوصول لها.


![](Penetration%20Testing/Images/Pasted%20image%2020260514141919.png)

---
- `auxiliary/scanner/mysql/mysql_writable_dirs`

```
Identify writable directories that can be accessed through MySQL.
```

![](Penetration%20Testing/Images/Pasted%20image%2020260514142003.png)

---
- `auxiliary/scanner/mysql/mysql_hashdump`

```
Extract password hashes associated with MySQL user accounts.
```

![](Penetration%20Testing/Images/Pasted%20image%2020260514142119.png)

---

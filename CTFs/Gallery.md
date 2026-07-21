# Objective

Exploit a **SQL Injection** vulnerability to bypass authentication, upload a **PHP Reverse Shell**, gain initial access to the target, escalate privileges to **Root**, and finally extract the **admin** user's password hash from the database.

---

# Initial Enumeration

We started by scanning the target using **Nmap** to identify the open ports and running services.

![](../Images/Pasted%20image%2020260420155636.png)

After identifying the open ports, we performed **Version Detection** and executed several Nmap scripts to gather more information about the target.

![](../Images/Pasted%20image%2020260420155716.png)

---

# Exploiting SQL Injection

We accessed the login page and tested it for SQL Injection using the following payload:

```sql
' OR 1=1#
```

The payload successfully bypassed the authentication mechanism and granted access to the application.

![](../Images/Pasted%20image%2020260420155852.png)

---

# Uploading a PHP Reverse Shell

After logging in, we noticed that the application allowed file uploads.

![](../Images/Pasted%20image%2020260705203843.png)

We searched for a **PHP Reverse Shell**.

![](../Images/Pasted%20image%2020260705203809.png)

We copied the shell to our machine and modified the callback IP address to point to our attack machine.

![](../Images/Pasted%20image%2020260705204001.png)

Next, we started a Netcat listener.

![](../Images/Pasted%20image%2020260705204042.png)

After uploading the PHP shell and accessing it through the browser, we received a reverse shell.

![](../Images/Pasted%20image%2020260705204130.png)

---

# Enumeration

Once we obtained a shell, we began enumerating the system.

During the enumeration process, we found a **backups** directory under:

```text
/var/backups
```

Inside it, we discovered a file containing credentials for another user.

![](../Images/Pasted%20image%2020260420160320.png)

---

# SSH Access

Using the discovered credentials, we logged into the target via SSH as the user:

```text
mike
```

![](../Images/Pasted%20image%2020260705204508.png)

---

# Checking Sudo Privileges

We checked the commands that the current user could execute with sudo.

```bash
sudo -l
```

The output showed that the user could execute a specific script with **Root** privileges.

![](../Images/Pasted%20image%2020260705204558.png)

---

# Analyzing the Script

We examined the script to understand its functionality.

It turned out that after running the script and typing:

```text
read
```

the script would launch the **nano** editor.

![](../Images/Pasted%20image%2020260705204702.png)

We executed the script and entered:

```text
read
```

which opened nano.

![](../Images/Pasted%20image%2020260705204747.png)

---

# Privilege Escalation via GTFOBins

We searched **GTFOBins** to learn how to exploit **nano** when executed through **sudo**.

![](../Images/Pasted%20image%2020260705204838.png)

Following the GTFOBins instructions, we pressed:

```text
CTRL + R
```

then:

```text
CTRL + X
```

andPasted%20  the command provided by GTFOBins.

![](../Images/Pasted%20image%2020260705204957.png)

This successfully spawned a **Root shell**.

![](../Images/Pasted%20image%2020260705205026.png)

---

# Extracting the Admin Password Hash

After obtaining Root privileges, we connected to the MySQL server.

```bash
mysql -u root
```

![](../Images/Pasted%20image%2020260705205118.png)

We listed the available databases.

```sql
show databases;
```

![](../Images/Pasted%20image%2020260705205231.png)

We selected the application's database.

```sql
use gallery_db;
```

![](../Images/Pasted%20image%2020260705205335.png)

Next, we listed the tables.

```sql
show tables;
```

![](../Images/Pasted%20image%2020260705205416.png)

Finally, we retrieved the usernames and password hashes.

```sql
select username,password from users;
```

As a result, we obtained the password hash of the **admin** user.

![](../Images/Pasted%20image%2020260705205458.png)
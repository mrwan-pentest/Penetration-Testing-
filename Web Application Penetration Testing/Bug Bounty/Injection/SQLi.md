# What is SQL Injection (SQLi)?

SQL Injection (SQLi) is one of the most common and dangerous web application vulnerabilities. It occurs when an application includes unsanitized user input in an SQL query, allowing an attacker to manipulate the database query.

## What Does It Do?

SQL Injection allows an attacker to inject malicious SQL statements into an application's database queries. Depending on the application's permissions, this may allow the attacker to:

- Bypass authentication
- Read sensitive data
- Modify or delete database records
- Execute administrative database operations
- In some cases, achieve Remote Code Execution (RCE)

## Why Is It Dangerous?

A successful SQL Injection attack can compromise the confidentiality, integrity, and availability of the application's data. Since databases often store sensitive information such as user credentials and personal data, SQL Injection remains one of the most critical web vulnerabilities.

## How It Works

Applications commonly build SQL queries using user-supplied input. If that input is not properly validated or parameterized, an attacker can modify the structure of the SQL query and change its intended behavior.

## Example

Instead of executing a query like:

```sql
SELECT * FROM users
WHERE username='admin'
AND password='password';
```

An attacker may inject additional SQL logic to alter the query and bypass authentication.

---

# Lab

## Step 1 - Identifying the Vulnerability

We started by testing the password field with a single quote (`'`). The application returned a database error, indicating that user input was likely being processed directly inside an SQL query. This behavior suggested that the application might be vulnerable to SQL Injection.

![](Penetration%20Testing/Images/Pasted%20image%2020260708205556.png)

Next, we tested the login form by injecting a simple condition after the password input. The application accepted the modified input, further confirming that the login query was vulnerable to SQL Injection.

![](Penetration%20Testing/Images/Pasted%20image%2020260708205639.png)

---

# Exploitation

## Method 1 - Authentication Bypass Using the Password Field

We entered a random password, closed the original SQL statement using a single quote, and then appended an `OR` condition that always evaluated to true.

This caused the authentication query to return a valid result, allowing us to bypass the login page successfully.

![](Penetration%20Testing/Images/Pasted%20image%2020260708210240.png)

---

## Method 2 - Authentication Bypass Using the Username Field

Instead of injecting into the password field, we injected into the username field.

We entered the target username, closed the string using a single quote, and commented out the remainder of the SQL query.

After that, we either entered a random password or left the password field empty. Since the remaining part of the SQL query was ignored, the application authenticated us successfully.

![](Penetration%20Testing/Images/Pasted%20image%2020260708210705.png)

---

## Method 3 - Modifying the Request with Burp Suite

If the application performs stronger input validation or client-side filtering, the HTTP request can be modified using Burp Suite.

First, we submitted the login form using normal credentials without any special characters.

![](Penetration%20Testing/Images/Pasted%20image%2020260708211416.png)

Next, we intercepted the HTTP request using Burp Suite.

![](Penetration%20Testing/Images/Pasted%20image%2020260708211533.png)

After intercepting the request, we modified the SQL Injection payload directly inside the HTTP request before forwarding it to the server.

![](Penetration%20Testing/Images/Pasted%20image%2020260708211937.png)

Finally, we forwarded the modified request.

![](Penetration%20Testing/Images/Pasted%20image%2020260708211620.png)

The server processed the injected payload, and we successfully bypassed the authentication mechanism.

![](Penetration%20Testing/Images/Pasted%20image%2020260708211953.png)

---
# Reading Database Information

## Using `ORDER BY`

The `ORDER BY` clause is normally used to sort query results. During SQL Injection, it is commonly used to determine the number of columns returned by the original SQL query. This information is essential for building successful `UNION SELECT` payloads later in the attack.

If an invalid column index is supplied and the application returns a database error, it indicates that the specified column does not exist. This behavior can also help confirm the presence of an SQL Injection vulnerability.

### Step 1 - Normal Request

We first accessed the application normally to observe its default behavior.

![](Penetration%20Testing/Images/Pasted%20image%2020260708215450.png)

### Step 2 - Testing the First Column

We tested the query using:

```sql
ORDER BY 1
```

This tells the database to sort the results using the first column.

![](Penetration%20Testing/Images/Pasted%20image%2020260708215338.png)

The request executed successfully, confirming that the first column exists.

![](Penetration%20Testing/Images/Pasted%20image%2020260708215426.png)

> **Note**
>
> In the URL, we used `%23` instead of `#`.
>
> `%23` is the URL-encoded representation of the `#` character and should be used when injecting payloads into URLs.

### Step 3 - Testing a Higher Column Number

Next, we tested a much larger column number.

![](Penetration%20Testing/Images/Pasted%20image%2020260708215640.png)

The application returned a database error, indicating that the specified column does not exist. This also suggested that the application was likely vulnerable to SQL Injection.

![](Penetration%20Testing/Images/Pasted%20image%2020260708215718.png)

---

# Reading Database Information

After identifying the SQL Injection vulnerability, the next objective was to determine the correct number of columns returned by the original query.

This is important because `UNION SELECT` requires both queries to return the same number of columns.

We tested multiple values using `ORDER BY` until the application generated an error.

The highest value that executed successfully was **5**, which confirmed that the original query returns **five columns**.

![](Penetration%20Testing/Images/Pasted%20image%2020260708220651.png)

## Using `UNION`

The `UNION` operator combines the results of two or more `SELECT` statements into a single result set.

During SQL Injection, attackers use `UNION SELECT` to retrieve arbitrary information from the database, such as database names, usernames, versions, tables, and sensitive records.

### Displaying the Available Columns

We first identified which columns were reflected in the application's response.

![](Penetration%20Testing/Images/Pasted%20image%2020260708220921.png)

### Retrieving Database Information

After identifying the reflected columns, we extracted useful database information such as:

- Database name
- Current database user
- Database version

![](Penetration%20Testing/Images/Pasted%20image%2020260708221105.png)

![](Penetration%20Testing/Images/Pasted%20image%2020260708221117.png)

---

# Finding Database Tables

Once the database name was identified, the next step was to enumerate its tables.

We queried the `information_schema.tables` table to retrieve all table names belonging to the target database.

```sql
UNION SELECT 1,table_name,NULL,NULL,5
FROM information_schema.tables
WHERE table_schema='owasp10'
```

The `information_schema` database is automatically created by the database management system and stores metadata about databases, tables, columns, and other objects.

The query returned all tables contained within the **owasp10** database.

![](Penetration%20Testing/Images/Pasted%20image%2020260708222505.png)

---

# Extracting Sensitive Data

After discovering the available tables, the next step was to enumerate their columns.

To retrieve all column names from the **accounts** table, we used:

```sql
UNION SELECT 1,column_name,NULL,NULL,5
FROM information_schema.columns
WHERE table_name='accounts'
```

This displayed all columns contained in the **accounts** table.

![](Penetration%20Testing/Images/Pasted%20image%2020260708223241.png)

Once the column names were identified, we extracted sensitive information such as usernames and passwords.

```sql
UNION SELECT 1,username,password,NULL,5
FROM accounts
```

The query successfully returned the usernames and passwords stored in the table.

![](Penetration%20Testing/Images/Pasted%20image%2020260708223718.png)

---
# SQL Injection (Blind)

## What is Blind SQL Injection?

Blind SQL Injection is a type of SQL Injection where the application does **not** display database errors or query results directly.

Instead of seeing the output, the attacker determines whether an injected SQL statement is **true** or **false** by observing changes in the application's behavior.

## How Does It Work?

The attacker injects SQL conditions into the application.

Based on the server's response, they can determine whether the condition is true or false and gradually extract information from the database.

## Types of Blind SQL Injection

### Boolean-Based Blind SQL Injection

The attacker sends conditions that evaluate to either **TRUE** or **FALSE** and observes differences in the application's response.

### Time-Based Blind SQL Injection

The attacker uses database delay functions (such as `SLEEP()`) to determine whether a condition is true based on the server's response time.

## Example

```sql
' AND 1=1 --
```

The page behaves normally because the condition is **TRUE**.

```sql
' AND 1=2 --
```

The page behaves differently because the condition is **FALSE**.

By repeating this process, an attacker can extract database information one character at a time.

```
order by 1
```

```
order by 1000000000000
```

---

 
## Discovering Complex SQL Injection Vulnerabilities

حاولنا نفعل inject بكندشن صحيح عشان نعرف هل سيتم تنفيذ الأمر
ولكن ظهر لنا هذا الخطأ

![](Penetration%20Testing/Images/Pasted%20image%2020260710210208.png)

من الواضح انه الخطأ بسبب أننا كتبنا  كوتس ' 
جربنا الأمر بدونها وتنفذ الأمر بشكل صحيح

![](Penetration%20Testing/Images/Pasted%20image%2020260710210416.png)


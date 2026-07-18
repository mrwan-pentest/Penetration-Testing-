l
## In web applications, Privilege Escalation occurs when a user gains permissions that were not intended for their account.

Instead of becoming **root** or **SYSTEM**, the attacker typically becomes a higher-privileged user, such as an administrator.

---

# Types of Privilege Escalation

## Vertical Privilege Escalation

A low-privileged user gains access to higher privileges.

Example:

```text
User → Admin
```

This is the most common type in web applications.

---

## Horizontal Privilege Escalation

A user accesses another user's account without increasing privilege level.

Example:

```text
User A → User B
```

---

# Common Examples

## Accessing the Admin Panel

A normal user visits:

```text
/admin
```

If access is granted, the application is vulnerable to Vertical Privilege Escalation.

---

## Changing the User Role

Original request:

```http
role=user
```

Modified request:

```http
role=admin
```

If the server accepts the new role, the attacker gains administrator privileges.

---

## Modifying User IDs

Original request:

```http
GET /profile?id=10
```

Modified request:

```http
GET /profile?id=11
```

If another user's profile is displayed, this is Horizontal Privilege Escalation through IDOR.

---

# How Is It Tested?

## A penetration tester may:

- Access hidden pages
    
- Modify request parameters
    
- Change cookies
    
- Manipulate JSON values
    
- Edit HTTP requests using Burp Suite
    

The objective is to determine whether the application properly enforces authorization.

---

# Why Does It Happen?

## Common causes include:

- Missing authorization checks
    
- Trusting client-side data
    
- Insecure role validation
    
- Broken Access Control
    

---

# Prevention

## Every request must be authorized on the server side.

The application should verify:

- Who is making the request
    
- What permissions they have
    
- Whether they are allowed to perform the requested action
    

---

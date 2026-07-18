## What is Broken Access Control?

Broken Access Control occurs when a web application fails to properly enforce user permissions.

As a result, users can access resources or perform actions they are not authorized to access.

---

# What is Access Control?

## Access Control determines:

- Who can access a resource
    
- What actions a user can perform
    
- Which data a user is allowed to view
    

Example:

|User|Permission|
|---|---|
|Admin|Manage users|
|Employee|View own profile|
|Guest|Access public pages|

---

# When Does It Become Broken?

## Access Control is considered broken when the application does not properly verify permissions.

Example:

An administrator accesses:

```text
/admin
```

A normal user manually visits the same URL:

```text
/admin
```

If the page loads successfully, the application is vulnerable to Broken Access Control.

---

# Example 1 – Admin Page Access

A regular user gains access to an administrator page without proper authorization.

This is a Broken Access Control vulnerability.

---

# Why Does It Happen?

## Common causes include:

- Missing permission checks
    
- Trusting client-side data
    
- Relying only on hidden buttons or JavaScript
    
- Insecure server-side authorization
    



---

# Common Types

## Vertical Privilege Escalation

A normal user gains administrator privileges.

---

## Horizontal Privilege Escalation

A user accesses another user's resources.

---

## IDOR

A user modifies an object identifier to access unauthorized data.

---

## Forced Browsing

A user directly accesses hidden or restricted pages by guessing or entering the URL.

---

# Prevention

## Applications should always verify permissions on the server side.

Never rely on:

- Hidden buttons
    
- Client-side validation
    
- JavaScript restrictions
    

Every request must be authorized by the server.

---

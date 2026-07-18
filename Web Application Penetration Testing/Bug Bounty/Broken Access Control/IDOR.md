رف# IDOR (Insecure Direct Object Reference)

## IDOR is a vulnerability that allows a user to access another user's data by modifying an object identifier, such as an ID, filename, or account number.

It is one of the most common types of **Broken Access Control**.

---

# How Does It Work?

## The application does not verify whether the user is authorized to access the requested resource.

Instead, it only checks the object identifier.

---

# Example

Original request:

```http
GET /profile?id=15
```

Modified request:

```http
GET /profile?id=16
```

If another user's profile is displayed, the application is vulnerable to IDOR.

---

# Why Does It Happen?

## The server trusts user-supplied identifiers without performing proper authorization checks.

---

# What Can an Attacker Access?

- User profiles
    
- Orders
    
- Invoices
    
- Documents
    
- Uploaded files
    
- Private messages
    

---

# How Is It Tested?

## A penetration tester modifies object identifiers in:

- URL parameters
    
- POST parameters
    
- JSON requests
    
- Cookies
    
- API endpoints
    

Then checks whether unauthorized data is returned.

---

# Prevention

## The server must verify that the authenticated user is authorized to access the requested resource before returning any data.

---
 
## What is OAuth?

OAuth is an **authorization protocol** that allows a third-party application to access a user's resources **without knowing the user's password**.

It is commonly used with:

- Google
    
- GitHub
    
- Microsoft
    
- Facebook
    

Example:

```text
Continue with Google
```

---

# Authentication vs Authorization

## Authentication

Authentication answers the question:

> **Who are you?**

The user proves their identity by logging in with valid credentials.

---

## Authorization

Authorization answers the question:

> **What are you allowed to access?**

The user grants permission for an application to access specific resources.

OAuth is designed to handle **authorization**, not authentication.

---

# How OAuth Works

1. The user clicks **"Login with Google."**
    
2. The application redirects the user to Google's login page.
    
3. The user authenticates with Google.
    
4. Google asks the user to approve the requested permissions.
    
5. Google returns an **Authorization Code**.
    
6. The application exchanges the code for an **Access Token**.
    
7. The application uses the Access Token to retrieve the user's information.
    

---

# Access Token

An **Access Token** is a temporary credential that allows an application to access protected resources on behalf of the user.

The application receives the token instead of the user's password.

---

# Why Is OAuth Secure?

The user's password is only shared with the identity provider (such as Google).

The third-party application never sees or stores the user's credentials.

---

# OAuth Vulnerabilities

OAuth itself is **not a vulnerability**.

Most security issues occur because of **incorrect implementation**.

---

# 1. Improper Redirect URI Validation

After successful authentication, the identity provider redirects the user back to the application.

Example:

```text
https://shop.com/callback
```

If the application does not properly validate the **redirect_uri**, an attacker may replace it with:

```text
https://evil.com/callback
```

As a result, the Authorization Code or Access Token may be sent to the attacker's server.

---

# 2. Missing State Parameter

OAuth uses a parameter called **state** to prevent CSRF attacks.

Example:

```text
state=9f82ab31
```

The application must verify that the returned state value matches the original request.

If the validation is missing, an attacker may perform CSRF or account-linking attacks.

---

# 3. Access Token Leakage

An application may accidentally expose an Access Token through:

- URL parameters
    
- Browser history
    
- Referer headers
    
- Server logs
    

If an attacker obtains the token, they may access the victim's account.

---

# 4. Account Takeover

Poor account linking logic may allow an attacker to associate their OAuth account with another user's account.

This can result in unauthorized access to the victim's account.

---

# Common OAuth Attack Flow

1. The attacker identifies a vulnerable OAuth implementation.
    
2. The attacker steals an Authorization Code or Access Token.
    
3. The attacker exchanges the code for a valid Access Token (if necessary).
    
4. The attacker accesses the victim's account using the stolen token.
    

---


# Cross-Site Request Forgery (CSRF)

## What is CSRF?

**Cross-Site Request Forgery (CSRF)** is a web vulnerability that tricks a **logged-in user** into sending an unwanted request to a trusted website.

The attacker does **not** steal the user's password or session.

Instead, they abuse the user's authenticated session.

---

# How Does CSRF Work?

1. The victim logs into a website (e.g., an online bank).
    
2. The website creates a valid **session cookie**.
    
3. The victim visits a malicious website.
    
4. The malicious website automatically sends a request to the trusted website.
    
5. The browser includes the victim's session cookie automatically.
    
6. The trusted website believes the request came from the legitimate user and processes it.
    

---

# Example

A user is logged into:

```text
https://bank.com
```

The attacker hosts the following page:

```html
<form action="https://bank.com/transfer" method="POST">
    <input type="hidden" name="to" value="Attacker">
    <input type="hidden" name="amount" value="5000">
</form>

<script>
document.forms[0].submit();
</script>
```

When the victim opens the malicious page, the browser automatically submits the request.

Since the victim is already authenticated, the bank processes the transfer.

---

# Why Is CSRF Dangerous?

An attacker may force a victim to:

- Transfer money
    
- Change an email address
    
- Change a password
    
- Delete an account
    
- Add a new administrator
    
- Perform any action that requires authentication
    

---

# Why Does It Work?

The browser automatically sends **session cookies** with requests to the trusted website.

If the application only checks whether the user is authenticated, it cannot distinguish between a legitimate request and a forged one.

---

# How to Prevent CSRF

Common defenses include:

- **CSRF Tokens**
    
- **SameSite Cookies**
    
- **Origin/Referer Validation**
    
- Re-authentication for sensitive actions
    


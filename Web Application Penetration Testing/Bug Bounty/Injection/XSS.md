# Cross-Site Scripting (XSS)

## What is XSS?

**Cross-Site Scripting (XSS)** is a web application vulnerability that allows an attacker to inject and execute **malicious JavaScript code** inside a victim's browser.

Unlike **Command Injection**, the code is **not executed on the server**. Instead, it runs in the victim's web browser.

---

# How XSS Works

A web application accepts user input and displays it back to users.

If the application does **not** properly validate, sanitize, or encode the input, an attacker can inject JavaScript instead of normal text.

Example:

```html
<script>alert("XSS")</script>
```

When another user visits the vulnerable page, the browser executes the injected script.

---

# Impact

A successful XSS attack may allow an attacker to:

- Steal session cookies
    
- Steal authentication tokens
    
- Perform actions on behalf of the victim
    
- Modify the content of the web page
    
- Redirect users to malicious websites
    
- Capture user input (Keylogging)
    

---

# Types of XSS

## 1. Reflected XSS

The malicious payload is included in the HTTP request and immediately reflected in the server's response.

The victim usually needs to click a malicious link.

---

## 2. Stored XSS

The malicious payload is permanently stored on the server, such as in:

- Comments
    
- Forum posts
    
- User profiles
    
- Messages
    

Every user who visits the affected page executes the malicious script.

---

## 3. DOM-Based XSS

The vulnerability exists in the client-side JavaScript.

The browser modifies the **Document Object Model (DOM)** using untrusted user input without proper validation.

The server is not directly involved.

---

# Where Does XSS Execute?

XSS executes inside the **victim's browser**.

It does **not** execute on the web server.


---

# OWASP Category

According to **OWASP Top 10 (2021)**, XSS is classified under:

```text
OWASP Top 10
│
└── Injection
    └── Cross-Site Scripting (XSS)
```

XSS is considered an **Injection** vulnerability because it allows an attacker to inject malicious JavaScript into a web page.


---

# Prevention

- Validate all user input.
    
- Encode output before displaying it in HTML.
    
- Sanitize user-supplied data.
    
- Implement a strong **Content Security Policy (CSP)**.
    
- Mark cookies as **HttpOnly** to reduce the risk of cookie theft.
    

---
# Discovering Basic Reflected XSS

## Step 1 - Test for XSS

To verify whether the application was vulnerable to **Reflected XSS**, we injected a simple JavaScript payload that displays an alert dialog.

If the application reflects the input without proper sanitization, the browser executes the script immediately.

![](../../../Images/Pasted%20image%2020260711205947.png)

## Step 2 - Confirm the Vulnerability

After submitting the payload, the alert dialog appeared in the browser, confirming that the application was vulnerable to Reflected XSS.

![](../../../Images/Pasted%20image%2020260711210108.png)

---

# Discovering Advanced Reflected XSS

Some applications attempt to block XSS by filtering specific keywords such as `<script>`.

Since HTML tag names are case-insensitive, a simple blacklist can often be bypassed by changing the capitalization of the tag.

For example:

```html
<scriPT>alert("XSS")</SCRipt>
```

![](../../../Images/Pasted%20image%2020260711211139.png)

The payload bypassed the filter and executed successfully.

![](../../../Images/Pasted%20image%2020260711211201.png)

---

# Discovering Stored XSS

## Step 1 - Inject a Persistent Payload

Unlike Reflected XSS, **Stored XSS** stores the malicious payload on the server, such as in a comment section, profile field, or message board.

We submitted a JavaScript payload that was stored by the application.

![](../../../Images/Pasted%20image%2020260714204213.png)

## Step 2 - Verify Persistent Execution

Each time a user visits the affected page, the stored payload is automatically executed in their browser.

This behavior confirms the presence of a Stored XSS vulnerability.

![](../../../Images/Pasted%20image%2020260714204312.png)

---

# Discovering Advanced Stored XSS

## Bypassing Input Length Restrictions

Initially, the input field restricted the number of characters that could be entered, preventing us from submitting a complete XSS payload.

![](../../../Images/Pasted%20image%2020260714204723.png)

Since this restriction was enforced only on the client side, we modified the page's HTML source code.

## Step 1 - Modify the Input Length

We inspected the page source and located the input field.

![](../../../Images/Pasted%20image%2020260714204841.png)

The field allowed only ten characters.

We increased the maximum length to one hundred characters.

![](../../../Images/Pasted%20image%2020260714204921.png)

After modifying the input length, we were able to enter the full payload.

To bypass the application's keyword filter, we also changed the capitalization of the `<script>` tag.

![](../../../Images/Pasted%20image%2020260714205534.png)

The payload executed successfully.

![](../../../Images/Pasted%20image%2020260714205550.png)

---

## Bypassing Quote Filters

Some applications filter single quotes (`'`) or double quotes (`"`), making it difficult to inject JavaScript strings.

One common bypass technique is to represent the string using ASCII character codes with the `String.fromCharCode()` function.

To generate the character codes, we used an online converter.

```text
https://charcode98.neocities.org/
```

![](../../../Images/Pasted%20image%2020260714210358.png)

The generated character codes were then passed to `String.fromCharCode()`.

```html
<scriPt>alert(String.fromCharCode(120,115,115,50))</scriPT>
```

Each ASCII value must be separated by a comma.

Using this technique, the payload successfully bypassed the filter and executed.

![](../../../Images/Pasted%20image%2020260714211247.png)
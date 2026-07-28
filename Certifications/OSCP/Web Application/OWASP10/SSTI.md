# Server-Side Template Injection (SSTI)

## What is SSTI?

**Server-Side Template Injection (SSTI)** is a web vulnerability that occurs when user input is **embedded directly into a server-side template** without proper sanitisation.

This allows an attacker to inject **template expressions**, which are executed by the template engine on the server.

Unlike **XSS**, where code executes in the victim's browser, **SSTI executes on the server**.

---

# How Does SSTI Work?

Many web applications use **Template Engines** to generate dynamic HTML pages.

Example:

```python
Hello {{ username }}
```

If the user enters:

```text
John
```

The page becomes:

```text
Hello John
```

However, if the application inserts user input directly into the template, an attacker may inject template syntax.

For example:

```text
{{7*7}}
```

Instead of displaying the text literally, the template engine evaluates the expression and returns:

```text
49
```

This confirms that the application is vulnerable to SSTI.

---

# Common Template Engines

## Python

- Jinja2
- Tornado
- Mako

---

## PHP

- Twig
- Smarty

---

## Java

- FreeMarker
- Velocity
- Thymeleaf

---

## Node.js

- Pug
- Handlebars
- EJS

---

# Example

Suppose a web application contains the following code:

```python
return render_template("Hello " + username)
```

Normal input:

```text
John
```

Output:

```text
Hello John
```

Attacker input:

```text
{{7*7}}
```

Output:

```text
Hello 49
```

This indicates that the server evaluated the injected template expression.

---

# Typical SSTI Payloads

Simple arithmetic:

```text
{{7*7}}
```

```text
${7*7}
```

```text
<%= 7*7 %>
```

Different template engines use different syntax.

---

# Why is SSTI Dangerous?

If an attacker gains access to the template engine, they may be able to:

- Execute server-side code
- Read sensitive files
- Access environment variables
- Execute operating system commands
- Achieve Remote Code Execution (RCE)

---

# Possible Impacts

An attacker may be able to:

- Read application files
- Read configuration files
- Access secrets and API keys
- Execute system commands
- Gain Remote Code Execution (RCE)
- Completely compromise the server

---

# How to Identify SSTI

Look for user input that is rendered inside server-generated pages.

Common locations include:

- Search fields
- Username fields
- Email templates
- Error messages
- Profile pages
- Report generators

A simple test payload is:

```text
{{7*7}}
```

If the application returns:

```text
49
```

instead of:

```text
{{7*7}}
```

the input is likely being evaluated by the template engine.

---

# SSTI vs XSS

| Feature | SSTI | XSS |
|---------|------|-----|
| Executes On | Server | Client (Browser) |
| Target | Template Engine | Browser |
| Main Impact | Remote Code Execution (RCE), File Read | JavaScript Execution |
| Severity | Usually Critical | Medium to High |

---

# Prevention

To prevent SSTI:

- Never concatenate user input directly into templates.
- Treat user input as plain text, not template code.
- Use safe template rendering functions.
- Keep template engines up to date.
- Restrict dangerous template functions and objects.
- Validate and sanitise user input.

---

# Summary

- **SSTI** occurs when user input is evaluated by a **server-side template engine**.
- Attackers can inject template expressions that execute on the server.
- Successful exploitation may lead to **file disclosure**, **system command execution**, and even **Remote Code Execution (RCE)**.
- Always render user input as **data**, not as executable template code.
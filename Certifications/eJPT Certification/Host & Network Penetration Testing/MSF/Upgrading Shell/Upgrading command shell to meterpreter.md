# Upgrading a Shell to Meterpreter

Sometimes, after exploiting a target, you only obtain a standard command shell. While functional, a basic shell has limited capabilities compared to a Meterpreter session.

To upgrade a normal shell into a Meterpreter session, Metasploit provides a dedicated post-exploitation module.

---

# Method 1: Using the `shell_to_meterpreter` Module

Use the following module:

```text
post/multi/manage/shell_to_meterpreter
```

This module automatically uploads the required Meterpreter payload to the target and migrates the current shell into a fully interactive Meterpreter session.

![](Penetration%20Testing/Images/Pasted%20image%2020260527163540.png)

### Advantages

- Converts a standard shell into Meterpreter.
- No need to re-exploit the target.
- Provides access to all Meterpreter features such as:
  - File upload/download
  - Process migration
  - Privilege escalation modules
  - Screenshot capture
  - Credential dumping
  - Network pivoting

---

# Method 2: Using the `sessions` Command

Another way to upgrade or interact with sessions is through Metasploit's built-in `sessions` command.

![](Penetration%20Testing/Images/Pasted%20image%2020260527163821.png)

Some commonly used options include:

```text
sessions
```

Lists all active sessions.

```text
sessions -i <ID>
```

Interact with a specific session.

```text
sessions -u <ID>
```

Attempt to upgrade a shell session to a Meterpreter session automatically.

---

# Summary

A standard shell provides basic command execution, while a Meterpreter session offers a much more powerful post-exploitation environment.

The two most common ways to upgrade a shell are:

1. Using the `post/multi/manage/shell_to_meterpreter` module.
2. Using the built-in `sessions -u <Session_ID>` command.

Whenever possible, upgrading to Meterpreter is recommended because it provides significantly more functionality for post-exploitation tasks.
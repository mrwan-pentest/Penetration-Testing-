# What is msfdb?

Simply put:

Metasploit uses a:

## Database

to store:

- Nmap scan results
- Hosts
- Vulnerabilities
- Sessions
- Credentials
- Workspaces

---

# Which Database Does It Use?

Metasploit relies on:

## PostgreSQL

as its backend database.

---

# What Happens Without a Database?

Metasploit will still function, but:

- Results will not be organized
- Scan data will not be saved
- Several features will be unavailable

---

# Starting the PostgreSQL Service

```bash
sudo systemctl start postgresql
```

### What Does This Command Do?

It starts the:

## PostgreSQL Database Server

---

# Enable PostgreSQL at Boot

```bash
sudo systemctl enable postgresql
```

### Why?

So that PostgreSQL starts automatically every time the system boots, eliminating the need to start it manually.

---

# Check the Service Status

```bash
sudo systemctl status postgresql
```

---

If you see:

```text
active (running)
```

then PostgreSQL is running successfully.

---

# Initializing msfdb

Before using the database with Metasploit, initialize it with:

```bash
sudo msfdb init
```

---

# What Does This Command Do?

It automatically performs the following tasks:

| Task | Purpose |
|------|---------|
| Creates a database | For Metasploit |
| Creates a database user | Used for authentication |
| Connects Metasploit to PostgreSQL | Automatically |
| Configures the environment | Completes the initial setup |

---

If the initialization succeeds, you'll typically see a message similar to:

```text
Database started
```

or

```text
Successfully connected
```

---

# Launch Metasploit

```bash
msfconsole
```

---

# Verify the Database Connection

Inside Metasploit, run:

```text
db_status
```

---

If the output is:

```text
Connected to msf
```

then the database is properly connected and ready to use.

---

![[Pasted image 20260523170606.png]]

![[Pasted image 20260523170623.png]]

![[Pasted image 20260523170637.png]]
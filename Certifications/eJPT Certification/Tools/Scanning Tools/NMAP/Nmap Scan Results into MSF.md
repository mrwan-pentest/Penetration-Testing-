# Importing Nmap Results into Metasploit Database

Metasploit can integrate with Nmap scan results by importing the scan output into its database.

The main benefit is:

```
Connecting the Scanning phase with the Exploitation phase
```

Instead of manually transferring information between tools, Metasploit can store and manage:

- Hosts
- Open Ports
- Running Services
- Vulnerabilities

This makes the penetration testing workflow more organized and efficient.

---

# Step 1 — Save Nmap Scan Results as XML

Metasploit can import Nmap results only from supported formats, and XML is the most commonly used format.

Run Nmap and save the output:

```
nmap -sV -oX scan.xml TARGET
```

## Explanation

- `-sV`  
    Performs Service Version Detection.
- `-oX`  
    Saves the output in XML format.
- `scan.xml`  
    The file that contains the Nmap results.

Example:

```
nmap -sV -oX target_scan.xml 192.168.1.10
```

---

# Step 2 — Start Metasploit Database

Launch Metasploit:

```
msfconsole
```

Metasploit uses a database to store scan information.

---

# Checking Database Status

Command:

```
db_status
```

## Purpose

Checks whether the Metasploit database is connected.

Example output:

```
[*] Connected to msf database
```

---

# Step 3 — Manage Workspaces

Workspaces help organize different penetration testing projects.

---

## View Existing Workspaces

Command:

```
workspace
```

## Purpose

Displays all available workspaces.

Example:

```
default
test_lab
client_project
```

---

## Create a New Workspace

Command:

```
workspace -a name
```

Example:

```
workspace -a internal_network
```

## Purpose

Creates a new workspace called:

```
internal_network
```

This keeps scan results separated from other projects.

---

# Step 4 — Import Nmap Results

Command:

```
db_import scan.xml
```

## Purpose

Imports the Nmap XML scan results into the Metasploit database.

Example:

```
db_import target_scan.xml
```

After importing, Metasploit stores:

- Target hosts
- Open ports
- Services
- Vulnerability information

---

# Step 5 — View Imported Information

After importing the scan, several commands can be used to review the results.

---

# Display Hosts

Command:

```
hosts
```

## Purpose

Shows discovered target systems.

Example information:

- IP Address
- Hostname
- Operating System

---

# Display Services

Command:

```
services
```

## Purpose

Displays discovered services and open ports.

Example:

```
PORT     SERVICE     VERSION
22       SSH         OpenSSH
80       HTTP        Apache
445      SMB         Windows SMB
```

---

# Display Vulnerabilities

Command:

```
vulns
```

## Purpose

Shows discovered vulnerabilities stored in the database.

Example:

```
Host        Vulnerability
192.168.1.10   MS17-010
```

---

# Workflow Summary

```
Nmap Scan
    |
    v
Save Results as XML
    |
    v
Start Metasploit
    |
    v
Connect Database
    |
    v
Create Workspace
    |
    v
Import XML Results
    |
    v
View Hosts / Services / Vulnerabilities
    |
    v
Begin Exploitation
```

---

# Common Commands Summary

|Command|Purpose|
|---|---|
|`db_status`|Check database connection|
|`workspace`|List workspaces|
|`workspace -a name`|Create a new workspace|
|`db_import file.xml`|Import Nmap XML results|
|`hosts`|Display discovered hosts|
|`services`|Display open ports and services|
|`vulns`|Display vulnerabilities|

This integration allows a smoother workflow between **Enumeration** and **Exploitation** inside Metasploit.
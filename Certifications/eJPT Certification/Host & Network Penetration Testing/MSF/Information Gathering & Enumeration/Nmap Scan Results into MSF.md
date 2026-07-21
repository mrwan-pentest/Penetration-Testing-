# Importing Nmap Scan Results into Metasploit

The primary benefit of importing Nmap results into Metasploit is:

```text
Seamlessly integrating the scanning phase with the exploitation phase.
```

Instead of scanning the target again, Metasploit can directly use the imported information to enumerate services, search for exploits, and manage targets.

---

# Step 1: Save the Nmap Scan as XML

First, save the Nmap scan results in XML format.

![](../../../../../Images/Pasted%20image%2020260513232600.png)

---

# Step 2: Start the Database

Start the PostgreSQL database used by Metasploit.

![](../../../../../Images/Pasted%20image%2020260513232702.png)

---

# Step 3: Verify the Database Status

Check that the database is connected.

```text
db_status
```

---

# Step 4: Display Existing Workspaces

List all available workspaces.

```text
workspace
```

---

# Step 5: Create a New Workspace

Create a workspace for the current engagement.

```text
workspace -a name
```

---

# Step 6: Import the Nmap Scan

Import the previously saved XML scan into the active workspace.

```text
db_import
```

![](../../../../../Images/Pasted%20image%2020260513232801.png)

---

# Database Query Commands

After importing the scan, Metasploit provides several commands to browse the collected information.

## Display Imported Hosts

```text
hosts
```

Shows all discovered target systems.

---

## Display Services

```text
services
```

Lists the open ports and the services running on each host.

---

## Display Vulnerabilities

```text
vulns
```

Displays any vulnerabilities associated with the imported hosts, if available.

![](../../../../../Images/Pasted%20image%2020260513233241.png)
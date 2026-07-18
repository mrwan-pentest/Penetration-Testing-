# What is a Workspace?

A **Workspace** is a separate project environment within Metasploit.

It stores information related to a specific engagement, including:

- Hosts
- Nmap scan results
- Services
- Sessions
- Credentials

---

# Why Use Workspaces?

Imagine you're working on multiple engagements at the same time:

- Company A
- Company B
- An eJPT lab

Without workspaces, all collected data would be stored together, making it difficult to stay organized.

With workspaces, each project has its own isolated environment.

| Workspace | Contains |
|-----------|----------|
| `companyA` | Assets and results for Company A |
| `companyB` | Assets and results for Company B |
| `ejpt-lab` | Systems and data for the eJPT lab |

---

# Workspace Commands

## Display Existing Workspaces

```text
workspace
```

Lists all available workspaces and indicates the currently active one.

---

## Create a New Workspace

```text
workspace -a ejpt
```

Creates a new workspace named:

```text
ejpt
```

---

## Switch Between Workspaces

```text
workspace ejpt
```

Changes the active workspace to:

```text
ejpt
```

---

## Delete a Workspace

```text
workspace -d ejpt
```

Deletes the specified workspace and its stored data.

---

## Rename a Workspace

```text
workspace -r oldname newname
```

Renames an existing workspace from:

```text
oldname
```

to:

```text
newname
```
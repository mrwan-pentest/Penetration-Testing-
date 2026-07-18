
# Understanding the .git Directory

## What is .git?

The `.git` directory is a hidden folder created by Git.

It contains all repository information, including:

- Commit history
    
- Branches
    
- Configuration
    
- Tags
    
- References
    
- Object database
    

Example:

```text
project/
├── index.php
├── login.php
└── .git/
```

Without the `.git` directory, Git cannot track changes.

---

# Why is .git Important in Pentesting?

Sometimes developers accidentally expose:

```text
.git/
```

on a web server.

If accessible, an attacker may recover:

- Source code
    
- Deleted files
    
- Credentials
    
- API keys
    
- Configuration files
    
- Development history
    

This can reveal sensitive information not visible on the website itself.

---

# What is Git?

Git is a Version Control System (VCS).

It helps developers:

- Track code changes
    
- Collaborate with teams
    
- Restore previous versions
    
- Manage project history
    

---

# Basic Git Workflow

```text
Working Directory
       ↓
      Git
       ↓
    Commits
       ↓
 Repository History
```

Every change can be saved as a:

```text
Commit
```

A commit is like a snapshot of the project at a specific point in time.

---

# Useful Git Commands

## Check Repository Status

```bash
git status
```

Shows:

- Modified files
    
- New files
    
- Deleted files
    

---

## View Commit History

```bash
git log
```

Short version:

```bash
git log --oneline
```

---

## Show Commit Details

```bash
git show <commit-id>
```

Example:

```bash
git show a1b2c3d
```

---

## View Branches

```bash
git branch
```

All branches:

```bash
git branch -a
```

---

## View File from an Old Commit

```bash
git show <commit-id>:config.php
```

Useful for finding deleted credentials or old configurations.

---

## Compare Changes

```bash
git diff
```

Shows differences between versions.

---

## Search for Sensitive Information

```bash
git log -p
```

Displays commits with code changes.

Look for:

- Passwords
    
- API Keys
    
- Database Credentials
    
- Hidden Endpoints
    

---

# Most Useful Commands for Pentesting

```bash
git log --oneline
git log -p
git show <commit-id>
git diff
git branch -a
git status
```

These commands are usually enough to investigate an exposed Git repository and recover valuable information.
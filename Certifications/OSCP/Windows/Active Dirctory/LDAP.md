
# LDAP (Lightweight Directory Access Protocol)

## Overview

**LDAP (Lightweight Directory Access Protocol)** is a network protocol used to **access, query, and manage information stored in a Directory Service**.

A Directory can be thought of as a structured database containing information about users, computers, groups, and other objects within an organization.

For example:

```
Domain
│
├── Users
│   ├── Ahmed
│   ├── Ali
│   └── Mohammed
│
├── Groups
│   ├── Domain Admins
│   └── IT
│
└── Computers
    ├── PC-01
    └── DC-01
```

LDAP allows applications and systems to communicate with this Directory and perform queries such as:

- Find users.
- Find groups.
- Find computers.
- Determine which groups a user belongs to.
- Retrieve attributes associated with an object.
- Search for specific objects within the Directory.

---

## LDAP and Active Directory

LDAP is a **protocol**, while **Active Directory (AD)** is a Directory Service developed by Microsoft.

Active Directory uses LDAP as one of its main protocols for accessing Directory information.

The relationship can be visualized as:

```
             LDAP
              │
              ▼
┌──────────────────────────┐
│     Active Directory     │
│                          │
│ Users                    │
│ Groups                   │
│ Computers                │
│ Organizational Units     │
│ Permissions              │
│ Other Directory Objects  │
└──────────────────────────┘
```

Therefore:

> **LDAP is not Active Directory. LDAP is a protocol used to communicate with and query Active Directory.**

---

## Example

Suppose an organization has an Active Directory domain:

```
corp.local
```

A system could use LDAP to query the Domain Controller and ask:

```
"Give me all users in the domain."
```

The Directory might return:

```
Administrator
Ahmed
Ali
Bob
```

Another query could ask:

```
"Which groups does Ahmed belong to?"
```

And the Directory might return:

```
Domain Users
IT
```

The important idea is that LDAP provides the mechanism for **searching and retrieving this Directory information**.

---

## LDAP in Active Directory Enumeration

LDAP is particularly important during **Active Directory Enumeration**.

When performing enumeration, an attacker or security tester may want to discover information such as:

```
Users
Groups
Computers
Domain information
Group memberships
Organizational Units (OUs)
Trust relationships
Other AD objects and attributes
```

Tools such as **PowerView** can perform various Active Directory enumeration tasks and retrieve information from the domain, including through LDAP.

This makes understanding LDAP important when learning **Active Directory Pentesting**.

---

## Simple Mental Model

Think of Active Directory as a large organizational directory:

```
Active Directory
       │
       │ contains
       ▼
Users / Groups / Computers / OUs
       ▲
       │
       │ queried through
       │
      LDAP
```

### Key Takeaway

> **LDAP is a protocol used to communicate with a Directory Service and query its information. In an Active Directory environment, LDAP allows systems and tools to search and retrieve information about users, groups, computers, and other AD objects.**
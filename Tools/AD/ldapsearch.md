## Overview

`ldapsearch` is a command-line tool used to **query LDAP Directory Services**.

In an **Active Directory** environment, it can be used to enumerate information such as:

- Users
- Groups
- Computers
- Domain information
- User attributes
- Group memberships

The basic idea is:

```
ldapsearch → LDAP Query → Domain Controller → Active Directory
```

---

## Basic Syntax

```
ldapsearch -x -H <LDAP_SERVER> -b "<BASE_DN>" "<FILTER>"
```

Important options:

|Option|Purpose|
|---|---|
|`-x`|Use Simple Authentication|
|`-H`|Specify the LDAP server|
|`-D`|Specify the account used for authentication|
|`-w`|Provide the password|
|`-W`|Prompt for the password|
|`-b`|Specify the Base DN|
|`-s sub`|Search the Base DN and its subtrees|

---

## Base DN

The Active Directory domain:

```
corp.local
```

is represented as:

```
DC=corp,DC=local
```

For example:

```
example.com
```

becomes:

```
DC=example,DC=com
```

---

# Common Commands

## 1. Anonymous LDAP Search

If the LDAP server allows anonymous access:

```
ldapsearch -x -H ldap://10.10.10.10 -b "DC=corp,DC=local"
```

This attempts to query the Directory without providing credentials.

---

## 2. Authenticated Search

When authentication is required:

```
ldapsearch -x \
-H ldap://10.10.10.10 \
-D "user@corp.local" \
-W \
-b "DC=corp,DC=local"
```

`-W` prompts you for the password instead of placing it directly in the command.

---

## 3. Enumerate Users

To find Active Directory users:

```
ldapsearch -x \
-H ldap://10.10.10.10 \
-D "user@corp.local" \
-W \
-b "DC=corp,DC=local" \
"(objectClass=user)"
```

To display only usernames:

```
ldapsearch -x \
-H ldap://10.10.10.10 \
-D "user@corp.local" \
-W \
-b "DC=corp,DC=local" \
"(objectClass=user)" \
sAMAccountName
```

`sAMAccountName` is the traditional Windows logon name.

---

## 4. Enumerate Groups

To find groups:

```
ldapsearch -x \
-H ldap://10.10.10.10 \
-D "user@corp.local" \
-W \
-b "DC=corp,DC=local" \
"(objectClass=group)"
```

To display group names:

```
ldapsearch -x \
-H ldap://10.10.10.10 \
-D "user@corp.local" \
-W \
-b "DC=corp,DC=local" \
"(objectClass=group)" \
sAMAccountName
```

---

## 5. Enumerate Computers

To find computers in the Domain:

```
ldapsearch -x \
-H ldap://10.10.10.10 \
-D "user@corp.local" \
-W \
-b "DC=corp,DC=local" \
"(objectClass=computer)"
```

To display their hostnames:

```
ldapsearch -x \
-H ldap://10.10.10.10 \
-D "user@corp.local" \
-W \
-b "DC=corp,DC=local" \
"(objectClass=computer)" \
dNSHostName
```

---

## 6. Search for a Specific User

To search for a specific username:

```
ldapsearch -x \
-H ldap://10.10.10.10 \
-D "user@corp.local" \
-W \
-b "DC=corp,DC=local" \
"(sAMAccountName=administrator)"
```

You can also search using a wildcard:

```
(sAMAccountName=admin*)
```

This searches for accounts whose `sAMAccountName` starts with `admin`.

---

## 7. Retrieve Specific Attributes

Instead of displaying all available information, specify the attributes you want:

```
ldapsearch -x \
-H ldap://10.10.10.10 \
-D "user@corp.local" \
-W \
-b "DC=corp,DC=local" \
"(objectClass=user)" \
sAMAccountName displayName mail
```

This requests:

```
sAMAccountName
displayName
mail
```

---

## 8. Search for Members of a Group

You can search for users belonging to a specific group using the `memberOf` attribute:

```
(memberOf=CN=Domain Admins,CN=Users,DC=corp,DC=local)
```

For example:

```
ldapsearch -x \
-H ldap://10.10.10.10 \
-D "user@corp.local" \
-W \
-b "DC=corp,DC=local" \
"(memberOf=CN=Domain Admins,CN=Users,DC=corp,DC=local)" \
sAMAccountName
```

---

# Important LDAP Filters

These are the main filters worth remembering:

|Purpose|LDAP Filter|
|---|---|
|Users|`(objectClass=user)`|
|Groups|`(objectClass=group)`|
|Computers|`(objectClass=computer)`|
|Specific user|`(sAMAccountName=alice)`|
|Users starting with `admin`|`(sAMAccountName=admin*)`|
|Objects with an email|`(mail=*)`|
|Members of a group|`(memberOf=...)`|

---

# LDAP vs LDAPS

LDAP commonly uses:

```
ldap://
```

and TCP port:

```
389
```

LDAPS uses:

```
ldaps://
```

and commonly TCP port:

```
636
```

Example:

```
ldapsearch -x \
-H ldaps://10.10.10.10:636 \
-D "user@corp.local" \
-W \
-b "DC=corp,DC=local" \
"(objectClass=user)"
```

---

# Quick Enumeration Cheat Sheet

```
# Users
ldapsearch -x -H ldap://DC_IP -D "user@domain.local" -W \
-b "DC=domain,DC=local" "(objectClass=user)" sAMAccountName

# Groups
ldapsearch -x -H ldap://DC_IP -D "user@domain.local" -W \
-b "DC=domain,DC=local" "(objectClass=group)" sAMAccountName

# Computers
ldapsearch -x -H ldap://DC_IP -D "user@domain.local" -W \
-b "DC=domain,DC=local" "(objectClass=computer)" dNSHostName

# Specific user
ldapsearch -x -H ldap://DC_IP -D "user@domain.local" -W \
-b "DC=domain,DC=local" "(sAMAccountName=USER)"

# Specific attributes
ldapsearch -x -H ldap://DC_IP -D "user@domain.local" -W \
-b "DC=domain,DC=local" "(objectClass=user)" sAMAccountName mail
```

## Key Takeaway

> **`ldapsearch` allows you to directly query Active Directory through LDAP.**
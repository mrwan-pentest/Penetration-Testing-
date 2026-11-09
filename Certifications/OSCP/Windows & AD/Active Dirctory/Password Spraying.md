## Overview

**Password Spraying** is an attack where an attacker tries **one password against many user accounts** instead of trying many passwords against one account.

The goal is often to avoid triggering account lockout policies.

```
Brute Force:
user1 → Password1, Password2, Password3...

Password Spraying:
Password123 → user1, user2, user3...
```

If the password is valid for an account, the attacker obtains **valid credentials**. What they can access afterward depends on that account's permissions.

## Attack Flow

```
Obtain Username List
        ↓
Choose Common Password
        ↓
Try Password Against Multiple Accounts
        ↓
Valid Credentials Found
        ↓
Authenticate to Allowed Services
```

## Example

Suppose we have:

```
user1
user2
user3
user4
```

Instead of trying many passwords against `user1`, we try one password such as:

```
Winter2026!
```

against all four accounts.

If `user3` uses that password, we have valid credentials for `user3`.

## Key Difference

| Attack                  | Approach                                          |
| ----------------------- | ------------------------------------------------- |
| **Brute Force**         | Many passwords → One account                      |
| **Password Spraying**   | One password → Many accounts                      |
| **Credential Stuffing** | Known username/password pairs → Multiple accounts |


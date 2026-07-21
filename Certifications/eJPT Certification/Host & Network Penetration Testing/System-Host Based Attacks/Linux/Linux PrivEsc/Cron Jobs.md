# Cron Jobs

## What is Cron?

Cron is a job scheduling service available on Linux and Unix systems that automatically executes commands or scripts at specified times.

It can be configured to run tasks:

- Every minute.
- Every hour.
- Daily.
- Weekly.
- Monthly.
- At system startup.

Cron is commonly used for administrative tasks such as backups, log rotation, and system maintenance.

## What is a Cron Job?

A **Cron Job** is a scheduled task managed by the Cron service.

For example:

```text
* * * * * /home/user/backup.sh
```

This entry instructs Cron to execute the following script every minute:

```text
/home/user/backup.sh
```

## Where Are Cron Jobs Stored?

Cron jobs can be stored in several locations, including:

```text
/etc/crontab
```

Individual user cron jobs can also be viewed using:

```bash
crontab -l
```

System-wide scheduled tasks are commonly located under:

```text
/etc/cron*
```

## Why Are Cron Jobs Important in Penetration Testing?

Cron jobs frequently execute with elevated privileges, including the **root** user.

If an attacker can modify a script executed by a privileged Cron job, arbitrary commands may be executed as **root**, leading to Privilege Escalation.

This makes writable Cron scripts a common privilege escalation vector on Linux systems.

## Enumerating Cron Jobs

A typical enumeration process includes checking the system-wide cron configuration:

```bash
cat /etc/crontab
```

Listing Cron-related directories:

```bash
ls -la /etc/cron*
```

Viewing the current user's scheduled tasks:

```bash
crontab -l
```

---

# Lab

## Step 1: Inspect the Home Directory

We began by inspecting the files in our home directory.

During enumeration, we discovered a file that unexpectedly appeared in our home directory even though we did not have permission to create or modify it.

![](Penetration%20Testing/Images/Pasted%20image%2020260521010637.png)

This suggested that an automated process might be copying the file.

## Step 2: Search for Related Files

We searched for other copies of the same file and discovered another version located in the `/tmp` directory.

![](Penetration%20Testing/Images/Pasted%20image%2020260521010811.png)

This indicated that an automated process was likely copying files between `/tmp` and our home directory.

A Cron job became the primary suspect.

## Step 3: Locate the Responsible Script

To identify the script responsible for this behavior, we searched the system for references to the file path.

![](Penetration%20Testing/Images/Pasted%20image%2020260521011052.png)

The search command used several useful options:

### `-n`

Displays the matching line number.

### `-r`

Performs a recursive search through all subdirectories.

### `-i`

Performs a case-insensitive search.

In our case, we searched under:

```text
/usr
```

because many system scripts and applications are commonly stored there.

Eventually, we located the script responsible for copying the file.

![](Penetration%20Testing/Images/Pasted%20image%2020260521011523.png)

## Step 4: Verify File Permissions

Next, we checked the permissions of the identified script.

We discovered that we had write permission, allowing us to modify its contents.

![](Penetration%20Testing/Images/Pasted%20image%2020260521011550.png)

## Step 5: Modify the Script

Since no text editor was available on the target system, we used `printf` to overwrite the script with a malicious payload.

```bash
printf '#! /bin/bash\necho "student ALL=NOPASSWD:ALL" >> /etc/sudoers' > /usr/local/share/copy.sh
```

### Purpose

This payload replaces the original script with one that appends the following entry to the `/etc/sudoers` file:

```text
student ALL=NOPASSWD:ALL
```

Once executed by the Cron job as **root**, the `student` user is granted permission to execute any command with `sudo` without being prompted for a password.

## Step 6: Wait for the Cron Job

Since the Cron job executed once every minute, we simply waited for the scheduler to run our modified script.

![](Penetration%20Testing/Images/Pasted%20image%2020260521011915.png)

## Step 7: Obtain Root Privileges

After the Cron job completed, the `student` user had unrestricted `sudo` privileges.

This allowed us to execute commands as **root** and successfully complete the privilege escalation process.

![](Penetration%20Testing/Images/Pasted%20image%2020260521011931.png)
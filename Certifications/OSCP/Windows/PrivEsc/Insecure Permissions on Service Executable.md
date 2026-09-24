# Windows Service Misconfiguration and Privilege Escalation

A Windows service can become a privilege escalation vector when a low-privileged user has permission to modify the service or the executable associated with it.

The general idea is to identify an insecure service, determine the path of the executable it runs, and verify whether we have permission to modify that executable. If the executable is writable, we can replace the legitimate service binary with a malicious payload that provides a shell when executed.

To identify potentially insecure services efficiently, we can use automated enumeration tools. One of the most well-known tools for Windows privilege escalation enumeration is **PowerUp**.

---

# Lab

## Step 1 — Enumerate the Service Configuration

We first gathered information about the target service, including its configuration and the path of the executable it uses.

We used `sc qc` to query the service configuration.

```
sc qc <service>
```

![](../../../../Images/Pasted%20image%2020260924211017.png)

The output allowed us to identify the executable path associated with the service.

## Step 2 — Check the Service Executable Permissions

After identifying the executable path, we checked its permissions using `icacls`.

```
icacls <path>
```

![](../../../../Images/Pasted%20image%2020260924211157.png)

The output showed that everyone had permission to modify the executable.

This is an insecure configuration because a low-privileged user who can modify the executable of a service may be able to replace the legitimate program with a malicious one.

## Step 3 — Locate the Service Executable

We navigated to the identified path and examined the executable used by the service.

![](../../../../Images/Pasted%20image%2020260924211417.png)

Since the executable was writable, we could proceed with replacing it with a malicious executable.

## Step 4 — Generate a Malicious Payload

We created a malicious executable that would provide us with a reverse shell when executed by the service.

We used `msfvenom` to generate the payload.

![](../../../../Images/Pasted%20image%2020260924212248.png)

The payload was configured to connect back to our attacking machine, where we would have a listener waiting for the connection.

## Step 5 — Host the Payload

We opened an HTTP server on the attacking machine to make the payload available to the target.

![](../../../../Images/Pasted%20image%2020260924220545.png)

We then used `curl` on the target machine to download the payload from our HTTP server.

![](../../../../Images/Pasted%20image%2020260924213904.png)

Using a temporary HTTP server provided a simple method for transferring the payload to the target.

## Step 6 — Stop the Service

Before replacing the executable, we stopped the target service.

This ensured that the original executable was no longer running or being used by the service.

![](../../../../Images/Pasted%20image%2020260924214557.png)

## Step 7 — Replace the Service Executable

We replaced the legitimate service executable with the malicious payload.

Because the permissions allowed us to modify the executable, we were able to perform this replacement using our current low-privileged account.

The important security issue here is that the service was configured to execute a file that our account could modify.

## Step 8 — Start a Listener

We configured a listener on the attacking machine to wait for the reverse connection from the payload.

![](../../../../Images/Pasted%20image%2020260924220634.png)

The listener needed to be active before starting the modified service so that the incoming connection could be received.

## Step 9 — Start the Modified Service

With the listener running, we started the service again.

![](../../../../Images/Pasted%20image%2020260924220652.png)

When the service started, Windows executed the malicious payload in the service's execution context.

The payload then connected back to our listener.

## Step 10 — Obtain a Shell

The reverse connection was successfully received, giving us a shell on the target machine.

![](../../../../Images/Pasted%20image%2020260924220713.png)

However, obtaining a shell does not automatically mean that we have `Administrator` or `SYSTEM` privileges.

We therefore needed to enumerate our current privileges and determine what additional escalation opportunities were available.

## Step 11 — Enumerate Windows Privileges

We checked the privileges assigned to our current account.

During enumeration, we identified:

```
SeImpersonatePrivilege
```

![](../../../../Images/Pasted%20image%2020260924220758.png)

`SeImpersonatePrivilege` is particularly interesting during Windows privilege escalation because it can potentially be abused to impersonate a higher-privileged security token.

At this point, we had identified another potential privilege escalation path.

## Step 12 — Abuse `SeImpersonatePrivilege` with PrintSpoofer

One of the well-known tools used to abuse `SeImpersonatePrivilege` is **PrintSpoofer**.

We transferred PrintSpoofer to the target machine and executed it from our existing shell.

The tool successfully abused the available impersonation privilege and allowed us to obtain a shell with `SYSTEM` privileges.

![](../../../../Images/Pasted%20image%2020260924221654.png)

The resulting security context was:

```
NT AUTHORITY\SYSTEM
```

We had therefore successfully escalated from our initial low-privileged shell to the Windows `SYSTEM` account.


# Key Takeaways

- A Windows service can become a privilege escalation vector when its executable is writable by a low-privileged user.
- `sc qc` can be used to inspect a service's configuration and identify the executable path.
- `icacls` can be used to determine whether the executable can be modified.
- **PowerUp** can automate the enumeration of several Windows privilege escalation opportunities.
- A writable service executable can be replaced with a malicious payload.
- The payload can provide a reverse shell when the service starts.
- Obtaining a shell does not necessarily mean that the current user has administrative privileges.
- `SeImpersonatePrivilege` is an important privilege to enumerate after obtaining a Windows shell.
- **PrintSpoofer** can be used to abuse `SeImpersonatePrivilege` in applicable environments.
- The important concept is not memorizing the tools. The attack depends on understanding the relationship between **service configuration, file permissions, execution context, and Windows privileges**.
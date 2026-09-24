# What is an Unquoted Service Path?

An **Unquoted Service Path** is a Windows Service configuration issue that occurs when the path to the Service executable contains **spaces but is not enclosed in quotation marks (`"`)**.

For example:

```
C:\Program Files\My Service\service.exe
```

A correctly quoted path would be:

```
"C:\Program Files\My Service\service.exe"
```

When a Service path contains spaces without quotes, Windows may interpret the path in multiple possible ways while attempting to locate the executable. If a low-privileged user can write to one of the directories that Windows checks, this behavior can potentially be abused for **Privilege Escalation**.

The important conditions are therefore:

- The Service path contains spaces.
- The path is not enclosed in quotes.
- A low-privileged user can write to an appropriate location in the path.
- The Service runs with higher privileges.

# Lab

## Step 1: Identify the Unquoted Service Path

We first identified a Windows Service whose executable path contained spaces but was not enclosed in quotation marks.

![Unquoted Service Path](../../../../Images/Pasted%20image%2020260924233555.png)

The important part is the combination of:

```
Path contains spaces
+
Path is not quoted
```

This makes the Service a potential candidate for an **Unquoted Service Path** Privilege Escalation attack.

## Step 2: Check Write Permissions

Before attempting exploitation, we need to determine whether we can create or modify a file in one of the locations involved in the Service path.

We tested whether we could create a file at the relevant location.

The file was created successfully, confirming that we had the required write permissions.

![Write Permission Test](../../../../Images/Pasted%20image%2020260924233702.png)

This is an important step because an Unquoted Service Path by itself does not necessarily mean that Privilege Escalation is possible. We also need sufficient permissions to place our executable in a location that Windows may search.

## Step 3: Generate the Payload

After confirming that we could write to the required location, we generated a Windows payload that would provide a Shell when executed.

![Payload Generation](../../../../Images/Pasted%20image%2020260924233755.png)

The payload is intended to be placed at the location that Windows may attempt to execute because of the ambiguous Service path.

## Step 4: Transfer the Payload

We then needed to transfer the Payload to the target machine.

An HTTP server was started to host the Payload, allowing the target machine to download it.

![HTTP Server and Payload Transfer](../../../../Images/Pasted%20image%2020260924234032.png)

The Payload was placed in the relevant location containing the space in the Service path.

The goal is for Windows to encounter our executable while resolving the unquoted Service path.

## Step 5: Start the Listener

Before starting the Service, we started a Listener to receive the incoming connection from the Payload.

![Listener](../../../../Images/Pasted%20image%2020260924234056.png)

The Listener must be ready before the Payload executes so that the resulting connection can be received.

## Step 6: Stop the Service

We stopped the vulnerable Service before restarting it.

![Stop Service](../../../../Images/Pasted%20image%2020260924234135.png)

Stopping the Service ensures that we can restart it and trigger the vulnerable execution behavior.

## Step 7: Start the Service

We then started the Service again.

![Start Service](../../../../Images/Pasted%20image%2020260924234159.png)

When Windows attempted to start the Service, it processed the unquoted executable path and located the Payload we had placed in the relevant location.

## Step 8: Obtain a Shell

The Payload executed successfully, and the Listener received the incoming connection.

![Shell](../../../../Images/Pasted%20image%2020260924234223.png)

We successfully obtained a Shell from the target machine.

# Key Takeaways

- An **Unquoted Service Path** occurs when a Service executable path contains spaces but is not enclosed in quotes.
- The missing quotes can cause Windows to interpret the executable path ambiguously.
- The configuration alone does not automatically mean the Service is exploitable.
- **Write permissions** to an appropriate location in the path are an important requirement.
- The Service's execution privileges are also important when determining the potential impact.
- The general idea is to take advantage of the way Windows resolves an unquoted executable path and place a malicious executable where Windows may attempt to find it.
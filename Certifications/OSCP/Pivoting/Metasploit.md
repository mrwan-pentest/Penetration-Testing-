
# Pivoting with Metasploit SOCKS Proxy

## Overview

When a compromised machine has access to an internal network that is not directly reachable from our attacking machine, we can use it as a **pivot**.

In this setup, we discovered an additional internal network and configured Metasploit to route our traffic through the compromised machine. We then used a **SOCKS proxy** with ProxyChains to access services on the internal network.


---
# Lab 


## Discovering the Internal Network

First, we enumerated the networks accessible through the compromised machine and discovered another network that was not directly reachable from our attacking machine.

![](../../../Images/Pasted%20image%2020260930232045.png)


We then added the discovered network to the routing configuration so that Metasploit could route traffic through the compromised session.

![](../../../Images/Pasted%20image%2020260930232247.png)

## Setting Up the SOCKS Proxy

Next, we used the following Metasploit module:

```
auxiliary/server/socks_proxy
```

This module creates a **SOCKS proxy** that allows external tools to send their traffic through the Metasploit session.

![](../../../Images/Pasted%20image%2020260930232350.png)

We configured the SOCKS proxy server and version to match the settings that would be used in our ProxyChains configuration.

The ProxyChains configuration file is:

```
/etc/proxychains4.conf
```

![](../../../Images/Pasted%20image%2020260930232605.png)


We configured the SOCKS server and SOCKS version in this file to match the Metasploit SOCKS proxy.

![](../../../Images/Pasted%20image%2020260930232710.png)

## Starting the Proxy

After configuring the module, we started the SOCKS proxy using:

```
run
```

Metasploit then started listening for SOCKS connections.
![](../../../Images/Pasted%20image%2020260930232801.png)


## Using ProxyChains

With the SOCKS proxy running and the internal network routed through the compromised machine, we could now use **ProxyChains** to send tools through the pivot.

The basic syntax is:

```
proxychains <command>
```

For example, instead of running a tool directly:

```
<command>
```

we prefix it with:

```
proxychains <command>
```

This causes the traffic from the tool to be redirected through the SOCKS proxy and ultimately through the compromised machine toward the internal network.
![](../../../Images/Pasted%20image%2020260930234042.png)



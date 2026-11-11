# Virtual Host Enumeration

## 1. Overview

**Virtual Host (VHost)** is a web server configuration that allows multiple websites or web applications to run on the same server using a single IP address.

The server identifies which website to display based on the Host HTTP Header sent with the client's request.

During penetration testing, **Virtual Host Enumeration** helps discover hidden or internal virtual hosts that may not have publicly accessible DNS records.

Tools such as **FFUF** automate this process by testing different hostnames using a wordlist.

---

## 2. Internal Subdomain Enumeration

First, we perform Virtual Host Enumeration to discover internal or hidden virtual hosts associated with the target domain.

We use FFUF with a subdomain wordlist:

```
ffuf -u http://ffuf.me -H "Host: FUZZ.ffuf.me" -w /usr/share/seclists/Discovery/DNS/subdomains-top1million-110000.txt
```

**Command breakdown:**

- -u: Specifies the target URL.
- -H: Adds or modifies an HTTP Header.
- Host: FUZZ.ffuf.me: Replaces FUZZ with each word from the wordlist.
- -w: Specifies the wordlist containing possible subdomain names.

![](../../../Images/Pasted%20image%2020261111205243.png)

## 3. Identifying Hidden Virtual Hosts

After running the scan, FFUF may identify a virtual host that returns a different response from the default website.

In our case, we discovered an internal subdomain that was not immediately accessible through normal DNS resolution.

![](../../../Images/Pasted%20image%2020261111205314.png)

## 4. Adding the Virtual Host to the Hosts File

After discovering the virtual host, we need to map its hostname to the target server's IP address so our local machine can resolve it.

First, open the local hosts file:

```
sudo nano /etc/hosts
```

Then add an entry using the target's IP address and the discovered hostname:

`<TARGET_IP> redhat.ffuf.me`

Replace <TARGET_IP> with the main server's IP address and redhat.ffuf.me with the discovered virtual host.

![](../../../Images/Pasted%20image%2020261111205449.png)

## 5. Accessing the Discovered Virtual Host

After saving the changes, we can access the discovered virtual host directly through a browser:

`http://redhat.ffuf.me`

Our system will resolve the hostname to the IP address specified in /etc/hosts, allowing us to access the corresponding website.


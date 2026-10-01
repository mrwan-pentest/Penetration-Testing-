# Dodge THM — Enumeration, FTP Access, SSH Port Forwarding, and Privilege Escalation

## Nmap Scan

We started with an Nmap scan to identify the exposed services:

![](../Images/Pasted%20image%2020261002012545.png)

The scan revealed several interesting services:

```
SSH
HTTP
HTTPS
```

The HTTPS service was particularly interesting because the TLS certificate could reveal additional hostnames.

---

## HTTPS Certificate Enumeration

We accessed port `443` and inspected the TLS certificate:

![](../Images/Pasted%20image%2020261002012700.png)

The certificate revealed multiple DNS names associated with the target:

![](../Images/Pasted%20image%2020261002012731.png)

We added all of the discovered hostnames to `/etc/hosts` so they would resolve to the target IP address:

![](../Images/Pasted%20image%2020261002012813.png)

This is important when dealing with virtual hosts because the web server may return different applications depending on the hostname supplied in the HTTP request.

---

## `ball.dodge.thm`

We visited:

```
/ball.dodge.thm
```

We then inspected the page source and noticed a JavaScript file related to the firewall functionality:

![](../Images/Pasted%20image%2020261002013029.png)

After opening the JavaScript file, we were redirected to another page:

![](../Images/Pasted%20image%2020261002013054.png)

The JavaScript code revealed that it was making a request to:

```
firewall10110.php
```

We accessed this page directly and found information about ports that were currently allowed or blocked:

![](../Images/Pasted%20image%2020261002013206.png)

---

## Modifying the Firewall Rules

We researched how to add firewall rules using **UFW (Uncomplicated Firewall)**.

The FTP service was not accessible initially, so we added a rule allowing FTP:

```
sudo ufw allow ftp
```

This allowed the FTP port through the firewall:

![](../Images/Pasted%20image%2020261002013502.png)

The important point here was that the firewall configuration itself became part of the attack surface.

---

## Anonymous FTP

With FTP now accessible, we connected anonymously:

![](../Images/Pasted%20image%2020261002013755.png)

The FTP server contained an SSH private key:

![](../Images/Pasted%20image%2020261002013933.png)

We obtained the private key and could therefore attempt SSH authentication without needing the user's password.

---

## SSH Access

We used the recovered private key to connect through SSH:

![](../Images/Pasted%20image%2020261002014135.png)

Once inside the machine, we enumerated the listening services.

One particularly interesting service was listening on:

```
127.0.0.1:10000
```

![](../Images/Pasted%20image%2020261002014224.png)

Because the service was bound to `localhost`, it was not directly accessible from our attacking machine.

This is where **SSH Local Port Forwarding** became useful.

---

## SSH Local Port Forwarding

We created an SSH tunnel using:

```
ssh -L 12345:localhost:10000 challenger@dodge.thm -i id_rsa_backup
```

The syntax is:

```
-L LOCAL_PORT:DESTINATION:DESTINATION_PORT
```

In our case:

```
12345:localhost:10000
```

means:

```
Kali localhost:12345
        │
        │ SSH tunnel
        ▼
Target localhost:10000
```

So when we connect to:

```
127.0.0.1:12345
```

on our Kali machine, SSH forwards that traffic through the SSH connection to:

```
127.0.0.1:10000
```

on the target.

![](../Images/Pasted%20image%2020261002014412.png)

We then verified that the forwarded port was accessible locally:

![](../Images/Pasted%20image%2020261002014459.png)

This confirmed that the SSH port forwarding was working.

---

## Accessing the Forwarded Web Service

We opened the forwarded port in the browser:

![](../Images/Pasted%20image%2020261002014534.png)

A login page was available.

We inspected the page source and found hardcoded credentials:

![](../Images/Pasted%20image%2020261002014836.png)

These credentials provided another set of SSH credentials:

![](../Images/Pasted%20image%2020261002015007.png)

We used them to switch to the newly discovered user:

![](../Images/Pasted%20image%2020261002015146.png)

---

## Privilege Escalation with `sudo`

After moving to the new user, we checked the commands that could be executed with `sudo`:

```
sudo -l
```

The output showed that we could execute a particular binary with elevated privileges:

![](../Images/Pasted%20image%2020261002015224.png)

This was a **sudo privilege escalation** opportunity.

Instead of trying to manually discover an exploitation technique for the binary, we checked **GTFOBins**, which provides documented techniques for abusing Unix binaries when they are available through `sudo` or other privileged contexts.

![](../Images/Pasted%20image%2020261002015315.png)

We used the corresponding GTFOBins technique for the allowed binary.

The command executed successfully and provided a root shell:

![](../Images/Pasted%20image%2020261002015412.png)

We confirmed that we had successfully escalated to:

```
root
```

---

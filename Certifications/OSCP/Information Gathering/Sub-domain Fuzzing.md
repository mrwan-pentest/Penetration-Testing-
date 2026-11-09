
## To do fuzzing with bash

```
for sub in $(cat /usr/share/seclists/Discovery/DNS/bitquark-subdomains-top100000.txt); do host $sub.google.com ;done
```

![](../../../Images/Pasted%20image%2020261105191518.png)


## If we want to show the domain associated with the IP

![](../../../Images/Pasted%20image%2020261105193152.png)


## Or we have a website called 

```
viewdns.info
```


## There is a powerful tool call FUFF to do sub-domain and other things
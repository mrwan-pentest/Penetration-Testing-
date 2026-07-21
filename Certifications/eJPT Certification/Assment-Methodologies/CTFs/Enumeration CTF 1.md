
### There is a samba share that allows anonymous access. Wonder what's in there!

# Nmap Scan

![](../../../../Images/Pasted%20image%2020260515125647.png)

![](../../../../Images/Pasted%20image%2020260515125745.png)


# Enumeration For SMB

![](../../../../Images/Pasted%20image%2020260515130027.png)

We Found Some Users

![](../../../../Images/Pasted%20image%2020260515130142.png)

We put them in a list

![](../../../../Images/Pasted%20image%2020260515130227.png)

we made brute force sharing for SMB

![](../../../../Images/Pasted%20image%2020260515130639.png)

we found shares !..

![](../../../../Images/Pasted%20image%2020260515130720.png)

We login in the file and got first flag !..

![](../../../../Images/Pasted%20image%2020260515130922.png)

---
### One of the samba users have a bad password. Their private share with the same name as their username is at risk!

We navigated to MSF, we used this model to do a brute forcing against SMB

![](../../../../Images/Pasted%20image%2020260515131546.png)

We got some creds

![](../../../../Images/Pasted%20image%2020260515131755.png)

we login in with the user josh with same name of share as the question mentioned

![](../../../../Images/Pasted%20image%2020260515132630.png)

---
### Follow the hint given in the previous flag to uncover this one.

we got a hint there is an FTP open !..

![](../../../../Images/Pasted%20image%2020260515132809.png)

we checked of all ports and found an FTP in a deferent port !

![](../../../../Images/Pasted%20image%2020260515133003.png)![](../../../../Images/Pasted%20image%2020260515133026.png)

We tried a brute forcing against the FTP using **hydra**
and we gat creds, then we log in FTP and the flag

---
### This is a warning meant to deter unauthorized users from logging in.

we log in SSH and got the flag !..

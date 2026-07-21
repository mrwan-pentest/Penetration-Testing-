
### There is a samba share that allows anonymous access. Wonder what's in there!

# Nmap Scan

![](Penetration%20Testing/Images/Pasted%20image%2020260515125647.png)

![](Penetration%20Testing/Images/Pasted%20image%2020260515125745.png)


# Enumeration For SMB

![](Penetration%20Testing/Images/Pasted%20image%2020260515130027.png)

We Found Some Users

![](Penetration%20Testing/Images/Pasted%20image%2020260515130142.png)

We put them in a list

![](Penetration%20Testing/Images/Pasted%20image%2020260515130227.png)

we made brute force sharing for SMB

![](Penetration%20Testing/Images/Pasted%20image%2020260515130639.png)

we found shares !..

![](Penetration%20Testing/Images/Pasted%20image%2020260515130720.png)

We login in the file and got first flag !..

![](Penetration%20Testing/Images/Pasted%20image%2020260515130922.png)

---
### One of the samba users have a bad password. Their private share with the same name as their username is at risk!

We navigated to MSF, we used this model to do a brute forcing against SMB

![](Penetration%20Testing/Images/Pasted%20image%2020260515131546.png)

We got some creds

![](Penetration%20Testing/Images/Pasted%20image%2020260515131755.png)

we login in with the user josh with same name of share as the question mentioned

![](Penetration%20Testing/Images/Pasted%20image%2020260515132630.png)

---
### Follow the hint given in the previous flag to uncover this one.

we got a hint there is an FTP open !..

![](Penetration%20Testing/Images/Pasted%20image%2020260515132809.png)

we checked of all ports and found an FTP in a deferent port !

![](Penetration%20Testing/Images/Pasted%20image%2020260515133003.png)![](Penetration%20Testing/Images/Pasted%20image%2020260515133026.png)

We tried a brute forcing against the FTP using **hydra**
and we gat creds, then we log in FTP and the flag

---
### This is a warning meant to deter unauthorized users from logging in.

we log in SSH and got the flag !..

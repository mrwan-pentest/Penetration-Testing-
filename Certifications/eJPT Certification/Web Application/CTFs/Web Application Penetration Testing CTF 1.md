
# - **Flag 1:** Sometimes, important files are hidden in plain sight. Check the root ('/') directory for a file named 'flag.txt' that might hold the key to the first flag.


### We checked on the website, and we can see there is a LFI, we exploited and got the first FLAG

![[Pasted image 20260610163129.png]]


# - **Flag 2:** Explore the structure of the server's directories. Enumeration might reveal hidden treasures.

### We did  brute force and got an interesting URL

![[Pasted image 20260610163339.png]]


### We navigated to the secured path and got the second FLAG

![[Pasted image 20260610163506.png]]

![[Pasted image 20260610163510.png]]


# - **Flag 3:** The login form seems a bit weak. Trying out different combinations might just reveal the next flag.

### It's time for hydra ! 
### Before doing brute force we collected some important information to brute force the login form

### We used Burp suite to see which method that used and other information


### We can see the method is POST, and the form of the username and password and the path of the login
![[Pasted image 20260610163843.png]]

### Finally we checked of the error message

![[Pasted image 20260610164133.png]]

### Now we are ready to brute force the login page

### we used this form after collecting all the information

```
hydra -f -V -L /usr/share/seclists/Usernames/top-usernames-shortlist.txt -P /root/Desktop/wordlists/100-common-passwords.txt target.ine.local http-post-form "/login:username=^USER^&password=^PASS^:Invalid username or password"
```

### We got creds 

![[Pasted image 20260610164410.png]]

### Then we logged in and got the third FLAG

![[Pasted image 20260610164528.png]]


# - **Flag 4:** The login form behaves oddly with unexpected inputs. Think of injection techniques to access the 'admin' account and find the flag.

### We attempted SQL injection to log in illegally


![[Pasted image 20260610164751.png]]

### And we got the Final FLAG

![[Pasted image 20260610164820.png]]


# This (what)tells search engines what to and what not to avoid.


## NMAP Scan

![[Pasted image 20260511215610.png]]

# robots.txt Discovery  
  
## Performed directory fuzzing using Gobuster and discovered the robots.txt file, which contained the flag.



# 2/What website is running on the target, and what is its version?

## Nmap Enumeration  
  
## Performed service and version detection using Nmap to enumerate the target services.


# 3/Directory browsing might reveal where files are stored.


## Uploads Directory Discovery

### Performed directory fuzzing on the target web application and discovered the uploads directory, where the flag was stored.


# 4/An overlooked backup file in the webroot can be problematic if it reveals sensitive configuration details.

## Backup File Discovery

### Performed directory fuzzing using common backup file extensions and discovered a backup file containing the flag.


# 5/Certain files may reveal something interesting when mirrored
## Website Mirroring with HTTrack

### Downloaded a local copy of the entire website using HTTrack in order to analyze its contents offline.

### After downloading the website, we examined the files and retrieved the flag from the page:xmlrpc0db0.php

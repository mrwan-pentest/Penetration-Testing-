
_Flag 1: The user ‘bob’ might not have chosen a strong password. Try common passwords to gain access to the server where the flag is located. (target1.ine.local)_

اولا فعلنا brute force  على الموقع

hydra -l bob -P /usr/share/metasploit-framework/data/wordlists/unix_passwords.txt target1.ine.local http-get

وجدنا creds

![[Pasted image 20260520144829.png]]

فعلنا fuzzing   على الموقع

![[Pasted image 20260520144857.png]]

ظهر معانا صفحة  webdav

عبر أداة davtest  اكتشفنا انه نستطيع رفع ملف asp

cadaver 
سجلنا عبر الأداة وشفنا الفلاج

![[Pasted image 20260520145156.png]]

# Flag 2: Exploring Valuable Files on the C: Drive

رفعنا الملف

![[Pasted image 20260520145244.png]]

وقرأنا الفلاج الثاني

![[Pasted image 20260520145306.png]]


# Flag 3: SMB Enumeration & Credential Attack

فعلنا بروتفورس عبر الميتا

![[Pasted image 20260520145421.png]]


فعلنا هذا الخيار عشان يفتح لكل مستخدم جلسة

![[Pasted image 20260520145445.png]]

دخلنا على مستخدم ال administrator

![[Pasted image 20260520145550.png]]


حددنا الشير وقرأنا الفلاج

![[Pasted image 20260520145612.png]]

# Flag 4: Searching the Desktop Directory

دخلنا لمجل Desktop  وقرأنا الفلاج

![[Pasted image 20260520145704.png]]
![[Pasted image 20260520145716.png]]



---
أو نستطيع عبر الهيدرا نفعل brute Force  لل SMB 
بعدين نسجل دخول عبر  smbclient  ثم نحصل على الفلاجات
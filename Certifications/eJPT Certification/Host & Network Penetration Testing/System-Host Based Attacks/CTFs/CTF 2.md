- **Flag 1**: Check the root ('/') directory for a file that might hold the key to the first flag on target1.ine.local.
Nmap Scan

![[Pasted image 20260521133644.png]]

Fuzzing

![[Pasted image 20260521133703.png]]

لاحظنا انه يحولني على .cgi  وهنا احتمال يكون عندنا ثغرة shellshock

![[Pasted image 20260521133804.png]]

عبر ال NMAP  تحققنا وطلع انه قابل للاستغلال

![[Pasted image 20260521133912.png]]


بحثنا كيف نستغل الثغرة وحصلنا على reverseshell

![[Pasted image 20260521133939.png]]

![[Pasted image 20260521133958.png]]

وجبنا الفلاج الأول 

![[Pasted image 20260521134034.png]]


**Flag 2**: In the server's root directory, there might be something hidden. Explore '/opt/apache/htdocs/' carefully to find the next flag on target1.ine.local

جبنا الفلاج الثاني

![[Pasted image 20260521134121.png]]


Investigate the user's home directory and consider using 'libssh_auth_bypass' to uncover the flag on target2.ine.local.

على التارجت الثاني سوينا فحص nmap  
ظهرت خدمة  ssh  ومشغله هذي السيرفس

![[Pasted image 20260521134316.png]]

بحثنا عن السيرفس في searchsploit  وشفنا لها ثغرة

![[Pasted image 20260521134459.png]]

قرأنا الثغرة وعرفنا كيف نستخدمها

![[Pasted image 20260521134532.png]]

فعلنا reverse shell code

![[Pasted image 20260521134600.png]]

حصلنا على شل

![[Pasted image 20260521134621.png]]

قرأنا الفلاج

![[Pasted image 20260521134650.png]]


The most restricted areas often hold the most valuable secrets. Look into the '/root' directory to find the hidden flag on target2.ine.local.


ظهر عندنا 2 باينري واحد عليه SUID
تحققنا من الأشياء المنفذه عليه
وظهر ان الباينري الاخر يتم تنفيذه بداخله


![[Pasted image 20260521134827.png]]

حذفنا الباينري واستبدلناه ب bin bash
وشغلنا الباينري وحصلنا على الروت

![[Pasted image 20260521134917.png]]

وقرأنا الفلاج

![[Pasted image 20260521135026.png]]

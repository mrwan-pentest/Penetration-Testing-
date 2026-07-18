
# ما هو Gobuster؟

```
Gobuster
```

أداة Enumeration سريعة جدًا مكتوبة بلغة Go.

تستخدم لاكتشاف:

- الملفات
- المجلدات
- Subdomains
- Virtual Hosts

التي لا تظهر بشكل مباشر للمستخدم.




---

## Directory Enumeration

```
gobuster dir -u http://target.com -w wordlist.txt
```

المعاني:

|الخيار|المعنى|
|---|---|
|dir|فحص المجلدات|
|-u|الرابط|
|-w|قائمة الكلمات|

مثال:

```
gobuster dir -u http://demo.ine.local -w /usr/share/wordlists/dirb/common.txt
```


---

# تحديد الامتدادات

بعض المواقع تستخدم:

```
.php.asp.aspx.txt
```

يمكن البحث عنها:

```
gobuster dir -u http://target.com -w wordlist.txt -x php,txt,html
```




---

# تغيير عدد Threads

افتراضيًا سريع.

يمكن زيادته:

```
gobuster dir -u http://target.com -w wordlist.txt -t 50
```

---

# Subdomain Enumeration 

مثال:

```
gobuster dns -d target.com -w subdomains.txt
```

قد يجد:

```
mail.target.comdev.target.comadmin.target.comvpn.target.com
```

---

# Virtual Host Enumeration

مفيد جدًا في eJPT.

```
gobuster vhost -u http://10.10.10.5 -w hosts.txt
```


قد يكتشف:

```
admin.target.localdev.target.localtest.target.local
```

---

# أهم Wordlists

في كالي:

```
/usr/share/wordlists/dirb/common.txt
```

أو:

```
/usr/share/seclists/
```

إذا كانت مثبتة.

---

# أهم الخيارات للحفظ 

### فحص المجلدات

```
gobuster dir
```

---

### الرابط

```
-u
```

---

### قائمة الكلمات

```
-w
```

---

### الامتدادات

```
-x php,txt,html
```

---

### عدد Threads

```
-t 50
```

---

### تجاهل أكواد

```
-b 404
```

---

### Subdomains

```
gobuster dns
```

---

### Virtual Hosts

```
gobuster vhost
```

---


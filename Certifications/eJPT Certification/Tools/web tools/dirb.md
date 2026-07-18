
# ما هي أداة Dirb؟ 

```
Dirb
```

هي أداة Web Content Scanner.

تستخدم لاكتشاف:

- المجلدات المخفية
- الملفات المخفية
- صفحات الإدارة
- النسخ الاحتياطية

داخل مواقع الويب.

---

# كيف تعمل؟

افترض أن الموقع:

```
http://target.com
```

وأنت لا ترى إلا الصفحة الرئيسية.


---

# أبسط استخدام

```
dirb http://target.com
```


---
# مع creds 

```
dirb http://target.com wordlist.txt -u usname:password
```


---

# استخدام Wordlist مخصصة

```
dirb http://target.com wordlist.txt
```

مثال:

```
dirb http://demo.ine.local /usr/share/wordlists/dirb/common.txt
```

---

# البحث عن امتدادات معينة

إذا كان الموقع PHP:

```
dirb http://target.com -X .php
```

أو أكثر من امتداد:

```
dirb http://target.com -X .php,.txt,.bak
```



---

# حفظ النتائج

```
dirb http://target.com -o results.txt
```



---

# أشهر Wordlists

### الافتراضية

```
/usr/share/dirb/wordlists/common.txt
```

---

### الأكبر

```
/usr/share/dirb/wordlists/big.txt
```

---

### SecLists

```
/usr/share/seclists/
```

إذا كانت مثبتة.

---

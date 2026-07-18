

أداة `smbmap` من أهم أدوات الـ SMB Enumeration ف

هي أداة خفيفة وسريعة جدًا تساعدك:

- تعرف الـ shares
- تعرف الصلاحيات
- هل تقدر تكتب؟
- هل تقدر تقرأ؟
- أحيانًا تنفيذ أوامر

# أولًا: وش فكرة smbmap؟

بدل ما تدخل يدوي بـ:

```
smbclient
```

الأداة تسوي:

- Enumeration كامل
- بشكل مرتب وسريع

---

# أبسط استخدام

```
smbmap -H TARGET
```

مثال:

```
smbmap -H 10.10.10.5
```

# ماذا يفعل؟

يحاول:

- قراءة الـ shares
- غالبًا كـ anonymous


---

# أهم شيء 

الأداة توضح لك:

| الصلاحية    | معناها          |
| ----------- | --------------- |
| READ ONLY   | تقدر تقرأ فقط   |
| READ, WRITE | تقدر ترفع ملفات |
| NO ACCESS   | ممنوع           |

---

# الدخول بحساب

إذا عندك username/password:

```
smbmap -H TARGET -u admin -p password123
```

---

# Pass-the-Hash

تدعم PTH 

```
smbmap -H TARGET -u administrator -p HASH
```

أحيانًا تستخدم:

```
--hashes
```

حسب النسخة.

---

# عرض الملفات داخل Share

```
smbmap -H TARGET -r public
```

معنى:

- recursively list


---

# تحميل ملف

```
smbmap -H TARGET --download "public/passwords.txt"
```

---

# رفع ملف 

إذا عندك write permission:

```
smbmap -H TARGET --upload shell.exe "public/shell.exe"
```
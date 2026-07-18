
أداة `dnsenum` تُستخدم في:

```
DNS Enumeration
```

أي جمع معلومات DNS الخاصة بالدومين المستهدف.

وهي من الأدوات المشهورة في:

- Reconnaissance
- Information Gathering
- Enumeration


---

# ماذا تفعل dnsenum؟

تقوم بجمع معلومات كثيرة عن الدومين مثل:

- DNS Records
- Name Servers
- MX Records
- Subdomains
- محاولة DNS Zone Transfer
- Google Scraping أحيانًا
- Brute Force للـ Subdomains

---

# الشكل الأساسي للأداة

```
dnsenum example.com
```

---

# ماذا يحدث عند التشغيل؟

الأداة تبدأ تلقائيًا بـ:

1. استخراج:
    - A Records
    - NS Records
    - MX Records
2. محاولة:

```
AXFR (Zone Transfer)
```

3. البحث عن Subdomains
4. أحيانًا تعمل Brute Force باستخدام Wordlist


---
# 1. A Record

يربط الدومين بعنوان IP.


# 2. NS Record (Name Server)

يحدد سيرفرات الـ DNS المسؤولة عن الدومين.

يعني:

```
مين يدير DNS لهذا الموقع؟
```

# 3. MX Record (Mail Exchange)

خاص بالإيميلات.

يحدد سيرفر البريد الإلكتروني للدومين.

مثال:

```
وين تروح إيميلات @example.com ؟
```



## TXT Record

يحتوي نصوص أو إعدادات.

أحيانًا تجد:

- SPF
- DKIM
- Verification Tokens

```
dig TXT example.com
```


---

# مثال عملي

```
dnsenum zonetransfer.me
```

قد يعطيك:

```
mail.zonetransfer.mevpn.zonetransfer.medev.zonetransfer.me
```

---

# أهم الخيارات (Options)

## 1. تنفيذ Brute Force

```
dnsenum --enum example.com
```

هذا الخيار يشغل:

- Enumeration كامل
- Subdomain Bruteforce
- Zone Transfer checks

---

## 2. تحديد Wordlist

```
dnsenum --dnsserver ns1.example.com example.com
```

تحديد DNS Server معيّن.

---

## 3. استخدام Wordlist مخصصة

```
dnsenum -f subdomains.txt example.com
```

- `-f`  
    تعني:

```
Filename / Wordlist
```

---

# تجربة Zone Transfer

الأداة تحاول تلقائيًا:

```
AXFR
```

وإذا كان السيرفر ضعيف الإعداد:  
تحصل على جميع سجلات DNS.




# ما هو CMS؟

CMS اختصار:

```
Content Management System
```

يعني:

```
نظام إدارة المحتوى
```

وهو برنامج يساعدك على إنشاء وإدارة موقع بدون الحاجة لكتابة كل شيء برمجياً.

---

## أمثلة مشهورة

### WordPress

الأشهر عالمياً.

### Joomla

نظام إدارة محتوى قديم ومشهور.

### Drupal

يستخدم كثيراً في المواقع الكبيرة والحكومية.

---

بدلاً من بناء موقع من الصفر:

```
HTML
CSS
Java Script
PHP
MySQL
```

يمكنك تثبيت:

```
WordPress
```

وخلال دقائق يصبح لديك موقع جاهز.

---

# لماذا يهتم المخترقون بـ CMS؟

لأنها منتشرة جداً.

مثال:

إذا وجدت ثغرة في:

```
WordPress Plugin
```

فقد تؤثر على آلاف أو ملايين المواقع.

---

## الأسباب

### 1. Ubiquity

يعني:

```
الانتشار الواسع
```

WordPress وحده يشغل نسبة ضخمة من مواقع الإنترنت.


### 2. Complexity

يعني:

```
التعقيد
```

CMS يحتوي على:

```
Plugins اضافات للموقع
Themes شكل المواقع
Extensions
Users
Roles
Databases
```

كل جزء قد يحتوي ثغرة.


### 3. Regular Updates

يتم إصدار تحديثات باستمرار.

إذا لم يحدّث المسؤول الموقع:

```
قد تبقى الثغرات القديمة موجودة.
```


### 4. User Data

غالباً CMS يخزن:

```
Emails
Passwords
User
Data
Comments
Posts
```

وهذه بيانات قيمة للمهاجم.

---

# أشهر المشاكل الأمنية في CMS

## 1. Vulnerabilities

مثل:

### SQL Injection

مثال:

```
' OR 1=1 --
```


### XSS

مثال:

```
<script>alert(1)</script>
```


### CSRF

إجبار الضحية على تنفيذ طلب بدون علمه.

---

# 2. Authentication & Authorization

## Authentication

يعني:

```
من أنت؟
```

مثال:

```
Login
Username
Password
```

---

## Authorization

يعني:

```
ماذا يسمح لك أن تفعل؟
```

مثال:

```
User
Editor
Admin
```


كمختبر اختراق يجب التأكد:

```
هل المستخدم العادي يستطيع الوصول لصفحات المدير؟
```

---

# 3. Configuration Issues

أخطاء الإعدادات.

مثال:

```
admin/admin
```


أو:

```
Directory Listing Enabled
```


أو:

```
Debug Mode Enabled
```

---

# 4. Plugin & Theme Security

هذه من أكثر النقاط أهمية.

في WordPress مثلاً:

```
Core
Plugins
Themes
```

غالباً الثغرات تأتي من:

```
PluginsThemes
```

وليس من WordPress نفسه.

---

# منهجية اختبار CMS




# المرحلة 1

## Information Gathering & Enumeration

جمع المعلومات.


### تحديد نوع الـ CMS

نسأل:

```
هل الموقع 
WordPress?
Drupal?
Joomla?
```


أدوات:

```
whatweb
wappalyzer
cmsmap
```


### معرفة الإصدار

مثال:

```
WordPress 5.2
```

ثم نبحث:

```
هل توجد ثغرات لهذا الإصدار؟
```


### معرفة المستخدمين

مثال:

```
admin
john
administrator
```


### معرفة Plugins

مثال:

```
contact-form-7wp-file-managerelementor
```


### معرفة Themes

مثال:

```
twentytwentythreeastra
```


### Directory Enumeration

باستخدام:

```
gobuster
dirb
feroxbuster
```

للعثور على:

```
/wp-admin/wp-content/uploads
```

---

# المرحلة 2

## Vulnerability Scanning

البحث عن الثغرات.

أدوات:

```
Nikto
WPScan
Nessus
OpenVAS
```


نبحث عن:

```
Misconfigurations
Known Vulnerabilities
Outdated Plugins
```

---

# المرحلة 3

## Authentication Testing

اختبار تسجيل الدخول.


### Username Enumeration

معرفة المستخدمين الموجودين.

مثال:

```
admin موجودjohn موجود
```


### Brute Force

تجربة كلمات مرور.

مثال:

```
admin:admin
admin:password
```


### Session Testing

اختبار الجلسات.

مثل:

```
Session FixationWeak Sessions
```

---

# المرحلة 4

## Exploitation

الاستغلال.

بعد العثور على الثغرة.


مثال:

وجدت:

```
Plugin Vulnerability
```

فتقوم باستغلالها.


أو:

```
RCELFISQLi
```

---

# المرحلة 5

## Post Exploitation

بعد الاختراق.


### Backdoor

زرع باب خلفي.

مثال:

```
<?php system($_GET['cmd']); ?>
```


### Web Shell

رفع شل ويب.

مثال:

```
c99r57php webshell
```


### استخراج البيانات

مثل:

```
UsersPasswordsEmailsDatabase
```


# ما هو WordPress؟

WordPress هو:

```
نظام إدارة محتوى (CMS)
```

يسمح لك بإنشاء:

- مدونات
- مواقع شركات
- متاجر إلكترونية
- مواقع إخبارية

بدون الحاجة لبرمجة الموقع بالكامل من الصفر.

---

## لماذا WordPress مشهور؟

لأنه:

### سهل الاستخدام

حتى الشخص غير المبرمج يستطيع:

```
إنشاء صفحاترفع صوركتابة مقالاتإدارة المستخدمين
```

من خلال لوحة تحكم.


### مفتوح المصدر

```
Open Source
```

يعني:

```
الكود البرمجي متاح للجميع
```

يمكن لأي شخص:

- قراءته
- تعديله
- تطوير إضافات له


### يدعم Plugins و Themes



```
Theme = شكل الموقع
Plugin = وظائف إضافية
```

---

# لماذا WordPress مهم للمخترق؟

لأن أغلب المواقع تستخدمه.

إذا تعلمت WordPress جيداً:

```
ستتمكن من اختبار عدد ضخم من المواقع.
```

---

# WordPress Security Relevance

## لماذا يهاجمه المهاجمون كثيراً؟

### 1. Highly Targeted

بسبب انتشاره.

إذا اكتشف المهاجم ثغرة في Plugin مشهور:

```
قد يخترق آلاف المواقع.
```


### 2. Plugin Ecosystem

يوجد آلاف الـ Plugins.

مثال:

```
Contact Form
File Upload
SEO
Backup
Gallery
```

كل Plugin قد يحتوي ثغرة.


### 3. Frequent Updates

WordPress يصدر تحديثات باستمرار.

إذا لم يتم تحديث الموقع:

```
تبقى الثغرات القديمة موجودة.
```

---

# أشهر ثغرات WordPress


## 1. Vulnerable Plugins and Themes

أكثر سبب للاختراق.

مثال:

```
Plugin قديم
```

فيه:

```
RCELFISQLi
```


كمختبر اختراق أول شيء تبحث عنه:

```
PluginsThemesVersions
```


## 2. Brute Force Attacks

مهاجمة صفحة تسجيل الدخول.

غالباً:

```
/wp-login.php
```

أو

```
/wp-admin
```


مثال:

```
admin : admin
admin : password
```


## 3. SQL Injection

إذا كان Plugin يرسل البيانات مباشرة لقاعدة البيانات.

مثال:

```
' OR 1=1 --
```


## 4. XSS

مثال:

```
<script>alert(1)</script>
```

قد يوجد في:

- Plugin
- Theme
- Custom Code


## 5. CSRF

إجبار المستخدم المسجل دخوله على تنفيذ أوامر دون علمه.

مثال:

```
تغيير كلمة المرورإنشاء مستخدم جديد
```


## 6. Insecure Configuration

مثل:

### كلمات مرور ضعيفة

```
admin/admin
```


### Debug Mode

```
WP_DEBUG=true
```


### صلاحيات خاطئة

```
777
```

على الملفات.

---

# WordPress Pentesting Methodology




# المرحلة 1

## Information Gathering & Enumeration

جمع المعلومات.


### Port Scanning

باستخدام:

```
nmap
```

نعرف:

```
80
443
3306
```


### معرفة إصدار WordPress

مثال:

```
WordPress 5.8
```

ثم نبحث:

```
هل توجد ثغرات لهذا الإصدار؟
```


### معرفة Plugins

مثال:

```
elementor
contact-form
-7wp-file-manager
```


### معرفة Themes

مثال:

```
astratwentytwentythree
```


### File & Directory Enumeration

باستخدام:

```
gobusterdirbferoxbuster
```

للعثور على:

```
/wp-admin/wp-content/uploads
```


# WPScan

أهم أداة هنا.

مثال:

```
wpscan --url http://target
```


تستطيع اكتشاف:

```
VersionUsersPluginsThemes
```

---


# المرحلة 2

## Vulnerability Scanning

البحث عن الثغرات.


باستخدام:

```
WPScan
Nikto
Nessus
```


نبحث عن:

```
Outdated Plugins
Outdated Themes
Misconfigurations
Known CVEs
```

---

# المرحلة 3

## Authentication Testing

اختبار تسجيل الدخول.


### Brute Force

استهداف:

```
/wp-login.php/wp-admin
```


### Session Testing

فحص:

```
Cookies
Sessions
Authentication Logic
```

---

# المرحلة 4

## Exploitation

الاستغلال.


مثال:

وجدنا:

```
Plugin Vulnerability
```

فنستغلها.

أمثلة:

```
SQLi
XSS
RCE
LFI
```

---

# المرحلة 5

## Post Exploitation

بعد الاختراق.


### Web Shell

مثال:

```
<?php system($_GET['cmd']); ?>
```


### Backdoor

إنشاء وسيلة رجوع لاحقاً.


### Exfiltration

سرقة البيانات.

مثال:

```
Users
Emails
Database
wp-config.php
```

---

# أهم ملفات WordPress للحفظ

## صفحة الدخول

```
/wp-login.php
```


## لوحة الإدارة

```
/wp-admin
```


## الإضافات

```
/wp-content/plugins/
```


## الثيمات

```
/wp-content/themes/
```


## ملف الإعدادات المهم جداً

```
wp-config.php
```
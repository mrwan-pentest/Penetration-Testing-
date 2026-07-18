

WMAP عبارة عن:

```
Web Vulnerability Scanner داخل Metasploit
```

وظيفته:

- فحص مواقع الويب
- البحث عن ثغرات
- استخدام Modules الخاصة بالويب تلقائيًا

# فكرته 

بدل ما تشغل:

- كل module يدويًا

WMAP يقوم:

```
بتجميع وتشغيل Web Modules تلقائيًا
```

# ماذا يفحص؟ 

قد يفحص:

- SQLi
- File Disclosure
- PUT Methods
- WebDAV
- Directory Listing
- Headers
- Vulnerabilities

---

# تشغيل WMAP 

داخل Metasploit:

```
load wmap
```

# عرض أوامر WMAP

```
wmap_commands
```

# إضافة الهدف

```
wmap_sites -a http://TARGET
```

# عرض المواقع المضافة

```
wmap_sites -l
```

# تحديد الهدف

```
wmap_targets -t http://TARGET
```

# تشغيل الفحص 

## فحص سريع

```
wmap_run -t
```


## فحص كامل

```
wmap_run -e
```



# مشاهدة النتائج

```
services
```

أو:

```
vulns
```


# مثال عملي 

```
msfconsole
load wmap
wmap_sites -a http://192.168.1.10
wmap_targets -t http://192.168.1.10
wmap_run -e
```

---
Lab

```
load wmap
```
## الوظيفة:

تحميل إضافة WMAP داخل Metasploit.

# إضافة موقع

```
wmap_sites -a 192.157.89.3
```

## الوظيفة:

```
إضافة الموقع إلى قاعدة بيانات WMAP
```

# تحديد الهدف الحالي

```
wmap_targets -t http://192.157.89.3
```

## الوظيفة:

```
اختيار الموقع الذي سيتم فحصه
```


# عرض المواقع المضافة

```
wmap_sites -l
```

## الوظيفة:

عرض جميع المواقع المحفوظة داخل WMAP.


# عرض الأهداف الحالية

```
wmap_targets -l
```

## الوظيفة:

عرض:

```
الـ Targets المحددة للفحص
```

# فحص Test Modules

```
wmap_run -t
```

## الوظيفة:

تشغيل:

```
Modules الخاصة بالاختبار السريع
```

غالبًا:

- Enumeration
- معلومات بسيطة
- فحص خفيف

# الفحص الكامل

```
wmap_run -e
```

## الوظيفة:

تشغيل:

```
كل Modules المناسبة
```

لفحص:

- ثغرات
- ملفات
- WebDAV
- Headers
- Directories
- SQLi checks
- وغيرها


# عرض أوامر WMAP

```
wmap_commands
```

يعرض كل أوامر WMAP.

# حذف موقع

```
wmap_sites -d ID
```


# حذف Target

```
wmap_targets -d ID
```


# عرض Modules المستخدمة

```
wmap_modules -l
```


# عرض معلومات Module

```
wmap_modules -i MODULE_NAME
```


# تشغيل Module معين فقط

```
wmap_run -m MODULE_NAME
```


# مثال 

```
wmap_run -m auxiliary/scanner/http/http_header
```
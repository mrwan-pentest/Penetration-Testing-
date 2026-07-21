# `-sV`

Service Version Detection.

يكشف:

- اسم الخدمة
- إصدارها

مثال:

```
Apache 2.4.41OpenSSH 8.2
```

```
nmap -sV target
```

# `--version-intensity`


هذا الخيار مرتبط بـ:

```
-sV
```

أي:

```
Service Version Detection
```

# فكرته ببساطة

يحدد:

```
مدى قوة/عدد المحاولات التي يستخدمها Nmap لمعرفة نسخة الخدمة
```

# القيم

القيمة تكون من:

```
0 → 9
```

# ماذا تعني؟

|القيمة|المعنى|
|---|---|
|0|فحص خفيف جدًا|
|9|فحص قوي جدًا|

# كلما زادت القيمة

Nmap:

- يجرب Probes أكثر
- يرسل Requests أكثر
- يحاول التعرف بدقة أكبر

لكن:

```
يصبح أبطأ
```


# مثال

```
nmap -sV --version-intensity 9 192.168.1.10
```


# ماذا يحدث هنا؟

Nmap:

```
يبذل أقصى محاولة لمعرفة النسخ والخدمات
```
---
# `-O`

OS Detection.

يحاول معرفة:

```
نظام التشغيل
```

مثل:

- Linux
- Windows

```
nmap -O target
```
# `--osscan-guess`

هذا خيار إضافي لـ `-O`.

# ماذا يفعل؟

يجعل Nmap:

```
يخمن نظام التشغيل حتى لو لم يكن متأكدًا
```

# مثال

```
nmap -O --osscan-guess 192.168.1.10
```


---
# `-A`

Aggressive Scan.

يشغل عدة أشياء معًا:

- OS Detection
- Version Detection
- NSE Scripts
- Traceroute

يعني تقريبًا:

```
Full Enumeration
```

```
nmap -A target
```

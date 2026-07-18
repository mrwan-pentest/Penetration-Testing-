

# 🧠 Subdomain Enumeration with Sublist3r

---

# 📌 أولًا: ما معنى Subdomain Enumeration؟

يعني:

> البحث عن النطاقات الفرعية (Subdomains) الخاصة بالموقع

مثال:

```
example.com
```

قد يكون لديه:

```
mail.example.com
admin.example.com
dev.example.com
test.example.com
```

هذه كلها Subdomains.

---

# 📌 ما هي Sublist3r ؟

أداة OSINT تُستخدم لاكتشاف الـ Subdomains الخاصة بأي دومين.

---

# 🎯 لماذا هذا مهم في الاختراق؟

لأن أحيانًا:

- الموقع الرئيسي آمن
- لكن subdomain فرعي يكون ضعيف 

مثال:

```
dev.example.com
```

قد يحتوي:

- لوحة تحكم
- نسخة تجريبية
- إعدادات ضعيفة

---

# ⚙️ كيف تعمل الأداة؟

تبحث في:

- محركات البحث
- شهادات SSL
- قواعد بيانات عامة
- مواقع أرشفة DNS

يعني:

> تجمع معلومات من الإنترنت بشكل Passive غالبًا

---

# ⚙️ طريقة الاستخدام

## فحص دومين:

```
sublist3r -d example.com
```

---

# 🔍 شرح الأمر

|الجزء|المعنى|
|---|---|
|`sublist3r`|تشغيل الأداة|
|`-d`|تحديد الدومين|
|`example.com`|الهدف|

---

# 📦 ماذا تعطيك النتائج؟

مثلًا:

```
admin.example.com
mail.example.com
dev.example.com
api.example.com
```

---

# ⚡ خيارات مهمة

## حفظ النتائج في ملف

```
sublist3r -d example.com -o results.txt
```

### `-o`

تعني:

> Output file

---

## تحديد عدد الـ Threads

```
sublist3r -d example.com -t 50
```

### `-t`

تعني:

> عدد العمليات المتزامنة (Threads)

كلما زادت:

- السرعة تزيد
- لكن قد يضغط أكثر على الشبكة
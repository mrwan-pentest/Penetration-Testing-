
DNSrecon هي أداة تُستخدم في اختبار الاختراق لجمع معلومات عن نظام الـ **DNS** الخاص بالدومين (Domain).

بمعنى بسيط:

> تساعدك تعرف “وش المخفي وراء الموقع” عن طريق تحليل DNS.

---

## 🔍 ما هي DNSrecon؟

- أداة OSINT و Reconnaissance
- تُستخدم لمعرفة سجلات DNS الخاصة بأي دومين
- تساعدك في اكتشاف:
    - Subdomains (نطاقات فرعية)
    - IP Addresses
    - Mail servers
    - Name servers
    - معلومات إضافية عن البنية التحتية للموقع

---

## 🧩 ماذا تفحص DNSrecon؟

### 1. 🧾 DNS Records

- A Record → يربط الدومين بـ IP
- MX Record → سيرفرات البريد
- NS Record → أسماء السيرفرات
- TXT Record → معلومات إضافية

---

### 2. 🌐 Subdomain Enumeration

- تبحث عن:
    - admin.example.com
    - mail.example.com
    - dev.example.com

---

### 3. 🎯 Zone Transfer (مهم جدًا في eJPT)

- تحاول تسحب كل بيانات DNS من السيرفر
- إذا السيرفر ضعيف → يعطيك كل الدومينز دفعة واحدة 😬



## ⚙️ كيف تُستخدم (أمثلة بسيطة)

### فحص دومين:

```
dnsrecon -d example.com
```

### البحث عن Subdomains:

```
dnsrecon -d example.com -t brt
```

### محاولة Zone Transfer:

```
dnsrecon -d example.com -t axfr
```



Explain:
```
dnsrecon -d example.com
```

- `dnsrecon` = تشغيل الأداة
- `-d` = تحديد الدومين (Domain)
- `example.com` = الهدف

يعني: “يا DNSrecon حلّل لي هذا الموقع”

---

# 1️⃣ فحص الدومين الأساسي

```
dnsrecon -d example.com
```

## 🔍 ماذا يفعل؟

- يجمع معلومات DNS الأساسية عن الموقع

## 📦 ماذا يعطيك؟

- IP Address للموقع
- Name Servers (NS)
- Mail Servers (MX)
- TXT Records
- أحيانًا Subdomains بسيطة

## 🧠 الفكرة:

> هذا “فحص عام” يعطيك صورة أولية عن البنية

---

# 2️⃣ البحث عن Subdomains

```
dnsrecon -d example.com -t brt
```

## 🔍 ماذا يعني `-t brt`؟

- `-t` = نوع الفحص (Type)
- `brt` = Brute Force

## 🧨 ماذا يفعل؟

- يجرب أسماء كثيرة تلقائيًا مثل:
    - admin.example.com
    - test.example.com
    - mail.example.com

## 🎯 الهدف:

> اكتشاف subdomains مخفية غير ظاهرة علنًا

## 🧠 الفكرة:

- مثل “تخمين كلمات المرور” لكن بدل كلمات مرور → أسماء subdomains

---

# 3️⃣ محاولة Zone Transfer (مهم جدًا)

```
dnsrecon -d example.com -t axfr
```

## 🔍 ماذا يعني `axfr`؟

- AXFR = DNS Zone Transfer

## 🧨 ماذا يحاول يفعل؟

- يسحب **كل بيانات DNS دفعة واحدة** من السيرفر

## ⚠️ إذا كان السيرفر ضعيف:

يعطيك:

- كل subdomains
- كل IPs
- كل السجلات DNS

## 🎯 الهدف:

> الحصول على “خريطة كاملة” للموقع

## 🧠 الفكرة:

- كأنك تطلب من السيرفر:  
    “اعطني كل معلوماتك الداخلية عن الدومين”

# 📌 ما هي أداة WafW00f ؟

أداة تُستخدم لاكتشاف:

> هل الموقع يستخدم WAF أم لا؟

وإذا نعم:

> ما نوع الـ WAF المستخدم؟

---

# 📌 ما هو WAF أصلًا؟

## 🔰 WAF = Web Application Firewall

هو جدار حماية خاص بالمواقع والتطبيقات web.

### 🎯 وظيفته:

- يراقب طلبات HTTP/HTTPS
- يمنع الهجمات مثل:
    - SQL Injection
    - XSS
    - LFI/RFI
    - وغيرها




---

# 🧩 لماذا هذا مهم في الاختبار؟

لأن وجود WAF يعني:

- بعض الهجمات قد تُحجب
- بعض الـ payloads لن تعمل
- تحتاج طرق bypass أو payloads مختلفة

---

# ⚙️ طريقة الاستخدام

## فحص موقع:

```
wafw00f example.com
```

![[Pasted image 20260510132937.png]]


في أداة WafW00f الخيار:

```
-a
```

يعني:

## 📌 Find all matches

أي:

> اعرض جميع أنواع الـ WAF المحتملة

---

# 🧠 بدون `-a`

الأداة غالبًا:

- تتوقف عند أول WAF تكتشفه

مثال:

```
Cloudflare detected
```

---

# 🧠 مع `-a`

الأداة تحاول:

- تعرض كل البصمات المطابقة
- وكل الـ WAFs المحتملة

مثال:

```
Cloudflare detectedAkamai detectedModSecurity detected
```

---

# ⚡ الاستخدام 

![[Pasted image 20260510134034.png]]


---

# 🔍 ماذا يفعل الأمر؟

- يرسل Requests للموقع
- يحلل الـ Responses
- يحاول معرفة:
    - هل يوجد WAF؟
    - من الشركة المصنعة؟

---

# 📦 مثال على النتائج

قد يظهر:

```
The site is behind Cloudflare WAF
```

أو:

```
No WAF detected
```

---

# 🧠 كيف يكتشف الـ WAF؟

يعتمد على:

- HTTP Headers
- Cookies
- طريقة رد السيرفر
- رسائل الحظر
- بصمات خاصة لكل WAF

---

# 🛡️ أمثلة على WAFs مشهورة

- Cloudflare
- AWS WAF
- Imperva
- F5 BIG-IP
- Akamai

---

# ⚡ فكرة مهمة جدًا في eJPT

وجود WAF لا يعني:

> “الموقع آمن بالكامل”

لكن يعني:

> يوجد طبقة حماية قد تعيق بعض الهجمات
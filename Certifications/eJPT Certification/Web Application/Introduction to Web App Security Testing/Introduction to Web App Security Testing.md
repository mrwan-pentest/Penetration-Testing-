


## ما هو Web Application؟

تطبيق يعمل على Web Server ويتم الوصول إليه عبر المتصفح.

أمثلة:

- Gmail
- Facebook
- Amazon
- Office 365

---

## كيف يعمل؟

```
Browser      ↓
HTTP/HTTPS   ↓
Web Server   ↓
Database
```

المستخدم يرسل Request.

السيرفر يعالجه ويرجع Response.

---

## مكونات الواجهة

### HTML

يبني الصفحة.

### CSS

التصميم والشكل.

### JavaScript

التفاعل والحركة.

---

## Client-Server Architecture

المتصفح = Client

السيرفر = Server

العميل يطلب.

السيرفر يرد.

---

## Stateless HTTP

HTTP لا يتذكر المستخدم.

لذلك تستخدم التطبيقات:

- Cookies
- Sessions
- Tokens

لكي تعرف أن هذا نفس المستخدم.

---

# Web Application Security

هدفه حماية:

### Confidentiality

سرية البيانات.

---

### Integrity

عدم تعديل البيانات بدون صلاحية.

---

### Availability

استمرار الخدمة وعدم توقفها.

---

## لماذا تطبيقات الويب هدف مهم؟

لأنها غالبًا تحتوي:

- Users
- Passwords
- Credit Cards
- Personal Data

وهي متاحة للعالم كله عبر الإنترنت.

---

# Threat vs Risk

## Threat

شيء يمكن أن يسبب ضررًا.

مثال:

- Hacker
- Malware
- Phishing

---

## Risk

احتمال حدوث الضرر + حجم الضرر.

```
Threat + Vulnerability = Risk
```

---

# أشهر تهديدات الويب

## SQL Injection

حقن أوامر SQL داخل التطبيق.

قد يؤدي إلى:

- قراءة البيانات
- تعديل البيانات
- حذف البيانات

---

## XSS

حقن JavaScript داخل صفحات الموقع.

قد يؤدي إلى:

- سرقة Cookies
- سرقة Session
- السيطرة على حسابات المستخدمين

---

## CSRF

إجبار مستخدم مسجل دخول على تنفيذ عملية دون علمه.

مثال:

- تغيير كلمة المرور
- تعديل الحساب

---

## Security Misconfiguration

إعدادات أمنية خاطئة.

أمثلة:

- كلمات مرور افتراضية
- Debug Mode
- صفحات إدارة مكشوفة

---

## Sensitive Data Exposure

تسريب بيانات حساسة.

مثل:

- كلمات المرور
- البيانات الشخصية
- معلومات الدفع

---

## Brute Force

تخمين كلمات المرور باستمرار حتى النجاح.

---

## Credential Stuffing

استخدام بيانات مسربة سابقًا لتسجيل الدخول في مواقع أخرى.

---

## File Upload Vulnerabilities

رفع ملفات خبيثة بدل الملفات العادية.

قد يؤدي إلى:

```
Remote Code ExecutionWeb Shell
```

---

## SSRF

جعل السيرفر نفسه يرسل طلبات نيابة عن المهاجم.

قد يسمح بالوصول إلى:

- Internal Services
- Cloud Metadata
- Internal Networks

---

## DoS / DDoS

إغراق السيرفر بالطلبات.

الهدف:

تعطيل الخدمة.

---

## Broken Access Control

فشل نظام الصلاحيات.

مثال:

المستخدم العادي يستطيع الوصول إلى بيانات مستخدم آخر أو لوحة الإدارة.

---

# Web Application Security Testing

هو عملية البحث عن:

- Vulnerabilities
- Weaknesses
- Security Risks

قبل أن يستغلها المهاجم.

---

## Vulnerability Scanning

فحص آلي باستخدام أدوات.

يبحث عن:

- SQLi
- XSS
- Misconfigurations
- Software Versions

---

## Penetration Testing

محاكاة هجوم حقيقي.

الهدف:

التحقق من إمكانية استغلال الثغرات.

---

## Code Review

مراجعة الكود للبحث عن:

- أخطاء برمجية
- ثغرات
- إعدادات غير آمنة

---

## Authentication Testing

اختبار آلية تسجيل الدخول.

السؤال:

```
هل أنت فعلاً من تدعي أنك؟
```

---

## Authorization Testing

اختبار الصلاحيات.

السؤال:

```
هل تملك صلاحية الوصول لهذا المورد؟
```

---

## Input Validation Testing

اختبار كيف يتعامل التطبيق مع مدخلات المستخدم.

مهم جدًا لمنع:

- SQLi
- XSS

---

## Session Management Testing

اختبار إدارة الـ Session.

البحث عن مشاكل مثل:

- Session Hijacking
- Session Fixation

---

## API Security Testing

اختبار واجهات API.

التركيز على:

- Authentication
- Authorization
- Data Exposure

---

# الفرق بين Security Testing و Pentesting

## Security Testing

الهدف:

```
Finding Vulnerabilities
```

اكتشاف الثغرات فقط.

قد يكون يدويًا أو آليًا.

---

## Pentesting

الهدف:

```
Exploiting Vulnerabilities
```

استغلال الثغرات والتأكد من تأثيرها.
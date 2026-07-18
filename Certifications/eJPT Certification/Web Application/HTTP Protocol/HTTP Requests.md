
# HTTP Request Components

أي HTTP Request يتكون عادة من 3 أجزاء:

```
Request Line
Headers
Body (اختياري)
```

مثال:

```
GET /login HTTP/1.1
Host: example.com
User-Agent: Firefox
Cookie: session=123456
username=admin&password=123456
```

---

# 1) Request Line

أول سطر في الطلب.

يتكون من 3 أجزاء:

```
GET /login HTTP/1.1
```

---

## HTTP Method

```
GET
```

يحدد ماذا تريد أن تفعل.

أمثلة:

- GET
- POST
- PUT
- DELETE
- PATCH


## URL / Path

```
/login
```

الملف أو الصفحة المطلوبة.


## HTTP Version

```
HTTP/1.1
```

إصدار البروتوكول.

---

# Request Headers

بعد Request Line تأتي الـ Headers.

شكلها دائماً:

```
Header-Name: Value
```

مثال:

```
Host: google.com
User-Agent: Firefox
```

الـ Headers تعطي معلومات إضافية للسيرفر.

---

# Request Body

اختياري.

يستخدم غالباً مع:

```
POST
PUT
PATCH
```

مثال:

```
POST /login HTTP/1.1

username=admin&password=123456
```

البيانات الموجودة أسفل الـ Headers هي الـ Body.

---

# مثال عملي كامل

```
GET / HTTP/1.1
Host: www.google.com
User-Agent: Firefox
Accept: text/html
Accept-Encoding: gzip
Connection: keep-alive
```

---

تقسيمه:

## Request Line

```
GET / HTTP/1.1
```

---

## Headers

```
Host: www.google.com
User-Agent: Firefox
Accept: text/htm
lAccept-Encoding: gzip
Connection: keep-alive
```

---

## Body

لا يوجد لأن GET عادة لا يحتوي Body.

---

# HTTP Methods




## GET

يستخدم لجلب البيانات.

مثال:

```
GET /products
```

معناه:

```
اعرض لي المنتجات
```


خصائصه:

- لا يغير البيانات.
- يستخدم للقراءة فقط.


مثال:

```
GET /profile
```

---

## POST

يرسل بيانات للسيرفر.

مثال:

```
POST /login
```

Body:

```
username=admin&password=123456
```


يستخدم في:

- Login
- Registration
- Upload

---

## PUT

تحديث مورد كامل.

مثال:

```
PUT /users/1
```


إذا كان المستخدم:

```
{ "name":"Ali", "age":20}
```

وأرسلت PUT:

```
{ "name":"Ahmed", "age":25}
```

يتم استبدال البيانات كاملة.

---

## PATCH

يشبه PUT لكن لتعديل جزء فقط.

مثال:

```
{ "age":25}
```

يعدل العمر فقط.

---

## DELETE

يحذف مورد.

```
DELETE /users/1
```


معناه:

```
احذف المستخدم رقم 1
```

---

## HEAD

مثل GET لكن بدون المحتوى.

يرجع Headers فقط.

مثال:

```
HEAD /file.zip
```


مفيد لمعرفة:

- حجم الملف
- تاريخ التعديل
- وجود الملف

---

## OPTIONS

يعرض ما هي الطرق المسموح بها.

مثال:

```
OPTIONS /api/users
```

قد يرجع:

```
GET, POST, PUT, DELETE
```



---

# URL / Path

في:

```
GET /downloads/index.php HTTP/1.1
```

الـ Path هو:

```
/downloads/index.php
```


الصفحة الرئيسية دائماً:

```
/
```

أمثلة:

```
//login/admin/uploads/api/users
```

---

# HTTP Protocol Version

في:

```
GET / HTTP/1.1
```

الجزء:

```
HTTP/1.1
```

هو إصدار البروتوكول.

---

# Host Header

من أهم الـ Headers.

مثال:

```
Host: www.google.com
```


السيرفر قد يستضيف عدة مواقع على نفس الـ IP.

الـ Host يخبره أي موقع تريد.


مثال:

```
IP واحد│├── google.com├── mail.google.com└── maps.google.com
```

السيرفر يحدد الموقع المطلوب من Host Header.


---

# User-Agent Header

مثال:

```
User-Agent: Firefox
```


يخبر السيرفر:

- نوع المتصفح
- الإصدار
- نظام التشغيل

مثال حقيقي:

```
User-Agent: Mozilla/5.0 (Windows NT 10.0)
```


---

# Accept Header

مثال:

```
Accept: text/html
```


يخبر السيرفر:

```
ما نوع البيانات التي أستطيع استقبالها؟
```


أمثلة:

```
Accept: text/html
```

HTML فقط.



---

# Accept-Encoding Header

مثال:

```
Accept-Encoding: gzip, deflate
```


معناه:

```
يمكنك ضغط البيانات قبل إرسالها
```


السيرفر يرسل:

```
gzip
```

بدلاً من البيانات العادية.

النتيجة:

- سرعة أكبر
- استهلاك أقل للشبكة

---

# Connection Header

مثال:

```
Connection: keep-alive
```


معناه:

```
لا تغلق الاتصال
```
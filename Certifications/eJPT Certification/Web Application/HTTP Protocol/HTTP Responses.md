
# ما هو HTTP Response؟

بعد أن يرسل المتصفح Request:

```
GET / HTTP/1.1
Host: google.com
```

السيرفر يرد:

```
HTTP/1.1 200 OK
Content-Type: text/html
<html>...</html>
```

هذا يسمى:

```
HTTP Response
```

---

# مكونات HTTP Response

يتكون من:

```
Status Line
Headers
Body
```

# مثال كامل

```
HTTP/1.1 200 OK
Date: Fri, 13 Mar 2015 11:26:05 GMT
Content-Type: text/html
Content-Length: 258
<html>...</html>
```

---

# 1) Status Line

أول سطر في الـ Response.

مثال:

```
HTTP/1.1 200 OK
```

يتكون من:

### HTTP Version

```
HTTP/1.1
```

---

### Status Code

```
200
```

---

### Status Message

```
OK
```

---

# أهم Status Codes

## 200 OK

```
200 OK
```

معناه:

```
كل شيء نجح
```


## 301 Moved Permanently

```
301
```

معناه:

```
تم نقل الصفحة نهائياً
```

مثال:

```
http://site.com
↓
https://site.com
```


## 302 Found

```
302
```

إعادة توجيه مؤقتة.


## 400 Bad Request

```
400
```

الطلب الذي أرسلته غير صحيح.


## 401 Unauthorized

```
401
```

يجب تسجيل الدخول.


مثال:

```
API يحتاج Token
```

ولم ترسل Token.


## 403 Forbidden

```
403
```

السيرفر فهمك.

لكن لا يسمح لك بالدخول.


مثال:

```
/admin
```

أنت لست Admin.


## 404 Not Found

```
404
```

الصفحة غير موجودة.


من أشهر الأكواد في الـ Web.


## 500 Internal Server Error

```
500
```

خطأ داخل السيرفر نفسه.

ظهور 500 أحياناً يدل على:

- خطأ برمجي
- Input غير متوقع
- احتمال وجود ثغرة

---

# Response Headers

بعد Status Line تأتي الـ Headers.

مثال:

```
Date: ...
Content-Type: ...
Server: ...
```

---

# Date Header

مثال:

```
Date: Fri, 13 Mar 2015 11:26:05 GMT
```


يبين:

```
وقت إنشاء الرد
```

---

# Cache-Control Header

من أهم الـ Headers.

مثال:

```
Cache-Control: private, max-age=3600
```


وظيفته:

```
التحكم في التخزين المؤقت (Cache)
```


بدلاً من تحميل الصفحة كل مرة.

المتصفح يحتفظ بنسخة مؤقتة.


## private

```
Cache-Control: private
```

البيانات تخص مستخدماً واحداً فقط.


## no-cache

```
Cache-Control: no-cache
```

تحقق من السيرفر قبل استخدام النسخة المخزنة.


## no-store

```
Cache-Control: no-store
```

لا تخزن الصفحة أبداً.


يستخدم كثيراً مع:

- البنوك
- الحسابات الحساسة


## max-age

```
Cache-Control: max-age=3600
```

احتفظ بالنسخة لمدة ساعة.

---

# Content-Type Header

من أهم Headers في اختبار الاختراق.

مثال:

```
Content-Type: text/html
```


يخبر المتصفح:

```
ما نوع البيانات القادمة؟
```

---


# Content-Encoding Header

مثال:

```
Content-Encoding: gzip
```


معناه:

```
تم ضغط البيانات قبل إرسالها
```


السيرفر يرسل:

```
HTML مضغوط
```

ثم المتصفح يفك الضغط تلقائياً.


أشهر القيم:

```
gzip
```

---

# Server Header

مثال:

```
Server: Apache
```

أو

```
Server: nginx
```

أو

```
Server: IIS
```


هذا الهيدر يخبرك بنوع Web Server.


---

# Content-Length Header

مثال:

```
Content-Length: 258
```

معناه:

```
حجم الـ Body بالبايت
```


إذا كان:

```
Content-Length: 50000
```

فحجم المحتوى:

```
50000 Bytes
```

---

# Response Body

آخر جزء من الـ Response.

مثال:

```
HTTP/1.1 200 OK
Content-Type: text/html

<html><h1>Welcome</h1></html>
```


الجزء:

```
<html><h1>Welcome</h1></html>
```

هو:

```
Response Body
```
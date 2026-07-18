

# ما هو HTTP؟

HTTP اختصار:

```
HyperText Transfer Protocol
```

وهو البروتوكول المسؤول عن التواصل بين:

```
Browser ↔ Web Server
```

مثال:

عندما تفتح:

```
https://google.com
```

المتصفح لا يفهم الموقع مباشرة.

بل يرسل:

```
HTTP Request
```

إلى السيرفر.

والسيرفر يرد بـ:

```
HTTP Response
```

---

#  Protocol ?
بروتوكول = مجموعة قواعد للتواصل.

مثل اللغة بين شخصين.

إذا لم يتبع الطرفان نفس القواعد فلن يفهم أحدهما الآخر.


---

# HTTP يعمل فوق TCP

في طبقات الشبكات:

```
Application Layer      
↓
HTTP      
↓
TCP      
↓
IP
```

بمعنى:

HTTP يعتمد على TCP لنقل البيانات.

---

# ماذا يعني Stateless؟

هذه من أهم النقاط.

HTTP لا يتذكر الطلب السابق.

مثال:

أرسلت Login.

بعد ثانية أرسلت طلبًا آخر.

HTTP لا يعرف أنك نفس الشخص.

كل Request يعتبر مستقلاً.


لذلك تستخدم المواقع:

- Cookies
- Sessions
- Tokens

لكي تتذكر المستخدم.

---

# Client-Server Model

في HTTP:

## Client

هو المتصفح.

مثل:

- Chrome
- Firefox
- Edge


## Server

هو الموقع.

مثل:

- Google
- Facebook
- Amazon


التواصل يكون:

```
Client   
↓ Request
 Server ↓ 
 Response 
 Client
```

---

# URL و URI

كل Resource له عنوان.

مثال:

```
https://site.com/login
```

أو

```
https://site.com/images/logo.png
```

السيرفر يعرف ماذا تريد من خلال هذا العنوان.


# HTTP Versions

## HTTP 1.0

الإصدار القديم.

كان يفتح اتصالاً جديداً لكل طلب.




## HTTP 1.1

الأكثر انتشاراً.

ميزة مهمة:

```
Persistent Connections
```

يعني:

يمكن إعادة استخدام نفس الاتصال.

بدل فتح اتصال جديد كل مرة.

---

# كيف تتم عملية التواصل؟

عندما تزور موقعاً:

```
Browser    
↓
HTTP Request    
↓
Server    
↓
HTTP Response    
↓
Browser
```

---

# HTTP Request

هو الطلب الذي يرسله العميل.

مثال:

```
GET / HTTP/1.1Host: site.com
```

معناه:

```
أعطني الصفحة الرئيسية
```

---

# HTTP Response

رد السيرفر.

مثال:

```
HTTP/1.1 200 OK
```

ثم يرسل:

- HTML
- CSS
- JavaScript

-

---

# ما معنى Resource؟

أي شيء يمكن طلبه من السيرفر.

مثل:

```
/
```

الصفحة الرئيسية.


```
/login
```

صفحة تسجيل الدخول.


```
/logo.png
```

صورة.


```
/api/users
```

API.

---

# ماذا تعني الرموز؟

## \r

اختصار:

```
Carriage Return
```

يعيد المؤشر لبداية السطر.


## \n

اختصار:

```
Line Feed
```

ينزل للسطر التالي.


## \r\n

يعني:

```
سطر جديد
```

مثل الضغط على Enter.

مثال:

```
GET /login HTTP/1.1
Host: site.com
User-Agent: Firefox
```

كل سطر ينتهي بـ:

```
\r\n
```
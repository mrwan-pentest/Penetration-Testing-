
# ما هو Access Token ؟

في ويندوز، عندما يسجل المستخدم الدخول،  
النظام ينشئ له شيء اسمه:

```
Access Token
```

وهذا التوكن يعتبر:
 “بطاقة الهوية والصلاحيات” الخاصة بالمستخدم داخل النظام.

# ماذا يحتوي الـ Token؟

يحتوي معلومات مثل:

- اسم المستخدم
- الـ SID
- المجموعات (Administrators وغيرها)
- الصلاحيات Privileges
- مستوى الصلاحية

# ما هو Token Impersonation؟

معناه:

> انتحال أو استخدام Token لمستخدم آخر.

يعني بدل أن تعمل بصلاحياتك،  
تستخدم Token خاص بمستخدم أقوى.


# أشهر نوعين

## 1) Impersonation Token

يسمح لك “بالتصرف” كمستخدم آخر مؤقتًا.

## 2) Primary Token

يستخدم لتشغيل Process كامل كمستخدم آخر.


# أشهر أدوات Token Impersonation

## داخل Metasploit

```
incognito
```


## خارج Metasploit

- JuicyPotato
- RoguePotato
- PrintSpoofer
- GodPotato

---
# PrivEsc with Metasploit

## Method 1 auto 
### using incognito

اولا نفعل load  لل incognito

![[Pasted image 20260519132904.png]]

نعرض اليوزرز الذي نستطيح ان ننتحل التوكن الخاص بهم

![[Pasted image 20260519132938.png]]

الان ننتحل التوكن الخاص بهذا الأدمن

![[Pasted image 20260519133022.png]]

وكذه حصلنا عليه

![[Pasted image 20260519133038.png]]


---
# PrivEsc with PrintSpoofer
## Method 2 manual

# أولا
## ارفع الأداة

مثلاً:

```
PrintSpoofer.exe
```


# ثم نفذ:

```
PrintSpoofer.exe -i -c cmd
```


# ماذا تعني الخيارات؟

## -i

Interactive

يعني افتح shell تفاعلي.

---

## -c

الأمر الذي تريد تشغيله.

مثلاً:

```
PrintSpoofer.exe -i -c powershell.exe
```


ويندوز غالبًا:

```
لا يخزن الباسورد الحقيقي
```

بل يخزن:

```
Hash
```

---

# ما هو الـ Hash؟ 

الـ Hash هو:

```
تحويل كلمة المرور إلى قيمة مشفرة ثابتة
```

مثلاً:

```
password123
```

قد تصبح:

```
482c811da5d5b4bc6d497ffa98491e38
```


---

# أين يخزن ويندوز الـ Hashes؟ 

غالبًا داخل:

```
SAM Database
```

---

# ما هو SAM؟ 

اختصار:

```
Security Account Manager
```

ويحتوي:

- المستخدمين
- الـ Password Hashes

---

# أين يوجد؟

```
C:\Windows\System32\config\SAM
```

---

# هل يمكن فتحه مباشرة؟ ❌

غالبًا لا،  
لأن النظام يقفله أثناء التشغيل.

ولهذا يحتاج المهاجم:

- SYSTEM
- أو أدوات خاصة

---

# أنواع الـ Hashes في ويندوز 

## 1) LM Hash

قديم جدًا وضعيف.

---

# لماذا ضعيف؟ 

لأنه:

- يحول الأحرف لـ Uppercase
- يقسم الباسورد نصفين
- سهل الكسر جدًا

---

# مثال:

```
PASSWORD
```

---

# هل ما زال مستخدم؟ ❌ غالبًا

الأنظمة الحديثة:

```
تعطله
```

---

# 2) NTLM Hash 

الأهم والأشهر.

---

# ما هو NTLM؟ 

اختصار:

```
NT LAN Manager
```

---

# هذا هو الـ Hash الذي نستخدمه غالبًا في:

- Pass-the-Hash
- SMB Authentication
- WinRM
- PsExec

---

# مثال NTLM Hash 

```
b4b9b02e6f09a9bd760f388b67351e2b
```

---

# كيف يحصل المهاجم على الـ Hashes؟ 

بعد الوصول لـ:

```
Administrator أو SYSTEM
```

يستخدم أدوات مثل:

- Mimikatz
- secretsdump
- hashdump
- reg save



---


## ثاني Hash

هذا المهم:

```
NTLM Hash
```

---

# كيف تُسرق الـ Hashes أيضًا؟ 

من:

```
LSASS Memory
```

---

# ما هو LSASS؟ 
اختصار:

```
Local Security Authority Subsystem Service
```


# ما وظيفته؟ 

هو Process مهم جدًا في ويندوز مسؤول عن:

- تسجيل الدخول
- Authentication
- Password validation
- Tokens
- Kerberos
- NTLM
- Sessions


# يعني باختصار 

LSASS هو:

```
مركز إدارة تسجيل الدخول والصلاحيات
```
---

# أشهر أداة 

# Mimikatz


---

# الفرق بين SAM و LSASS 

## SAM

يحتوي Hashes المخزنة.

---

## LSASS

يحتوي Credentials حية داخل الذاكرة.



**John the Ripper (John)** هي أداة لاختبار قوة كلمات المرور واستعادة كلمات المرور من الـ Hashes.

الفكرة الأساسية:

```
Password --> Hash
```

John يحاول العثور على كلمة المرور الأصلية التي أنتجت ذلك الـ Hash.

---

## أين تستخدم؟

في الاختبارات الأمنية بعد الحصول على:

```
/etc/shadow
```

أو:

```
SAM Database
```

أو أي ملف يحتوي Hashes.

---



## أشهر أمر

```
john hashes.txt
```

الوظيفة:  
محاولة كسر جميع الـ Hashes الموجودة في الملف.

---

## استخدام Wordlist

```
john --wordlist=/usr/share/wordlists/rockyou.txt hashes.txt
```

الوظيفة:  
تجربة كلمات المرور الموجودة في RockYou على الـ Hashes.

---

## عرض النتائج

```
john --show hashes.txt
```

الوظيفة:  
إظهار كلمات المرور التي تم العثور عليها.

---

## معرفة أنواع الـ Hashes

أشهر الأنواع:

```
$1$ = MD5 Crypt$5$ = SHA256 Crypt$6$ = SHA512 Crypt
```

مثال:

```
$6$abc$...
```

هذا SHA512 Crypt.

---

## تحديد النوع يدويًا

```
john --format=sha512crypt hashes.txt
```

الوظيفة:  
إجبار John على استخدام صيغة SHA512 Crypt.

---

## حفظ الجلسة

إذا أوقفت John:

```
john --restore
```

الوظيفة:  
استكمال العمل من آخر نقطة.

---

## أوضاع العمل

### Single Mode

يعتمد على معلومات المستخدم:

```
john hashes.txt
```

---

### Wordlist Mode

يعتمد على قاموس كلمات:

```
john --wordlist=rockyou.txt hashes.txt
```

---

### Incremental Mode

يجرب جميع الاحتمالات الممكنة (بطيء جدًا):

```
john --incremental hashes.txt
```

---

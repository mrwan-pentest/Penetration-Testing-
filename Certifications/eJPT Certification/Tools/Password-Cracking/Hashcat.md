
# ما هي Hashcat؟

**Hashcat** هي:

> أداة متقدمة لكسر (Crack) كلمات المرور من خلال الهاش باستخدام قوة المعالج أو كرت الشاشة (GPU)

---

# ماذا تعني “كسر الهاش”؟

عندك:

cd06ca7c7e10c99b1d33b7485a2ed808

هذا **NTLM Hash**

هدف Hashcat:  
👉 إيجاد كلمة المرور الأصلية (مثلاً: Password123)

---

# كيف تعمل Hashcat؟

تعتمد على فكرة:

1. توليد كلمات محتملة
2. تحويلها إلى Hash
3. مقارنة النتيجة مع الهاش الهدف

إذا تطابق:  
👉 تم العثور على كلمة المرور

---

# أنواع الهجمات في Hashcat

## 1. Dictionary Attack

تستخدم قائمة كلمات جاهزة

hashcat -m 1000 hash.txt wordlist.txt

---

## 2. Brute Force

يجرب كل الاحتمالات

hashcat -m 1000 hash.txt ?a?a?a?a?a?a

---

## 3. Hybrid Attack

كلمة + أرقام

hashcat -m 1000 hash.txt wordlist.txt ?d?d

---

## 4. Rule-Based Attack

تعديل الكلمات (أول حرف كابيتال، إضافة أرقام...)

hashcat -m 1000 hash.txt wordlist.txt -r rules/best64.rule

---

# ما معنى -m ؟

هو نوع الهاش

## أمثلة:

|النوع|القيمة|
|---|---|
|NTLM|1000|
|MD5|0|
|SHA1|100|
|bcrypt|


---

# ما هي Rules في Hashcat؟

هي:

> تعليمات تغيّر الكلمات من الـ wordlist قبل ما يتم تحويلها إلى Hash

بدل ما تجرب:

password

تقدر تولّد:

Password  
password1  
Password123  
P@ssword

بدون ما تضيفها فعلياً في القائمة

---

# كيف تضيف Rule؟

## الطريقة الأساسية:

hashcat -m 1000 hash.txt wordlist.txt -r rule.txt

---

# أهم القواعد (Rules)

## 1. أول حرف Capital

c

تحول:

password → Password

---

## 2. كل الأحرف Capital

u

---

## 3. كل الأحرف Small

l

---

## 4. إضافة رقم في النهاية

$1

---

## 5. إضافة أرقام متعددة

$1$2$3

---

## 6. استبدال حرف

s a @

تحول:

password → p@ssword

---

# كيف تبني Rule خاص فيك

## مثال 1:

### أول حرف كابيتل + إضافة 123

c $1 $2 $3

---

## مثال 2:

### أول حرف كابيتل + إضافة رقمين عشوائيين

c $1 $2

---

## مثال 3:

### Capital + استبدال a بـ @

c sa@

---

# كتابة Rule في ملف

افتح ملف:

nano myrules.rule

واكتب:

c $1 $2 $3  
c sa@  
c $!

---

# تشغيله

hashcat -m 1000 hash.txt wordlist.txt -r myrules.rule

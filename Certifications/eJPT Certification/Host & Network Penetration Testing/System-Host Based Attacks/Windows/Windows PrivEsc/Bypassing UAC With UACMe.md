
#  ما هو UAC؟ 

UAC اختصار:

```
User Account Control
```

وهي نافذة ويندوز المشهورة:

```
Do you want to allow this app to make changes?
```


# لماذا UAC موجود؟ 

حتى لو كنت:

```
Administrator
```

ويندوز لا يعطيك صلاحيات كاملة مباشرة.

بل يشغلك بصلاحيات:

```
محدودة
```

حتى توافق على نافذة الـ UAC.


# الفكرة المهمة جدًا

في ويندوز يوجد فرق بين:

## Administrator

عضو Administrators Group.


## Elevated Administrator

Admin مع:

```
صلاحيات مرتفعة فعلًا
```


# لذلك أحيانًا ترى هذا 

داخل Meterpreter:

```
getuid
```

ويظهر:

```
WIN-XXX\Administrator
```

لكن عندما تحاول:

- Disable Defender
- Dump SAM
- SYSTEM Actions

تفشل.


# لماذا؟ 

لأن:

```
UAC ما زال يحمي النظام
```


# ما معنى Bypass UAC؟ 

يعني:

```
تجاوز نافذة UAC والحصول على Elevated Session
```

بدون أن يضغط المستخدم:

```
Yes
```


---
# الآن ما هي UACMe؟ 

UACMe


# هي عبارة عن ماذا؟ 

مشروع يحتوي:

```
عشرات طرق تجاوز UAC
```

باستخدام:

- AutoElevate
- DLL Hijacking
- Mock Directories
- COM Hijacking
- Scheduled Tasks
- وغيرها


# لماذا يوجد كل هذه الطرق؟

لأن:

```
مايكروسوفت كانت تصلح طريقةويكتشف الباحثون طريقة جديدة
```

# رابط المستودع 

https://github.com/hfiref0x/UACME

![[Pasted image 20260519015121.png]]


لو اردنا ان تعرف كل طريقة لأي نظام تستخدم من هنا

![[Pasted image 20260519015200.png]]


لو أردنا تنزيل الأداه من هنا

![[Pasted image 20260519015232.png]]


---

# PrivEsc with UCAMe

اولا نتحقق اننا ضمن جروب الادمنستراتور

![[Pasted image 20260519020307.png]]

انشأنا ملف  Temp  عشان ننقل الى داخله الأداه والبايلود

أو

```
cd C:\\Users\\admin\\AppData\\Local\\Temp
```

![[Pasted image 20260519020410.png]]

نقلنا الأداه 

![[Pasted image 20260519020436.png]]

ثم نقلنا البايلود

![[Pasted image 20260519020459.png]]


ايضا شغلنا  Lesner عشان نحصل على الجلسة

![[Pasted image 20260519020602.png]]


شغلنا الأداه 
23 معناه الطريقة التي سوف نستخدمها وكل طريقة تستهدف انماظ محددة

![[Pasted image 20260519020659.png]]


وحصلنا على meterpreter

---

في مديولات على الميتا ولكن الأفضل هذه الأداة
لو نريد نبجث عن موديلات نكتب

search bypassuac

ونجرب الموديلات المتاحه

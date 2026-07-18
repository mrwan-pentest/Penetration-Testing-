




هي ميزة في نظام ملفات NTFS تسمح للملف الواحد أن يحتوي على “Streams” إضافية مخفية.

يعني الملف ليس مجرد محتوى واحد فقط.

# الفكرة 

عندك ملف عادي:

```
note.txt
```

عادة يحتوي:

```
hello
```

لكن في NTFS يمكن إضافة محتوى مخفي داخله:

```
note.txt:hidden
```

بدون أن يظهر في:

```
dir
```


# لماذا هذا مهم أمنيًا؟

لأن المهاجم يستطيع:

- إخفاء Payload
- إخفاء سكربت
- إخفاء بيانات
- عمل Persistence

داخل ملف يبدو طبيعي.

# هل ADS تعتبر ملفًا جديدًا؟

❌ لا

هي Stream مرتبط بملف موجود.

# أين تعمل؟

✅ فقط على:

```
NTFS
```


# هل تعمل على FAT32؟

❌ لا.

# كيف أعرف أن جهازي NTFS؟

نفذ:

```
fsutil fsinfo volumeinfo C:
```

سترى:

```
File System Name : NTFS
```

---

# عمليًا — إنشاء ADS

## 1) أنشئ ملف عادي

```
echo hello > file.txt
```


# 2) أضف Stream مخفي

```
notepad file.txt:hidden.txt
```

سيقول:

```
Do you want to create?
```

اضغط Yes.


# 3) اكتب أي شيء

مثلاً:

```
this is hidden
```

ثم احفظ.


# ماذا حدث الآن؟

أصبح لدينا:

```
file.txt
```

لكن داخله stream مخفي.


# لو تفحص عادي

```
dir
```

لن ترى شيئًا.

سيظهر فقط:

```
file.txt
```


# كيف نقرأ الـ ADS؟

```
notepad file.txt:hidden.txt
```

أو:

```
more < file.txt:hidden.txt
```


# كيف نكشف الـ ADS؟

## باستخدام dir /r

```
dir /r
```

سيظهر:

```
file.txt:hidden.txt:$DATA
```

---

# ماذا يعني $DATA؟

هذا هو الـ stream الأساسي لنظام NTFS.

---

# عمليًا — إخفاء ملف داخل ADS

## أنشئ payload تجريبي

مثلاً:

```
calc.exe
```


# انسخه داخل stream

```
type calc.exe > file.txt:calc.exe
```


# الآن payload مخفي داخل file.txt




# كيف نشغل payload من ADS؟

قديماً:

```
start .\file.txt:calc.exe
```

---

# لكن في الأنظمة الحديثة

ويندوز أصبح يمنع كثيرًا من هذه الأساليب مباشرة.

لذلك غالبًا تُستخدم ADS اليوم:

- للإخفاء
- persistence
- bypass بسيط
- forensic tricks

أكثر من التنفيذ المباشر.
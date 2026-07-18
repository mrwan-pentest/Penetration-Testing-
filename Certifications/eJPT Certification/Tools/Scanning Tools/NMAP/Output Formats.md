# `-oN`

حفظ النتائج كنص عادي.

```
nmap -oN scan.txt target
```
---
# `-oX`

حفظ النتائج بصيغة:

```
XML
```

مفيد للأدوات والتحليل.

```
nmap -oX scan.xml target
```

مثال على استخدامها في الميتا

![[Pasted image 20260513145212.png]]

![[Pasted image 20260513145247.png]]

---
# `-oG` (غير مستخدم بكثرة)

يعني:

```
Grepable Output
```


# الفكرة

صيغة:

```
سهلة للبحث بـ grep
```

# مثال

```
nmap -oG scan.gnmap TARGET
```

# لماذا مفيد؟

حتى تستخدم:

```
grepawkcut
```


# مثال

```
grep open scan.gnmap
```



هذا النوع:

```
أصبح قديم نسبيًا
```

وXML أفضل غالبًا.

---
# `-oA`

يعني:

```
All Formats
```


# ماذا يفعل؟

يحفظ:

- Normal
- XML
- Grepable

كلها دفعة واحدة.
# مثال

```
nmap -oA fullscan TARGET
```

# سينتج:

|الملف|النوع|
|---|---|
|`fullscan.nmap`|Normal|
|`fullscan.xml`|XML|
|`fullscan.gnmap`|Grepable|
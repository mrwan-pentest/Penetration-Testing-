
وهو:

```
نظام سكربتات داخل Nmap
```

يسمح لـ Nmap بأن يفعل أكثر من مجرد:

- Port Scanning
- Service Detection
---
مسار ال Scripts 

	/usr/share/nmap/scripts

# `-sC`

تشغيل:

```
Default NSE Scripts
```

يفحص:

- معلومات إضافية
- vulnerabilities بسيطة
- banners
- configs

```
nmap -sC target
```

---
# `--script-help`


يستخدم لـ:

```
عرض معلومات ومساعدة عن سكربتات NSE
```

---

# فكرته 🔥

بدل أن تشغل السكربت مباشرة،  
تستطيع معرفة:

- ماذا يفعل؟
- لأي Category ينتمي؟
- كيف يستخدم؟
- هل هو آمن؟
- ما هي Arguments الخاصة به؟

---

# مثال

```
nmap --script-help http-enum
```
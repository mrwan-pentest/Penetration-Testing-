فكرتها ببساطة:

> تتصل بخدمة Windows عبر RPC وتستخرج معلومات عن النظام والمستخدمين والدومين.

---

## متى أستخدمها؟

بعد أن تجد:

```
445/tcp open
```

أو:

```
139/tcp open
```

على جهاز Windows.

---

## الاتصال

بدون كلمة مرور (Null Session):

```
rpcclient -U "" -N 192.168.1.10
```

مع اسم مستخدم وكلمة مرور:

```
rpcclient -U administrator 192.168.1.10
```

---

## أهم الأوامر داخل rpcclient

### معرفة معلومات النظام

```
srvinfo
```

يعرض:

- اسم النظام
- إصدار ويندوز

---

### معرفة اسم الدومين

```
lsaquery
```

يعرض:

- Domain Name
- SID

---

### استخراج المستخدمين

```
enumdomusers
```

مثال:

```
user:[Administrator]user:[Guest]user:[john]
```

هذا من أكثر الأوامر استخدامًا.

---

### استخراج المجموعات

```
enumdomgroups
```

---

### معلومات مستخدم معين

أولاً خذ RID من `enumdomusers`

ثم:

```
queryuser 0x1f4
```

غالبًا:

```
0x1f4 = Administrator
```

---

### استخراج SID

```
lookupnames Administrator
```

أو:

```
lookupsids S-1-5-21-...
```
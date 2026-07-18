**xfreerdp / xfreerdp3** هي أداة في لينكس تستخدم للاتصال عبر بروتوكول:

👉 **RDP (Remote Desktop Protocol)** الخاص بويندوز

يعني: تعطيك **سطح مكتب Windows كامل عن بعد**


# ⚙️ متى تستخدمها في الاختراق؟

تستخدمها عندما:

- تجد منفذ **3389 مفتوح**
- وعندك **Username + Password**
- وتريد دخول الجهاز بواجهة رسومية (GUI)


# 🔥 الاستخدام الأساسي

`xfreerdp /v:<IP> /u:<username> /p:<password>`

## وضع شاشة كاملة:

`xfreerdp /v:192.168.1.10 /u:admin /p:123456 /f`

## مشاركة الحافظة (نسخ/لصق):

`xfreerdp /v:192.168.1.10 /u:admin /p:123456 +clipboard`

## تجاهل شهادات الأمان:

`xfreerdp /v:192.168.1.10 /u:admin /p:123456 /cert:ignore`


- ## تكبر/تصغر نافذة الاتصال
`xfreerdp /v:192.168.1.10 /u:admin /p:pass /dynamic-resolution`

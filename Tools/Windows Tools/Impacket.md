
# ما هي Impacket؟

**Impacket** هي:

> مكتبة + مجموعة أدوات مكتوبة بلغة Python للتعامل مع بروتوكولات الشبكات، خصوصاً بروتوكولات ويندوز

---

# ماذا يعني “التعامل مع بروتوكولات”؟

يعني تقدر:

- تبني اتصال SMB
- تتعامل مع NTLM
- تستخدم RPC
- تحاكي طريقة ويندوز في المصادقة

---

# لماذا Impacket مهمة في الاختراق؟

لأنها تسمح لك:

> تنفيذ هجمات على ويندوز بدون الحاجة للدخول للنظام نفسه

يعني:

- Remote Execution
- Pass-the-Hash
- Dumping credentials
- Enumeration

---

# أهم البروتوكولات التي تدعمها

- SMB (مشاركة الملفات)
- NTLM (المصادقة)
- RPC
- Kerberos
- LDAP

---

# أهم أدوات Impacket (اللي تستخدمها فعلياً)

## 1. psexec.py

يشبه أداة PsExec

psexec.py admin@target

أو باستخدام hash:

psexec.py admin@target -hashes LM:NTLM

👉 يعطيك shell

---

## 2. wmiexec.py

تنفيذ أوامر عبر WMI

wmiexec.py admin@target

✔ أقل ضجيج (stealth أكثر)

---

## 3. smbexec.py

تنفيذ عبر SMB

smbexec.py admin@target

---

## 4. secretsdump.py

🔥 مهم جداً

secretsdump.py admin@target

👉 يسحب:

- NTLM hashes
- SAM
- LSA secrets

---

## 5. GetUserSPNs.py

هجوم Kerberoasting

---

## 6. lookupsid.py

استخراج المستخدمين من SID





مثال

![[Pasted image 20260410082320.png]]


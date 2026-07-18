**NetExec (nxc)** هي أداة حديثة في اختبار الاختراق تُستخدم لـ:

- Enumeration
- Authentication testing
- Remote command execution
- Lateral movement

👉 تعتبر تطوير لـ **CrackMapExec (CME)** لكن أسرع وأقوى وأكثر دعمًا.
 تتحقق فقط ما تسوي اتصال , يعني تتحقق هل نقدر  نتصل او لا 
# ⚙️ الفكرة العامة

NetExec تتعامل مع بروتوكولات ويندوز/لينكس وتعمل:

- تجربة credentials
- فحص الشبكة
- تنفيذ أوامر عن بعد
- استخراج معلومات حساسة


# 🔥 أهم البروتوكولات التي تدعمها NetExec

## 1) SMB (الأهم)

📌 المنافذ: 445

تستخدم لـ:

- مشاركة الملفات
- enumeration
- تنفيذ أوامر (بعض الحالات)

مثال:

`nxc smb <IP> -u user -p pass`


## 2) WinRM

📌 المنافذ: 5985 / 5986

تستخدم لـ:

- Remote shell على Windows

مثال:

`nxc winrm <IP> -u user -p pass`


## 3) SSH

📌 المنفذ: 22

تستخدم لـ:

- Linux remote access
- credential testing

مثال:

`nxc ssh <IP> -u user -p pass`


📌 المنفذ: 3389

تستخدم لـ:

- فحص تسجيل الدخول
- أحياناً الوصول لسطح المكتب

مثال:

`nxc rdp <IP> -u user -p pass`



## 5) LDAP (Active Directory)

📌 المنفذ: 389 / 636

تستخدم لـ:

- Enumeration داخل الدومين
- Users / groups / policies

مثال:

`nxc ldap <IP> -u user -p pass`


## 6) MSSQL

📌 المنفذ: 1433

تستخدم لـ:

- Database access
- sometimes command execution

مثال:

`**nxc mssql <IP> -u user -p pass**`



## 7) FTP

📌 المنفذ: 21

تستخدم لـ:

- login testing
- file access

مثال:

`nxc ftp <IP> -u user -p pass`


# 🧪 أهم أوامر NetExec (مختبر اختراق)

## فحص SMB كامل

`nxc smb 192.168.1.10`

## استخراج معلومات النظام

`nxc smb <IP> -u user -p pass --system`

## تنفيذ أوامر (SMB / WinRM حسب الدعم)

`nxc smb <IP> -u user -p pass -x "whoami"`


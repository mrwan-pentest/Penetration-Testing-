**Evil-WinRM** هي أداة تستخدم في اختبار اختراق أنظمة Windows عبر بروتوكول **WinRM**.

👉 وظيفتها الأساسية:

- تعطيك **Remote Shell (PowerShell)** على جهاز Windows
- بعد تسجيل الدخول باستخدام **Username + Password** أو Hash

# ⚙️ كيف تعمل؟

تعتمد على:

- WinRM Service في ويندوز
- المنافذ:
    - 5985 (HTTP)
    - 5986 (HTTPS)


# 🧪 الاستخدام الأساسي

## تسجيل دخول مباشر:

`evil-winrm -i <IP> -u username -p password`

## باستخدام NTLM hash:

`evil-winrm -i <IP> -u username -H <hash>`

# 📁 أوامر مفيدة داخل Evil-WinRM

- `رفع ملف:`

`upload file.txt`

- `تنزيل ملف:`

`download secret.txt`

- `معرفة المستخدم:`

`whoami`

- `معلومات النظام:`

`systeminfo`


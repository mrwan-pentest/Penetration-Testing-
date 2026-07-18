# CrackMapExec (CME) 

CrackMapExec

أداة مشهورة جدًا في:

- SMB Enumeration
- Active Directory
- Pass-the-Hash
- Lateral Movement


# وظيفتها الأساسية

```
تتعامل مع أجهزة ويندوز داخل الشبكة بسرعة
```


# ماذا تستطيع؟

- فحص SMB
- اختبار Username/Password
- Pass-the-Hash
- تنفيذ أوامر
- Dump SAM
- Enumeration
- Sessions
- Shares
- Users

---

# أشهر استخدام

## فحص SMB

```
crackmapexec smb 192.168.1.10
```


## تجربة باسورد

```
crackmapexec smb IP -u admin -p password
```


## Pass-the-Hash

```
crackmapexec smb IP -u administrator -H HASH
```


## تنفيذ أمر

```
crackmapexec smb IP -u admin -p pass -x whoami
```

## عرض الـ Shares

```
crackmapexec smb IP -u admin -p pass --shares
```

---

# NXC 

NetExec

NXC أو:

```
NetExec
```

هو:

```
النسخة الحديثة من CrackMapExec
```

# لماذا ظهر؟ 

لأن:

```
CrackMapExec توقف تطويره لفترة
```

فتم إنشاء:

```
NetExec (nxc)
```


---



## فحص SMB

```
nxc smb IP
```


## تسجيل دخول

```
nxc smb IP -u admin -p pass
```


## Pass-the-Hash

```
nxc smb IP -u administrator -H HASH
```


## تنفيذ أوامر

```
nxc smb IP -u admin -p pass -x whoami
```


# البروتوكولات التي يدعمها NXC 

- SMB
- WinRM
- SSH
- FTP
- RDP
- MSSQL
- LDAP


# استخداماتهم غالبًا 

- Active Directory Enumeration
- Password Spraying
- Pass-the-Hash
- Lateral Movement
- SMB Enumeration

# عرض المديول 

```
nxc smb IP -u admin -p pass -L
```
# تفعيل RDP

```
nxc smb IP -u admin -p pass -M rdp -o ACTION=enable
```
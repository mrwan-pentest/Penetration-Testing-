هو برنامج في لينكس يسمح لك:

```
تتصل بخدمة RDP الخاصة بويندوز
```

يعني مثل:

```
Remote Desktop Connection في ويندوز
```

لكن على كالي/لينكس.

---
# الاستخدام الأساسي

```
xfreerdp /u:username /p:password /v:ip
```

# Pass-the-Hash عبر xfreerdp 


بدل Password تستخدم:

```
NTLM Hash فقط
```


# مثال 

```
xfreerdp /u:administrator /pth:HASH /v:TARGET
```

# تجاهل شهادة RDP 

أحيانًا يظهر خطأ Certificate.

أضف:

```
/cert:ignore
```

# تفعيل Full Screen 

```
/f
```


# تحديد Resolution 

```
/size:1920x1080
```


# تفعيل خيار تكبير وتصغير النافذة

/`dynamic-resolution`

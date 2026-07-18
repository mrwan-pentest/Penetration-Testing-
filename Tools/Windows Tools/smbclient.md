
**smbclient** هي أداة في لينكس للتعامل مع بروتوكول **SMB (Server Message Block)** الخاص بمشاركة الملفات في ويندوز.

👉 تستخدم لـ:

- الاتصال بـ SMB shares
- استعراض الملفات
- تحميل ورفع ملفات
- اختبار الوصول بدون صلاحيات



# ⚙️ متى تستخدمها في الاختراق؟

تستخدمها عندما:

- تجد المنفذ **445 مفتوح**
- تريد فحص الـ shares
- أو الدخول بدون كلمة مرور (Anonymous / Guest)


# 🔍 أهم الاستخدامات

## 1) عرض الـ shares (المشاركات)

`smbclient -L //<IP> -N`

📌 `-L` = List shares  
📌 `-N` = بدون password (Anonymous login)



## 2) الدخول إلى Share

`smbclient //<IP>/<share> -N`


# 📁 أوامر داخل smbclient (بعد الدخول)

## عرض الملفات:

ls

## تغيير مجلد:

cd folder

## تحميل ملف:

get file.txt

## رفع ملف:

put file.txt


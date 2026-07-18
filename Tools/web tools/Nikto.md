
# ما هي Nikto ؟

هي أداة **فحص سيرفرات الويب** تبحث عن:

✅ ملفات حساسة  
✅ مجلدات شائعة  
✅ نسخ قديمة  
✅ إعدادات خاطئة  
✅ صفحات Admin  
✅ Vulnerabilities معروفة  
✅ Default files

هي ليست brute force، بل **Enumeration Scanner**.

---

# لماذا مهمة؟

لأنها توفر وقتك بدل ما تبحث يدويًا.

مثال:

بدل أن تجرب:

/admin  
/login  
/backup  
/phpinfo.php  
/robots.txt

هي تفعل ذلك تلقائيًا.

---

# طريقة الاستخدام الأساسية

nikto -h http://target

مثال:

nikto -h http://10.130.150.94:8080

---

# أهم الخيارات 

## تحديد الهدف

-h

مثال:

nikto -h http://10.10.10.10

---

## تحديد بورت

-p

مثال:

nikto -h 10.10.10.10 -p 8080

---

## استخدام SSL

-ssl

---

## Basic Auth 

-id username:password

مثال:

nikto -h http://10.130.150.94:8080 -id joker:password123

---

## حفظ النتائج

-o result.txt

---

## نوع الإخراج

-Format txt  
-Format html

---

# مثال كامل

nikto -h http://10.130.150.94:8080 -id joker:batman -o scan.txt
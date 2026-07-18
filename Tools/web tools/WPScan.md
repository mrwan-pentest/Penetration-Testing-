
أداة متخصصة في **فحص مواقع WordPress** لاكتشاف:

✅ نسخة WordPress  
✅ المستخدمين (Users)  
✅ القوالب (Themes)  
✅ الإضافات (Plugins)  
✅ ثغرات معروفة  
✅ إعدادات ضعيفة




## فحص سريع للموقع

wpscan --url http://target


هذا يعطيك:

- هل الموقع WordPress؟
- الإصدار
- ملفات مهمة
- ملاحظات عامة


# أهم أوامر تحتاجها

---

## 1. معرفة نسخة WordPress

wpscan --url http://target --enumerate vp



---

## 2. اكتشاف المستخدمين

مهم جدًا.

wpscan --url http://target --enumerate u


## 3. اكتشاف Plugins

أهم شيء غالبًا.

wpscan --url http://target --enumerate p

قد يظهر:

contact-form-7  
revslider  
woocommerce

ثم تبحث عن ثغرات.




## 4. اكتشاف Themes

wpscan --url http://target --enumerate t

# Brute Force 

إذا عندك اسم مستخدم:

wpscan --url http://target -U admin -P rockyou.txt

أو قائمة مستخدمين:

wpscan --url http://target -U users.txt -P passwords.txt
أداة تابعة ل john  
وظيفتها تحول ملفات GPG و PGPالى هاش
عشان نقدر نكسره بي john

 بعد ما نحصل على الباسوورد نفعل import بي الملف الذي فكينا حقه الهاش  
 gpg --import filename
 نتأكد عن طريق
 gpg --list-secret-keys 
بعدين نفك الملف الذي نريده 
gpg --decrypt backup.pgp

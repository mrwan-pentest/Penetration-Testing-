
اذا الموقع يستخدم HTTP Basic Auth

	gobuster dir -u http://TARGET -U username -P password -w /usr/share/wordlists/dirb/common.txt

Ex:
	`gobuster dir -u http://10.128.163.215:8080 -U admin -P secret123 -w /usr/share/wordlists/dirb/common.txt`
	
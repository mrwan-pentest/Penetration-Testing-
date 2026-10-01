## Overview

**Credentials Harvesting** is the process of collecting authentication material such as **passwords, password hashes, and other credentials** from a compromised system.

It is commonly performed during the **Post-Exploitation** phase after gaining access to a target.

To dump protected credential material such as password hashes, we generally need **elevated privileges** on the target system.

---

# Lab

## Step 1: Dump Password Hashes

After obtaining elevated privileges, we can use **Impacket's `secretsdump`** to extract credential information from the target.

The following command authenticates to the target using valid credentials and attempts to dump available credential material:

```
impacket-secretsdump user1:'12345l**'@192.168.227.139
```

![](../../../../Images/Pasted%20image%2020260928210324.png)

The output can contain password hashes, including **NTLM hashes**, depending on the privileges and credential sources available on the target.

---

## Step 2: Authenticate Using the NTLM Hash

Once an NTLM hash has been obtained, we can use **Impacket's `wmiexec`** to authenticate to the target using the hash instead of the plaintext password.

```
impacket-wmiexec administrator@192.168.227.139 -hashes :8b27c4f513c9fa58257bcf7736236705
```

![](../../../../Images/Pasted%20image%2020260928210430.png)

If the supplied hash is valid and the account has the required permissions, `wmiexec` can provide a command shell on the target.

This technique is an example of **Pass-the-Hash**, where an NTLM hash is used for authentication without knowing the account's plaintext password.
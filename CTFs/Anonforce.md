# FTP Enumeration and Root Credential Recovery

## The objective is to enumerate the FTP service, recover sensitive files, crack encrypted credentials, and ultimately obtain the root password to gain full access to the target system.

---

# Nmap Enumeration

## Performed an Nmap scan to identify the open ports and running services on the target.

!![](../Images/Pasted%20image%2020260627234319.png)

![](../../Images/Pasted%20image%2020260721202303.png)



# Service Enumeration

## Used Nmap NSE scripts to gather additional information about the discovered services.

!![](../Images/Pasted%20image%2020260627234403.png)

# Anonymous FTP Access

## Discovered that the FTP service allowed anonymous authentication and identified a writable directory.

!![](../Images/Pasted%20image%2020260627234505.png)

# FTP Login

## Logged into the FTP server using anonymous authentication.


!![](../Images/Pasted%20image%2020260627234741.png)


# User Flag

## Retrieved the first flag from the FTP server.

!![](../Images/Pasted%20image%2020260627234719.png)


# Writable Directory Enumeration

## Navigated to the writable directory identified during enumeration.

!![](../Images/Pasted%20image%2020260406173247.png)

# File Retrieval

## Downloaded the available files from the writable directory for further analysis.

!![](../Images/Pasted%20image%2020260406173643.png)

# Private Key Discovery

## Discovered a PGP private key within the downloaded files.

!![](../Images/Pasted%20image%2020260406173838.png)


# Private Key Hash Extraction

## Converted the encrypted private key into a crackable hash using **pgp2john**.

!![](../Images/Pasted%20image%2020260406173944.png)

# Password Cracking

## Cracked the extracted hash to recover the passphrase protecting the private key.

!![](../Images/Pasted%20image%2020260406174038.png)


# Importing the Private Key

## Imported the recovered private key before attempting to decrypt the encrypted backup.

```bash
gpg --import private.asc
```

!![](../Images/Pasted%20image%2020260406174530.png)

# Key Verification

## Verified that the private key was successfully imported into the local GPG keyring.

!![](../Images/Pasted%20image%2020260406174606.png)

# Backup Decryption

## Decrypted the backup file using the recovered passphrase.

```bash
gpg --decrypt
```

!![](../Images/Pasted%20image%2020260627235238.png)

# Root Hash Extraction

## Extracted the root password hash from the decrypted backup.

!![](../Images/Pasted%20image%2020260627235306.png)


# Root Password Recovery

## Cracked the root password hash and successfully recovered the root password.

!![](../Images/Pasted%20image%2020260627235437.png)

# SSH Authentication

## Authenticated to the target over SSH as the **root** user using the recovered credentials.

!![](../Images/Pasted%20image%2020260627235601.png)

# Root Flag

## Obtained the root flag after successfully gaining full administrative access.

!![](../Images/Pasted%20image%2020260627235637.png)
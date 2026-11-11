# SNMP Enumeration

## 1. Preparing the Target IP List

First, we prepare a list of IP addresses so we can use it during the SNMP community string brute-force process.

We can generate the IP list using the following script:

```
for ip in $(seq 1 254); do echo 10.129.42.$ip; done > ip.txt
```

This command generates IP addresses from `10.129.42.1` to `10.129.42.254` and saves them in `ip.txt`.

## 2. Discovering SNMP Community Strings

Next, we use onesixtyone to scan the target IP addresses and identify valid SNMP community strings.

![](../../../Images/Pasted%20image%2020261106210813.png)

The scan identifies an IP address associated with a specific community string.

## 3. Enumerating SNMP Information with snmpwalk

After discovering a valid community string, we can use snmpwalk to retrieve information from the target device.

For example:

```
snmpwalk -c public -v1 -t 10 10.129.42.195
```

Command breakdown:

- `-c public`: Specifies the SNMP community string.
    
- `-v1`: Uses SNMP version 1.
    
- `-t 10`: Sets the timeout to 10 seconds.
    
- `10.129.42.195`: Specifies the target IP address.
    

![](../../../Images/Pasted%20image%2020261106211315.png)

## 4. Enumerating Specific Information Using OIDs

We can also use OIDs (Object Identifiers) to retrieve specific information instead of dumping the entire SNMP tree.

For example, to enumerate installed software on the target system, we can use:

```
snmpwalk -c public -v1 -t 10 10.129.42.195 1.3.6.1.2.1.25.6.3.1.2
```

This OID belongs to the `HOST-RESOURCES-MIB` and is used to retrieve the names of installed software entries.

![](../../../Images/Pasted%20image%2020261106212049.png)

Other useful enumeration targets include:

- System information.
    
- Running processes.
    
- Network interfaces.
    
- Installed software.
    
- System users, where exposed through the relevant MIBs.
    

Key takeaway: SNMP enumeration can reveal valuable information about a target system, especially when its community strings are weak or improperly configured.
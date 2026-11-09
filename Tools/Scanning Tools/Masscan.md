# Masscan

## Overview

**Masscan** is a high-speed TCP port scanner used to discover open ports on individual hosts or authorized network ranges.

It is commonly used for:

- Quickly identifying open ports across a network.
- Checking whether specific services are exposed.
- Performing initial port discovery before detailed enumeration with Nmap.

Masscan focuses on port discovery; it does not replace detailed service and version enumeration. On Linux, it generally requires elevated privileges, so run it with `sudo`.

## Basic Usage

### 1. Scan Selected Ports on a Host

This command checks whether SSH, HTTP, or HTTPS ports are open on the target:

Bash

```
sudo masscan TARGET -p22,80,443 --rate 1000
```

### 2. Scan a Port Range

This command scans ports 1–1000 across an authorized network range:

Bash

```
sudo masscan TARGET_RANGE -p1-1000 --rate 1000
```

### 3. Scan the Full TCP Port Range

This command scans ports 1–65535 on a single target:

Bash

```
sudo masscan TARGET -p1-65535 --rate 1000
```

### 4. Save Results to a File

This command saves the scan results in a readable list format:

Bash

```
sudo masscan TARGET -p1-1000 --rate 1000 -oL results.txt
```

## Important Options

|Option|Description|
|---|---|
|`-p <ports>`|Ports to scan, such as `-p22,80,443` or `-p1-1000`|
|`--rate <packets-per-second>`|Sets the packet transmission rate|
|`--exclude <IP/range>`|Excludes a host or network range from the scan|
|`--excludefile <file>`|Excludes targets listed in a file|
|`--banners`|Attempts to retrieve banners from supported services|
|`--wait <seconds>`|Waits for responses before the scan exits|
|`--retries <count>`|Sets the number of probe retries|
|`--adapter-ip <IP>`|Specifies the source IP address used for scanning|
|`-oL <file>`|Saves results in list format|
|`-oJ <file>`|Saves results in JSON format|
|`-oX <file>`|Saves results in XML format|

## Useful Examples

### Exclude a Host

This command scans the range while excluding a specific host:

Bash

```
sudo masscan TARGET_RANGE -p80,443 --exclude 192.0.2.10 --rate 500
```

### Exclude Targets Listed in a File

This command skips the IP addresses or ranges listed in `exclude.txt`:

Bash

```
sudo masscan TARGET_RANGE -p80,443 --excludefile exclude.txt --rate 500
```

### Attempt to Retrieve Service Banners

This command scans common service ports and attempts to retrieve banners where supported:

Bash

```
sudo masscan TARGET -p22,80,443 --banners --rate 500
```

### Save Results as JSON

This command writes the results to a JSON file for later review or processing:

Bash

```
sudo masscan TARGET -p1-1000 --rate 1000 -oJ results.json
```
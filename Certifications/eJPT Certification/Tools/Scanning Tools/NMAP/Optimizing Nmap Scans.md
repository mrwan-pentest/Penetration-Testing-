# `--host-timeout`

Used for:

```
Setting the maximum amount of time allowed to scan a single host
```

Meaning:

If a device is:

- Very slow
- Not responding
- Causing the entire scan to take longer

This option tells Nmap:

```
"If this time is exceeded, skip this host and move to the next one"
```

---

## Example

```
nmap --host-timeout 30s 192.168.1.10
```

Meaning:

```
Scan 192.168.1.10 for a maximum of 30 seconds
```

If the scan does not finish within this time:

```
Nmap stops scanning this host and moves on
```

---

## Supported time units

|Value|Meaning|
|---|---|
|`s`|Seconds|
|`m`|Minutes|
|`h`|Hours|

Examples:

```
--host-timeout 2m
```

Means:

```
Allow a maximum of 2 minutes for each host
```

---

# When do we use it?

Useful when scanning:

- Large networks
- Many hosts
- Unstable or slow targets

Example:

You are scanning:

```
10.10.10.0/24
```

and one host does not respond.

Without:

```
--host-timeout
```

Nmap may wait a long time for that host.

---

# `--scan-delay`

Used for:

```
Adding a delay between packets
```

Instead of sending packets quickly, Nmap waits for a specific amount of time between each packet.

---

## Example

```
nmap --scan-delay 1s 192.168.1.10
```

Meaning:

```
Wait 1 second between each packet sent
```

---

# Why use it?

## 1) Reduce Network Noise

A fast scan generates:

```
A lot of traffic
```

With a delay:

```
Less traffic is generated
```

---

## 2) Avoid Rate Limiting

Some systems detect a large number of requests in a short time and block the scanner.

Adding a delay makes the scan slower but quieter.

---

## 3) Reduce Detection Possibility

Systems like:

- IDS
- IPS
- Firewalls

may detect:

```
A large number of requests in a short period
```

Adding delay makes the scan pattern less obvious.

---

# Time Units

|Value|Meaning|
|---|---|
|`ms`|Milliseconds|
|`s`|Seconds|

Examples:

```
--scan-delay 500ms
```

Means:

```
Wait half a second between each packet
```

---

```
--scan-delay 2s
```

Means:

```
Wait two seconds between each packet
```

---

# Difference Between Them

|Option|Function|
|---|---|
|`--host-timeout`|Sets the maximum total time allowed for scanning one host|
|`--scan-delay`|Adds a delay between packets during the scan|

Simple example:

`--host-timeout`

Means:

> Do not spend more than 5 minutes on this host.

`--scan-delay`

Means:

> Wait 1 second between every request sent to this host.
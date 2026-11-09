# Service Version & OS Detection

## `-sV` — Service Version Detection

Detects:

- Service name
- Service version

Example output:

```
Apache 2.4.41
OpenSSH 8.2
```

Usage:

```
nmap -sV target
```

## `--version-intensity`

Controls the intensity of Service Version Detection (`-sV`).

It determines how many Probes Nmap uses to identify services and their versions.

### Values

Range: `0–9`

|Value|Meaning|
|---|---|
|`0`|Light detection|
|`9`|Most intensive detection|

Higher intensity means:

- More Probes.
- More Requests.
- Potentially more accurate identification.
- Longer scan time.

Example:

```
nmap -sV --version-intensity 9 192.168.1.10
```

Nmap performs its most intensive version detection.

---

## `-O` — OS Detection

Attempts to identify the target's Operating System.

Examples:

- Linux
- Windows

Usage:

```
nmap -O target
```

## `--osscan-guess`

An additional option for OS Detection (`-O`).

Makes Nmap provide its best guess about the target's OS when identification is uncertain.

Example:

```
nmap -O --osscan-guess 192.168.1.10
```

---

## `-A` — Aggressive Scan

Enables multiple detection features together:

- OS Detection
- Service Version Detection
- NSE Default Scripts
- Traceroute

Usage:

```
nmap -A target
```

**Note:** `-A` enables several enumeration features in one scan. It does not mean every possible Nmap scan is enabled.
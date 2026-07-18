### Devices that communicate with each other to exchange data.

Examples:

- Computer
- Router
- Server
- Phone

---

In networking there are:

Layers

Each layer has a specific function.

---

OSI Model

It consists of 7 layers.

---

Layer Order

|Number|Layer|Function|
|---|---|---|
|7|Application|Applications and services|
|6|Presentation|Encryption and encoding|
|5|Session|Session management|
|4|Transport|TCP / UDP|
|3|Network|IP routing|
|2|Data Link|MAC address|
|1|Physical|Cables and signals|

---

1. Physical Layer

Handles the physical transmission of data.

Includes:

- Cables
- Signals
- Wireless communication

It defines how data is physically transmitted.

---

2. Data Link Layer

Works with MAC addresses.

Example:  
AA:BB:CC:DD:EE:FF

Devices in the same network communicate using MAC addresses.

---

3. Network Layer

One of the most important layers.

Works with IP addresses.

Example:  
192.168.1.10

Its function is to route data between networks.

Main protocol:  
IP

---

Important Concepts

Router

Connects different networks together.

---

Subnet

Network segmentation.

Example:  
192.168.1.0/24

Meaning:

- Full network
- Around 254 usable hosts

---

4. Transport Layer

Very important for penetration testing.

Handles:

- Ports
- TCP
- UDP

---

What is a Port?

A service endpoint.

Examples:

|Service|Port|
|---|---|
|HTTP|80|
|HTTPS|443|
|SSH|22|
|FTP|21|

---

TCP

Reliable connection.

Features:

- Ensures data delivery
- Uses handshake process

Used in:

- HTTP
- SSH
- FTP

---

UDP

Fast but unreliable connection.

Features:

- No delivery confirmation

Used in:

- DNS
- Streaming
- VoIP

---

TCP vs UDP

|TCP|UDP|
|---|---|
|Reliable|Fast|
|Slower|Faster|
|Connection-oriented|Connectionless|

---

Connection-Oriented

Requires establishing a connection before sending data.

---

Connectionless

Sends data without establishing a connection.

---

5. Session Layer

Session management layer.

---

What is a Session?

A connection session between two devices.

Examples:

- Login sessions
- Maintaining connections
- Opening and closing sessions

---

Example

When logging into a website:

- Session is created
- Maintained
- Then closed

---

6. Presentation Layer

Responsible for formatting, translation, and encryption.

Functions:

- Data formatting
- Encryption / Decryption
- Compression

---

Example

HTTPS uses:

SSL/TLS encryption

---

Meaning of Presentation

How data is represented.

Examples:

- JPEG
- PNG
- MP4
- UTF-8

---

7. Application Layer

The layer users interact with most.

Includes:

- HTTP
- HTTPS
- DNS
- FTP
- SMTP

---

Important Protocols (eJPT)

|Protocol|Function|Port|
|---|---|---|
|HTTP|Websites|80|
|HTTPS|Secure websites|443|
|FTP|File transfer|21|
|SSH|Remote access|22|
|DNS|Domain resolution|53|
|SMTP|Email sending|25|

---

DNS (Short Explanation)

Converts domain names like:

google.com

Into IP addresses.

---

Useful Tools

|Tool|Function|
|---|---|
|ping|Connectivity test|
|traceroute|Route tracking|
|netdiscover|Network discovery|
|nmap|Port and service scanning|
|dig|DNS enumeration|

---

What is a Packet?

A packet is a data unit.

All network data is split into small packets before transmission.

---

Simple Example

When you:

- Send a message
- Open a website
- Download a file

Data is not sent all at once.

It is split into packets.

---

Why packets are used

- Easier handling
- Faster transmission
- Better routing
- Easier retransmission on errors

---

Packet Structure

Packets usually contain:

|Part|Function|
|---|---|
|Header|Control information|
|Payload|Actual data|

---

Think of it like a package

|Real World|Network|
|---|---|
|Shipping label|Header|
|Content inside box|Payload|

---

Header contains

|Field|Meaning|
|---|---|
|Source IP|Sender address|
|Destination IP|Receiver address|
|Protocol|Protocol type|
|Port|Service port|
|TTL|Time to live|
|Flags|Control info|

---

Example Packet

Source IP: 192.168.1.5  
Destination IP: 8.8.8.8  
Protocol: TCP  
Port: 80  
Data: GET / HTTP/1.1

---

Encapsulation

Each layer adds its own header.

---

How encapsulation works

Application Layer:

- Generates data (HTTP request)

Transport Layer:

- Adds TCP header and ports

Network Layer:

- Adds IP header

Data Link Layer:

- Adds MAC address

Physical Layer:

- Converts data into bits

---

Data names per layer

|Layer|Name|
|---|---|
|Application|Data|
|Transport|Segment|
|Network|Packet|
|Data Link|Frame|
|Physical|Bits|

---

Example

ping 8.8.8.8 sends ICMP packets.

---

Nmap

Sends:

- TCP packets
- UDP packets
- SYN packets
- ICMP packets

and analyzes responses.

---

Common Protocols

|Protocol|Function|
|---|---|
|TCP|Reliable communication|
|UDP|Fast communication|
|ICMP|Ping|
|HTTP|Web|
|DNS|Domain resolution|

---

TCP Packet Flags

|Flag|Function|
|---|---|
|SYN|Start connection|
|ACK|Acknowledge|
|FIN|End connection|
|RST|Reset connection|
|PSH|Push data immediately|
|URG|Urgent data|

---

SYN

Start connection request.

---

ACK

Acknowledgement of received data.

---

FIN

Terminate connection request.

---

RST

Connection rejected or reset.

---

3-Way Handshake

TCP connection establishment process.

---

Why it is needed

TCP is reliable, so both sides must confirm readiness.

---

Steps

1. SYN  
    Client requests connection.
2. SYN-ACK  
    Server agrees and responds.
3. ACK  
    Client confirms connection.

---

Connection becomes Established.

---

Real Example

When opening:

[https://google.com](https://google.com)

A TCP handshake happens before loading the page.
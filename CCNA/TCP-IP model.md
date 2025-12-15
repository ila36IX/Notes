

![](https://i.imgur.com/rJ1Z7wS.png)

##  The Physical Layer (Layer 1)

Sends and receives bits as electrical, optical, or radio signals over the medium. Defines things like cables, connectors, signal levels, and link speeds. 

**Examples**: copper UTP cables, fiber-optic cables, Wi-Fi radios and antennas, network interface cards (NICs). 

![](https://i.imgur.com/WBdHQxy.png)

The physical aspects of transmitting data are very complex. Network engineers typically don't have to know the low-level details.

## The Local Network layer or Access Layer or Data Link layer (Layer 2)

[[The access layer]]

![](https://i.imgur.com/HNJPPcv.png)

Provides hop-to-hop delivery of messages on a local network. 
A hop is one step along the path between two devices: from one router or host, to the next router or host in the path. 
Switches don't count: a switch just extends the local network, allowing multiple devices to connect. 
Uses MAC (Media Access Control) addresses to identify interfaces.

**Protocols at this layer include**: 
- Ethernet (IEEE 802.3) 
- Wi-Fi (IEEE 802.11)

## The Internet layer (Layer 3)

Provides end-to-end delivery between hosts across multiple networks.

- Internet = internetwork (between networks) 

Uses IP addresses to identify hosts in the network. 
Routers operate mainly at this layer, using the message's destination IP address to forward the message toward its final destination host.

**Protocols at this layer include**: 
- IP (IPv4, IPv6)
## The Transport layer (Layer 4)

Provides end-to-end communication between application **processes**. Also called "process-to-process" or "service-to-service".

Uses **port numbers** to identify the processes on each host. 

**Protocols at this layer include:** 
- UDP (User Datagram Protocol)
- TCP (Transmission Control Protocol)

## The Application layer (Layer 5)
Is where network communications meet applications. 
Defines how application processes format, send, and interpret data.

**Protocols at this layer include:** 
- Browsing web pages (HTTP/HTTPS) 
- Transferring files (FTP, TFTP) 
- Sending/receiving email (SMTP, POP3, IMAP) 
### Encapsulation

The message moves down the stack, each layer encapsulate the data with a header including the information needed for the layer. 

![](https://i.imgur.com/r4uxSY8.png)

The decapsulation happens in the reverse order.

## PDU

Protocol Data Unit (PDU) is standardized block of information, or a "container," carrying user data and protocol-specific control information (like headers/trailers) for communication between peer layers in a computer network

![](https://i.imgur.com/vEfgnlB.png)

### TCP/IP VS. OSI model

![](https://i.imgur.com/ckCYOQD.png)

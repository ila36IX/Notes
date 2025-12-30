#Networking
# The access layer

![](https://i.imgur.com/ybKCyRG.png)

Ethernet is technology commonly used in local area networks. Devices access the Ethernet LAN using an Ethernet Network Interface Card (NIC). Each Ethernet NIC has a unique address permanently embedded on the card known as a Media Access Control (MAC) address. The MAC address for both the source and destination are fields in an Ethernet frame.

Ethernet operates at layer 2, the data link layer, of the OSI model.
## Ethernet Frame

![](https://i.imgur.com/EMG0Ya2.png)

Each computer message is encapsulated in a specific format, called a **frame**, before it is sent over the network. A frame acts like an envelope; it provides the address of the intended destination and the address of the source host.

- **Preamble**: allows receivers to synchronize their clock at the bit-level with the transmitter.
- **SFD**:  start frame delimiter, marks the end of preamble, and beginning of the rest of the frame.
- **Length or Type**: indicates the size of the payload in bytes, it also can contain the type of the IP protocol used

| EtherType value | Protocol |
| :-------------: | :------: |
|     0x0800      |   IPv4   |
|     0x0806      |   ARP    |
|     0x86DD      |   IPv6   |

- **Data**: is the actual payload
- **FCS**: Frame check sequence detects corrupted data by running the **CRC** algorithm over the received data
### Ethernet switches vs Ethernet Hub

[Great demonstration](https://www.instagram.com/reel/DMsmIogRRcP)

In Ethernet hubs only one message can be sent through an Ethernet hub at a time. Two or more messages sent at the same time will cause a collision.  they operates by forwarding the frame to all the hosts in the network.
Switches uses the MAC address table to determine which host to forward the frame to rather than broadcasting it.
#### Ethernet Switches and the table of MAC addresses

Ethernet switches make their forwarding decision based on destination MAC address.
Ethernet switches add entries to their *MAC address table* based on the source MAC address.
When a switch receives an Ethernet frame and the destination MAC address of that frame is not in its *MAC address table*, the switch will _flood_ the frame out all ports except in the incoming port.

##  How does hosts know the MAC address of the destination

#### ARP

The Address Resolution Protocol (ARP) is a communication protocol for discovering the link layer address, such as a MAC address, associated with an internet layer address, typically an IPv4 address.

The host broadcasts a request containing the target node's IP address, and the node with that IP address replies with its MAC address.

![](https://i.imgur.com/T2ucoeC.png)

This is the way it works:

The ARP request has distention MAC address of `FF.FF.FF.FF.FF.FF` which means broadcasting the frame to all the hosts in the network, only the one with the destination IP address will send a Unicast ARP replay back.

![](https://i.imgur.com/5W1Yrzx.png)

Every host has an ARP table you can use `arp` command to show the ARP table of your device:

![](https://i.imgur.com/MjttEHM.png)
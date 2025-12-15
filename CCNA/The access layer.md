# The access layer

![](https://i.imgur.com/ybKCyRG.png)

Ethernet is technology commonly used in local area networks. Devices access the Ethernet LAN using an Ethernet Network Interface Card (NIC). Each Ethernet NIC has a unique address permanently embedded on the card known as a Media Access Control (MAC) address. The MAC address for both the source and destination are fields in an Ethernet frame.

Ethernet operates at layer 2, the data link layer, of the OSI model.
## Ethernet Frame

![](https://i.imgur.com/EMG0Ya2.png)

Each computer message is encapsulated in a specific format, called a **frame**, before it is sent over the network. A frame acts like an envelope; it provides the address of the intended destination and the address of the source host.

### Ethernet Switches and the table of MAC addresses

Ethernet switches make their forwarding decision based on destination MAC address.
Ethernet switches add entries to their *MAC address table* based on the source MAC address.
When a switch receives an Ethernet frame and the destination MAC address of that frame is not in its *MAC address table*, the switch will forward the frame out all ports except in the incoming port.


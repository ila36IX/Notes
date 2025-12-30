#Networking
# The Network layer

![](https://i.imgur.com/zBwOMQU.png)

## IP address format

![](https://i.imgur.com/AwYsWzA.png)
## IPv4 address classes

![](https://i.imgur.com/aFwNnFZ.png)

**Host portion** of the address is all 0's is the **Network Address** or the identifier of the network.
**Host portion** of the address is all 1's is the **Broadcast Address**.

## IP class by the first octet

![](https://i.imgur.com/sZ3j3gJ.png)

You can know the IP class by the first octet range.

## IPv4 header

![](https://i.imgur.com/xfLIMV7.png)

- **Version**: Which IP version we are using, for IPv4, this is always equal to 4.
- **Internet Header Length (IHL)**: Indicates size of the header due to the optional 14th field. Its minimum value is 5 (x4 = 20 bytes) and maximum is 15 (x4 =  60 bytes).
- **Differentiated Services Code Point (DSCP)**: (*6 bits*) Originally defined as the type of service (ToS). Real-time data streaming makes use of the DSCP field. An example is Voice over IP (VoIP).
- **Explicit Congestion Notification (ECN)**: (*2 bits*) This field allows end-to-end notification of network congestion without dropping packets.
- **Total Length**: (*2 bytes*) Indicates the entire size of the IP packet (header and data) in bytes. The minimum size is 20 bytes (if you have no data) and the maximum size is 65.535 bytes, that’s the highest value you can create with 16 bits.
- **Identification**: (*2 bytes*) If the IP packet is fragmented then each fragmented packet will use the same identification number to identify to which IP packet they belong to.
- **IP Flags**: These (*3 bits*) are used for fragmentation:
    - The first bit is always set to 0.
    - The second bit is called the **DF (Don’t Fragment) bit** and indicates that this packet should not be fragmented.
    - The third bit is called the **MF (More Fragments)** bit and is set on all fragmented packets except the last one. The last fragment has a non-zero _Fragment Offset_ field, so it can still be differentiated from an unfragmented packet.
- **Fragment Offset**: (_13 bit_) field specifies the position of the fragment in the original fragmented IP packet.
- **Time to Live**: (_1 bytes_) Every time an IP packet passes through a router, the time to live field is decremented by 1. Once it hits 0 the router will drop the packet and sends an ICMP time exceeded message to the sender. Used to prevent packets from looping around forever (if you have a routing loop).
- **Protocol**: (_1 byte_) field tells us which protocol is enapsulated in the IP packet, for example TCP has value 6 and UDP has value 17.
- **Header Checksum**: (_2 bytes_) used to store a checksum of the header. The receiver can use the checksum to check if there are any errors in the header. When a packet arrives at a router, the router decreases the _TTL_ field in the header. Consequently, the router must calculate a new header checksum before sending it out again.
- **Source Address**: (_4 bytes_) Source IP address.
- **Destination Address**: (_4 bytes_) Destination IP address.
- **IP Option**: this field is not used often, is optional and has a variable length based on the options that were used. When you use this field, the value in the header length field will increase. An example of a possible option is “source route” where the sender requests for a certain routing path.

IPv4 packets are fragmented if they are larger than the *MTU (Maximum Transmission Unit)*.
### Packet tracer output

![](https://i.imgur.com/V3aFixj.png)

## Routing

Routing is the process of selecting a path for traffic in a network or between or across multiple networks.
### Connected/Local Route

When enabling a router interface and configured with an IP address two routes are automatically added to the routing table:

![](https://i.imgur.com/S3lAZxS.png)

**Connected Route:** A route to the network connected to the interface. If the IP is `192.168.1.1` the _connected route_ will be `192.168.1.0`.

**Local Route:** A route to the exact IP address configured on the interface. If the IP is `192.168.1.1` the _local route_ will be `192.168.1.1`.

> The router will look for the **most specific match** to forward the packet.
This is different then the switches, which look for the **exact match** in the MAC address table to forward frames.

**Static routing**: Manually configure the router to *next hop* route in the path to the destination.
**Dynamic route**: 

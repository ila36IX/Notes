# Networks and Hosts


IPv4 addresses are 32-bit and consist of two parts: network and host. 
**The network portion**, shown in blue, is identified by a subnet mask, such as 255.255.255.0. The example 192.168.5.11 with a subnet mask of 255.255.255.0 has the first three octets (192.168.5) as the network and the last octet (11) as **the host**. 

This hierarchical addressing simplifies routing as routers only need to know how to reach each network. Multiple logical networks can exist on one physical network if their network portions differ, allowing communication within the same network but requiring routing for communication across different networks.

![](https://i.imgur.com/duckvGK.png)

## Unicast transmission

Unicast transmission refers to one device sending a message to one other device in one-to-one communications.
A unicast packet has a destination IP address that is a unicast address which goes to a single recipient. A source IP address can only be a unicast address, because the packet can only originate from a single source. This is regardless of whether the destination IP address is a unicast, broadcast, or multicast.

## Broadcast

Broadcast transmission refers to a device sending a message to all the devices on a network in one-to-all communications.

A broadcast packet has a destination IP address with all ones (1s) in the host portion, or 32 one (1) bits (255.255.255.255).

## Routing to the Internet

> **Private addresses are not globally routable**

Most internal networks, from large enterprises to home networks, use private IPv4 addresses for addressing all internal devices (intranet) including hosts and routers. However, private addresses are not globally routable.

![](https://static.packt-cdn.com/products/9781789340501/graphics/assets/e3bf647a-f2b1-4d81-ae69-512dbaa160c9.png)

Every packet have a source IPv4 address that is a private address and a destination such as IPv4 address that is public (globally routable). Packets with a private address must be filtered (discarded) or translated to a public address before forwarding the packet to an ISP.

### NAT

Before the *ISP* can forward this packet, it must translate the source IPv4 address, which is a private address, to a public IPv4 address using Network Address Translation (NAT). NAT is used to translate between private IPv4 and public IPv4 addresses. This is usually done on the router that connects the internal network to the ISP network. Private IPv4 addresses in the organization’s intranet will be translated to public IPv4 addresses before routing to the internet.

## Loopback addresses
### Special IP: localhost

![](https://fossbytes.com/wp-content/uploads/2016/10/localhost-127.0.0.1.jpg)

**localhost** is a *hostname* that refers to the current computer used to access it. The name localhost is reserved for *loopback* purposes. It is used to access the network services that are running on the host via the *loopback* network interface. Using the *loopback* interface bypasses any local network interface hardware.

### 255.255.255.255

User to broadcast a packet to every host in the network except the source host.

## Assignment of IP Addresses
![](https://upload.wikimedia.org/wikipedia/en/e/ed/Internet_Assigned_Numbers_Authority_logo.svg)**Internet Assigned Numbers Authority**: is a standards organization that oversees global IP address allocation, autonomous system number allocation, root zone management in the Domain Name System (DNS), media types, and other Internet Protocol–related symbols and Internet numbers.

**Regional Internet registry :** (RIR) is an organization that manages the allocation and registration of Internet number resources within a region of the world.

![assignment of ip addresses](https://i.imgur.com/chwtz5F.png)

1. **Public IPv4 Addresses:** Globally routed over the internet, public IPv4 addresses must be unique.
2. **IANA Management:** The Internet Assigned Numbers Authority (IANA) manages and allocates IP address blocks.
3. **Regional Internet Registries (RIRs):** There are five RIRs responsible for IP address allocation. 
4. **RIR Allocation to ISPs:** RIRs allocate IP addresses to Internet Service Providers (ISPs).
5. **ISP Distribution:** ISPs distribute IPv4 address blocks to organizations and smaller ISPs.

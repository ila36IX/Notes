# Dynamic Host Configuration Protocol

DHCP is a protocol that assigning every host in the network to dynamic IP address, that address is not permanently assigned to a host but is only leased for a period of time. If the host is powered down or taken off the network, the address is returned to the pool for reuse.

Many home networks and small businesses use a wireless router and modem. the wireless router is both a DHCP client and a server.

The DHCP server is configured with a range, or pool, of IPv4 addresses that can be assigned to DHCP clients. 

## DHCP protocol

![](https://i.imgur.com/krXY4BZ.png)

1. A client that needs an IPv4 address will send a **DHCP Discover message** which is a broadcast with a destination IPv4 address of 255.255.255.255 (32 ones) and a destination MAC address of FF-FF-FF-FF-FF-FF (48 ones). 
2. All hosts on the network will receive this broadcast **DHCP frame**. 
3. The server will respond with a **DHCP Offer**, suggesting an IPv4 address for the client. 
4. The host then sends a **DHCP Request** asking to use the suggested IPv4 address. 
5. The server responds with a **DHCP Acknowledgment**.
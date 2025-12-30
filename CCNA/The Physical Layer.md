#Networking
# The physical layer

![](https://i.imgur.com/t2pyoZZ.png)

The physical layer defines the means of transmitting a stream of raw bits over a physical data link connecting network nodes.

The physical layer consists of the electronic circuit transmission technologies of a network. It is a fundamental layer underlying the higher level functions in a network, and can be implemented through a great number of different hardware technologies with widely varying characteristics.
## Ethernet

Ethernet is a family of wired computer networking technologies commonly used in local area networks (LAN),

RJ45 cable is a utp type cable

![img](https://i.imgur.com/Rj0O62B.png)


![](https://i.imgur.com/3Q23y3M.jpeg)

**UTP Straight-through** cable are the cables that uses the same pins to receive and transmit data.
**UTP Crossover** cable reverse the pins to connect the some type of device e.g. router, switch...
**MDI-X** is the technology that modern network interfaces used to automatically adjust which pin to use to receive and to transmit.
__TX__: Transmitting pins
**RX**: Receiving pins

## SFP

![](https://i.imgur.com/ln7DsOb.png)

SFP is a transceiver that enable efficient data transmission by seamlessly converting optical and electrical signals allowing data to be transmitted over long distances.

![](https://imgur.com/tKSEOLJ.png)

## Fiber optic cable

The components of fiver-Optic cable are:

![img](https://i.imgur.com/HoBy2Rc.png[/img])

## Ethernet Hub

![](https://i.imgur.com/nzjcjDj.jpeg)

An Ethernet hub or repeater hub is a network hardware device for connecting multiple Ethernet devices together and making them act as a single network segment

Hubs operate at the Physical Layer (Layer 1) of the OSI model, functioning as simple multi-port repeaters that transmit raw electrical signals or bits to all connected devices, without understanding data frames, MAC addresses, or IP addresses, making them "dumb" devices that broadcast data everywhere.

Not like the switch for example which looks the same but operates in the layer 2 (data link).

Ethernet hubs operate exclusively in half-duplex mode, necessitating the use of *CSMA/CD* to manage access to the shared physical medium. Since a hub functions as a single collision domain, a collision occurs whenever two or more hosts attempt to transmit frames simultaneously. Upon detecting such a collision, the CSMA/CD protocol forces the stations to cease transmission, emit a jam signal, and wait for a randomized backoff period before attempting retransmission.
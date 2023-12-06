![](https://dl.dropbox.com/scl/fi/knd37i3rq2u7ky7k802om/Screenshot_12.png?rlkey=jygnky3o8nb5ubc8dftcy5mcq&row=2)

	[A]ll [P]eople [S]eems [T]o [N]eed [D]ata [P]rocessing.

**OSI** (Open Systems Interconnection) model consists of seven layers, each serving a specific function in network communication.
### Application

Where you interact with the program and the data. You use your computer and a program like a browser or an email client to write your message.

## Transport

The **Transport layer** takes your message and splits it into smaller pieces, called segments. It also adds some information to each segment, like a sequence number and a checksum, to make sure that your message can be reassembled and verified on the other end.

### TCP/UDP
#### TCP (Transmitting Control Protocol)

![](https://www.cloudflare.com/img/learning/cdn/tls-ssl/tcp-handshake-diagram.png)

TCP does this by using what's called a **three-way handshake** (SYN ACK-SYN ACK) :

1. the sender computer sends a message called a **SYN** (synchronize)
2. The receiving computer then replies with an **ACK** (acknowledgement) and it also includes a **SYN** message of its own, so this message is called a **SYN-ACK** 
3. The sending computer acknowledges with an **ACK** message.

Now we have an open TCP connection. A similar process is also followed when closed in this connection down.

**Sequence numbers**: TCP will assign numbers to segments as they are sent, this way the receiving device can collect these segments, reorder them correctly and determine if any segments are missing. The sequence number is just one field in the TCP header. The way this works is by using sequence numbers and acknowledgement numbers. 

![](https://media.tenor.com/ZyWq25EtZxYAAAAC/the-office-dwight-schrute.gif)

  
**Checksum:** is like a math calculation done on the data. If the data travels without problems, the result of the calculation at the receiving end should be the same as the one at the sending end. But if there are issues, like some bits getting mixed up, the calculation results won't match, and the data part (segment) will be thrown away.
#### UDP (User Datagram Protocol)

UDP is like a machine gun of data just firing and firing not caring if data is lost or not, It has one goal and that goal is to send data and that is useful in the situations where we need live real-time connections. For example, voice calls, video calls and gaming all need fast real-time connections. We can't afford latencies in these situations. We can handle a loss of voice data because who really cares about a bit of jitter in a voice call? 

![](https://skminhaj.files.wordpress.com/2016/02/92926-tcp_udp_headers.jpg)

At a UDP header as you can see there is a lot less information here than there is on the TCP header. We only have the port numbers, the length of the data and a checksum the small header means less information but is lighter and is quicker. Perfect for real-time traffic.

### Port numbers

![](https://media.tenor.com/BbrOTVqxTZsAAAAC/cats-animals.giff)

Port numbers are like mailboxes for computers, helping them manage different types of data. Just as you install a *letterbox* for your house to receive mail, computers use port numbers to receive application data. For instance, a web server might have port 80 assigned for HTTP, and a mail server could use port 25 for SMTP.

When you make a request, like accessing a website, your computer adds the destination port number (e.g., 80 for HTTP) to the TCP header. The server receives the request, looks at the port number, and directs it to the right application (e.g., the web server). The response follows a similar process, with port numbers ensuring the data reaches the correct application on both ends.

The IP address gets the data to the computer but it's the port number that gets the data to the right application.

| Port Number | Protocol   | Service       |
|-------------|------------|---------------|
| 20          | TCP/UDP    | FTP Data      |
| 21          | TCP        | FTP Control   |
| 22          | TCP/UDP    | SSH           |
| 25          | TCP        | SMTP          |
| 53          | TCP/UDP    | DNS           |
| 80          | TCP        | HTTP          |
| 110         | TCP        | POP3          |
| 143         | TCP        | IMAP          |
| 443         | TCP        | HTTPS         |
| 3389        | TCP/UDP    | RDP (Remote Desktop) |

#### netstat

The `netstat` command will show your computer's source port (your mailbox) and the destination port (the web server's mailbox). Changing the port, like using :53 for DNS, won't work if the server isn't expecting that type of data.

```shell
netstat
```
## Network

In this layer it takes each segment and wraps it in another layer of information, called a packet. This layer adds the source and destination addresses of your computer and your friend’s computer, so that the network knows where to send the packets.

### IP
**Internet Protocol address** is a numerical label assigned to each device connected to a computer network that uses the Internet Protocol for communication. It serves two main purposes: identifying the host or network interface and providing the location of the host in the network.

IP addresses are essential for data routing and addressing in the network. There are two types of IP addresses: 
- IPv4 (Internet Protocol version 4): Composed of four sets of numbers separated by dots (e.g., 192.168.0.1)
- IPv6 (Internet Protocol version 6): longer and formatted differently to accommodate the growing number of devices connected to the internet

![](https://www.webopedia.com/wp-content/uploads/2020/10/what-is-the-difference-between-ipv6-and-ipv4_5f85a8b80d255-2.jpeg)

| | Bits | Possibilities | Example |
|--| -- | -- | -- |
|IPv4| 32-bit | 2^32 (4 billion)| 1.160.10.240 |
|IPv6| 128-bit | 2^128 (infinite-Like number) | 3ffe:1900:4545:3:200:f8ff:fe21:67cf| 

### Special IP: localhost

![](https://fossbytes.com/wp-content/uploads/2016/10/localhost-127.0.0.1.jpg)

**localhost** is a hostname that refers to the current computer used to access it. The name localhost is reserved for loopback purposes. It is used to access the network services that are running on the host via the loopback network interface. Using the loopback interface bypasses any local network interface hardware.





## Data link

Takes each packet and converts it into a stream of bits, which are the basic units of data in a network. This layer also adds some information to each packet, like a header and a trailer, to help the devices on the network communicate with each other.

## Physical

Finally, the **Link layer** sends the bits over the physical medium, which can be a cable, a wireless signal, or a fiber optic. The bits travel from one device to another.

- **base station:** Another word for the first router that handles your packets as they are forwarded to the Internet. 
- **broadcast:** Sending a packet in a way that all the stations connected to a local area network will receive the packet. 
- **gateway:** A router that connects a local area network to a wider area network such as the Internet. Computers that want to send data outside the local network must send their packets to the gateway for forwarding. 
- **MAC Address:** An address that is assigned to a piece of network hardware when the device is manufactured. 
- **token:** A technique to allow many computers to share the same physical media without collisions. Each computer must wait until it has received the token before it can send data.
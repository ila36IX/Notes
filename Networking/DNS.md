# Domain Name System

Is the technology that translates human-adapted, text-based domain names to machine-adapted, numerical-based IP. When users type domain names into the **URL** bar in their browser, **DNS** servers are responsible for translating those domain names to numeric IP addresses, leading them to the correct website.

### IP address of a hostname

You can use the `host` command to look up to a DNS name and get back an IP address.

```shell
host -t a google.com

# the some utilety
dig google.com
```

To git more details use `dig` command which provides an output that is more closer to the way it's stored in DNS server.

```sh
dig google.com
```

## DNS record types

### A (address)

An **A record** maps a domain name to the IP address (Version 4) of the computer hosting the domain. An A record uses a domain name to find the IP address of a computer connected to the internet
### AAAA Record

Is the some as a **A record** the only difference is A records points to Version 4 IP address (IPv4), and the **AAAA** record points to version 6 IP address (IPv6).

### CNAME Records

**CNAME records** can be used to alias one name to another. CNAME stands for Canonical Name.

A common example is when you have both `example.com` and `www.example.com` pointing to the same application and hosted by the same server. To avoid maintaining two different records, it’s common to create:

- An `A` record for `example.com` pointing to the server IP address
- A `CNAME` record for `www.example.com` pointing to `example.com`

### MX Record (Mail Exchange)

A mail exchanger record (MX record) specifies the mail server responsible for accepting email messages on behalf of a domain name. It is a resource record in the Domain Name System (DNS). It is possible to configure several MX records, typically pointing to an array of mail servers for load balancing and redundancy.

### How DNS works?

![](https://ucf37b03d18f023a412529a8e52b.previews.dropboxusercontent.com/p/thumb/ACJ0HyCWfAwn9oPtSDzeWpTUxrP0xRKa4yKR6Bij-s6ihX5AbVaiGJB2NJ33Q4pn74DTbkRBFFbKJ5ty7rJTbOXqZ2HXFsvVJwA1IOh8GeyC4ZCkOHAtvmqMEEV9OJaS9QzVS5Laga6d8NEHOXMa72rXaQnms6TY1gJqva9hHP9UcbgRB0fyAxMaY_ipkDccPzGojKDcaIGt87eurdFeBLrg2eYu-YppRXNRqEjd4-wNDrdDO8RSyvnPzriSn-s2q8a-vUhle5hd0MnRKc9y_PeieS6lVv26CQpcv-yj4h4J7giPmBd4zHJNXj1-X4b8eAr6j-lXpQWkuzwJT2zWmbg1N9OPK2wmpPvex04QswdcIq-zPS0dRpsacob3LL7yLl8/p.png)


1. **Resolver Queries Root Server:**
	- Resolver initiates the process by querying a root nameserver.
	- Root server responds with the address of a Top Level Domain (TLD) DNS server.

2. **Resolver Queries TLD Server:**
	- Resolver queries the TLD server based on the TLD obtained from the root server.
	- TLD server responds with the IP address of the domain's authoritative nameServer.

3. **Resolver Queries Authoritative NameServer:**
	- Resolver queries the authoritative nameserver for the specific domain.
	- Authoritative nameserver responds with the IP address of the origin server.

4. **Resolver Passes IP Address to Client:**
	- Resolver passes the origin server's IP address back to the client.

5. **Client Communicates with Origin Server:**
	- Client initiates a direct query to the origin server using the obtained IP address.
	- Origin server responds by sending website data to be interpreted and displayed by the web browser.
	
![](https://www.cloudns.net/blog/wp-content/uploads/2023/04/Authoritative-DNS-server-2048x1154.png)

### What Is Round Robin DNS?

Round robin DNS is nothing but a simple technique of load balancing various Internet services such as Web server, e-mail server by creating multiple DNS **A records** with the same name.

Instead of a single static IP address for a domain, Round Robin DNS provides a list of IP addresses, and each time a DNS query is made, the order of these addresses is changed.

### What is a DNS NS record?

NS stands for *nameserver*, and the *nameserver* record indicates which DNS server is authoritative for that domain (i.e. which server contains the actual DNS records). Basically, NS records tell the Internet where to go to find out a domain's IP address. A domain often has multiple NS records which can indicate primary and secondary nameservers for that domain. Without properly configured NS records, users will be unable to load a website or application.

![](https://obsidian.md/images/screenshot-1.0-hero-combo.png)
# Network segmentation

A large broadcast domain is a network that connects many hosts. A problem with a large broadcast domain is that these hosts can generate excessive broadcasts and negatively affect the network. This results in slow network operations due to the significant amount of traffic it can cause, and slow device operations because a device must accept and process each broadcast packet.

> **Slow network operations and slow device operations are the result of excessive broadcast traffic.**

![](https://i.imgur.com/fcLbYHz.png)
### Subnetting

> **Routers will not forward an IPv4 broadcast packet by default.**

The solution is to reduce the size of the network to create smaller broadcast domains in a process called **subnetting**. These smaller network spaces are called **subnets**.

![](https://i.imgur.com/3gf9D14.png)


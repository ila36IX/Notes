## HTTP

[Link to learn](https://learn.udacity.com/courses/ud256/lessons/a361ca1c-aa14-4d98-8f15-1d0f50c1afb1/concepts/88a49899-7095-447a-9079-93fd51432997)

You can send an `http` request to a running server using this command:

```shell
printf 'HEAD / HTTP/1.1\r\nHost: en.wikipedia.org\r\n\r\n' | nc en.wikipedia.org 80
```

The first part of this command is just printing a formatted string using `printf`, this format above is a very special because it contains an actual `http` request, the `nc` part is using this string to send it across `TCP` to the server. 

### Used network sockets:

`lsof` is an abbreviation for "list open files," and the inclusion of the `-i` flag in the command signifies its focus on presenting information pertaining to network connections. 

The output reveals the open ports utilized by incoming responses from the server side, ensuring the accurate delivery of messages to the appropriate application or even specific tabs within an application.

```shell
# Find the process that opened a local internet port:
lsof -i :port
```

### How to Check Network Connectivity

PING (Packet Internet Groper) command is used to check the network connectivity between host and server/host. This command takes as input the IP address or the URL.
Ping uses **ICMP** (Internet Control Message Protocol) to send an **ICMP echo message** to the specified host if that host is available then it sends **ICMP reply message**.

```shell
ping google.com
```

### IP address of a hostname

You can use the `host` command to look up to a DNS name and get back an IP address.

```shell
host -t a google.com

# the some utilety
dig google.com
```


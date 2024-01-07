## HTTP

[Link to learn](https://learn.udacity.com/courses/ud256/lessons/a361ca1c-aa14-4d98-8f15-1d0f50c1afb1/concepts/88a49899-7095-447a-9079-93fd51432997)

You can send an `http` request to a running server using this command:

```shell
printf 'HEAD / HTTP/1.1\r\nHost: en.wikipedia.org\r\n\r\n' | nc en.wikipedia.org 80
```

The first part of this command is just printing a formatted string using `printf`, this format above is a very special because it contains an actual `http` request, the `nc` part is using this string to send it across `TCP` to the server. 

This command is used to asks the server to send just the headers for a resource, rather than sending the full data. You can do **GET** requests as well, though:

```sh
printf "GET / HTTP/1.0\r\n\r\n" | nc google.com 80
```

By this following command, we make up a server-like that listen for requests from the browser, and at the some time response to those requests by sending an `HTTP` request to `www.efff.org`.

```sh
printf 'HTTP/1.1 302 Moved\r\nLocation: https://www.eff.org/' | nc -l 2345
```

To connect to this port using the browser, you can use :

`<your ip>:port`
	
### Used network sockets:

`lsof` is an abbreviation for "list open files," and the inclusion of the `-i` flag in the command signifies its focus on presenting information pertaining to network connections. 

The output reveals the open ports utilized by incoming responses from the server side, ensuring the accurate delivery of messages to the appropriate application or even specific tabs within an application.

```shell
# Find the process that opened a local internet port:
lsof -i :port
```


### Listen of a Port

It  is quite simple to build a very basic client/server model using nc.
On one console, start `nc` listening on a specific port for a connection.
For example:

```sh
 nc ‐l 1234
```

`nc` is now listening on port 1234 for a connection.  On a second console
(or a second machine), connect to the machine and port  being  listened
on:

```sh
nc ‐N 127.0.0.1 1234
```

There  should now be a connection between the ports.  Anything typed at
the second console will be concatenated to the first,  and  vice‐versa.
After  the  connection  has  been set up, nc does not really care which
side is being used as a ‘server’ and which side  is  being  used  as  a
‘client’.  The connection may be terminated using an EOF (‘^D’), as the
`-N` flag was given.

`nc` in this case is using a plain **TCP**, with no other layers (SSH, HTTPS, HTTP) between it and the network.

### How to Check Network Connectivity

PING (Packet Internet Groper) command is used to check the network connectivity between host and server/host. This command takes as input the IP address or the URL.
Ping uses **ICMP** (Internet Control Message Protocol) to send an **ICMP echo message** to the specified host if that host is available then it sends **ICMP reply message**.

```shell
ping google.com
```



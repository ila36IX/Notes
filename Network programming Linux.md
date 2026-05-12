# Network programming

![](https://i.imgur.com/CBMWgCO.png)

```c
struct addrinfo {
    int              ai_flags;     // AI_PASSIVE, AI_CANONNAME, etc.
    int              ai_family;    // AF_INET, AF_INET6, AF_UNSPEC
    int              ai_socktype;  // SOCK_STREAM, SOCK_DGRAM
    int              ai_protocol;  // use 0 for "any"
    size_t           ai_addrlen;   // size of ai_addr in bytes
    struct sockaddr *ai_addr;      // struct sockaddr_in or _in6
    char            *ai_canonname; // full canonical hostname

    struct addrinfo *ai_next;      // linked list, next node
};
```

`struct sockaddr * ai_addr` is the field which contains the port an the host
data, it can be cast to `struct socketadd_in` of `_in6`.

```c
// for ipv4
struct sockaddr_in {
    short int          sin_family;  // Address family, AF_INET
    unsigned short int sin_port;    // Port number
    struct in_addr     sin_addr;    // Internet address (uint32_t)
                                    // struct in_addr {
                                    //     uint32_t s_addr;
                                    // };
    unsigned char      sin_zero[8]; // Same size as struct sockaddr
};

// for ipv6
struct sockaddr_in6 {
    u_int16_t       sin6_family;   // address family, AF_INET6
    u_int16_t       sin6_port;     // port, Network Byte Order
    u_int32_t       sin6_flowinfo; // IPv6 flow information
    struct in6_addr sin6_addr;     // IPv6 address
                                   // struct in6_addr {
                                   //     unsigned char   s6_addr[16];   // IPv6 address
                                   // };
    u_int32_t       sin6_scope_id; // Scope ID
};
```

## getaddinfo

```c
void get_my_host_address_info()
{
    struct addrinfo hints   = {};
    struct addrinfo *result = NULL;

    // Only the ai_flags, ai_family, ai_socktype, and
    // ai_protocol fields of the addrinfo structure can be set. else
    // should be set to 0.

    // Restricts the network layer address resolution process to a 
    // specified protocol suite
    hints.ai_family = AF_INET; // address family specifying communication 
                               // range. 
                               // AF_UNSPEC to accept both v4 and v6
                               // AF_UNIX) domain allows communication between                                // processes

    hints.ai_socktype = SOCK_STREAM; // Specifies transport layer service
    hints.ai_flags    = AI_PASSIVE;  // fill my ip

    int status;
    if ((status = getaddrinfo(NULL, "3490", &hints, &result)) != 0)
    {
        fprintf(stderr, "gai error: %s\n", gai_strerror(status));
        exit(1);
    }
    
    freeaddrinfo(result); // free everything!
}
```
  
To resolve an address from domain name:

```c
int status;
struct addrinfo hints;
struct addrinfo *servinfo;  // will point to the results

memset(&hints, 0, sizeof hints); // make sure the struct is empty
hints.ai_family = AF_UNSPEC;     // don't care IPv4 or IPv6
hints.ai_socktype = SOCK_STREAM; // TCP stream sockets

// get ready to connect
status = getaddrinfo("1337.ma", "80", &hints, &servinfo);
```

## Socket
### Random Load Balancing

Assigns connections randomly to servers.
Useful for UPTIME but questionable in other scenarios.

### Round Robin

Distributes connections evenly in a circular queue to each server.
Suitable for balanced server configurations.

### Weighted Round Robin

Similar to Round Robin but with weights for each server based on its capacity.
Improves on Round Robin by considering server capacities.

### Dynamic Round Robin

Dynamically adjusts weights based on continuous monitoring of server performance.
Offers a dynamic approach to load balancing.

### Fastest

Routes connections to the server with the fastest response time.
Straightforward but may lead to congestion if response times change rapidly.

### Least Connections

Directs new connections to the server with the fewest existing connections.
May cause congestion with varying connection durations.

### Observed

Combines logic from Least Connections and Fastest algorithms.
Ranks servers based on connection count and response time.

### Predictive

Utilizes the ranking method of Observed but considers trends in server performance over time.
Favors servers with improving performance.

[More informations ⇾](https://community.f5.com/t5/technical-articles/intro-to-load-balancing-for-developers-the-algorithms/ta-p/273759)

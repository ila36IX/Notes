# Docker playing around

```bash
docker pull ubuntu
docker run -d -it --hostname somehting --name container_name ubuntu[:14.1]

# To connect to the container
sudo docker exec -it container_name bash
```

> For port forwarding use `-p host-port:container-port`
> Example: `-p 127.0.0.1:8080:80/tcp`
> This binds port `80` of the container to TCP port `8080` on `127.0.0.1` of the host.

To see the container IP address:

```bash
docker inspect -f '{{ .NetworkSettings.Networks.bridge.IPAddress }}' container_name
```

Now you have all the servers running in you machine, they all need to update their package manager, and installing **MySQL** server:

```bash
apt update
apt upgrade -y
apt install mysql-server -y

service mysql start

# OR in simple fotm
/etc/init.d/mysql start
```

### Wandering how much space docker is using?

```bash
docker system df [-v]
```

### Starting a Stopped Container

```bash
docker start <container_name_or_id>

# To see a list of existing containers
docker ps -a
```
### Stopping container

```bash
docker stop <container_name_or_id>
```

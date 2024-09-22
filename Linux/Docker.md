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

# Show only the working containers
docker ps
```

### Show logs

```bash
docker logs <id>
docker logs -f <id> # On time logs
```
### Stopping container

```bash
docker stop <container_name_or_id>
```

### Cleaning up

```bash
docker rm <id>
docker rm -f <id> # if container is running

# Remove unused images
docker image prune 
docker image prune -f

# Remove unused build cache
docker builder prune
docker builder prune -f

# Remove unused volumes
docker volume prune
docker volume prune -f
```

**Regularly clean up:** To prevent the cache from growing too large, consider running:

```bash
docker system prune
```

periodically to remove unused images, containers, volumes, and networks.
## Dockerfile

This `Dockerfile` creates a container image based on Ubuntu 18.04, sets up a Python 3.7 environment with Flask and Flask-Babel, and runs a Flask application.

```dockerfile
# Use Ubuntu 18.04 as the base image
FROM ubuntu:18.04

# Set environment variables
ENV PYTHONUNBUFFERED 1
ENV DEBIAN_FRONTEND noninteractive
ENV FLASK_DEBUG 1

# Update and install system dependencies
RUN apt-get update && apt-get install -y \
    python3.7 \
    python3-pip \
    python3.7-dev \
    && rm -rf /var/lib/apt/lists/*

# Set Python 3.7 as the default python version
RUN update-alternatives --install /usr/bin/python3 python3 /usr/bin/python3.7 1
RUN update-alternatives --set python3 /usr/bin/python3.7

# Upgrade pip
RUN python3 -m pip install --upgrade pip

# Install Flask and Flask-Babel
RUN pip3 install Flask==2.1.0 Flask-Babel==2.0.0

# Set the working directory in the container
WORKDIR /app
COPY . /app

# Command to run the Flask application
CMD ["python3", "-m", "flask", "run", "--host=0.0.0.0"]
```

The script builds a Docker image from the current directory and runs it as a container, mapping port 5000 on the host machine to port 5000 inside the container and mounting the current working directory as a volume. To use it, save the script as a `.sh` file (e.g., `run_flask_app.sh`), make sure the Dockerfile is in the same directory, and then run the script:

```sh
#!/bin/bash

IMAGE_NAME="flask-babel-app"
CONTAINER_NAME="my_flask_babel_app"

# Check if image exists
if ! docker images --quiet --filter=reference="$IMAGE_NAME" | grep -q "$IMAGE_NAME"; then
    # Build image if it doesn't exist
    docker build -t "$IMAGE_NAME" . || exit 1
fi

# Check if container exists
if ! docker ps --quiet --filter=name="$CONTAINER_NAME" | grep -q "$CONTAINER_NAME"; then
    # Run container if it doesn't exist
    docker run -d -p 5000:5000 -v "$(pwd):/app" --env VARIABLE_NAME=value --name "$CONTAINER_NAME" "$IMAGE_NAME" || exit 1
else
    # Start existing container
    docker start "$CONTAINER_NAME" || exit 1
fi

echo "Happy coding :)"
```

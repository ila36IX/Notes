hi
```sh
# This will remove the container after quiting
docker run --rm -it ubuntu /bin/fish
```

```sh
docker run --pid host busybox:1.29 ps
# Should list all processes running on the computer. This will not use custom name space.
```

## Building an image from a container

```sh
# Modifies file in container
docker container run --name hw_container ubuntu:latest touch /HelloWorld

# Commits change to new image
docker container commit hw_container hw_image
```

## Removing a container

```shell
# Always remember to clean up your workspace, like this:
docker container rm -vf container-name
```
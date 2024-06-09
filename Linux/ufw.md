# Uncomplicated FireWall

![](https://i.imgur.com/WlvUrnW.png)

`ufw`  is simple tool that makes configuring firewalls easy, but be aware that it could be also danger as it could make your server inaccessible via `ssh` if you done a bad configuration, so before adding any rules you have first to stop `ufw` by running the following command:

```bash
echo "y" | sudo ufw disable

sudo systemctl stop ufw

# SHOULD PRINTS:
sudo ufw status
# Status: inactive 
```

Get rid of the old configuration, and start fresh

```bash
echo "y" | sudo ufw reset
```

Deny every connection that starts from outside the server, and allow every connection from inside the server:

```bash
sudo ufw default deny incoming
sudo ufw default allow outgoing
```

The two essential protocols that we want to keep active are `http`, `https` and `ssh`:

```bash
sudo ufw allow ssh
sudo ufw allow http
sudo ufw allow https
sudo ufw allow 'Nginx Full'
```

Now if everything goes well, you can enable the `ufw` again.

```bash
echo "y" | sudo ufw enable
```

If you ever deny port ``22/TCP`` and log out from your server, you will not be able to reconnect to to it via SSH, always check if the connection via `ssh` is not refused before closing the main TCP session where you made something wrong. 

UFW rule that allows connections from your replica server through the source’s firewall.

```bash
sudo ufw allow from [replica_server_ip] to any port 3306
```

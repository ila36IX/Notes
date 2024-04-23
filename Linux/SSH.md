# Secure shell

*error* Permission denied (publickey)

Usually you need to run this command:

```shell
ssh-add path/to/private_key
```

**public key**: Must append ( ``>>`` ) it in the file `~/.ssh/authorized_kes` inside the remote server.
**private kay**: Connecting to remote server using a specific private key

```bash
ssh -i path/to/pkey usename@host 
```


Copy file to remote server:

```shell
scp path/to_file username@host:destenation/path
```

Be aware that this file `/etc/ssh/ssh_config` exists, and its the first one that `ssh` use to decide what to do next:

```bash
# This is the ssh client system-wide configuration file.  See
# ssh_config(5) for more information.  This file provides defaults for
# users, and the values can be changed in per-user configuration files
# or on the command line.

# Configuration data is parsed as follows:
#  1. command line options
#  2. user-specific file
#  3. system-wide file
# Any configuration value is only changed the first time it is set.
# Thus, host-specific definitions should be at the beginning of the
# configuration file, and defaults at the end.

# Site-wide defaults for some commonly used options.  For a comprehensive
# list of available options, their meanings and defaults, please see the
# ssh_config(5) man page.

Include /etc/ssh/ssh_config.d/*.conf

Host *
#   ForwardAgent no
#   ForwardX11 no
#   ForwardX11Trusted yes
#   HostbasedAuthentication no
#   GSSAPIAuthentication no
#   GSSAPIDelegateCredentials no
#   GSSAPIKeyExchange no
#   GSSAPITrustDNS no
#   BatchMode no
#   CheckHostIP yes
#   AddressFamily any
#   ConnectTimeout 0
#   StrictHostKeyChecking ask
#   IdentityFile ~/.ssh/id_rsa
#   IdentityFile ~/.ssh/id_dsa
#   IdentityFile ~/.ssh/id_ecdsa
#   Port 22
#   Ciphers aes128-ctr,aes192-ctr,aes256-ctr,aes128-cbc,3des-cbc
#   MACs hmac-md5,hmac-sha1,umac-64@openssh.com
#   EscapeChar ~
#   Tunnel no
#   TunnelDevice any:any
#   PermitLocalCommand no
#   VisualHostKey no
#   ProxyCommand ssh -q -W %h:%p gateway.example.com
#   RekeyLimit 1G 1h
#   UserKnownHostsFile ~/.ssh/known_hosts.d/%k
    SendEnv LANG LC_*
    HashKnownHosts yes
    GSSAPIAuthentication yes
    IdentityFile ~/.ssh/school
    PasswordAuthentication no
```

## copy file to a remote server

```bash
scp -T -i $PATH_TO_SSH_KEY $PATH_TO_FILE $USERNAME@$IP:$DESTENATION_PATH

# check if file exist

ssh $USERNAME@$IP "ls $DESTENATION_PATH"
```

## fcp

`scp` copies files between hosts on a network.

`scp` uses the SFTP protocol over a **ssh** connection for data transfer, and uses the same authentication and provides the same security as a login session

```bash
 # Copy a local file to a remote host:
scp [-i path/private_key] path/to/local_file user@host:remote_destenation_path
```

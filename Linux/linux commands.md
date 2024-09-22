tr
To view all running processes along with their child processes in a “tree” format, use the following command:

```bash
ps axf
```

## tcpdump

Dump traffic on a network.

```bash
tcpdump -i any -c 100 -n port 53
```

``-i``: interface card to listen into use ``tcpdump -D`` to see them
`-c`: Many packets to receive before exit
`-n`: IP addresses only (No application names)

To preview DNS ( port 53 ) lookup you can run this command:

```bash
sudo tcpdump -i any -n port 53
```

Save Output to file:

```bash
sudo tcpdump -w ./breakme.pcap -c 30 -v
```

`-v`: is used just to tell that packets are received
## host

Gives you the IP address that a domain name is pointing to,  and its record type (A, AAAA, MX, CNAME..)

```bash
host getalien.tech
host ip_address
```


## List the opining ports

```
netstat -tlnp
```

## hydra

hydra

Online password guessing tool.

Guess SSH credentials using a given username and a list of passwords:
  
```
hydra -l username -P path/to/wordlist.txt host_ip ssh
```

  Guess HTTPS webform credentials using two specific lists of usernames and passwords ("https_post_request" can be like "username=^USER^&password=^PASS^"):
  
```bash
hydra -L path/to/usernames.txt -P path/to/wordlist.txt host_ip https-post-form "url_without_host:https_post_request:login_failed_string"
```
  
Guess FTP credentials using usernames and passwords lists, specifying the number of threads:
  
```
hydra -L path/to/usernames.txt -P path/to/wordlist.txt -t n_tasks host_ip ftp
```

## awk 

1. **Print Each Line:**

```bash
awk '{ print }' file.txt
```

2. **Print Specific Fields:**

```bash
# Print the first field of each line 
awk '{ print $1 }' file.txt`
```    

3. **Filtering Records:**

```bash    
# Print lines where the second field is "example" 
awk '$2 == "example" { print }' file.txt`
``` 

4. **Arithmetic Operations:**

```bash
# Calculate and print the sum of numbers in the first column 
awk '{ sum += $1 } END { print sum }' file.txt
```

5. **Conditional Statements:**

```bash
# Print lines where the first field is greater than 10 
awk '$1 > 10 { print }' file.txt`
``` 

6. **Custom Field Separator:**

```bash
# Set the field separator to ':' 
awk -F':' '{ print $1 }' file.txt`
``` 

7. **Built-in Variables:**

```bash
# Print the total number of lines 
awk 'END { print NR }' file.txt`
```

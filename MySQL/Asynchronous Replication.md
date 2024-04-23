
![](https://i.imgur.com/nDF0ohm.png)
# Master-slave replication

Asynchronous replication provides lower write latency since a write is acknowledged locally by a source before being written to the replicas.
### The binary logs

The events are recorded within the binary log in different formats according to the type of event. MySQL replication has three kinds of binary logging formats:

- **Row-based replication:**  Replication of the source to the replica works by copying the events representing the replica’s table rows’ changes.

- **Statement-based replication:** The source writes SQL statements to the binary log. Replication of the source to the replica works by executing the SQL statements on the replica.

- **Mixed replication:** MySQL uses a statement-based log by default but switches to a row-based log for certain unsafe statements that have a nondeterministic behavior (used unsafe functions like ``now()``).
#### 1. Binary log dump thread

The source creates a thread to send the binary log contents to a replica when the replica connects.
#### 2. Replication I/O thread

The replica creates an I/O thread connected to the source and asks it to send the updates recorded in its binary logs. The replication I/O thread reads the updates that the source’s *Binlog Dump thread* sends 

#### 3. Replication SQL thread

The replica creates a SQL thread to read the relay log written by the replication I/O thread and execute the transactions contained in it.

## Inside the replica

Once the replica instance has been initialized, it creates two threaded processes.  _IO thread_ and SQL thread:

1.  _IO thread_, connects to the source MySQL instance and reads the binary log events line by line, 
2.  _IO thread_ copies logs over to a local file on the replica’s server called the _relay log_. 
3. _SQL thread_, reads events from the relay log and then applies them to the replica instance as fast as possible.

![](https://i.imgur.com/488FzV0.png)

## Source DB configuration

 ``/etc/mysql/mysql.conf.d/mysqld.cnf`` is the path to the file that will consists of the configuration.

```
[mysqld] 
log-bin=mysql-bin 
server-id=1
# bind_address /comment_this_one
# Everyone could access your server from outside, so its good idea
# to make a firewall rule that deny any ip addess except the slave's
binlog_do_db= db_name # Slave will clone replicate this database and ignore others
```

You’ll need to restart the server after making these changes because these parameters are not dynamic.

```bash
/etc/init.d/mysql restart
```

### Source server new user

Create a user account on the source server that the replica can use to connect.

```mysql
CREATE USER 'repl'@'%' IDENTIFIED BY 'P@ssw0rd89!';
GRANT REPLICATION SLAVE ON *.* TO 'repl'@'%';

/* if slave server has a static ip, it's more secure to use it instead of % sign */
```

### Creating a snapshot of database if already exists

You can make a snapshot of database if it's already exists by the following:

```bash
sudo mysqldump -uroot -proot db > db.sql
```

In the slave server, you'll want to create the database `db` and clone into it the file `db.sql`.

```bash
sudo mysql db < /tmp/db.sql
```

###  Get the source log file and log pos of the master server

```mysql 
SHOW MASTER STATUS;
```
## Slave DB server configuration

 ``/etc/mysql/mysql.conf.d/mysqld.cnf`` is the path to the file that will consists of the configuration.

```
server-id = 2
log_bin = /var/log/mysql/mysql-bin.log
binlog_do_db = db
relay-log = /var/log/mysql/mysql-relay-bin.log
```

Than restart the server!

```bash
/etc/init.d/mysql restart
```

Now it's time to make the configure the database replica, inside your slave database run:

```sql
CHANGE REPLICATION SOURCE TO
SOURCE_HOST='source_server_ip',
SOURCE_USER='repl',
SOURCE_PASSWORD='password',
SOURCE_LOG_FILE='mysql-bin.000001',
SOURCE_LOG_POS=899;
```

To get the `SOURCE_LOG_FILE` and `SOURCE_LOG_POS` you have to run this query in your **Source server**:

```mysql
SHOW MASTER STATUS;
```

Than run the replica:

```mysql
START REPLICA;
```

To check if everything works well:

```mysql
SHOW REPLICA STATUS\G;
```


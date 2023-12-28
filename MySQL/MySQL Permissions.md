
## Linux basics
### Linux existing users

You can list all the users that are in you system by having a look to this file `etc/passwd`.

![](https://oracle-patches.com/images/2021/02/06/etc_passwd_file.png)

If you want to connect to one of theme just run this command:

```shell
su - username

# Or
sudo -u username bash
```

There also a little problem in this way as you will see a prompt that asking you for a password that you have no idea of what it is, no problem thanks to the power of `root`, just run this command to change the password of a specific user:

```shell
sudo passwd username
```

### Create a new user

The general syntax to create a new user is  the `useradd` command as follows:

```shell
# Create a new user with a default home directory and prompt the user to set a password:
adduser username

# Create a new user without a home directory:
adduser --no-create-home username

# Create a new user with a home directory at the specified path:
adduser --home path/to/home username

# Create a new user with the specified shell set as the login shell:
adduser --shell path/to/shell username

# Create a new user belonging to the specified group:
adduser --ingroup group username

```

### Set permissions to user

You can either change the owner of the file with

```shell
[sudo] chown username: foldername
```

or you can add the user to the group that owns the file with

```shell
usermod -a -G {group-name} username
```

If you want to apply it recursively to all the sub-directories: add the -R flag like this:

```shell
# -R for recursive
setfacl [-R] -m u:username:[r][w][x] myfolder
```

## MySQL GRANT

The `CREATE USER`statement creates a user account with no privileges, by using the `SHOW GRANTS` statement, it will show the privileges assigned to **super@localhost**.

```mysql
CREATE USER super@localhost 
IDENTIFIED BY 'Secure1Pass!';

SHOW GRANTS FOR super@localhost;
```
*The `USAGE` means that the `super@localhost` can log in to the database but has no privilege.*

### New superuser

To make a new super user, you can give the new user all the permissions (grants):

```mysql
GRANT ALL ON *.* TO super@localhost;
```

### More permissions
#### Database privileges

**Database privileges** apply to all objects in a particular database. To assign database-level privileges, you use the `ON database_name.*` syntax, for example:

```mysql
GRANT INSERT, SELECT, ...  ON db_name.*  TO bob@localhost;
```

#### Table privileges

**Table privileges** apply to all columns in a table.

```mysql
GRANT ALL ON db_name.employees TO bob@localhsot;
```

#### Column privileges

**Column privileges** apply to individual columns within a table.

```mysql
GRANT 
	SELECT (employeeNumner,lastName, firstName,email), 
	UPDATE(lastName) 
ON db_name.employees TO bob@localhost;
```

### Delete existing user
Just as you can delete databases with `DROP`, you can use `DROP` to delete a user:

```mysql
DROP USER 'username'@'localhost';
```
More info [Here](https://www.digitalocean.com/community/tutorials/how-to-create-a-new-user-and-grant-permissions-in-mysql)



# Born2BeRoot

![](https://i.imgur.com/8TOLpQw.png)

> Note: In this project, you'll find many vague words that are probably new to you, or you've already heard of them but don't know exactly what they are. The mission of this project is that you need to have a simple idea about each one of these words. Ask a peer what exactly an "IP" address is, what is the reason to use SSH...
> 
> Just try to ask simple questions - that will help a lot. Don't ask generic questions as they're hard to answer and also hard to understand their answers. Split your questions into simple and precise ones.

*It's important for you to learn how to ask good questions :)

![](https://meme-generator.com/wp-content/uploads/mememe/2019/12/mememe_687fdfeb95d57cc392aee056d0aa4a94-1.jpg)

## What is a VM?
[⏯ Watch](https://youtu.be/UBVVq-xz5i0?si=-UTXEVNsMDkbY5SP)

First of all you need to know what are you doing, a good start is to know what the [virtual  machine](https://www.coursera.org/articles/what-is-a-virtual-machine) is? how it works, and why the hell we need to simulate a machine inside our original machine (or the host machine `:)`).

In simple words, a virtual machine is software-based machine with operating system that runs on top of your main one, but is isolated from it. For example, if you want to show off your skills in front of your friends and you run `rm -rf /`, that wouldn't be a good idea - even if you look cool, your *OS go bye-bye*. But if you have a virtual machine, you can run this command safely, and your main OS will remain safe.

Q: But how is it possible to an OS (operating system) to run just like a program, isn't it need it's own CPU, RAM,...

* Wow, what a great question, and its answer will provide us with a good reason to use the word "virtual". It's all related to a piece of software called "[hypervisor](https://en.wikipedia.org/wiki/Hypervisor)", that creates virtual hardware pieces and tricks (lie to) the guest OS into "thinking" it's running on real physical hardware, it creates a perfect fake computer environment for each virtual machine.
- A VM uses "virtualized" resources instead of direct physical components.
- A VM sees a RAM as if it was a physical hardware, but these are actually virtualized components managed by the hypervisor.

![](https://www.sudops.com/wp-content/uploads/2014/03/Hypervisor_infra.jpg)

What is the difference between Host OS vs Guest OS? *"Exited to hear your answer :)"*

Good now we have a good understanding of what a VM is, so let us create one, first you need to have a piece of software called `virtaulBox` (a Type 2 hypervisor) to create and run virtual machines on our computer.

![](https://i.imgur.com/LqQxxtt.png)

[⏯ Watch](https://youtu.be/wX75Z-4MEoM?si=gk-KOOuULc96tl0Q)

Now by installing the `virtualBox`, it's like we have the virtual hardware, what do you think we still need? yes we need an OS (operating system), like Linux the 🐐, but what is Linux?

**Linux** was created in the 1990 by Linus Torvalds, it started just as side project to practice operating systems, and grows to be one of the bigger and complicated projects in the open-source community with more that 1.3M commits in [GitHub](https://github.com/torvalds/linux):

![](https://i.imgur.com/NCmoCwF.png)

But you have to know that Linux by itself does not create a complete OS, yes it gives you a way to handle your machine resources, it provides you with an API? A-P-I what?

![](https://cdn.filestackcontent.com/FT68ZQs2SEesYa93I30C)

> Think of an API like this: when you need to turn off the light in a room, instead of playing around with wires, the electrical engineer has built a structure behind the walls and gives you just a switch to click in when you need to turn the light on/off. That's what Linux is; it gives you easy-to-use "switch-like" controls (sysCalls) to handle instructions needed by the user, like scheduling a process, writing a file, allocating a memory area, and more...

![](https://i.imgur.com/ubfool9.png)

Q: So now we have that scary things called __system calls__, what can we do with them?

- Again you are the master of good questions, and to be clear Linux mission is only giving you this black box to use machine resources, so we need something that will consume (use) those sysCalls to make an actual working system, "Haaave you met GNU project?"

**GNU** is the messing part to create a functional system it's a set of tools and software, that uses those system calls to make programs that can take a simple inputs and output results, like Bash, GCC, Emacs, cat, make, ls, kill,.. and all the utilities you are using in your shell, it is all part of the GNU (GNU Not Unix) project. what is UNIX? "ask some one :)"

![](https://i.imgur.com/az0efnw.png)


Q: Ahah so Linux by itself isn't enough? there is more utilities that creates the OS? 
- Yes, next time when you say I run "Linux", technically you running GNU/Linux OS, Linux is just the kernel (the core part) of that OS.

From this point, we have a working system. To be clear, the "UI" or interface (where you are currently reading this) is not a necessary part of the system. The main mission of a system is to perform calculations, so whatever way you give this machine commands, if it's performing those calculations, it is considered a working operating system.

![](https://i.imgur.com/7I7RVvf.jpeg)

That's why having a CLI (Command Line Interface) is sometimes enough. You interact with the machine using only the command line. The machine you used to get this file that you currently reading doesn't have a display because its mission is solely to respond to your request by sending this file. Similarly, most servers don't have a UI (User Interface); you interact with them using only the CLI.

Can you tell me what a server is? "I'll let you find out by yourself :)"

The GUI (Graphical User Interface), sometimes called a DE (Desktop Environment), it is the part of the system that allows us to interact using a mouse, a display screen, and other visual elements. It's composed of processes running in the background that interact with your screen drivers. For example, if you have ever used Ubuntu, it uses "GNOME" as its desktop environment.

![](https://i.imgur.com/UfYcO6A.png)

In `born2beRoot` they asked you to use the "minimal service", that means you have to avoid installing a DE so the only way to interact with your VM is the CLI (command line), why? "I'll let finding out why to you!"

### Linux distribution

A complete Linux system package called a distribution. Many Linux distributions are available to meet just about any computing requirement you could have. Most distributions are customized for a specific user group, such as business users. Multimedia enthusiasts, software developers, or average home users. Each customized distribution includes the software packages required to support specialized functions, such as audio and video editing software for multimedia enthusiasts, or compilers and integrated development environment for software developers.

There is a [huge number of available distributions](https://upload.wikimedia.org/wikipedia/commons/1/1b/Linux_Distribution_Timeline.svg), but we will focus on two ones that have been motioned in the project subject:

- Rocky
- Debian

Here's a list of some key [differences](https://amadla.medium.com/debian-linux-vs-rocky-os-exploring-the-best-choice-for-your-server-dfd6b3d80c1a) between Debian and Rocky Linux:

| Feature               | Debian                                  | Rocky Linux                              |
| --------------------- | --------------------------------------- | ---------------------------------------- |
| **Origin**            | Created by Ian Murdock in 1993          | Created by Gregory Kurtzer in 2021       |
| **Stability Focus**   | Prioritizes stability over new features | Focuses on stability and enterprise use  |
| **Package Manager**   | `apt`                                   | `dnf` \|\| `yum`                         |
| **Base Distribution** | Independent                             | Based on Red Hat Enterprise Linux (RHEL) |
| **Release Model**     | Stable releases                         | Rolling release model                    |
| **Long-term Support** | Yes                                     | Yes                                      |
| **Default DE**        | Various (e.g., GNOME, KDE)              | GNOME                                    |
| **Community Support** | Strong                                  | Strong                                   |
| **LSM**               | appArmor                                | SELinux                                  |
| **User Interface**    | Can be minimalistic or full-featured    | Typically full-featured                  |

#### Why Choose Debian Over Rocky Linux?

- **Stability**: Debian is known for its rock-solid stability, making it ideal for servers and critical systems.
- **Package Management**: `apt` is widely used and familiar to many Linux users.

We'll focus on Debian because it's more stable and easier to setup and we are a bit more familiarize with it, as it's what Ubuntu uses (the OS in Linux machines in C3 & C4) and also have the `apt` package manager.

- What is a package manager? what is `apt`, `pacman`, `dnf`...
- Give a list of 10 Linux distributions
- What is a DE? Give 3 examples of DE?
- What is `Ubuntu`?
- What is Linux?
#### appArmor

[AppArmor](https://computingforgeeks.com/apparmor-cheat-sheet-for-linux-system-administrators/) is a system. It sets rules to restrict what files, directories, or system resources a program can access.

To check if `appArmor` is running:

```bash
sudo aa-status
sudo systemctl status apparmor
```

## Partitioning

__File system:__ Is data structure that an operating system uses to manage files on a disk or partition, for example: 

- **Ext4** – is a file system Created for Linux-based systems. Includes major improvements over ext3 such as support for large volumes and files. Provides faster disk checks and fragmentation avoidance.

### Partitions (Primary vs Logical)

__Primary Partition:__ This is a primary division of the hard drive that can host an operating system. You can have up to four primary partitions on a single drive, it can be made "bootable", meaning the system can start from them.

__Logical Partition:__ subdivision within an extended partition that can be used to store data or install operating systems, it is usually not bootable. They reside within an extended partition.
### Logical Volumes vs Logical Partitions

[READ](https://medium.com/@ahmedmansouri/understanding-disk-partitioning-in-linux-logical-volumes-vs-logical-partitions-796d46587d64)

![](https://contabo.com/blog/wp-content/uploads/2023/03/image.png)

### How Mounting Works?

**Mounting** means connecting a storage device or partition to a specific directory in the Linux file system.
When a partition is **mounted** to a directory (e.g., `/home`), any files you access in `/home` are actually stored on that separate partition, not on the root partition.

> `/home` is **logically inside the root directory** and **physically resides** on a completely different storage space.

- Partition tables (MBR vs GPT)
- Swap space
- Boot process
- GRUB bootloader

## Directory Structure:

![](https://i.pinimg.com/originals/f1/56/6a/f1566aef2c7fe30b37490f0ae02e817b.png)

## Change default font

```
setfont /usr/share/consolefonts/Lat7-Terminus28x14.psf
```

## Config users

![](https://i.imgur.com/qGpYVAI.png)

- [READ: hi root](https://www.clrn.org/what-is-root-linux/)
- [READ: Create new user](https://linuxize.com/post/how-to-create-users-in-linux-using-the-useradd-command/)

Install the `sudo` utility, which allows executing single commands with superuser or alternative user privileges. Unlike logging in as root and performing all actions with unrestricted access, `sudo` provides a more secure approach.

Q: If `sudo` command is just to run command as `root` user, why don't we just log-in as root and do everything we need freely? "I'll let finding out why to you!"

You need to have two users in your created machine:
- root (It should be exists by default)
- aljbari (your user name)
### How?

`useradd`: Create a new user.
`userdel`: Remove a user.
`usermod`: Change user details.

```sh
# Create a new user:
 sudo useradd username

# Remove a user:
 sudo userdel username
 
# Create a new user belonging to additional groups:
 sudo useradd -G|--groups group1,group2,... username
```

For example to add a user to the `sudo` group you can do the following:

```bash
# Add to sudo group
sudo usermod -aG sudo aljbari42
```

### Groups

Those are your friends: `groupadd`, `groupdel`, `groupmod`, `groups`.

```sh
# Print group memberships a user:
groups alien

# Create a new group:
sudo groupadd user42

# Delete an existing group:
sudo groupdel trash

# Change the group name:
sudo groupmod --new-name g61 g69

```

**TASK**: Create the group "aliens" and create those users: "heatblast", "XLR7", "upgrade", all those users must belong to "aliens" group.
- Make "XLR7" a superuser
- I made a typo, please rename the user "XLR7" to "XLR8"

![](https://media.tenor.com/svkW47X_XAcAAAAM/xlr8.gif)

## ssh

- [READ: SSH Essentials](https://www.digitalocean.com/community/tutorials/ssh-essentials-working-with-ssh-servers-clients-and-keys)
- [Watch: How ssh works](https://www.youtube.com/watch?v=ORcvSkgdA58)
- [Watch: SSH crash course](https://www.youtube.com/watch?v=hQWRp-FdTpc)
- [Watch: SSH keys](https://www.youtube.com/watch?v=dPAw4opzN9g)
- [READ: You have to know what is RSA in brief](https://en.wikipedia.org/wiki/RSA_(cryptosystem))

```sh
# install ssh server
sudo apt install openssh-server
# check if ssh in running
sudo service ssh status
# change the port form 22 default to 4242
# than change the line #Port 22 ro Port 4242 without #
sudo vim /etc/ssh/sshd_config
#after saving the file restert ssh
sudo service ssh restart
```

In this point you've played a bit with  `IP` address and port `4242`, you need to know what those are, [Watch: you don't have to watch it all](https://youtu.be/3b_TAYtzuho?si=Q4lDxvkqUtwpdIip)

If you watch the video above you'll learn about TCP, and for your information SSH is using that protocol to establish the connection, so for short you're using the IP and the port because they are essential parts for TCP (that thing that makes connection possible) to work.

Q: what is the default port used by the ssh?
### localhost?

![](https://images.hdqwalls.com/download/there-is-no-place-like-localhost-f9-3840x2160.jpg)

`localhost` is a special IP address that routes network requests back to your own machine, effectively telling the protocol to communicate within the same computer rather than across a network.

You hopefully know by now that SSH is a network protocol for remote command execution. 

For learning purposes, we'll simulate connecting to a VM using the loopback IP `127.0.0.2`, which in real scenarios would be replaced with the actual remote machine's IP address.

There is some kind of service that are running on localhost (`127.0.0.1`),  so will need to change the IP to `127.0.0.2`, and that will be the trick.

>Note: we'll not use `localhost` in this case, because it's a special host that refer exactly to the `127.0.0.1`, how did I know this? easy just have a look to the following file:

```sh
$ cat /etc/hosts                                                                 
127.0.0.1 localhost
127.0.1.1 dump-ubuntu-benguerir
# more text here...
```

As you can see using __localhost__ we'll make you use `127.0.0.1`, there is something running in that particular IP on port 4242, so let's use `127.0.0.2` the next available IP.

Q: How did you know that something is running in port `4242` on localhost?

### Port forwarding

As I was saying, everything is isolated in your VM. Even if you installed SSH and made it running on port 4242, that doesn't mean anything to the host machine; nothing will be changed, so SSH will not run on the host machine.

However, this isn't impossible. You just need to configure `VirtualBox` to make changes in the host and guest machines by going to `Settings->Network->Advanced->Port Forwarding` (_I hope you like linke lists_), and do those changes:

![](https://i.imgur.com/2WZACTG.png)

![](https://i.imgur.com/GW0SjSX.png)

---

![](https://i.imgur.com/JHVfSSC.png)
####  Let's connect...

Haaaaaave you met `ssh` command?

![](https://i.imgur.com/vypF2RJ.png)

```sh
ssh aljbari@127.0.0.2 -p 4242

# what would heppend if?
ssh aljbari@127.0.0.2 
```

![](https://c.tenor.com/SjlVZ624hncAAAAC/tenor.gif)

__Warning__: It essential to prevent connecting with ssh to VM using `root` user, you have to configure your machine to completely disable `root` login.

### Disabling Root Login

To do this, open the SSH daemon configuration file with `root` or `sudo` on your VM:

```sh
sudo vim /etc/ssh/sshd_config
```

Inside, search for a directive called `PermitRootLogin`. If it is commented, uncomment it. Change the value to “no”:

```
PermitRootLogin no
```

**Task**: Instead of authenticating with your password, set up a ssh key in you VM and connect using the public and private key  :)

![](https://media.makeameme.org/created/i-dont-know-5b79c0.jpg)

## hostname

[READ: How to change hostname on Linux](https://linuxconfig.org/how-to-change-hostname-on-linux)

`hostname` identify the device on a network.

```sh
# you can see yourhost name using on of those:
hostname
hostnamectl
cat /etc/hostname

# Set the hostname of the computer:
sudo hostnamectl set-hostname "alien-lab"
```


## Passwords policies

### Password expression rules

[READ](https://linuxconfig.org/linux-reset-password-expiration-age-and-history)

`chage`: Change user account and password expiry information.

```sh
# List password information for the user:
chage --list username

# Enable password expiration in 10 days:
sudo chage --maxdays 10 username

# Disable password expiration:
sudo chage --maxdays -1 username

# Set account expiration date:
sudo chage --expiredate YYYY-MM-DD username

# Force user to change password on next log in:
sudo chage --lastday 0 username
```

This above command will change password expiration policy for a particular user, but if you want to set a global policy for all users the file :`/etc/login.defs` is your friend:

```
PASS_MAX_DAYS 30
PASS_MIN_DAYS 2
PASS_WARN_AGE 7
```

- `PASS_MAX_DAYS 30`: Maximum number of days a password can be used before mandatory change (30 days)
- `PASS_MIN_DAYS 2`: Minimum number of days between password changes (prevents frequent changes)
- `PASS_WARN_AGE 7`: Number of days before password expiration that user receives warning (7 days)

## Password rules

![](https://images.hothardware.com/contentimages/newsitem/36056/content/Password_Meme.jpg)

- [READ: pwquality - Linux Manuals](https://www.systutorials.com/docs/linux/man/5-pwquality.conf/)
- [READ: Enforce Password Policies in Linux](https://www.linuxtechi.com/enforce-password-policies-linux-ubuntu-centos/)

To set password rules, you need first a simple program that will made that process easier:

```sh
sudo apt install libpam-pwquality
```

Than change the file `/etc/pam.d/common-password` by adding the required policies.

```
password requisite pam_pwquality.so retry=3 minlen=12 dcredit=-1 ucredit=-1 lcredit=-1 ocredit=-1 dcredit=-1 maxrepeat=3 enforce_for_root
```

`retry=3`:  Prompt three times invalid password before canceling.
`minlen=10`: password must be at least 10 characters long
`dcredit=-1`: It must contain an uppercase letter
`ucredit=-1`: It must contain a lowercase letter
`dcredit=-1`: It must contain a digit
`maxrepeat=3`: it must not contain more than 3 consecutive identical character (for example `111` is not allowed)


## TODO:

- /boot
- /var
- /etc
- /home
- /dev
- /proc
- /sys
- /tmp
- /usr

Networking:

- SSH
- Network protocols
- IP addressing
- DNS
- Ports
- UFW (firewall)

User Management:

- Users and groups
- Sudo privileges
- Password policies
- Authentication

System Administration:

- System logs
- Cron jobs
- System monitoring
- Backup management
- Package management (apt)
- Service management (systemd)

Security:

- SELinux/AppArmor
- SSH key pairs
- SSL/TLS
- Firewall rules
- Directory permissions

Commands & Tools:

- Basic shell commands
- Text editors (vim/nano)
- Monitoring tools (top, htop)
- Disk tools (fdisk, parted)
- Networking tools (netstat, ss)``
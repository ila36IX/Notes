### Sever up time

```bash
w
```

You can also have look at [**run-queue length**](https://www.brendangregg.com/blog/2017-08-08/linux-load-averages.html) (`load average: 0.03, 0.20, 0.42`), which represent what CPU load is. the sum of the number of processes that are currently running plus the number that are waiting (queued) to run.

This means that higher numbers indicate a serious trouble which will wake you up in the middle of the night.

### Last used command

```bash
history
```

### Currently running processes

```bash
top
```

 ### Disk usage
 
```bash
df
df -h
du
```

### Opening ports

```bash
netstat -lpdn | grep mysql
```

### Many cores CPU has

```bash
cat /proc/cpuinfo | grep "model name" | wc -l
```

## Is the software started?

```bash
service NAME_OF_THE_SERVICE status
/etc/init.d/NAME_OF_THE_SERVICE status
```

## Is the software process running?

```bash
pgrep -lf NAME_OF_THE_PROCESS
ps auxf
```


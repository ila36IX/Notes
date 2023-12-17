# Functions
### The `trim` function

Delete white spaces around string.

```mysql
select trim('    test    ');

select trim('*' from '**test**');

select trim(leading '*' from '**test**');

select trim(trailing '*' from '***test***');
```

### The `CURDATE` function
Gives the current date, you can get from it the year, month and day.

```mysql
SELECT CURDATE();
SELECT YEAR(CURDATE());
SELECT MONTH(CURDATE());
SELECT DAY(CURDATE());
```

### The `CURTIME` function
Gives the current time, you can get from it the hour, minute and second.

```mysql
SELECT CURTIME();
SELECT HOUR(CURTIME());
SELECT MINUTE(CURTIME());
SELECT SECOND(CURTIME());
```



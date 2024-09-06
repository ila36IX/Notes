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

### The `NOW` function
Give the current data & time, it has all the previous mentions properties like `YEAR`, `DAY`, `Hour`, `SECOND`...

```mysql
SELECT NOW();
SELECT YEAR(NOW());
SELECT MONTH(NOW());
SELECT DAY(NOW());

SELECT NOW();
SELECT HOUR(NOW());
SELECT MINUTE(NOW());
SELECT SECOND(NOW());
```
### The `LENGTH` function

```mysql
SELECT d, LENGTH(d) FROM table_name;
```

### The  `COALESCE` function
 
```mysql
# if null use the second parm
select id, COALESCE(username, 'unknow') from table_name;
SELECT IFNULL(split, '2022') from your_table;
```

### The `Last_INSERTED_ID` function

```mysql
INSERT INTO users (name) VALUES ("Bob");
SET @user_bob = LAST_INSERT_ID();

INSERT INTO projects (name) VALUES ("Python is cool");
SET @project_py = LAST_INSERT_ID();

INSERT INTO corrections (user_id, project_id, score) VALUES (@user_bob, @project_py, 91);
```

### The `DATE_SUB` function

```mysql
-- Records with last meeting happend more than a month from `currdate`.
SELECT * FROM WHERE last_meeting < DATE_SUB(CURDATE(), INTERVAL 1 MONTH);
```
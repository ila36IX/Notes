# Database Structures

### create database

Remember that database name is an actual director name, so be aware that Unix-like OSs are case-sensitive, but windows is not.

```mysql
CREATE DATABASE lucy;
DROP DATABASE lucy;
```

When creating a new table, every column is created using this syntax:
`name type [DEFAULT value] [NOT NULL | NULL] `

_Default values must follow the data type declaration and come before any `NOT NULL` statement._
## Column Types
### Integer types

`INT_type [(width)] [UNSIGNED] [ZEROFILL]`

| Type	| Storage (Bytes)	| Minimum Value Signed	| Minimum Value Unsigned | Maximum Value Signed	| Maximum Value Unsigned |
| -- | -- | -- | -- | -- | -- |
| TINYINT | 1 |	-128	| 0 |	127	| 255 |
| SMALLINT | 	2	| -32768	 | 0 |	32767 |	65535 |
| MEDIUMINT |	3 |	-8388608 |	0	| 8388607	 | 16777215 |
| INT |	4 |	-2147483648 |	0 | 2147483647	| 4294967295 |
| BIGINT |	8	| -263 |	0	| 2^63-1	| 2^64-1 |

### The problem with FLOAT types

When string value that are approximations of real quantities, you will get an unexpected behavior such as `1/3` is not as the some as `3 * (1 / 3)`, this is kind of a problem, That’s where **DOUBLE** and **FLOAT** are useful : they let you store values such as `2/3` or `pi` with a large number of decimal places, allowing accurate approximate representations of exact quantities. You can later use the `ROUND()` function to restore the results to a given precision.

```mysql
CREATE TABLE wage (monthly DOUBLE);
INSERT INTO wage VALUES (50000/12);
SELECT * FROM wage; -- 4166.666666666
SELECT monthly*12 FROM wage; -- 49999.999999992004
-- as you see, we expect the number 50000, but instead..
-- it is a decimal number which is just close to our original value
SELECT ROUND(monthly*12,5) FROM wage; -- This will fix the problem
SELECT ROUND(monthly*12,8) FROM wage; -- But always use the right amount of precision
```

There is also another option which is using the **DECIMAL** type, `DECIMAL(digit_wide, many_of_theme_that_is_decimal)`.

##### Fixed-point types

DECIMAL(10, 2) This will ensure that the number that stored in database has 2 digits after the decimal point.

For example, a column declared as price `DECIMAL(4,2)` can be used to store values in the range `–99.99` to `99.99`.

### String types

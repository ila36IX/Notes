# MySQL join

![](https://s3.amazonaws.com/alx-intranet.hbtn.io/uploads/medias/2020/3/bc2575fee3303b731031.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOUSBVO6H7D%2F20231217%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20231217T173039Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=3ea0b2116fa244434a3c5c57d0d601e87aa0b295ed3688e3d9fcdf615dfe25d3)

## What is join?

JOIN is a clause used in SQL to link data from one table to another table using one or more data column shared between two tables.

In other words, we combine data of the two existing tables into one. For example, **`table1`** has data about `x` and `y`, **`table2`** has data about `y` and `z`, so we join **`table1`** and **`table2`** to get a **`table3`** with all data of `x`, `y`, and `z`.

## How important is JOIN in SQL?

For storing data, it’s not efficient to put everything into one table as it makes the table become heavier and lower its performance a lot. So it’s better to divide information into many different tables, faster storing, faster retrieving. But every now and then, you will need to select data from multiple tables, that’s where JOIN comes in handy.

```mysql
SELECT cFirstName, cLastName, orderDate
FROM customers 
INNER JOIN orders 
USING (custID);
```

```mysql
SELECT cFirstName, cLastName, orderDate 
FROM customers 
INNER JOIN orders 
ON customers.custID = orders.custID;
```

You can save a bit of typing by specifying an **alias** for each table name (such as `c` and `o` in this example),

```mysql
SELECT cFirstName, cLastName, orderDate 
FROM customers c 
INNER JOIN orders o 
ON c.custID = o.custID;
```

One important effect of all **natural** (join using the columns have the some name in both tables) and **inner** joins is that any unmatched PK value simply drops out of the result. In our example, this means that any customer who didn’t place an order isn’t shown.

Suppose that we want a list of _all_ customers, along with order date(s) for those who did place orders. To include the customers who did **not** place orders, we will use an **outer join**, which may take either the `USING` or the `ON` clause syntax.

```mysql
SELECT cFirstName as F, cLastName as L, orderDate as D
FROM customers c 
LEFT OUTER JOIN orders o 
ON c.custID = o.custID;
```

	All customers and order dates

|F|L|D|
|---|---|---|
|Tom|Jewett|NULL|
|Alvaro|Monge|2003-07-20|  
|Alvaro|Monge|2003-07-18|
|Alvaro|Monge|2003-07-14|
|Wayne|Dick|2003-07-14|

*Notice that for customers who placed no orders, any attributes from the Orders table are simply filled with **NULL** values.*

The word **left** refers to the order of the tables in the FROM clause (customers on the left, orders on the right). The **left** table here is the one that might have unmatched join attributes—the one from which we want _all_ rows. We could have gotten exactly the same results if the table names and outer join direction were reversed:

```mysql
SELECT cFirstName, cLastName, orderDate 
FROM orders o 
RIGHT OUTER JOIN customers c 
ON o.custID = c.custID;
```

#### 7 types of JOINs and how to use them

Check out this [link](https://tableplus.com/blog/2018/09/a-beginners-guide-to-seven-types-of-sql-joins.html)



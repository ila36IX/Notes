# SQL Basics

```mysql
SHOW DATABASES;
USE world;
SHOW CREATE DATABASE world;
SHOW TABLES;
```

Let's find out more about each of the tables that make up the `world_wide` database, to see the statement used to create a database, you can use the **SHOW CREATE DATABASE** statement.

```mysql
SHOW COLUMNS FROM actor;
DESCRIBE actor; -- or DESC actor;
```

### The SELECT Statement

Show all columns of a table:

```mysql
SELECT * FROM table_name;

-- Choosing Columns
SELECT att1, att2, att3+attr2 [AS alies] from table_name;

-- By Database
SELECT attr_name FROM database_name.tables_name;
```

### The WHERE Clause

The `WHERE` clause is a powerful tool that allows you to filter which rows are returned from a SELECT statement. You use it to return rows that match a condition.

```mysql
SELECT * FROM sakila.language WHERE name = 'English';

SELECT city FROM city WHERE city_id < 5;

SELECT city FROM city WHERE name > "b"; -- it's Case insensitivity
 
```

#### The `<>` and `!=` operator:

If you want to find all languages that don’t have a language_id of 2, you’d type:

```mysql
SELECT language_id, name FROM sakila.language
	WHERE language_id <> 2; -- or language_id != 2

SELECT language_id, name FROM sakila.language
	WHERE NOT (language_id = 2);  -- like <> operator
```

	Note that you can use either the <> or != operator for the not-equal condition.

### The LIKE clause

To find matches that begin with a prefix, contain a string, or end in a suffix. For example, we might want to find all album names beginning with the word “Retro.” We can do this with the `LIKE` operator in a `WHERE` clause.

```mysql
SELECT title FROM film WHERE title LIKE '%family%';

-- Using the "or" and "and" operator
SELECT title FROM film_list WHERE 
(category like 'Sci-Fi' OR category LIKE 'Family') 
AND rating LIKE 'PG';
```

`%` : Zero or more characters.  
`_` : Matches a single character.

#### The BETWEEN operator

The `BETWEEN` operator is used to filter the result set based on a specified range of values. It is often used in conjunction with the WHERE clause.

```mysql
SELECT columns 
FROM table 
WHERE column_name BETWEEN value1 AND value2;
```

### The ORDER BY Clause

The ORDER BY clause indicates that sorting is required, followed by the column that should be used as the sort key. It sorting by name in alphabetically **ascending** order—the default sort is case-insensitive and in ascending order, and MySQL automatically sorts alphabetically because the columns are character strings.

```mysql
SELECT name FROM customer_list
	ORDER BY name
	LIMIT 10;
```

we can compound the sorting with two or more columns. in this example it will sort the addresses alphabetically, but grouped by district

```mysql
SELECT address, district FROM address
	ORDER BY district, address;
```
	sort by district and for every address that have the some district will be sorted as well

`DESC` : z, y, m, d, a, 9, 5, 1...
`ASC` : The default will sort in this order: 1, 2, 5, 9 , a, c, d...

```mysql
SELECT address, district FROM address
	ORDER BY district ASC, address DESC
	LIMIT 10;
```

### The LIMIT clause
Its basic form allows you to limit the number of rows returned from a SELECT statement.

**Usage :** `LIMIT start_row, many_rows`

```mysql
SELECT name FROM customer_list LIMIT 5, 5;
```
The output is rows 6 to 10 from the SELECT query.

## Unique value

```mysql
SELECT DISTINCT names FROM db_table; 
```
## Group by

```mysql
SELECT class, AVG(age) FROM db_table GROUP BY class;  
```
#### GROUP_CONCAT

```mysql
SELECT
    places.`name`,
    GROUP_CONCAT(amenities.`name` SEPARATOR ', ') as amenities
FROM
    places
    JOIN place_amenity ON place_amenity.place_id = places.id
    JOIN amenities ON place_amenity.amenity_id = amenities.id
GROUP BY places.`name`;
```
## Just the rows with tv and tub (Many to Many hell)

```mysql
SELECT column_lists FROM table_name WHERE condition  
INTERSECT  
SELECT column_lists FROM table_name WHERE condition;   
```

```mysql
SELECT
    place_id,
    count(amenities.`id`),
    group_concat(amenities.`name` separator ', ') as amenities
FROM
    place_amenity
    JOIN amenities ON place_amenity.amenity_id = amenities.id
WHERE
    place_id in (
        SELECT
            place_id
        FROM
            place_amenity
            JOIN amenities ON place_amenity.amenity_id = amenities.id
        WHERE
            amenities.`name` = 'Tv'
        INTERSECT
        SELECT
            place_id
        FROM
            place_amenity
            JOIN amenities ON place_amenity.amenity_id = amenities.id
        WHERE
            amenities.`name` = 'Hot tub'
    )
group by place_id;
```
## Examples

```mysql 
Select
    distinct places.`name`
from
    places
    JOIN place_amenity ON place_amenity.place_id = places.id
    JOIN amenities ON place_amenity.amenity_id = amenities.id
    JOIN cities ON cities.`id` = places.`city_id`
    JOIN states ON states.`id` = cities.`state_id`
where
    cities.`id` = "660c9bbd-76c4-454f-b9a4-87efab0e948f"
    or states.`id` = "5976f0e7-5c5f-4949-aae0-90d68fd239c0"
    or states.`id` = "541bba6e-9543-4b33-8062-77ef26cd9778"
    and (
        places.`id` in (
            SELECT
                place_id
            FROM
                place_amenity
                JOIN amenities ON place_amenity.amenity_id = amenities.id
            WHERE
                amenities.`name` = 'Tv'
            INTERSECT
            SELECT
                place_id
            FROM
                place_amenity
                JOIN amenities ON place_amenity.amenity_id = amenities.id
            WHERE
                amenities.`name` = 'Hot tub'
        )
    );
```
## Joining Two Tables

![](https://i.imgur.com/xe8IiEb.png)

The statement has two parts: first, two table names separated by the INNER JOIN keywords; and second, the ON keyword that specifies the required columns to compose the condition.

```mysql
SELECT city, country FROM city INNER JOIN country
	ON city.country_id = country.country_id
	WHERE country.country_id < 5
	ORDER BY country, city;
```

If in the join condition the column names in both tables used for matching are the same, you can use the USING clause instead:
- **Instead of :** `ON city.country_id = country.country_id`
- **We can use :** `using (country_id)`

### The INSERT clause

Insert multiple values at once:

```mysql
INSERT INTO language VALUES (NULL, 'Spanish', NOW()),
	(NULL, 'Hebrew', NOW());

-- OR

INSERT INTO actor (actor_id, first_name, last_name, last_update)
	VALUES (NULL, 'Vinicius', 'Grippa', NOW());
```

To make MySQL insert the current right data by default, we can use the some syntax above but without mentioning the column name that has a default value.

```mysql
INSERT INTO city (city, country_id) VALUES ('Bebedouro', 19); -- The time will be inserted auto..
```

Inserting multiple records at once.

```mysql
INSERT INTO city (city,country_id) VALUES
	('Sao Carlos',19),
	('Araraquara',19),
	('Ribeirao Preto',19);
```

Or You may use the `DEFAULT` key word as well:

```mysql
INSERT INTO country VALUES (NULL, 'Uruguay', DEFAULT);
```

## The DELETE Statement
It is possible to delete all rows of a table in a single statement by the this way:

```mysql
DELETE FROM table_name;
```

When you use the `TRUNCATE` TABLE statement, MySQL takes the shortcut of dropping the table, removing the table structures, and then re-creating them. When there are many rows in a table, this is much faster.

```mysql
TRUNCATE TABLE payment;
```

### Using WHERE, ORDER BY, and LIMIT

```mysql
DELETE FROM rental WHERE rental_id < 10;
DELETE FROM rental WHERE id IN (1, 5, 9);
```

## The UPDATE Statement
Using the `UPDATE` statement to change all the rows in a table:

```mysql
UPDATE payment SET amount=amount*1.1;
```

```mysql
UPDATE actor SET last_name= UPPER('cruz')
	WHERE first_name LIKE 'PENELOPE'
	AND last_name LIKE 'GUINESS';
```


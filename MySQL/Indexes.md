> Index is not the solution for any performance issue, but well used, it’s really powerful!


## Syntax

```mysql
ALTER TABLE `table` ADD INDEX `index_name` (`product_id`);
ALTER TABLE people ADD INDEX  `index_name` (`first_name`(5));

SHOW INDEXES FROM people;

ALTER TABLE `table_name` DROP INDEX `index_name`:
```

## Prefix Indexing

By indexing just a part of a string column, you can make the index much smaller and faster. For example, indexing only the first four or five characters of a string reduces the size of the index while potentially maintaining the selectivity.

Prefix indexing is especially suitable for long, evenly distributed, and unique strings, such as UUIDs and hashes.

```mysql
select
	count(distinct first_name) / count(*) as origin, -- 0.0060
	count(distinct LEFT(first_name, 2)) / count(*) as left2, -- 0.00037
	count(distinct LEFT(first_name, 3)) / count(*) as left3, -- 0.0048
	count(distinct LEFT(first_name, 4)) / count(*) as left4, -- 0.0054
	count(distinct LEFT(first_name, 5)) / count(*) as left5, -- 0.0055
```

These results show that as you add more characters to the prefix for indexing, the number of unique values decreases. However, after a certain point, adding more characters provides only a small benefit compared to the extra storage needed.

**Please note that using the prefix index will not help in sorting and group operations!**


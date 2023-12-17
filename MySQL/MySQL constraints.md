# MySQL constraints


| Constraint       | Description                                                                                                           |
|------------------|-----------------------------------------------------------------------------------------------------------------------|
| PRIMARY KEY      | Uniquely identifies each record in a table. Used to enforce the uniqueness of a particular column or a combination.    |
| FOREIGN KEY      | Establishes a link between data in two tables, ensuring referential integrity. The values in this column must exist in the referenced column in another table.|
| UNIQUE           | Ensures that all values in a column are unique. Similar to PRIMARY KEY, but can be used for non-primary key columns.    |
| NOT NULL         | Ensures that a column cannot have a NULL (empty) value.                                                               |
| CHECK            | Specifies a condition that must be satisfied for the values in a column.                                              |
| DEFAULT          | Provides a default value for a column if no value is specified during an INSERT operation.                             |                  |
| ENUM             | String object with a value chosen from a list of permitted values. if the value is not available in the `ENUM` an empty string will be inserted.|
| SET              | A SET can have zero or more values. Each of the values must be chosen from a list of permitted values.|



```mysql
CREATE TABLE Authors(
	Id INTEGER PRIMARY KEY, 
	LastName TEXT NOT NULL,
	FirstName TEXT NOT NULL, 
	City VARCHAR(55)),
	Gender TEXT ENUM ("male", "female", "other"),
	CIN VARCHAR(30) UNIQUE
);

CREATE TABLE Books(
	BookId INTEGER PRIMARY KEY, 
	Title VARCHAR(50),
    AuthorId INTEGER,
    Released INT DEFAULT YEAR(CURDATE()),
    Awards SET('BookBrowse', 'Pulitzer', 'Booker', 'Edgar'), -- In insertion values are separated by commas.                                                                      -- No spaces are allowed.
    FOREIGN KEY(AuthorId)
	    REFERENCES Authors(AuthorId)
);
```

We create the `Books` table. Here we have an `AuthorId` column name, which acts as a foreign key. It references to the primary key of the `Authors` table.
 
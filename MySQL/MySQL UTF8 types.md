

### What he hell is `utf8mb4_0900_ai_ci`

`utf8mb4_0900_ai_ci` refers to a character set and collation in the context of database management systems, particularly MySQL. Let me break down what each part of this expression means:

1. **utf8mb4**: This stands for "UTF-8 Multibyte 4-byte." It's a character encoding capable of representing a wide range of characters.

2. **0900**: This indicates the Unicode version. In this case, it refers to Unicode version 9.0. Unicode is a standardized character encoding that assigns a unique number to every character in the world's writing systems.

3. **ai_ci**: This stands for **accent-insensitive** and **case-insensitive.** It specifies the collation, which determines how string comparison and sorting should be performed. In this case, it implies that the collation is both accent-insensitive (diacritics are treated as the base character) and case-insensitive (uppercase and lowercase letters are considered equivalent).  

```mysql
SELECT "A" COLLATE  utf8mb4_0900_ai_ci = "a"; #True
SELECT "A" COLLATE  utf8mb4_0900_as_cs = "a"; #False - You don't have to use lower() to compare
SELECT "a" COLLATE  utf8mb4_0900_ai_ci = "â"; #True
SELECT "a" COLLATE  utf8mb4_0900_as_cs = "â"; #False
```

### Change schema character set 

```mysql
-- converts hbtn_0c_0 database to UTF8
-- Specifying the database characterset

ALTER DATABASE hbtn_0c_0
CHARACTER SET utf8mb4
COLLATE utf8mb4_unicode_ci;

-- SELECT DATABASE
USE hbtn_0c_0;

-- Specifying the Table characterset
ALTER TABLE first_table
CONVERT TO
CHARACTER SET utf8mb4
COLLATE utf8mb4_unicode_ci;

-- Specifying the Column characterset
ALTER TABLE first_table MODIFY
name VARCHAR(256)
CHARACTER SET utf8mb4
COLLATE utf8mb4_unicode_ci;                           
```

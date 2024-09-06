
> Use the CALL` statement to execute a stored procedure.

## `IN` parameter

IN is the default mode. When defining an ``IN`` parameter in a stored procedure, the calling program must pass an argument to the stored procedure, this argument will be used inside the procedure but changing it will not cause to change it in the outside.

```mysql
DELIMITER //

CREATE PROCEDURE GetOfficeByCountry(
	IN countryName VARCHAR(255)
)
BEGIN
	SELECT * FROM offices
	WHERE country = countryName;
END //

DELIMITER ;
```

## `OUT` parameter

Doesn't have an *init* value, and it must be updated from inside the procedure, the updated value of that variable is available from outside the procedure.

```mysql
SET @test = 'Pizza';

DELIMITER $$

CREATE PROCEDURE test_out_param(OUT value VARCHAR(255))
BEGIN
    SET value = 'apple';
    SELECT * FROM items WHERE name = value;
END $$
DELIMITER $$

CALL test_out_param(@test); -- It will show the output of select
SELECT @test; -- 'apple' // it got changed from inside
```

## `INOUT` parameter

To simple it's *init* value are accessible from inside the procedure and it's updated value from inside the procedure are updated also in the outside.

## Procedure examples


```mysql
CREATE PROCEDURE GetCustomerLevel(
    IN  pCustomerNumber INT, 
    OUT pCustomerLevel  VARCHAR(20))
BEGIN
    DECLARE credit DECIMAL(10,2) DEFAULT 0;

    SELECT creditLimit 
    INTO credit
    FROM customers
    WHERE customerNumber = pCustomerNumber;

    IF credit > 50000 THEN
        SET pCustomerLevel = 'PLATINUM';
    END IF;
END$$

DELIMITER ;
```

```mysql
-- Creates a stored procedure `AddBonus` that adds 
-- a new correction for a student.
DELIMITER $$
CREATE PROCEDURE AddBonus (
    user_id VARCHAR(255),
    project_name VARCHAR(255), 
    score INT)
BEGIN
    DECLARE project_id INT;

    SELECT id INTO project_id FROM projects WHERE name = project_name;
    IF project_id IS NULL THEN
        INSERT INTO projects (name) VALUES (project_name);
        SET project_id = LAST_INSERT_ID();
    END IF;

    INSERT INTO corrections (user_id, project_id, score) VALUES (user_id, project_id, score);
END;$$

DELIMITER ;

```

Decreases the quantity of an item after adding a new order

```mysql
-- Creates a trigger that decreases the quantity of an item after adding a new
-- order.

CREATE TRIGGER on_order BEFORE INSERT ON orders
FOR EACH ROW 
UPDATE items
SET quantity = quantity - NEW.number
WHERE name = NEW.item_name
```

> Updating multiple tables for one action from your application can generate issue: network disconnection, crash, etc… to keep your data in a good shape, let MySQL do it for you!


Creates a trigger that resets the attribute `valid_email` only when the email has been changed.

```mysql
DELIMITER $$
CREATE TRIGGER on_email_updated BEFORE UPDATE ON users
FOR EACH ROW
BEGIN
    IF NEW.email != OLD.email THEN
        SET NEW.valid_email = 0;
    END IF;
END;$$
DELIMITER ;
```

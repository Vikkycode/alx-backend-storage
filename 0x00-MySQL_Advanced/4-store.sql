-- Creates a trigger that decreases the quantity of an item after a new order is added.
-- The trigger is executed after an INSERT operation on the 'orders' table.
-- For each row inserted into 'orders', the corresponding item's quantity is updated in the 'items' table.
DELIMITER //
CREATE TRIGGER decrease_quantity_after_order
AFTER INSERT ON orders
FOR EACH ROW
BEGIN
  -- Decrease the quantity of the item in the 'items' table
  -- by the number of items ordered (from the 'orders' table).
  UPDATE items
  SET quantity = quantity - NEW.number
  WHERE name = NEW.item_name;
END //
DELIMITER ; 

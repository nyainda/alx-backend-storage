-- creates a trigger that decreases the quantity of an item after adding a new order.

-- Quantity in the table items can be negative.

CREATE TRIGGER update_items_after_orders
AFTER INSERT ON orders
FOR EACH ROW UPDATE items
-- NEW has the updated data of table that triggered the trigger.(orders)
SET quantity = quantity - NEW.number
WHERE items.name = NEW.item_name;

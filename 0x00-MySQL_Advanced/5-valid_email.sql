-- Creates a trigger that resets the 'valid_email' attribute to 0 (false) 
-- only when the email address is changed during an UPDATE operation.
DELIMITER //
CREATE TRIGGER reset_valid_email_on_email_change
BEFORE UPDATE ON users
FOR EACH ROW
BEGIN
  -- Check if the old email is different from the new email.
  IF OLD.email != NEW.email THEN
    -- If the email has changed, reset the 'valid_email' attribute.
    SET NEW.valid_email = 0; 
  END IF;
END //
DELIMITER ;

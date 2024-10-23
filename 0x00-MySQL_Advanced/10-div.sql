-- Creates a function SafeDiv that divides two numbers 
-- and returns the result or 0 if the divisor is 0.
DELIMITER //
CREATE FUNCTION SafeDiv(a INT, b INT)
RETURNS DECIMAL(10, 2)
BEGIN
  -- Check if the divisor (b) is 0.
  IF b = 0 THEN
    -- If b is 0, return 0 to avoid division by zero error.
    RETURN 0;
  ELSE
    -- If b is not 0, perform the division and return the result.
    RETURN a / b;
  END IF;
END //
DELIMITER ;

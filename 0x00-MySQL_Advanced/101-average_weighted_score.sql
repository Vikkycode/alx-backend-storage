-- Creates a stored procedure named 'ComputeAverageWeightedScoreForUsers'
-- that computes and stores the average weighted score for all students.
DELIMITER //
CREATE PROCEDURE ComputeAverageWeightedScoreForUsers()
BEGIN
  -- Declare a cursor to iterate through each user.
  DECLARE done INT DEFAULT FALSE;
  DECLARE current_user_id INT;
  DECLARE cur CURSOR FOR SELECT id FROM users;
  DECLARE CONTINUE HANDLER FOR NOT FOUND SET done = TRUE;

  -- Open the cursor.
  OPEN cur;

  -- Loop through each user.
  read_loop: LOOP
    -- Fetch the next user ID.
    FETCH cur INTO current_user_id;

    -- Exit the loop if there are no more users.
    IF done THEN
      LEAVE read_loop;
    END IF;

    -- Calculate and update the average weighted score for the current user.
    CALL ComputeAverageWeightedScoreForUser(current_user_id);
  END LOOP;

  -- Close the cursor.
  CLOSE cur;
END //
DELIMITER ;

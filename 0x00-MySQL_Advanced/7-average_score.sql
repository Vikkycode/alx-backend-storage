-- Creates a stored procedure named 'ComputeAverageScoreForUser' 
-- that computes and stores the average score for a student.
DELIMITER //
CREATE PROCEDURE ComputeAverageScoreForUser(
    IN user_id INT
)
BEGIN
  -- Calculate the average score for the given user.
  -- The result is rounded to 2 decimal places.
  UPDATE users
  SET average_score = (
    SELECT ROUND(AVG(score), 2)
    FROM corrections
    WHERE user_id = user_id -- Match the user_id from the procedure parameter
  )
  WHERE id = user_id; -- Update the average_score for the specified user
END //
DELIMITER ;

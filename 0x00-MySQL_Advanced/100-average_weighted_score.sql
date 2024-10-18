-- Creates a stored procedure named 'ComputeAverageWeightedScoreForUser'
-- that computes and stores the average weighted score for a student.
DELIMITER //
CREATE PROCEDURE ComputeAverageWeightedScoreForUser(
    IN user_id INT
)
BEGIN
  -- Declare variables to store the weighted sum and total weight.
  DECLARE weighted_sum DECIMAL(10, 2) DEFAULT 0;
  DECLARE total_weight INT DEFAULT 0;

  -- Calculate the weighted sum and total weight for the given user.
  SELECT SUM(c.score * p.weight), SUM(p.weight)
  INTO weighted_sum, total_weight
  FROM corrections c
  JOIN projects p ON c.project_id = p.id
  WHERE c.user_id = user_id;

  -- Update the user's average_weighted_score.
  -- If the total weight is 0, the average weighted score is set to 0 to avoid division by zero.
  UPDATE users
  SET average_weighted_score = IF(total_weight > 0, weighted_sum / total_weight, 0)
  WHERE id = user_id;
END //
DELIMITER ;

-- Creates a stored procedure named 'AddBonus' that adds a new correction for a student.
-- If the project name doesn't exist in the 'projects' table, it creates a new project.
DELIMITER //
CREATE PROCEDURE AddBonus (
    IN user_id INT,
    IN project_name VARCHAR(255),
    IN score INT
)
BEGIN
  -- Check if the project exists in the 'projects' table.
  IF NOT EXISTS (SELECT * FROM projects WHERE name = project_name) THEN
    -- If the project doesn't exist, insert it into the 'projects' table.
    INSERT INTO projects (name) VALUES (project_name);
  END IF;

  -- Insert the new correction into the 'corrections' table.
  INSERT INTO corrections (user_id, project_id, score)
  VALUES (user_id, (SELECT id FROM projects WHERE name = project_name), score);
END //
DELIMITER ;

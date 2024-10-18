-- Creates a view named 'need_meeting' that lists students 
-- who have a score below 80 and haven't had a meeting recently.
CREATE VIEW need_meeting AS
SELECT name
FROM students
WHERE score < 80 
  AND (last_meeting IS NULL OR last_meeting < DATE_SUB(CURDATE(), INTERVAL 1 MONTH));

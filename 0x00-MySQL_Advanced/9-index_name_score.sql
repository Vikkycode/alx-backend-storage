-- Creates an index named 'idx_name_first_score' on the 'names' table.
-- This index includes the first character of the 'name' column and the 'score' column.
CREATE INDEX idx_name_first_score ON names (name(1), score);

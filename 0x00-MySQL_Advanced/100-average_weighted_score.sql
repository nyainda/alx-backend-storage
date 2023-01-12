-- creates a stored procedure ComputeAverageWeightedScoreForUser
-- that computes and store the average weighted score for a student.

DELIMITER $$

CREATE PROCEDURE ComputeAverageWeightedScoreForUser(user_id INT)
  BEGIN
    DECLARE computed_average_weighted_score FLOAT;
    SET computed_average_weighted_score = (SELECT (SUM(weight * score)/ SUM(weight)) FROM corrections INNER JOIN projects ON projects.id = corrections.project_id WHERE corrections.user_id = user_id );
    UPDATE users SET average_score = computed_average_weighted_score WHERE users.id = user_id;
  END;
$$
DELIMITER ;


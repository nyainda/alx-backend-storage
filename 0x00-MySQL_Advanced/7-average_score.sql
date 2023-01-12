-- creates a stored procedure ComputeAverageScoreForUser that
-- computes and store the average score for a student.

DELIMITER $$

DROP PROCEDURE IF EXISTS ComputeAverageScoreForUser;
CREATE PROCEDURE ComputeAverageScoreForUser(user_id INT)
  BEGIN
    DECLARE computed_average_score FLOAT;
    SET computed_average_score = (SELECT AVG(score) FROM corrections WHERE corrections.user_id = user_id);
    UPDATE users SET average_score = computed_average_score WHERE users.id = user_id;
  END;
$$
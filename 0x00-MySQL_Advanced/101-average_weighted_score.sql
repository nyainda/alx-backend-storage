-- creates a stored procedure ComputeAverageWeightedScoreForUsers

-- that computes	and store the average weighted score for all students.

DELIMITER ||

DROP PROCEDURE IF EXISTS ComputeAverageWeightedScoreForUsers;

CREATE PROCEDURE ComputeAverageWeightedScoreForUsers()
BEGIN
	DROP VIEW IF EXISTS averages_view;
	CREATE VIEW averages_view AS
		SELECT
		    corr.user_id, (
		        SUM(corr.score * pro.weight) / SUM(pro.weight)
		    ) as result
		FROM corrections AS corr
		    JOIN projects AS pro ON pro.id = corr.project_id
		GROUP BY corr.user_id;
	UPDATE users
	SET average_score = (
	        SELECT result
	        FROM averages_view
	        WHERE
	            users.id = user_id
	    );
	DROP VIEW IF EXISTS averages_view;
END||
DELIMITER ;
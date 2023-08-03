"""
SELECT student_id, AVG(grade) AS average
FROM grades
GROUP BY student_id
ORDER BY average DESC
LIMIT 5
"""
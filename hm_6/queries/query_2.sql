"""
SELECT student_id, discipline_id, AVG(grade) AS average
FROM grades
WHERE discipline_id=1
GROUP BY discipline_id, student_id
ORDER BY average DESC
LIMIT 1
"""
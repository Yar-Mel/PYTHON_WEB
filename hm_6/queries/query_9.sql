"""
SELECT students.fullname as student, disciplines.discipline
FROM grades
INNER JOIN students ON grades.student_id  = students.id
INNER JOIN disciplines ON grades.discipline_id  = disciplines.id
GROUP BY student_id, discipline_id
"""
"""
SELECT students.fullname as student, groups.name as [group], disciplines.discipline, grade
FROM grades
INNER JOIN students ON grades.student_id = students.id
INNER JOIN disciplines ON grades.discipline_id = disciplines.id
INNER JOIN groups ON students.group_id = groups.id
WHERE group_id = 1
ORDER BY date_of DESC
LIMIT 1
"""
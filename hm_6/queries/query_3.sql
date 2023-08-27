"""
SELECT groups.name as [group], disciplines.discipline, AVG(grade) AS average
FROM students
INNER JOIN grades ON students.id = grades.student_id
INNER JOIN disciplines ON grades.discipline_id = disciplines.id
INNER JOIN groups ON students.group_id = groups.id
GROUP BY [group], discipline
"""
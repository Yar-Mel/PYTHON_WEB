"""
SELECT teachers.fullname as teacher, disciplines.discipline, AVG(grade) as average
FROM disciplines
INNER JOIN teachers ON disciplines.teacher_id = teachers.id
INNER JOIN grades ON grades.discipline_id  = disciplines.id
GROUP BY teacher_id
"""
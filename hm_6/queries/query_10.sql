"""
SELECT disciplines.discipline, students.fullname as student, teachers.fullname as teacher
FROM disciplines, students
INNER JOIN teachers ON disciplines.teacher_id = teachers.id
GROUP BY disciplines.discipline, students.fullname, teachers.fullname
"""
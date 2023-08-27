"""
SELECT students.fullname as student, teachers.fullname as teacher, discipline, AVG(grade) AS average
FROM grades
INNER JOIN students ON students.id = grades.student_id
INNER JOIN disciplines ON disciplines.id = grades.discipline_id
INNER JOIN teachers ON teachers.id = disciplines.teacher_id
WHERE student_id = 1
GROUP BY student_id, teacher_id
"""
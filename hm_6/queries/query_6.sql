"""
SELECT groups.name as groups, students.fullname as students FROM students
INNER JOIN groups ON students.group_id = groups.id
ORDER by groups.name
"""
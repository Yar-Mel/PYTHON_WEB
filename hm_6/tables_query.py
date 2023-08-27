
teachers = """
    CREATE TABLE teachers (
    id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    fullname STRING );
"""

groups = """
    CREATE TABLE [groups] (
    id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    name STRING UNIQUE );
"""

students = """
    CREATE TABLE students (
    id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    fullname STRING,
    group_id REFERENCES [groups] (id) );
"""

disciplines = """
    CREATE TABLE disciplines (
    id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    discipline STRING,
    teacher_id REFERENCES teachers (id) );
"""

grades = """
    CREATE TABLE grades (
    id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    student_id REFERENCES students (id),
    discipline_id REFERENCES disciplines (id),
    grade INTEGER,
    date_of DATE );
"""

DROP_QUERIES = [
    "DROP TABLE IF EXISTS teachers;",
    "DROP TABLE IF EXISTS [groups];",
    "DROP TABLE IF EXISTS students;",
    "DROP TABLE IF EXISTS disciplines;",
    "DROP TABLE IF EXISTS grades;",
]

CREATE_QUERIES = [teachers, students, groups, disciplines, grades]

from faker import Faker
from random import randint
from random import choice

# SETTINGS
NUMBER_OF_TEACHERS = 5
NUMBER_OF_STUDENTS = 10
NUMBER_OF_GRADES = 2
DISCIPLINES = [
    "Biology",
    "Chemistry",
    "Computer Science",
    "Mathematics",
    "Physics"
]
GROUPS = [
    "Group_1",
    "Group_2",
    "Group_3"
]

fake = Faker()


def add_teachers(cursor):
    query = "INSERT INTO teachers (fullname) VALUES (?);"
    for _ in range(NUMBER_OF_TEACHERS):
        cursor.execute(query, (fake.name(),))


def add_students(cursor):
    query = "INSERT INTO students (fullname, group_id) VALUES (?, ?);"
    for _ in range(NUMBER_OF_STUDENTS):
        cursor.execute(query, (fake.name(), randint(1, len(GROUPS))))


def add_groups(cursor):
    query = "INSERT INTO [groups] (name) VALUES (?);"
    for group in GROUPS:
        cursor.execute(query, (group,))


def add_disciplines(cursor):
    query = "INSERT INTO disciplines (discipline, teacher_id) VALUES (?, ?);"
    for discipline in DISCIPLINES:
        cursor.execute(query, (discipline, randint(1, NUMBER_OF_TEACHERS)))


def add_grades(cursor):
    query = "INSERT INTO grades (student_id, discipline_id, grade, date_of) VALUES (?, ?, ?, ?);"
    for student_id in range(1, NUMBER_OF_STUDENTS+1):
        for discipline_id in range(1, len(DISCIPLINES)+1):
            for _ in range(NUMBER_OF_GRADES):
                cursor.execute(query, (
                    student_id,
                    discipline_id,
                    randint(60, 100),
                    fake.date()
                )
                               )


def seeds(connection):
    cursor = connection.cursor()
    add_teachers(cursor)
    add_groups(cursor)
    add_students(cursor)
    add_disciplines(cursor)
    add_grades(cursor)

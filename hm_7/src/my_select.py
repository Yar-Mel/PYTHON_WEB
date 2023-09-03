from sqlalchemy import func, desc

from src.models import Teacher, Student, Discipline, Grade, Group
from src.db import session


def select_1():
    result = (session.query(
        Student.fullname, func.round(func.avg(Grade.grade), 2).label('avg_grade')
        )
        .select_from(Grade)
        .join(Student)
        .group_by(Student.id)
        .order_by(desc('avg_grade'))
        .limit(5)
        .all()
    )
    return result


def select_2(discipline_id):
    result = (
        session.query(
            Student.fullname, func.round(func.avg(Grade.grade), 2).label("avg_grade")
        )
        .join(Grade, Student.id == Grade.student_id)
        .filter(Grade.discipline_id == discipline_id)
        .group_by(Student.id)
        .order_by(desc("avg_grade"))
        .limit(1)
        .first()
    )
    return result


def select_3(discipline_id):
    result = (
        session.query(
            Group.name, func.round(func.avg(Grade.grade), 2).label("avg_grade")
        )
        .join(Grade, Group.id == Grade.student_id)
        .filter(Grade.discipline_id == discipline_id)
        .group_by(Group.name)
        .all()
    )
    return result


def select_4():
    result = (
        session.query(
            func.round(func.avg(Grade.grade), 2).label("avg_grade")
        )
        .scalar()
    )
    return result


def select_5(teacher_id):
    result = (session.query(
            Discipline.name
        )
        .filter(Discipline.teacher_id == teacher_id)
        .all()
    )
    return result


def select_6(group_id):
    result = (
        session.query(
            func.concat(Student.fullname.label("fullname"))
        )
        .join(Group, Student.group_id == Group.id)
        .filter(Group.id == group_id)
        .all()
    )
    return result


def select_7(group_id, discipline_id):
    result = (
        session.query(
            Student.fullname, Grade.grade
        )
        .join(Grade, Student.id == Grade.student_id)
        .filter(Student.group_id == group_id, Grade.discipline_id == discipline_id)
        .all()
    )
    return result


def select_8(teacher_id):
    result = (
        session.query(
            func.round(func.avg(Grade.grade), 2).label("avg_grade")
        )
        .join(Discipline, Grade.discipline_id == Discipline.id)
        .filter(Discipline.teacher_id == teacher_id)
        .scalar()
    )
    return result


def select_9(student_id):
    result = (
        session.query(
            Discipline.name
        )
        .join(Grade, Discipline.id == Grade.discipline_id)
        .filter(Grade.student_id == student_id)
        .distinct()
        .all()
    )
    return result


def select_10(student_id, teacher_id):
    result = (
        session.query(
            Discipline.name
        )
        .join(Grade, Discipline.id == Grade.discipline_id)
        .join(Teacher, Discipline.teacher_id == Teacher.id)
        .filter(Grade.student_id == student_id, Teacher.id == teacher_id)
        .distinct()
        .all()
    )
    return result

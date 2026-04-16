from datetime import date

from business.school import School
from models.course import Course
from models.student import Student
from models.teacher import Teacher


def test_add_course_should_add_a_course():
    school = School()
    course = Course(
        name="Physique",
        start_date=date(2025, 9, 1),
        end_date=date(2026, 6, 30)
    )
    school.add_course(course)
    assert course in school.courses


def test_add_teacher_should_add_a_teacher():
    school = School()
    teacher = Teacher(
        first_name="Sophie",
        last_name="Turner",
        age=42,
        hiring_date=date(2025, 9, 1)
    )
    school.add_teacher(teacher)
    assert teacher in school.teachers


def test_add_student_should_add_a_student():
    school = School()
    student = Student("Rémi", "Campistron", 43)

    school.add_student(student)
    assert student in school.students


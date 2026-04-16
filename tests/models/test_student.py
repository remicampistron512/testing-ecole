from datetime import date

from models.course import Course
from models.student import Student


def test_student_number_should_increment():
    Student.students_nb = 0
    student = Student("Rémi","Campistron",43)
    assert student.student_nbr == 1


def test_course_should_be_added_to_courses_taken():
    student = Student("Rémi", "Campistron", 43)
    course = Course(
        name="Physique",
        start_date=date(2025, 9, 1),
        end_date=date(2026, 6, 30)
    )
    student.add_course(course)
    assert len(student.courses_taken) == 1


def test_student_should_be_added_to_student_taking_it():
    student = Student("Rémi", "Campistron", 43)
    course = Course(
        name="Physique",
        start_date=date(2025, 9, 1),
        end_date=date(2026, 6, 30)
    )
    student.add_course(course)
    assert student in course.students_taking_it
from datetime import date

from models.course import Course
from models.teacher import Teacher


def test_hiring_date_should_be_stored_properly():
    teacher = Teacher (
        first_name="Sophie",
        last_name="Turner",
        age=42,
        hiring_date=date(2025, 9, 1)
    )
    assert teacher.hiring_date == date(2025, 9, 1)


def test_teacher_should_be_added_to_course():
    teacher = Teacher(
        first_name="Sophie",
        last_name="Turner",
        age=42,
        hiring_date=date(2025, 9, 1)
    )
    course = Course(
        name="Théatre",
        start_date=date(2025, 9, 1),
        end_date=date(2026, 6, 30)
    )

    teacher.add_course(course)
    assert course.teacher == teacher
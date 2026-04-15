from datetime import date

from models.course import Course


class FakeTeacher:
    def __init__(self, name="Mme Dupont"):
        self.name = name
        self.courses_teached = []

    def __str__(self):
        return self.name


def test_str_output_without_teacher():
    course = Course(
        name="Physique",
        start_date=date(2025, 9, 1),
        end_date=date(2026, 6, 30)
    )
    expected = "Physique (2025-09-01 – 2026-06-30),\npas d'enseignant affecté"

    assert str(course) == expected


def test_str_output_with_teacher():
    course = Course(
        name="Maths",
        start_date=date(2025, 9, 1),
        end_date=date(2026, 6, 30)
    )
    teacher = FakeTeacher("Mme Dupont")
    course.set_teacher(teacher)

    expected = "Maths (2025-09-01 – 2026-06-30),\nenseigné par Mme Dupont"

    assert str(course) == expected


def test_course_creation():
    course = Course(
        name="Maths",
        start_date=date(2025, 9, 1),
        end_date=date(2026, 6, 30)
    )
    assert course.name == "Maths"
    assert course.start_date == date(2025, 9, 1)
    assert course.end_date == date(2026, 6, 30)
    assert course.teacher is None
    assert course.students_taking_it == []

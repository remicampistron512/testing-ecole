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
        name = "Physique",
        start_date = date(2025, 9, 1),
        end_date = date(2026, 6, 30)
    )
    expected = "Physique (2025-09-01 – 2026-06-30),\npas d'enseignant affecté"

    assert str(course) == expected


from datetime import date

from business.school import School
from models.course import Course


def test_add_course_should_add_a_course():
    school = School()
    course = Course(
        name="Physique",
        start_date=date(2025, 9, 1),
        end_date=date(2026, 6, 30)
    )
    school.add_course(course)
    assert course in school.courses

from datetime import date

from models.teacher import Teacher


def test_hiring_date_should_be_stored_properly():
    teacher = Teacher (
        first_name="Sophie",
        last_name="Turner",
        age=42,
        hiring_date=date(2025, 9, 1)
    )
    assert teacher.hiring_date == date(2025, 9, 1)

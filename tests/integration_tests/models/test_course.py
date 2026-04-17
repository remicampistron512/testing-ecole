from datetime import date

from models.course import Course
from models.student import Student


class FakeTeacher:
    def __init__(self, name="Mme Dupont"):
        self.name = name
        self.courses_teached = []

    def __str__(self):
        return self.name


class FakeStudent:
    def __init__(self, name="Alice"):
        self.name = name
        self.courses_taken = ["Physique"]

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


def test_adding_same_teacher_should_not_duplicate_course():
    course = Course(
        name="Maths",
        start_date=date(2025, 9, 1),
        end_date=date(2026, 6, 30)
    )
    teacher = FakeTeacher("Mme Dupont")
    course.set_teacher(teacher)
    course.set_teacher(teacher)
    assert course.teacher == teacher
    assert teacher.courses_teached.count(course) == 1


def test_add_student_should_add_student_to_course_and_course_to_student():
    course = Course(
        name="Maths",
        start_date=date(2025, 9, 1),
        end_date=date(2026, 6, 30)
    )
    student = FakeStudent("Alice")

    course.add_student(student)

    assert len(course.students_taking_it) == 1
    assert student in course.students_taking_it
    assert course in student.courses_taken


def test_adding_another_teacher_should_remove_course_from_taught_courses():
    course = Course(
        name="Maths",
        start_date=date(2025, 9, 1),
        end_date=date(2026, 6, 30)
    )

    teacher = FakeTeacher("Mme Dupont")
    teacher2 = FakeTeacher("Mr Dupuis")
    course.set_teacher(teacher)
    course.set_teacher(teacher2)

    assert len(teacher.courses_teached) == 0
    assert len(teacher2.courses_teached) == 1


def test_add_student(mocker):
    course = Course(
        name="chimie",
        start_date=date(2025, 9, 1),
        end_date=date(2026, 6, 30)
    )

    student = Student(
        first_name="Rémi",
        last_name="Campistron",
        age=43
    )

    # Mock de la liste des cours enseignés par l'enseignant pour isoler le test
    mocker.patch.object(student, 'courses_taken', [])

    course.add_student(student)

    assert student in course.students_taking_it
    assert course in student.courses_taken


def test_add_student_with_mocker(mocker):
    course = Course(
        name="chimie",
        start_date=date(2025, 9, 1),
        end_date=date(2026, 6, 30)
    )

    student = Student(
        first_name="Rémi",
        last_name="Campistron",
        age=43
    )

    mock_list = mocker.patch.object(student, 'courses_taken', autospec=True)
    course.add_student(student)
    assert student in course.students_taking_it

    mock_list.append.assert_called_once_with(course)


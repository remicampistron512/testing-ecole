from models.student import Student


def test_student_number_should_increment():
    Student.students_nb = 0
    student = Student("Rémi","Campistron",43)
    assert student.student_nbr == 1
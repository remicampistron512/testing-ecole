from unittest.mock import patch

from business.school import School


def test_init_static_should_initialize_expected_numbers():
    school = School()

    with patch.object(school, "add_student") as mock_add_student, \
            patch.object(school, "add_course") as mock_add_course, \
            patch.object(school, "add_teacher") as mock_add_teacher:
        school.init_static()

    assert mock_add_student.call_count == 3
    assert mock_add_course.call_count == 9
    assert mock_add_teacher.call_count == 6

from models.person import Person


def test_person_output_for_str_without_address():
    first_name = "Rémi"
    last_name ="Campistron"
    age = 43
    sut = Person(first_name,last_name,age)
    assert sut.__str__() == "Rémi Campistron (43 ans)"


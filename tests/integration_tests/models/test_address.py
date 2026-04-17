from models.address import Address


def test_should_output_same_string():

    street = "78,rue du Treuilh"
    city = "Tartas"
    postal_code = 40400
    sut = Address(street,city,postal_code)
    expected_output = "78,rue du Treuilh, 40400 Tartas"
    assert sut.__str__() == expected_output


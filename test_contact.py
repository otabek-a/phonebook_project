from contact import Contact

contact = Contact('Zarif','Naxalov','+998 93 123 45 67')

def test_contact():
    assert contact.first_name == 'Zarif'
    assert contact.last_name == 'Naxalov'
    assert contact.phone_number == '+998 93 123 45 67'
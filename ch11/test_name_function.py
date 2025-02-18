from name_function import get_formatted_name

def test_first_last_name():
    formatted_name = get_formatted_name('janis','joplin')
    assert formatted_name == 'Janis Joplin'

def test_first_middle_last_name():
    formated_name = get_formatted_name('wofgang','mozart','amadeus')
    assert formated_name == 'Wofgang Amadeus Mozart'
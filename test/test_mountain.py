"""Test Mountain module"""


from lib.mountain import Mountain


def test_first_valid_example():
    given_string = "/\\"
    assert Mountain(given_string).is_valid()


def test_second_valid_example():
    given_string = '//\\\\//\\\\'
    assert Mountain(given_string).is_valid()


def test_third_valid_example():
    given_string = '////\\\\\\/////\\\\\\\\\\\\'
    assert Mountain(given_string).is_valid()


def test_first_invalid_example():
    given_string = '//\\'
    assert Mountain(given_string).is_valid() == False


def test_second_invalid_example():
    given_string = '\\///\\\\'
    assert Mountain(given_string).is_valid() == False


def test_third_invalid_example():
    given_string = '///\\\\\\\\/'
    assert Mountain(given_string).is_valid() == False


"""Search indexes by slash"""


def test_search_indexes_by_slash():
    given_data = '///\\\\\\'
    expected_result = { 'begin_index': 2, 'end_index': 3 }
    result = Mountain(given_data).search_indexes('slash')
    assert result == expected_result


def test_search_indexes_by_brackets():
    given_data = '\\/'
    expected_result = { 'begin_index': 0, 'end_index': 0 }
    result = Mountain(given_data).search_indexes('slash')
    assert result == expected_result

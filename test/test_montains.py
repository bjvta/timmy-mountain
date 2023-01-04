"""Test Montains module"""

from lib.mountains import counter_of_slashes, delete_both_slashes, is_valid_montain, search_up_down_indexes


def test_first_valid_example():
    given_string = "/\\"
    assert is_valid_montain(given_string)


def test_second_valid_example():
    given_string = '//\\\\//\\\\'
    assert is_valid_montain(given_string)


def test_third_valid_example():
    given_string = '////\\\\\\/////\\\\\\\\\\\\'
    assert is_valid_montain(given_string)


def test_first_invalid_example():
    given_string = '//\\'
    assert is_valid_montain(given_string) == False


def test_second_invalid_example():
    given_string = '\\///\\\\'
    assert is_valid_montain(given_string) == False


def test_third_invalid_example():
    given_string = '///\\\\\\\\/'
    assert is_valid_montain(given_string) == False



"""
Counter of slashes
"""

def test_counter_slashes():
    given_data = "///\\\\"
    expected_result = 3
    result = counter_of_slashes('/', given_data)
    assert result == expected_result


def test_counter_backslashes():
    given_data = "///\\\\"
    expected_result = 2
    result = counter_of_slashes('\\', given_data)
    assert result == expected_result


def test_search_indexes_success():
    given_data = '///\\\\\\'
    expected_result = { 'up_index': 2, 'down_index': 3 }
    result = search_up_down_indexes(given_data)
    assert result == expected_result


def test_search_indexes_invalid():
    given_data = '\\/'
    expected_result = { 'up_index': 0, 'down_index': 0 }
    result = search_up_down_indexes(given_data)
    assert result == expected_result


"""
Delete the string
"""

def test_delete_both():
    given_data = '//\\\\'
    up_index = 1
    expected_result = '/\\'
    result = delete_both_slashes(given_data, up_index)
    assert result == expected_result


def test_delete_both_single_top():
    given_data = '/\\'
    up_index = 0
    expected_result = ''
    result = delete_both_slashes(given_data, up_index)
    assert result == expected_result

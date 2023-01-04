"""Test Tunnels module"""

from lib.tunnels import is_valid_tunnel, has_valid_brackets, search_entrance_exit_index


def test_first_valid_example():
    given_data = '/>//\\\\<\\'
    assert is_valid_tunnel(given_data)


def test_second_valid_example():
    given_data = '//>/\\<\\/>/>/\\<\\<\\\\'
    assert is_valid_tunnel(given_data)


def test_first_invalid_example():
    given_data = '/>//\\\\\\\\'
    assert is_valid_tunnel(given_data) == False


def test_second_invalid_example():
    given_data = '///\\<\\/>/>/\\\\\\<\\\\'
    assert is_valid_tunnel(given_data) == False


"""
brackets counter
"""

def test_valid_brackets_one():
    given_data = '/>//\\\\<\\'
    assert has_valid_brackets(given_data)


def test_valid_brackets_two():
    given_data = '//>/\\<\\/>/>/\\<\\<\\\\'
    assert has_valid_brackets(given_data)


def test_invalid_brackets_one():
    given_data = '/>//\\\\\\\\'
    assert has_valid_brackets(given_data) == False


def test_invalid_brackets_two():
    given_data = '///\\<\\/>/>/\\\\\\<\\\\'
    assert has_valid_brackets(given_data) == False


"""search entrance and exit char index"""


def test_search_entrance_exit_index():
    given_data = '/><\\'
    expected_result = { 'entrance_index': 1, 'exit_index': 2 }
    result = search_entrance_exit_index(given_data)
    assert result == expected_result

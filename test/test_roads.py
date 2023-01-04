"""Test Roads module"""


from lib.roads import changes_to_become_valid_mountain


def test_roads_example_one():
    given_data = '//\\'
    expected_result = 1
    result = changes_to_become_valid_mountain(given_data)
    assert result == expected_result


def test_roads_example_two():
    given_data = '\\///\\\\'
    expected_result = 2
    result = changes_to_become_valid_mountain(given_data)
    assert result == expected_result


def test_roads_example_three():
    given_data = '///\\\\\\\\/'
    expected_result = 2
    result = changes_to_become_valid_mountain(given_data)
    assert result == expected_result


def test_roads_example_four():
    given_data = '///\\\\\\\\/'
    expected_result = 2
    result = changes_to_become_valid_mountain(given_data)
    assert result == expected_result


def test_roads_example_five():
    given_data = '//\\\\\\\\/'
    expected_result = 3
    result = changes_to_become_valid_mountain(given_data)
    assert result == expected_result


def test_roads_example_six():
    given_data = '//\\\\\\\\//'
    expected_result = 4
    result = changes_to_become_valid_mountain(given_data)
    assert result == expected_result

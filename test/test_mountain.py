"""Test Mountain module"""


from lib.mountain import Mountain, Tunnel


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


""" Tunnel """

def test_first_valid_example_tunnel():
    given_data = '/>//\\\\<\\'
    assert Tunnel(given_data).is_valid()


def test_second_valid_example_tunnel():
    given_data = '//>/\\<\\/>/>/\\<\\<\\\\'
    assert Tunnel(given_data).is_valid()


def test_first_invalid_example_tunnel():
    given_data = '/>//\\\\\\\\'
    assert Tunnel(given_data).is_valid() == False


def test_second_invalid_example_tunnel():
    given_data = '///\\<\\/>/>/\\\\\\<\\\\'
    assert Tunnel(given_data).is_valid() == False



""" Roads  """


def test_roads_example_one():
    given_data = '//\\'
    expected_result = 1
    result = Mountain(given_data).changes_to_become_valid_mountain()
    assert result == expected_result


def test_roads_example_two():
    given_data = '\\///\\\\'
    expected_result = 2
    result = Mountain(given_data).changes_to_become_valid_mountain()
    assert result == expected_result


def test_roads_example_three():
    given_data = '///\\\\\\\\/'
    expected_result = 2
    result = Mountain(given_data).changes_to_become_valid_mountain()
    assert result == expected_result


def test_roads_example_four():
    given_data = '///\\\\\\\\/'
    expected_result = 2
    result = Mountain(given_data).changes_to_become_valid_mountain()
    assert result == expected_result


def test_roads_example_five():
    given_data = '//\\\\\\\\/'
    expected_result = 3
    result = Mountain(given_data).changes_to_become_valid_mountain()
    assert result == expected_result


def test_roads_example_six():
    given_data = '//\\\\\\\\//'
    expected_result = 4
    result = Mountain(given_data).changes_to_become_valid_mountain()
    assert result == expected_result

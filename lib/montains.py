"""Montains Module"""


def is_valid_montain(data):
    slashes_length = counter_of_slashes('/', data)
    backslashes_length = counter_of_slashes('\\', data)
    if slashes_length != backslashes_length:
        return False

    while len(data) >= 1:
        indexes = search_up_down_indexes(data)
        up_index = indexes['up_index']
        down_index = indexes['down_index']
        if up_index == down_index:
            return False

        if data[up_index] == '/' and data[down_index] == '\\':
            data = delete_both_slashes(data, up_index)

    return True


def counter_of_slashes(slash, data):
    counter = 0
    for character in data:
        if character == slash:
            counter += 1

    return counter


def search_up_down_indexes(data):
    i = 0
    while i < len(data) - 1:
        if data[i] == '/' and data[i + 1] == '\\':
            return { 'up_index': i, 'down_index': i + 1 }
        i += 1
    return { 'up_index': 0, 'down_index': 0 }


def delete_both_slashes(data, up_index):
    data = data[0:up_index:] + data[up_index + 2: :]
    return data

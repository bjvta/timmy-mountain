"""Tunnels module"""

from .mountains import counter_of_slashes, search_up_down_indexes, delete_both_slashes


def is_valid_tunnel(data):
    slashes_length = counter_of_slashes('/', data)
    backslashes_length = counter_of_slashes('\\', data)
    if slashes_length != backslashes_length or not has_valid_brackets(data):
        return False

    while len(data) >= 1:
        indexes = search_up_down_indexes(data)
        up_index = indexes['up_index']
        down_index = indexes['down_index']
        if up_index == down_index:
            entrance_index = search_entrance_exit_index(data)['entrance_index']
            exit_index = search_entrance_exit_index(data)['exit_index']
            if entrance_index == exit_index:
                return False
            else:
                up_index = entrance_index
                down_index = exit_index

        if data[up_index] == '/' and data[down_index] == '\\' or (data[up_index] == '>' and data[down_index] == '<'):
            data = delete_both_slashes(data, up_index)
    return True



def has_valid_brackets(data):
    entrance_char_amount = 0
    exit_char_amount = 0
    for char in data:
        if char == '>':
            entrance_char_amount += 1
        if char == '<':
            if entrance_char_amount == 0:
                return False
            exit_char_amount += 1
    return entrance_char_amount == exit_char_amount


def search_entrance_exit_index(data):
    i = 0
    while i < len(data) - 1:
        if data[i] == '>' and data[i + 1] == '<':
            return { 'entrance_index': i, 'exit_index': i + 1 }
        i += 1
    return { 'entrance_index': 0, 'exit_index': 0 }


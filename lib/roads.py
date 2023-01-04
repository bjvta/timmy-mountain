"""Roads module"""


from lib.mountains import delete_both_slashes, is_valid_montain, search_up_down_indexes


def changes_to_become_valid_mountain(data):
    if is_valid_montain(data):
        return 0

    while len(data) > 0:
        indexes = search_up_down_indexes(data)
        up_index = indexes['up_index']
        down_index = indexes['down_index']

        if up_index == down_index:
            return len(data)
        if data[up_index] == '/' and data[down_index] == '\\':
            data = delete_both_slashes(data, up_index)

    return len(data)

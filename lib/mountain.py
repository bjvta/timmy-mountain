"""Mountain Class Module"""


from exceptions.invalid_exception import InvalidData, ValidData
from lib.mountains import counter_of_slashes


class Mountain:
    def __init__(self, data):
        self.data = data

    def is_valid(self):
        try:
            self.valid_the_counter_slashes()
            self.iterate_data()
            return True

        except InvalidData:
            return False


    def search_indexes(self, type):
        begin = '>'
        end = '<'
        if type == 'slash':
            begin = '/'
            end = '\\'
        i = 0
        while i < len(self.data) - 1:
            if self.data[i] == begin and self.data[i + 1] == end:
                return { 'begin_index': i, 'end_index': i + 1 }
            i += 1
        return { 'begin_index': 0, 'end_index': 0 }

    def iterate_data(self):
        while len(self.data) >= 1:
            indexes = self.search_indexes('slash')
            up_index = indexes['begin_index']
            down_index = indexes['end_index']
            if up_index == down_index:
                raise InvalidData
            if self.data[up_index] == '/' and self.data[down_index] == '\\':
                self.data = self.delete_two_char_at_index(up_index)

    def delete_two_char_at_index(self, index):
        self.data = self.data[0:index:] + self.data[index + 2: :]
        return self.data

    def valid_the_counter_slashes(self):
        slashes_length = counter_of_slashes('/', self.data)
        backslashes_length = counter_of_slashes('\\', self.data)
        if slashes_length != backslashes_length:
            raise InvalidData

    def changes_to_become_valid_mountain(self):
        if self.is_valid():
            return 0

        while len(self.data) > 0:
            indexes = self.search_indexes('slash')
            up_index = indexes['begin_index']
            down_index = indexes['end_index']

            if up_index == down_index:
                return len(self.data)
            if self.data[up_index] == '/' and self.data[down_index] == '\\':
                self.data = self.delete_two_char_at_index(up_index)

        return len(self.data)


class Tunnel(Mountain):

    def iterate_data(self):
        while len(self.data) >= 1:
            indexes = self.search_indexes('slash')
            up_index = indexes['begin_index']
            down_index = indexes['end_index']
            if up_index == down_index:
                entrance_indexes = self.search_indexes('brackets')
                entrance_index = entrance_indexes['begin_index']
                exit_index = entrance_indexes['end_index']
                if entrance_index == exit_index:
                    raise InvalidData
                else:
                    up_index = entrance_index
                    down_index = exit_index
            if self.data[up_index] == '/' and self.data[down_index] == '\\' or \
                 (self.data[up_index] == '>' and self.data[down_index] == '<'):
                self.data = self.delete_two_char_at_index(up_index)

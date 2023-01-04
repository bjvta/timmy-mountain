"""Mountain Class Module"""


from exceptions.invalid_exception import InvalidData
from lib.mountains import counter_of_slashes


class Mountain:
    def __init__(self, data):
        self.data = data

    def is_valid(self):
        try:
            self.valid_the_counter_slashes()
            while len(self.data) >= 1:
                indexes = self.search_indexes('slash')
                up_index = indexes['begin_index']
                down_index = indexes['end_index']
                if up_index == down_index:
                    return False
                if self.data[up_index] == '/' and self.data[down_index] == '\\':
                    self.data = self.delete_two_char_at_index(up_index)
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

    def delete_two_char_at_index(self, index):
        self.data = self.data[0:index:] + self.data[index + 2: :]
        return self.data

    def valid_the_counter_slashes(self):
        slashes_length = counter_of_slashes('/', self.data)
        backslashes_length = counter_of_slashes('\\', self.data)
        if slashes_length != backslashes_length:
            raise InvalidData

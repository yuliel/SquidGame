from CharMask import CharMask


class CodeMask:

    def __init__(self, code):
        self.__code_mask = {}
        for x, i in zip(code, range(len(code))):
            if x not in self.__code_mask.keys():
                self.__code_mask[x] = CharMask(len(code))
            self.__code_mask.get(x).add_char(i)

    def __str__(self):
        return f"code mask: {str(self.__code_mask)}"

    def is_bull(self, key, location):
        try:
            return self.__code_mask.get(key).is_char_in_position(location)
        except AttributeError:
            return False

    def is_cow(self, key, compared_code):
        try:
            self_chars_to_handle = self.__code_mask.get(key).get_chars_num_to_handle()
            compared_chars_to_handle = compared_code.get_chars_num_to_handle(key)

            if self_chars_to_handle < compared_chars_to_handle:
                self.__code_mask.get(key).decrease_skip_balance()
                return False
            elif self_chars_to_handle > compared_chars_to_handle:
                self.__code_mask.get(key).increase_skip_balance()
                return True
            else:
                return True
        except AttributeError:
            return False

    def get_chars_num_to_handle(self, key):
        try:
            return self.__code_mask.get(key).get_chars_num_to_handle()
        except AttributeError:
            return 0

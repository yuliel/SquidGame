class CharMask:

    def __init__(self, number_of_digits):
        self.__flags = [False for n in range(number_of_digits)]
        self.__count = 0
        self.__skip_balance = 0

    def __str__(self):
        return f"bitmask = {str(self.__flags)}, count = {self.__count} , skipped = {self.__skip_balance} "

    def add_char(self, position):
        self.__flags[position] = True
        self.__count += 1

    def is_char_in_position(self, position):
        return self.__flags[position]

    def get_chars_num_to_handle(self):
        return self.__count - self.__skip_balance

    def increase_skip_balance(self):
        self.__skip_balance += 1

    def decrease_skip_balance(self):
        self.__skip_balance -= 1

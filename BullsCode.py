"""
THIS CLASS HANDLES OPERATIONS ON THE NUMERIC CODE WHICH IS THE BASIS FO THE BULLS AND COWS GAME
"""
from consts import BULL, COW
from random import randint
from CodeMask import CodeMask


class BullsCode:
    def __init__(self, secret_code=None, number_of_digits=4):
        if secret_code is None:  # set a random code
            self.__secret_code = list(str(randint(0, pow(10, number_of_digits))).zfill(number_of_digits))
        else:                    # get a code in constructor
            self.__secret_code = list(secret_code)
        self.__code_mask = CodeMask(self.__secret_code)  # set the mask for optimization in future comparisons

    def __str__(self):
        #        return f"code: {self.__secret_code}, mask:{str(self.__code_mask)}"
        return f"code: {self.__secret_code}"

    def __char_exists(self, key):
        return self.__code_mask.char_exists(key)

    def __is_bull(self, key, location):
        return self.__code_mask.is_bull(key, location)

    def __is_cow(self, key, compared_code):
        return self.__code_mask.should_handle_cow(key, compared_code)

    def get_code(self):
        return self.__secret_code

    def get_chars_num_to_handle(self, key):
        return self.__code_mask.get_chars_num_to_handle(key)

    def check(self, compared_code):
        result = []
        location = 0
        for x in compared_code.get_code():                        # for each character in secret code
            if self.__char_exists(x):                             #  check if character appears also in our code
                if self.__is_bull(x, location):                          #    check if this is a bull
                    result += BULL                                #       if it is a bull handle it
                elif self.__is_cow(x, compared_code):  #    then check if this should be handled as a cow or skip
                    result += COW                                 #       if it is a cow handle it
            location += 1

        return sorted(result)


if __name__ == "__main__":

    assert BullsCode("1234").check(BullsCode("1234")) == ['B', 'B', 'B', 'B']

    assert BullsCode("1254").check(BullsCode("1234")) == ['B', 'B', 'B']
    assert BullsCode("1234").check(BullsCode("1254")) == ['B', 'B', 'B']

    assert BullsCode("8555").check(BullsCode("1550")) == ['B', 'B']
    assert BullsCode("1550").check(BullsCode("8555")) == ['B', 'B']

    assert BullsCode("5558").check(BullsCode("1550")) == ['B', 'B']
    assert BullsCode("1550").check(BullsCode("5558")) == ['B', 'B']

    assert BullsCode("5555").check(BullsCode("1550")) == ['B', 'B']
    assert BullsCode("1550").check(BullsCode("5555")) == ['B', 'B']

    assert BullsCode("1550").check(BullsCode("3852")) == ['B']
    assert BullsCode("3852").check(BullsCode("1550")) == ['B']

    assert BullsCode("9080").check(BullsCode("1550")) == ['B']
    assert BullsCode("1550").check(BullsCode("9080")) == ['B']

    assert BullsCode("9008").check(BullsCode("1550")) == ['C']
    assert BullsCode("1550").check(BullsCode("9008")) == ['C']

    assert BullsCode("9245").check(BullsCode("1550")) == ['C']
    assert BullsCode("1550").check(BullsCode("9245")) == ['C']

    assert BullsCode("0089").check(BullsCode("1500")) == ['C', 'C']
    assert BullsCode("1500").check(BullsCode("0089")) == ['C', 'C']

    assert BullsCode("0849").check(BullsCode("4900")) == ['C', 'C', 'C']
    assert BullsCode("4900").check(BullsCode("0849")) == ['C', 'C', 'C']

    assert BullsCode("5005").check(BullsCode("1550")) == ['C', 'C', 'C']
    assert BullsCode("1550").check(BullsCode("5005")) == ['C', 'C', 'C']

    assert BullsCode("5678").check(BullsCode("8765")) == ['C', 'C', 'C', 'C']

    assert BullsCode("1550").check(BullsCode("3585")) == ['B', 'C']
    assert BullsCode("3585").check(BullsCode("1550")) == ['B', 'C']

    assert BullsCode("5587").check(BullsCode("1550")) == ['B', 'C']
    assert BullsCode("1550").check(BullsCode("5587")) == ['B', 'C']

    assert BullsCode("2777").check(BullsCode("7722")) == ['B', 'C', 'C']
    assert BullsCode("7722").check(BullsCode("2777")) == ['B', 'C', 'C']

    assert BullsCode("2787").check(BullsCode("7780")) == ['B', 'B', 'C']
    assert BullsCode("7780").check(BullsCode("2787")) == ['B', 'B', 'C']

    assert BullsCode("2787").check(BullsCode("7782")) == ['B', 'B', 'C', 'C']
    assert BullsCode("7782").check(BullsCode("2787")) == ['B', 'B', 'C', 'C']

    assert BullsCode("7340").check(BullsCode("2777")) == ['C']
    assert BullsCode("2777").check(BullsCode("7340")) == ['C']

    assert BullsCode("127770").check(BullsCode("773409")) == ['C', 'C', 'C']
    assert BullsCode("3454323").check(BullsCode("9834570")) == ['B', 'C', 'C']


    code = BullsCode("1550")
    print("secret = ", code)
    for x in range(15):
        curr_guess = BullsCode()
        print(f"guess {x} = {curr_guess}. result = {curr_guess.check(code)}.")

import string


class NonAlphabetItem(Exception):
    def __init__(self, letter: str):
        self.letter = letter
        super().__init__(f'Non-alphabet letter found: {self.letter}')


class InvalidLetterType(Exception):
    def __init__(self, letter: str, type_: type):
        self.letter = letter
        self.type = type_
        super().__init__(f'Must use str: {self.letter} ({self.type.__name__}) is invalid')


# ------------------------------------------------------------------------------------------------------

lowercase = string.ascii_lowercase
uppercase = string.ascii_uppercase
letters = string.ascii_letters


def get_letter_index(letter: str):
    if type(letter) != str:
        raise InvalidLetterType(letter, type(letter))

    if letter not in letters:
        raise NonAlphabetItem(letter)

    index = lowercase.index(letter) if letter in lowercase else uppercase.index(letter)

    return index + 1


def letter_index_map(letter_list: list):
    new_list = list(map(get_letter_index, letter_list))

    return new_list


if __name__ == '__main__':
    try:
        print(letter_index_map(['a', 'Z', 'C', 'e']))
        print(letter_index_map([3, 'blah', 'C', 'e']))

    except (NonAlphabetItem, InvalidLetterType) as e:
        print(e)

    try:
        print(letter_index_map(['a', 'blah', 'C', 'e']))

    except (NonAlphabetItem, InvalidLetterType) as e:
        print(e)

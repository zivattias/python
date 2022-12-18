import string


class InvalidInput(Exception):
    def __init__(self):
        super().__init__('Wrong input for letter, use alphabet letters only.')


class AlphabetIterator:

    def __init__(self, start: str):
        if not start.isalpha():
            raise InvalidInput()
        self.start = start

        self.lower_alphabet = list(string.ascii_lowercase)
        self.upper_alphabet = list(string.ascii_uppercase)

    def __iter__(self):
        self.char = self.start
        return self

    def __next__(self):
        if self.char == self.lower_alphabet[-1] or self.char == self.upper_alphabet[-1]:
            raise StopIteration()

        if self.char in self.lower_alphabet:
            index = self.lower_alphabet.index(self.char)
            case = self.lower_alphabet
        else:
            index = self.upper_alphabet.index(self.char)
            case = self.upper_alphabet

        self.char = case[index + 1]

        return self.char


while True:
    try:
        character = input('Enter a letter to start from: ')
        for char in AlphabetIterator(character):
            print(char)
        print('Finished')

    except InvalidInput as e:
        print(e)

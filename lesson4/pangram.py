import string
alphabet: list = list(string.ascii_lowercase)


def is_pangram(s: str) -> bool:
    return tuple(alphabet) <= tuple(s.lower())


s_: str = input('Type: ')
print(is_pangram(s_))


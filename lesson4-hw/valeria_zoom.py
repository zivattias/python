import string
alphabet: list = list(string.ascii_lowercase)


def is_pangram(s: str) -> bool:
    for i in alphabet:
        if i not in s:
            return False
    return True

s_: str = input('Type: ').lower()
print(is_pangram(s_))
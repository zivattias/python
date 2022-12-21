# Write a regular expression to look for 3 digits, possibly separated by whitespace.
import re


def three_digits(string: str):
    pattern = '\d\s\d\s\d'
    search = re.search(pattern, string)
    if search is None:
        pattern = '\d\d\d'
        return re.search(pattern, string)
    return search


if __name__ == '__main__':
    print(three_digits('ANANAS3 3 3BYE'))
    print(three_digits('LOL333LOL'))
    print(three_digits('LOLOL'))

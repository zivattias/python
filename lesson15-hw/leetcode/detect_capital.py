from re import match


def detect_capital(string: str):
    if match('^([A-Z]*)+$', string) or \
        match('^([a-z]*)+$', string) or \
        match('^[A-Z]([a-z]*)+$', string):
        return True
    return False


# ^ matches the start of the string.
# ([A-Z]*) matches zero or more uppercase letters.
# + requires one or more matches of the preceding pattern (in this case, [A-Z]*).
# $ matches the end of the string.


if __name__ == '__main__':
    strings = ['USA', 'leetcode', 'FlaG', 'Israel', 'FLag']
    for string in strings:
        print(detect_capital(string))

# Given a word, check whether it's a Capitalized word (starts from upper case, the second char is a lower case)

import re

def check_capped(word: str):
    match = re.match('[A-Z][a-z]', word)
    if match is not None:
        return True
    return False

if __name__ == '__main__':
    print(check_capped('Hello'))
    print(check_capped('wOrld'))
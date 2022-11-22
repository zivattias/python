# Write a Python function that receives a string as a parameter
# and calculates the number of upper case letters and lowercase letters.
# (The function should return 2 numbers in a tuple)

s1: str = "Ziv Attias"

def count_type_letters(s: str) -> tuple:
    low: int = 0
    up: int = 0
    for letter in s:
        if letter.isupper():
            up += 1
        elif letter.islower():
            low += 1
        else:
            pass
    return low, up

print(count_type_letters(s1))
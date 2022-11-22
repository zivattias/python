# Write a Python function to check whether a string is a pangram or not. Pangrams are words or
# sentences containing every letter of the alphabet at least once.
# For example : "The quick brown fox jumps over the lazy dog"

import string
alphabet = list(string.ascii_lowercase)  # a > z, list

def is_pangram(s: str) -> bool:
    s = s.lower()
    is_p = True
    for letter in alphabet:
        if letter not in s:
            is_p = False
            break
    return is_p

print(is_pangram('The quick brown fox jumps over the lazy dog'))


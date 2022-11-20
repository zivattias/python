import string
alphabet: list = list(string.ascii_lowercase)
# # # Write a function that receives the string as a parameter and return the string in reverse order.
#
#
# def reverse_order(n: str) -> str:
#     return n[-1::-1]
#
#
# print(reverse_order(input('Enter a string to reverse: ')))
#
# # # Write a Python function to check whether a number falls in a given range.
# # # (The function receives number and range (from/to) as parameters and returns True/False)
#
#
# def is_in_range(num: int, start: int, to: int) -> bool:
#     return num in range(start, to)
#
#
# num1: int = int(input('Enter a number: '))
# range_start: int = int(input('Enter a starting point: '))
# range_end: int = int(input('Enter an end point: '))
#
# print(is_in_range(num1, range_start, range_end))
#
# # # Write a Python function that receives a string as a parameter
# # # and calculates the number of upper case letters and lowercase letters. (The function should return 2 numbers)
# # lowercase: str = "abcdefghijklmnopqrstuvwxyz"
# # uppercase: str = lowercase.upper()
#
#
# def letter_calc(string: str) -> tuple:
#     total_l: int = 0
#     total_u: int = 0
#     for char in string:
#         if char.islower():
#             total_l += 1
#         else:  # spaces included
#             # if char.isupper():
#             if char.isspace():
#                 pass
#             else:
#                 total_u += 1
#     return total_l, total_u
#
#
# string1: str = input('Enter a sentence: ')
# print(letter_calc(string1))
# #
# # # Write a Python function to check whether a string is a pangram or not.
# # # Pangrams are words or sentences containing every letter of the alphabet at least once.
# # # For example : "The quick brown fox jumps over the lazy dog"
#
#
#
# def is_pangram(sentence: str) -> bool:
#     for char in sentence:
#         return char in alphabet
#
#
# pangram: str = input('Enter a sentence to check if pangram: ').strip().lower()
# print(is_pangram(pangram))

def ispangram(sentence: str):
    abc: list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
                 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    for i in abc:
        while i not in sentence:
            return False
            exit
    else:
        return True
print(ispangram("abcdefghijklmnopqrstuvwxyzg"))
# Implement a function that filters out vowels from the given string and returns the original string without the vowels.
# Vowels are the following letters (both lowercase and uppercase): a, e,  i, o, u
# Use filter() to filter vowels from a given word (string)


vowels = ['a', 'e', 'i', 'o', 'u']

# def is_vowel(char: str) -> bool:
#     if char.lower() not in vowels:
#         return True
#     return False

if __name__ == '__main__':

    while True:
        string = input('Enter a string: ')
        print(''.join(filter(lambda c: c.lower() not in vowels, string)))

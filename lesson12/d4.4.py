# Implement a function that receives a list of strings,
# and returns a new list of strings with all the original strings sorted by the string length.

strings_list = [
    'hello',
    'world',
    'beautiful',
    'hi',
    'a'
]

print(sorted(strings_list, key=len))
print(sorted(strings_list, key=lambda s: len(s)))


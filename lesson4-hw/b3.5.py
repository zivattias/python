# Write a Python function that checks whether a passed string is palindrome or not.

s1: str = 'Step on no pets'

def is_palindrome(s: str) -> bool:
    return s[::].lower() == s[::-1].lower()

print(is_palindrome(s1))
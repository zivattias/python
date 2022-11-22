# Write a function that receives the string as a parameter and return the string in reverse order.

s1: str = 'Hello World'

def reversed_string(s: str) -> str:
    return s[::-1]

print(reversed_string(s1))

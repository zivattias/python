# Write a Python function that prints out the first n rows of Pascal's triangle.

# Print Pascal's Triangle in Python
from math import factorial

def pascal_n(n: int):
    for i in range(n):
        for j in range(n - i + 1):
            # for left spacing
            print(end=" ")
        for j in range(i + 1):
            # nCr = n!/((n-r)!*r!)
            print(factorial(i) // (factorial(j) * factorial(i - j)), end=" ")
        # for new line
        print()

n1 = int(input('Enter number of rows: '))
pascal_n(n1)

# Write a Python function to calculate the factorial of a number (a non-negative integer).
# Arguments types: int
# Return value type: int
num1 = 7

def factorial_calc(num: int) -> int:
    factorial = 1
    if num < 0:
        print("Sorry, a factorial for negative numbers doesn't exist.")
    elif num == 0:
        return factorial
    elif num > 0:
        for i in range(1, num + 1):
            factorial *= i
        return factorial

print(factorial_calc(num1))
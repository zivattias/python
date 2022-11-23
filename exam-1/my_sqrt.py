# Implement a function my_sqrt that receives a non-negative integer x,
# and returns the square root of x rounded down to the nearest integer.
# The returned integer should be non-negative as well.
# You must not use any built-in exponent function or operator like x ** 0.5 or math.sqrt()  in python.

# Example 1:
# Input: x = 4
#
# Output: 2
#
# Explanation: The square root of 4 is 2, so we return 2.

# Example 2:
# Input: x = 8
#
# Output: 2
#
# Explanation: The square root of 8 is 2.82842..., and since we round it down to the nearest integer, 2 is returned.

# def sqrt(n: int) -> int:
#     sq = int()

def sqrt(n: [int]) -> [int | float]:
    sq = int()

    for y in range(0, n + 1):
        if n // y == y:
            sq = y
        # elif n // y == y - 1:
        #     sq = y - 1

    return sq

_n = int(input('Enter a number: '))
print(sqrt(_n))

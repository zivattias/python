# Write a Python function to check whether a number is perfect or not.

num = 496

def is_perfect(n: int) -> bool:
    factors_sum: int = 0
    for k in range(1, n):
        if n % k == 0:
            factors_sum += k
    if factors_sum == n:
        return True
    else:
        return False

print(is_perfect(num))
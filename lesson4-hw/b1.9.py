# Write a Python function that takes a number as a parameter and checks if the number is prime or not.
# A prime number (or a prime) is a natural number greater than 1 and
# that has no positive divisors other than 1 and itself.

num: int = 43

def is_prime(n: int) -> bool:
    prime_ind = None
    if n == 2:
        prime_ind = True
    for k in range(2, n):
        if n % k != 0:
            prime_ind = True
        else:
            prime_ind = False
            break
    return prime_ind

print(is_prime(num))
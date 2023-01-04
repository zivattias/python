from functools import lru_cache
import math

@lru_cache
def get_factorial(num: int):
    return math.factorial(num)


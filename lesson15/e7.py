# Implement a python program that gets from the user a list of big numbers, and counts the factorial of these numbers.
# You should perform the calculations as fast as possible and print the results to the user in a friendly manner
# immediately when the result is ready. Hint: Use multiprocessing with ProcessPoolExecutor + callbacks.
#
# For example, if the user inserts the following:
#
# 7465917345693745, 3434534534, 232323, 33334444445455, 7777777, 888888
#
# You should print something like:
#
# 7465917345693745! = …
# 3434534534! = …
# …
#
# Total time took: ….
import math
import time
from concurrent.futures import ProcessPoolExecutor, as_completed, ThreadPoolExecutor


def calc_fact(num: int):
    fact = 1
    for i in range(1, num + 1):
        fact = fact * i
    return (num, fact)

def print_result(f):
    print(f"{f.result()[0]}! = {f.result()[1]}")

# def display_nums(nums: list):
#     with ProcessPoolExecutor(max_workers=5) as executor:
#         facts = [executor.submit(calc_fact, num) for num in nums]
#         for fact in facts:
#             fact.add_done_callback(print_result)


if __name__ == '__main__':
    start = time.perf_counter()
    nums = [1550] * 100000
    with ProcessPoolExecutor() as executor:
        results = [executor.submit(calc_fact, num) for num in nums]
        # for result in results:
        #     result.add_done_callback(print_result)
    end = time.perf_counter()
    print(f"Runtime: {(end-start):.2f} seconds")


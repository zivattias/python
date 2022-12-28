# Write a program that receives a number of seconds from a user and
# counts down this amount of seconds in resolution of 0.1 second by printing the amount of time left.
# For example, if the user inserts 3, your program should constantly print:
# 3 seconds left
# 2.9 seconds left
# 2.8 seconds left
# 2.7 seconds left
# ….
# 0.1 seconds left
# DONE!
import time
from concurrent.futures import ThreadPoolExecutor
import requests
from requests import RequestException


def count_down(num: int):
    n = 0
    counter = 0
    with ThreadPoolExecutor() as executor:
        while n <= num:
            print(f"{(num - n):.1f} seconds left")
            time.sleep(0.1)
            n += 0.1
            counter += 1
            if counter % 10 == 0:
                executor.submit(print(get_quote()))
    print('Done')


def get_quote():
    response = requests.get('https://api.kanye.rest')
    if response.status_code < 400:
        return response.json()['quote']
    raise RequestException()

start = time.perf_counter()
count_down(3)
print(f"Runtime: {(time.perf_counter() - start):.2f} seconds")

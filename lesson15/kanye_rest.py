import requests
from requests.exceptions import *
from concurrent.futures import ThreadPoolExecutor, Future, as_completed, ProcessPoolExecutor

URL = 'https://api.kanye.rest'


def get_quote(num):
    response = requests.get(URL)
    if response.status_code < 400:
        print(f"Getting quote {num}")
        return {'id': num, 'quote': response.json()['quote']}
    raise RequestException()


def display_quote(f: Future):
    if f.exception():
        print(f'Could not get quote for ID: {f.result()["id"]}')
    elif f.done():
        print(f'The quote number {f.result()["id"]} is: "{f.result()["quote"]}"')


# def display_quote(ret_val: dict):
#     print(f'The quote number {ret_val["id"]} is: "{ret_val["quote"]}"')


with ThreadPoolExecutor() as executor:
    futures = [executor.submit(get_quote, i) for i in range(1, 100)]

    # Perform display_quote for future, according to submission que:
    for future in futures:
        future.add_done_callback(display_quote)

# As soon as a future completes, perform display_quote(future):
#     for future in as_completed(futures):
#         display_quote(future)

# for i in range(1, 100):
#     ret_val = get_quote(i)
#     display_quote(ret_val)

import requests
from concurrent.futures import ThreadPoolExecutor, as_completed


with ThreadPoolExecutor(max_workers=16) as executor:
    while True:
        executor.submit(requests.get, 'https://min-api.cryptocompare.com/stats/rate/limit')

import base64
import os
from concurrent.futures import ThreadPoolExecutor

import requests


class HTTPError(Exception):
    def __init__(self):
        super().__init__("HTTP Error!")


URLS = [
    'https://edulabs.co.il/',
    'https://www.google.com/'
]

url_ids = [base64.urlsafe_b64encode(f"{URL}".encode()).decode().strip("=") for URL in URLS]


def retrieve_domain_analysis(uri: str):
    response = requests.get(f'https://www.virustotal.com/api/v3/urls/{uri}',
                            headers={'x-apikey': os.environ["VT_KEY"]})
    if response.status_code == 200 or response.status_code == 201:
        return response.json()
    # if response.status_code == 404:
    #     requests.post(f'https://www.virustotal.com/api/v3/urls/{uri}',
    #                   headers={
    #                       'accept': 'application/json',
    #                       'content-type': 'application/x-www-form-urlencoded',
    #                       'x-apikey': os.environ["VT_KEY"],
    #                   },
    #                   data=f'url={uri}')
    raise HTTPError()


def get_domain_reputation(json_resp: dict):
    stats = json_resp['data']['attributes']['last_analysis_stats']
    total_values_sum = sum(stats.values())
    max_val = max(stats.values())
    max_key = list(stats.keys())[list(stats.values()).index(max_val)]
    ratio = max_val / total_values_sum
    return max_key, ratio


if __name__ == '__main__':
    with ThreadPoolExecutor() as executor:
        submissions = [(i, executor.submit(retrieve_domain_analysis, uri)) for i, uri in enumerate(url_ids)]
        for submission in submissions:
            print(f"{URLS[submission[0]]}: {get_domain_reputation(submission[1].result())}")

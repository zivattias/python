# WIP
import base64
import os
import requests
import datetime
from concurrent.futures import ThreadPoolExecutor
from consts import *
from exceptions import *
from threading import Lock
from functools import lru_cache


class VTAnalyzer:
    """
    VirusTotal API responses:

    URL analysis:
    1. 404 for a never-scanned URL
    2. 200 for a scanned URL, returns an analysis dict:
    Result stats - ["data"]["attributes"]["last_analysis_stats"] (dict['harmless', 'malicious', 'suspicious', 'undetected'])
    Last submission date - ["data"]["attributes"]["last_submission_date"] (epoch timestamp)

    URL scan:
    1. 400 for an invalid URL - "Unable to canonicalize url"
    2. 200 for success, returns dict["data"] = {"type": "analysis, "id": str}

    Additional argument option:
    --quota / -q for verbose waiting if the user ran out of VT's available quota
    """

    def __init__(self):
        # Cache maps URL Base64 strings to a respective (last_analysis_time, (result, ratio)) nested tuple
        self._cache: dict[str: tuple[str, tuple[str, float]]] = dict()
        self._cache_age = 180
        # A uniformed Lock() for threaded actions, e.g. accessing cache and executing actions on it
        self._lock = Lock()
        # Environmental API key variable
        self._token = os.environ["VT_KEY"]

    def check_cache(self, epoch: str) -> bool | datetime.date:
        # Check cache (convert epoch to date) and validate last analysis time
        # returns a datetime.date object
        pass

    @staticmethod
    def url_encoder(url: str):
        return base64.urlsafe_b64encode(f"{url}".encode()).decode().strip("=")

    @staticmethod
    def perform_scan_url(url: str) -> bool:
        data = f"url={url}"
        headers = {
            "accept": "application/json",
            "x-apikey": os.environ["VT_KEY"],
            "content-type": "application/x-www-form-urlencoded"
        }
        response = requests.post(SCAN_URL, data=data, headers=headers)
        if response.status_code == 200:
            return True
        raise BadRequest(request=response, status_code=response.status_code)

    def get_urls_reputation(self, urls: list) -> list[str]:
        return [self._get_reputation_for_single_uri(url) for url in urls]

    def _get_reputation_for_single_uri(self, url: str):
        if url in self._cache and \
            datetime.date.today() - self.check_cache(self._cache[url][0]) <= datetime.timedelta(days=self._cache_age):
            return self._cache[url][1]

        response = requests.get(ANALYSIS_URL + self.url_encoder(url),
                                headers={'x-apikey': os.environ["VT_KEY"]})

        if response.status_code == 404:
            self.perform_scan_url(url)



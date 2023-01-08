# WIP
import base64
import os
import argparse
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
    """

    def __init__(self):
        # Cache maps URL Base64 strings to a respective (last_analysis_time, (result, ratio)) nested tuple
        self._cache: dict[str: tuple[str, tuple[str, float]]] = dict()
        # A uniformed Lock() for threaded actions, e.g. accessing cache and executing actions on it
        self._lock = Lock()
        # Argparse utilization
        self._parser = argparse.ArgumentParser(prog="URL Reputation Check, Powered by VirusTotal's API",
                                               description="The program allows you to check URL(s)",
                                               epilog="By Ziv Attias")
        self._parser.add_argument('url', help='URL to scan')
        self._parser.add_argument('-k', '--apikey')
        self._parser.add_argument('-s', '--scan', action='store_true')
        # Environmental API key variable
        self._token = os.environ["VT_KEY"]

    def check_cache(self, epoch: str) -> bool:
        # Check cache and validate last analysis time
        pass

    @staticmethod
    def url_encoder(url: str):
        return base64.urlsafe_b64encode(f"{url}".encode()).decode().strip("=")

    @staticmethod
    def perform_scan_url(url: str) -> bool:
        data = f"url={url}"
        headers = {
            "accept": "application/json",
            "x-apikey": "d0a6e2b1f6c04e78f9225b3ead707a06ad672101ff55858f5a13ed07085fbf81",
            "content-type": "application/x-www-form-urlencoded"
        }
        response = requests.post(SCAN_URL, data=data, headers=headers)
        if response.status_code == 200:
            return True
        raise BadRequest(request=response, status_code=response.status_code)

    def get_urls_reputation(self, urls: list) -> dict[str, bool]:
        # Get reputation for multiple URLs
        pass

    def _get_reputation_for_single_uri(self, uri: str):
        if uri in self._cache and self.check_cache(self._cache[uri][0]):
            pass
        response = requests.get(ANALYSIS_URL + uri,
                                headers={'x-apikey': os.environ["VT_KEY"]})
        if response.status_code == 404:
            # scan
            pass

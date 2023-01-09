import os
import json
import base64
import requests
import argparse
from consts import *
from exceptions import *
from threading import Lock
from datetime import datetime, timedelta
from concurrent.futures import ThreadPoolExecutor


class VTAnalyzer:
    """
    VTAnalyzer is a Class-based Python program that allows user-friendly interaction with through the command line
    Provided with URL(s), it will return a reputation-wired result whether the URL you specify is
    MALICIOUS or HARMLESS.

    --apikey / -k (followed by <APIKEY_STRING>) - use a designated API key
    --scan / -s (bool variable) - perform a force-scan for the URL prior to accessing its results
    --quota / -q (bool variable) - verbose waiting in case of insufficient API quota

    VirusTotal API responses:

    URL analysis:
    1. 404 for a never-scanned URL
    2. 200 for a scanned URL, returns an analysis dict:
    Result stats - ["data"]["attributes"]["last_analysis_stats"] (dict['harmless', 'malicious', 'suspicious', 'undetected'])
    Last analysis date - ["data"]["attributes"]["last_analysis_date"] (epoch timestamp)

    URL scan:
    1. 400 for an invalid URL - "Unable to canonicalize url"
    2. 200 for success, returns dict["data"] = {"type": "analysis, "id": str}
    """

    def __init__(self):
        # Cache maps URL strings to a respective (last_analysis_date, (result, ratio)) nested tuple
        mode = 'w' if not os.path.exists('cache.json') else 'r'
        with open('cache.json', mode=mode) as f:
            self._cache: dict[int: tuple[str, tuple[str, float]]] = json.load(f)
        # Uniformed Lock() for threaded actions, e.g. accessing cache and executing actions on it
        self._lock = Lock()
        # Argparse initialization
        self._parser = argparse.ArgumentParser(prog="URL Reputation Check, Powered by VirusTotal's API",
                                               description="The program allows you to check URL(s)",
                                               epilog="By Ziv Attias")
        self._parser.add_argument('-u', '--url', nargs='*',
                                  help='followed by one or more URLs, separated by a whitespace')
        self._parser.add_argument('-k', '--apikey',
                                  help='followed by custom VT API key')
        self._parser.add_argument('-s', '--scan', action='store_true',
                                  help='force URL scan')
        self._parser.add_argument('-q', '--quota', action='store_true',
                                  help='verbose wait in case of quota insufficiency')
        self._parser.add_argument('-v', '--verbose', action='store_true',
                                  help='verbose prints throughout the process')
        self._parser.add_argument('-a', '--age', default=182,
                                  help='declare cache max age (days), default = 182')
        self._args = self._parser.parse_args()
        # API key init
        if self._args.apikey:
            self._token = self._args.apikey
        else:
            self._token = os.environ["VT_KEY"]
        # Cache age
        self._cache_age = self._args.age

    @staticmethod
    def encode_url(url: str):
        """
        Encodes URL string to Base64
        :param url: str
        :return url: base64
        """
        return base64.urlsafe_b64encode(f"{url}".encode()).decode().strip("=")

    def check_cache(self, epoch: int) -> bool:
        """
        Check cached content age
        :param epoch: str
        :return bool: if today's date - last analysis date <= self._cache_age
        """
        datetime_epoch = datetime.utcfromtimestamp(epoch)

        if self._args.verbose:
            print(f"Last analysis date: {datetime_epoch.date()}")

        return True if datetime.utcnow() - datetime_epoch <= timedelta(days=self._cache_age) else False

    def scan_url(self, url: str) -> bool:
        """
        Scans URL using VirusTotal API
        :param url: URL string
        :return bool: if scan succeeded
        :raise BadRequest(): scan failed
        """
        data = f"url={url}"
        headers = {
            "accept": "application/json",
            "x-apikey": self._token,
            "content-type": "application/x-www-form-urlencoded"
        }
        if self._args.verbose:
            print(f"Scanning URL {url}...")

        response = requests.post(SCAN_URL, data=data, headers=headers)

        if response.status_code == 200:
            if self._args.verbose:
                print(f"URL has been successfully scanned!")
            return True
        raise BadRequest(request=response, status_code=response.status_code)

    @staticmethod
    def _get_url_reputation(json_resp: dict):
        """
        Get URL reputation from a JSON-type response
        :param json_resp: dict
        :return tuple(max_key, ratio): max_key in ['harmless', 'malicious', 'suspicious', 'undetected'],
        ratio = accuracy percentage
        """
        stats = json_resp['data']['attributes']['last_analysis_stats']
        total_values_sum = sum(stats.values())
        max_val = max(stats.values())
        max_key = list(stats.keys())[list(stats.values()).index(max_val)]
        ratio = max_val / total_values_sum * 100
        return max_key, ratio

    def analyze_url(self, url: str):
        """
        Analyze URL using VirusTotal API
        :param url: str
        :return: None
        If the URL hasn't been scanned before, the method will perform a scan and re-analyze
        Finally, it will store the data in self._cache accordingly
        """
        url = f"{ANALYSIS_URL}/{self.encode_url(url)}"
        headers = {
            "accept": "application/json",
            "x-apikey": self._token
        }

        response = requests.get(url=url, headers=headers)
        if response.status_code == 404:
            if self._args.verbose:
                print(f"Found no analysis for URL {url}, proceeding to scan")
            if self.scan_url(url):
                self.analyze_url(url)

        if response.status_code == 200 or response.status_code == 202:
            json_resp = response.json()
            last_analysis_date = json_resp["data"]["attributes"]["last_analysis_date"]
            max_key, ratio = self._get_url_reputation(json_resp)

            self._cache[url] = (last_analysis_date, (max_key, ratio))

    def main(self):
        args = self._args

        if isinstance(args.urls, list):
            for url in args.urls:
                pass

        if isinstance(args.urls, str):
            pass

        if url in self._cache:
            pass
        # check if last_analysis_date stands with cache policy
        # if it does, return result
        # if it doesn't, re-analyze
        if url not in self._cache:
            pass
        # analyze url
        # if analysis status code is 404 > scan > re-analyze
        # store url data in self._cache

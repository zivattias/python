import os
import json
import base64
import requests
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
    Result stats - ["data"]["attributes"]["last_analysis_stats"]
    (dict['harmless', 'malicious', 'suspicious', 'undetected'])
    Last analysis date - ["data"]["attributes"]["last_analysis_date"] (epoch timestamp)

    URL scan:
    1. 400 for an invalid URL - "Unable to canonicalize url"
    2. 200 for success, returns dict["data"] = {"type": "analysis, "id": str}
    """

    def __init__(self, urls: list[str], apikey: str, scan: bool, quota: bool, verbose: bool, age: str):
        self._urls = urls
        self._scan = scan
        self._quota = quota
        self._verbose = verbose
        # API key init
        self._token = apikey if apikey else os.environ["VT_KEY"]
        # Cache age
        self._cache_age = int(age)

        # Cache maps URL strings to a respective (last_analysis_date, (result, ratio)) nested tuple
        if not os.path.exists('cache.json'):
            self._cache = dict()
        else:
            with open('cache.json', mode='r') as f:
                self._cache = json.load(f)

        # Uniformed Lock() for threaded actions, e.g. accessing cache and executing actions on it
        self._lock = Lock()

    @staticmethod
    def encode_url(url: str):
        """
        Encodes URL string to Base64
        :param url: str
        :return url: base64
        """
        return base64.urlsafe_b64encode(f"{url}".encode()).decode().strip("=")

    def check_cache(self, epoch: int, url: str) -> bool:
        """
        Check cached content age
        :param url: URL str
        :param epoch: Unix timestamp int
        :return bool: if today's date - last analysis date <= self._cache_age
        """
        datetime_epoch = datetime.utcfromtimestamp(epoch)

        if datetime.utcnow() - datetime_epoch <= timedelta(days=self._cache_age):
            print(f"Found valid cached data for URL: {url}. "
                  f"Last analysis date: {datetime_epoch.date().strftime('%d-%m-%Y')}") if self._verbose else None
            return True
        return False

    def scan_url(self, url: str) -> tuple[bool, str]:
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

        print(f"Scanning URL {url}...") if self._verbose else None

        response = requests.post(SCAN_URL, data=data, headers=headers)

        if response.status_code == 200:
            print(f"URL {url} has been successfully scanned!") if self._verbose else None
            return True, url
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
        total_values_sum, max_val = sum(stats.values()), max(stats.values())
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
        # In case of force-scanning the input for this func is a Future obj, thus extracting its result
        # Which is tuple[bool, url: str]
        # if not isinstance(url, str):
        #     url = url.result()[1]

        full_url = f"{ANALYSIS_URL}/{self.encode_url(url)}"
        headers = {
            "accept": "application/json",
            "x-apikey": self._token
        }

        print(f"Analyzing URL {url}...") if self._verbose else None

        response = requests.get(url=full_url, headers=headers)

        if response.status_code == 404:
            print(f"Found no analysis for URL {url}, initializing scan") if self._verbose else None
            self.analyze_url(url) if self.scan_url(url)[0] else None

        if response.status_code == 200 or response.status_code == 202:
            json_resp = response.json()
            last_analysis_epoch = json_resp["data"]["attributes"]["last_analysis_date"]
            max_key, ratio = self._get_url_reputation(json_resp)

            with self._lock:
                self._cache[url] = (last_analysis_epoch, (max_key, ratio))

            return self._cache[url]

    def _single_url_flow(self, url: str) -> list:
        source = 'cache'

        if (url not in self._cache) or ((url in self._cache) and (not self.check_cache(self._cache[url][0], url))):
            print(f"Either URL {url} not in cache or cache is outdated, proceeding to analysis")
            self.analyze_url(url)
            source = 'api'

        return [url, self._cache[url][0], self._cache[url][1][0], self._cache[url][1][1], source]

    def main(self):
        ret_val = list()
        # If user input a list of URLs:
        if isinstance(self._urls, list):
            with ThreadPoolExecutor() as executor:
                for url in self._urls:
                    if self._scan:
                        executor.submit(self.scan_url, url)
                        result = executor.submit(self.analyze_url, url).result()
                        ret_val.append([url, result[0], result[1][0], result[1][1], 'api'])
                    else:
                        ret_val.append(executor.submit(self._single_url_flow, url).result())

        # If user input a single URL:
        if isinstance(self._urls, str):
            self.scan_url(self._urls) if self._scan else None
            ret_val.append(self._single_url_flow(self._urls))

        # Pretty result prints:
        for result in ret_val:
            print(f"URL: {result[0]}, analysis date: {datetime.utcfromtimestamp(result[1]).strftime('%d-%m-%Y')},"
                  f" result: {result[2]}, accuracy: {result[3]:.2f}%, source: {result[4]}")

        # Save cache:
        with open('cache.json', 'w') as f:
            json.dump(self._cache, f)

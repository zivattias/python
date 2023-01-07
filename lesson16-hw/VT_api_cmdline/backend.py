# WIP
import base64
import os
import argparse
from concurrent.futures import ThreadPoolExecutor
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

    @staticmethod
    def base_encoder(url: str):
        return base64.urlsafe_b64encode(f"{url}".encode()).decode().strip("=")

    def get_urls_reputation(self, urls: list) -> dict[str, bool]:
        pass

    def _get_reputation_for_single_url(self, url: str):
        pass

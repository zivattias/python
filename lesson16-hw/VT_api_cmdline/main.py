from backend import VTAnalyzer
import argparse

if __name__ == '__main__':
    # VTAnalyzer initialization
    analyzer = VTAnalyzer
    # Argparse utilization
    parser = argparse.ArgumentParser(prog="URL Reputation Check, Powered by VirusTotal's API",
                                           description="The program allows you to check URL(s)",
                                           epilog="By Ziv Attias")
    parser.add_argument('url', help='URL to scan')
    parser.add_argument('-k', '--apikey')
    parser.add_argument('-s', '--scan', action='store_true')




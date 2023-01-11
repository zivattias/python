from backend import VTAnalyzer
import argparse

if __name__ == '__main__':
    # Argparse initialization
    parser = argparse.ArgumentParser(prog="URL Reputation Check, Powered by VirusTotal's API",
                                     description="The program allows you to check URL(s)",
                                     epilog="By Ziv Attias")
    parser.add_argument('url', nargs='*',
                        help='one or more URLs, separated by a whitespace')
    parser.add_argument('-k', '--apikey',
                        help='followed by custom VT API key')
    parser.add_argument('-s', '--scan', action='store_true',
                        help='force URL scan')
    parser.add_argument('-q', '--quota', action='store_true',
                        help='verbose wait in case of quota insufficiency')
    parser.add_argument('-v', '--verbose', action='store_true',
                        help='verbose prints throughout the process')
    parser.add_argument('-a', '--age', default=182,
                        help='declare cache max age (days), default = 182')
    args = parser.parse_args(['https://mcdonalds.com', 'https://facebook.com', '-v', '-a', '1'])

    # Create an instance of VTAnalyzer with the parsed arguments and run main()
    analyzer = VTAnalyzer(urls=args.url, apikey=args.apikey, scan=args.scan,
                          quota=args.quota, verbose=args.verbose, age=args.age)
    analyzer.main()

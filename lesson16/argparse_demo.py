import argparse

if __name__ == '__main__':
    # Create a parser
    parser = argparse.ArgumentParser(
        prog='VirusTotal Scanner',
        description='The program allows to check a URL with VirusTotal API',
        epilog='Text at bottom for help'
    )

    # Define arguments so it will know how to parse
    parser.add_argument('url', help='URL to scan')  # positional argument
    parser.add_argument('-k', '--apikey')           # option that takes a value
    parser.add_argument('-s', '--scan', action='store_true')    # on/off flag

    # Perform the parse
    args = parser.parse_args(['https://edulabs.co.il', '-k', 'my_key', '-s'])
    print(args.url, args.apikey, args.scan)

    # Here will come the call for actual logic

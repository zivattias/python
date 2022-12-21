# Match two digits then any character then two non digits
import re


def match_2dac2d(string: str):
    match = re.match('[0-9]{2}.[0-9]{2}', string)
    return match

if __name__ == '__main__':
    print(match_2dac2d('23A08342'))
    print(match_2dac2d('23082C3432'))
    print(match_2dac2d('98B084C3765'))
    print(match_2dac2d('98708676543'))
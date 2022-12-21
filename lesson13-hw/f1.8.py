# Find all the israeli cell phone numbers in the text.
# In this exercise, israeli cell phone number answers the following:
# format: <000-0000000>
# starts from 05

import re


def get_israeli_phones(string: str) -> list[str]:
    pattern = '05\d-\d{7}'
    matches = re.findall(pattern, string)
    return matches


if __name__ == '__main__':
    string = '052-8039540hello-world052-1110004$56&&04-56768999!!052-99987!!'
    print(get_israeli_phones(string))

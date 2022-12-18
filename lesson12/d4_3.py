# Implement a function that gets a list of strings that represent dates in format dd-mm-yyyy.
# Use map() and filter() to filter from this list all the dates that are Fridays and Saturdays.
# Test with the following list: ['12-12-2021', '18-12-2021', '19-12-2021]
# Write 2 additional unit tests to test your implementation
import unittest
from datetime import datetime

class NonMatchingDates(Exception):
    def __init__(self):
        super().__init__('All dates are either Friday/Saturday, no dates to display')

def filter_weekend(dates: list[str]) -> list[str]:
    pre_format = filter(lambda x: x.weekday() not in [4, 5],
                        map(lambda x: datetime.strptime(x, '%d-%m-%Y'), dates))

    post_format = list(map(lambda x: datetime.strftime(x, '%d-%m-%Y'), pre_format))

    if len(post_format) == 0:
        raise NonMatchingDates()

    return post_format


class TestFilterWeekend(unittest.TestCase):

    def test_function(self):
        self.assertEqual(filter_weekend(['24-12-2022', '23-12-2022', '22-12-2022']), ['22-12-2022'])
        self.assertEqual(filter_weekend(['12-12-2021', '18-12-2021', '19-12-2021']), ['12-12-2021', '19-12-2021'])
        with self.assertRaises(NonMatchingDates):
            filter_weekend(['24-12-2022', '23-12-2022'])


if __name__ == '__main__':
    # print(filter_weekend(dates_list))
    unittest.main()

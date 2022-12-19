# Implement a simple class DateIterator that should be initialized with a date and implements iterator protocol
# (__iter__ and __next__ method)  that on every iteration returns the next date up until the end of the month.

import calendar
from datetime import datetime, timedelta


class DateIterator:
    def __init__(self, date: str):
        try:
            self.date = datetime.strptime(date, '%d-%m-%Y').date()
        except ValueError:
            raise ValueError("Incorrect data format, should be DD-MM-YYYY")

        self.month_in_date = datetime.strftime(self.date, '%d-%m-%Y').split('-')[1]
        self.year_in_date = datetime.strftime(self.date, '%d-%m-%Y').split('-')[2]

        self.max_days = calendar.monthrange(int(self.year_in_date), int(self.month_in_date))

    def __iter__(self):
        self.date = self.date
        return self

    def __next__(self):
        self.day_in_date = int(datetime.strftime(self.date, '%d-%m-%Y').split('-')[0])
        if self.day_in_date == self.max_days[1]:
            raise StopIteration
        self.date += timedelta(days=1)

        return self.date


for i in DateIterator('19-12-2022'):
    print(i)

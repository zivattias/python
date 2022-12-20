# Rewrite DateIterator as a generator

import calendar
from datetime import datetime, timedelta


def date_generator(date: str):
    date = datetime.strptime(date, '%d-%m-%Y').date()

    day_in_date = int(date.day)
    month_in_date = date.month
    year_in_date = date.year

    max_days = calendar.monthrange(int(year_in_date), int(month_in_date))[1]

    for day in range(day_in_date, max_days + 1):
        yield datetime.strftime(datetime.strptime(f'{day}-{month_in_date}-{year_in_date}', '%d-%m-%Y'), '%d-%m-%Y')

generator = date_generator('26-12-2022')
print(generator)
print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))
# StopIteration:
print(next(generator))

import datetime


class NegativeYearError(Exception):
    def __init__(self, birth_year):
        super().__init__(f'Negative year {birth_year} not allowed.')


class YearInFutureError(Exception):
    def __init__(self, birth_year):
        super().__init__(f'Future birth year {birth_year} invalid.')


def get_age(birth_year: int) -> int:
    if birth_year < 0:
        # raise Exception('negative year is not allowed')
        raise NegativeYearError(birth_year)
    if birth_year > datetime.datetime.utcnow().year:
        raise YearInFutureError(birth_year)
    return datetime.datetime.utcnow().year - birth_year

#
# try:
#     b_year = int(input('insert your year: '))
#     age = get_age(b_year)
#     print(f'you are {age} years old')
#     print('Inside try after get_age')
#
# except ValueError:
#     print('year must be a number')
#
# except Exception as e:
#     print(e)
#
# finally:
#     print('bye')

print(type(YearInFutureError))
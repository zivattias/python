# # year = int(input('Enter a year: '))
# # if (year % 4 != 0) or (year % 100 == 0 and year % 400 != 0):
# #     print('not leap')
# # else:
# #     print('leap')
#
#
# def is_leap_year(gadu):
#     not_leap = gadu % 4 != 0 or gadu % 100 == 0 and gadu % 400 != 0
#     return not not_leap
#
#
# gadu = int(input('Enter your year: '))
# is_leap = is_leap_year(gadu)
# if is_leap:
#     print('Inserted year is a leap year')
# else:
#     print('Inserted year is NOT a leap year')
def is_leap_year(year):
    if (year % 4 != 0) or (year % 100 == 0 and year % 400 != 0):
        return True
    else:
        return False


def is_31_days_month(month, year):  # 31 days - January, March, May, July, August, October, and December.
    if month != 2:
        if is_leap_year(month):
            return 31
        else:
            return 30
    else:
        if is_leap_year(year)
            return 29
        else:
            return 28



year = int(input('Enter a year: '))
month = int(input('Enter a month (e.g. 1, 2, 3 [...] 12): '))
print(f"Days number: {days_in_month(month, year)}")

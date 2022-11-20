day = int(input("Enter the day (e.g. 1, 2, [...], 20 etc.): "))
month = int(input("Enter the month (e.g. 1, 2, 3 etc.): "))
year = int(input("Enter the year (e.g. 2022): "))

is_leap = (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0)
if is_leap:
    leap_status = "is"
else:
    leap_status = "isn't"

total_days = 0
season = None

if month == 1 or month == 2 or (month == 3 and day <= 19):
    season = "Winter"
elif month == 4 or month == 5 or (month == 6 and day <= 20) or (month == 3 and day > 19):
    season = "Spring"
elif month == 7 or month == 8 or (month == 9 and day <= 22) or (month == 6 and day > 20):
    season = "Summer"
else:
    season = "Autumn"

if month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
    total_days = 31
if month == 2 and is_leap:
    total_days = 29
elif month == 2 and not is_leap:
    total_days = 28
else:
    total_days = 30

print(f"According to your input, the season is {season} and your month has {total_days} days. \nThe year is {year} and it {leap_status} a leap year.")

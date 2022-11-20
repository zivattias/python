year = int(input("Enter year: "))
is_leap = (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0)
print("Is given year a leap year?", is_leap)

def get_year():
    while True:
        year = input("Insert a year: ")
        if year.isdigit():
            year = int(year)
            return year


my_year = get_year()
print(my_year)

###


def get_num_from_user(message):
    while True:
        num = input(message)
        if num.isdigit():
            num = int(num)
            return num


my_year = get_num_from_user("Insert a year: ")
my_month = get_num_from_user("Insert a month: ")
print(my_month, my_year)

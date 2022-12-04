import datetime

d2 = input('Insert a date (DD/MM/YYY): ')

date2 = datetime.datetime.strptime(d2, "%d-%m-%Y")

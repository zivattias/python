from datetime import date, time, datetime, timedelta
import pyluach

print(date.today())
datetime.now()
now = datetime.now()
now_time = datetime.time(datetime.now())
print(now_time)
print(now)

print(now.weekday())

today = date.today()

print(today.weekday())
today.replace(year=2023)

td = timedelta(hours=1)
print(now + td)
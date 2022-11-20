month_list = []
season_list = []
date_list = []
i = 0
j = 0
for i in range(2):
    date = input("Enter a date dd.mm.yyyy: ")
    date_data = date.split(".")
    month = int(date_data[1])
    day = int(date_data[0])
    month_list.append(month)
    if 1 <= month <= 2 or (month == 3 and day <= 19):
        season = "Winter"
    elif 4 <= month <= 5 or (month == 6 and day <= 20) or (month == 3 and day > 19):
        season = "Spring"
    elif 7 <= month <= 8 or (month == 9 and day <= 22) or (month == 6 and day > 20):
        season = "Summer"
    else:
        season = "Autumn"
    season_list.append(season)
    date_list.append(date)

for j in range(len(date_list)):
    print(f"Your date {date_list[j]} is in season {season_list[j]}")


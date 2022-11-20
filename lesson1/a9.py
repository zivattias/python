old_m = int(input("Insert current monthly salary: "))
old_a = old_m * 12
new_m = int(input("Insert new monthly salary: "))
new_a = new_m * 12
print(f"With your current job you earn {old_m} a month, and {old_a} a year. \nIf you join the new job, you'll earn {new_m} a month, and {new_a} a year, \nresulting in a {new_a - old_a} annual difference, or a {new_m - old_m} monthly difference.")
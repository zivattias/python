# # insert 10 grades and print their average
# count = 0
# grades = []
# grades_sum = 0
# while count < 3:
#     grade = int(input("Insert grade: "))
#     grades.append(grade)
#     grades_sum += grade
#     count += 1
# print(len(grades))
# print(f"Grades: {grades}. Average: {grades_sum / len(grades)}")
#
# # drink game
# drink_type = input("Insert drink: ").lower().strip()  # beer / wine
# while drink_type not in ['beer', 'wine']:
#     drink_type = input("Incorrect input. Insert drink:").lower().strip()
# print(f"Your type: {drink_type}")
#
# # more option - flag:
# flag = True
# while flag:
#     drink_type = input("Insert drink: ").lower().strip()
#     if drink_type in ["beer", "wine"]:
#         flag = False
# print(f"Your drink: {drink_type}")

# # class question:
# flag = True
# maxi = 0
# while flag:
#     x = input("Enter a number, to exit type '$': ")
#     if x != '$':
#         if int(x) > int(maxi):
#             maxi = x
#     elif x == '$':
#         flag = False
# print(f"Largest number: {maxi}")

# Valeria's solution:
end_of_input = False
temp_max = None

while not end_of_input:
    i = input("Insert num or $ to finish: ")
    if i == '$':
        end_of_input = True
    else:
        num = int(i)
        if temp_max is None:  # temp_max is declared as 'None' to prevent pre-setting
            temp_max = num
        if num > temp_max:
            temp_max = num
print(f"Max num: {temp_max}")
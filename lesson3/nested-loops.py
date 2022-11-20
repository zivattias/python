rows = int(input("Enter rows number: "))

for i in range(0, rows):
    for j in range(0, i + 1):
        print("*", end=' ')
    print("\n", end='')

# for i in range(rows, 0, -1):
#     for j in range(0, i - 1):
#         print("*", end=' ')
#     print("\r")


# names = []
# grades = []
# for name_idx in range(3):
#     grades.append([])
#     names.append(input("Enter a name: "))
#     for grade_idx in range(2):
#         grades[name_idx].append(int(input("Insert a grade: ")))
# print(names, grades)

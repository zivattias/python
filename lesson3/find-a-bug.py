# Get 3 numbers as input and print them from the smallest to biggest
# Are there any bug(s)? Test different inputs and find a bug
# Use PyCharm debugger to find the bug(s) and fix

num1 = int(input("Insert num 1: "))
num2 = int(input("Insert num 2: "))
num3 = int(input("Insert num 3: "))

min_num, middle_num, max_num = None, None, None

if num1 <= num2 and num1 <= num3:
    min_num = num1
    if num2 < num3:
        middle_num, max_num = num2, num3
    else:
        middle_num, max_num = num3, num2
elif num2 <= num1 and num2 <= num3:
    min_num = num2
    if num1 < num3:
        middle_num, max_num = num1, num3
    else:
        middle_num, max_num = num3, num1  # was 'num2, num1'
else:  # didn't get negative values
    min_num = num3
    if num1 < num2:
        middle_num, max_num = num1, num2
    else:
        middle_num, max_num = num2, num1

print(min_num, middle_num, max_num)

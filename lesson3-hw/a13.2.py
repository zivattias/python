# Write a program that receives a list of numbers, and prints the minimum number

num_list = []
temp = None

while True:
    num = input("Enter a number to the list, $ to stop: ")
    if num == '$':
        break
    else:
        if not num.isdigit():
            print("Invalid input. Use numbers.")
            continue
        else:
            num = int(num)
            num_list.append(num)
            continue

print(num_list)

for x in range(len(num_list)):
    if x == 0:
        temp = num_list[x]
        continue
    else:
        if num_list[x] < num_list[x-1]:
            temp = num_list

print(temp)

# Write a number that receives a list of numbers, and finds the second-largest number

list_range = int(input("Enter total amount of numbers to be given: "))
a_li = []

for a in range(list_range):
    b = input("Enter a number: ")
    a_li.append(b)
    a_li.sort()

print(f"Second largest number: {a_li[-2]}")

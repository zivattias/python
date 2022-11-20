num = input("Enter a number: ")
list_squares = []

while not num.isnumeric():
    num = input("Wrong input. Try again using an integer only: ")

num = int(num)
for x in range(1, num+1):
    square = num ** x
    list_squares.append(square)

print(list_squares)

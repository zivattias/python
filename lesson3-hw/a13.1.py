# Write a program that receives a number from a user and calculates the sum of all numbers from 1 to a given number
total_sum = 0

while True:
    num = input("Enter a number: ")
    if not num.isdigit():
        print("Enter a number please. Nothing else.")
        continue
    else:
        num = int(num)
        for x in range(1, num+1):
            total_sum += x
        break
print(total_sum)

num1 = input("Enter first number: ")
num2 = input("Enter second number: ")
num3 = input("Enter third number: ")

lar = med = small = 0

# equal check
if num1 == num2 == num3 or num1 == num2 or num2 == num3:
    exit("One or more of your numbers are equal.")
# num classification
if num1 > num2 and num1 > num3:
    lar = num1
    if num2 > num3:
        med = num2
        small = num3
    elif num3 > num2:
        med = num3
        small = num2
elif num2 > num1 and num2 > num3:
    lar = num2
    if num1 > num3:
        med = num1
        small = num3
    elif num3 > num1:
        med = num3
        small = num1
elif num3 > num1 and num3 > num2:
    lar = num3
    if num2 > num1:
        med = num2
        small = num1
    elif num1 > num2:
        med = num1
        small = num2
# result
print(f"{small, med, lar}")

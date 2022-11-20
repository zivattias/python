# continue
# example: print all the numbers from 1 up to n,
# skipping those which digits sum is even
num = int(input("Insert a num: "))
i = 0
numbers_sum = 0
while i < num:
    i = i + 1

    digits_sum = 0
    temp = i
    while temp > 0:
        digits_sum = digits_sum + temp % 10
        temp = temp // 10

    if digits_sum % 2 == 0:
        continue

    print(i)
    numbers_sum += i

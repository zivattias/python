# print multi table of given number

num = int(input("Enter a num: "))

for x in range(1, 11):
    if x < 10:
        print(f"{format(x, '>2.0f')} * {num} = {x * num}")
    else:
        print(f"{x} * {num} = {x * num}")

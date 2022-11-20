fact = int(input("Enter a number: "))
fact_total = 1

for x in range(1, fact+1):
    if fact == 0:
        print(f'Factorial of 0: {fact_total}')
    else:
        fact_total *= x

print(fact_total)
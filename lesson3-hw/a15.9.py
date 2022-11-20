l1 = []
odds = 0
evens = 0


while True:
    value = input('Enter a number to your list, $ to exit: ')
    if value[0] == '-':
        if value[1::].isdigit():
            value = int(value)
            l1.append(value)
            continue
    if value.isdigit():
        value = int(value)
        l1.append(value)
        continue
    elif value == '$':
        break
    print('Invalid input.')

print(l1)

for x in range(len(l1)):
    if l1[x] % 2 == 0:
        evens += 1
    else:
        odds += 1

print(f"Evens: {evens}, Odds: {odds}")

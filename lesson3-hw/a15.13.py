while True:
    n = input('Enter number: ')
    if n.isdigit():
        n = int(n)
        break
    print('Invalid input. You can only use positive integers.')

for i in range(1, n+1):
    for j in range(0, i):
        print(i, end=' ')
    print("\n", end='')
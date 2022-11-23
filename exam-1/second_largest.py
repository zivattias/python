def second_largest():
    _l = list()
    while True:
        n = input('Enter a number, "$" to stop: ')
        if n == '$':
            if len(_l) > 0:
                break
            else:
                print('The list is empty, thus no second largest number is printed. Restart the program.')
                break
        if float(n):
            n = float(n)
            _l.append(n)
        elif n.lstrip('-').isdigit() or int(b):
            n = int(n)
            _l.append(n)
        else:
            print(f'You entered "{n}". Please use digits only!')
    _l.sort()
    return _l[-2]

print(f'Second largest number is: {second_largest()}')
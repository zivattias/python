
while True:
    rows = input('Enter number of rows: ')
    columns = input('Enter number of columns: ')
    if rows.isdigit() and columns.isdigit():
        rows = int(rows)
        columns = int(columns)
        break
    print('Invalid input. You can only use positive integers.')

for x in range(rows):
    for y in range(columns-1):
        print('$', end='')
    print('$')
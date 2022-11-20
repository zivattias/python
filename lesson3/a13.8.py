# rows = input("Enter a number of rows: ")
# for x in range(1, int(rows)+1):
#     for k in range(1, x):
#         print(k, end=' ')
#     print(x, end='')
#     print('\n', end='')
#
rows = input("Enter a number of rows: ")
for x in range(1, int(rows)+1):
    for k in range(1, x + 1):
        print(k, end=' ')
    print('\n', end='')

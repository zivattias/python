# Right Triangle Star Pattern
#
# Input: 5
#
# Output:
#
# *
# * *
# * * *
# * * * *
# * * * * *

n = 5
for row in range(n):
    print()
    for col in range(row + 1):
        print('* ', end='')

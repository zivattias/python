# Print list in reverse order using a for loop

l: list = [1, 2, 3, 4, 5, 6]

for x in range(1, len(l) + 1):
    print(l[-x], end=' ')

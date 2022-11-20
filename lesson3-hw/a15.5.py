n_list = []
n = int(input("Enter sum length (n): "))
static = '2'
list_sum = 0

for x in range(1, n+1):
    value = ''.join(static) * x
    n_list.append(value)
    list_sum += int(value)

print(f"{n_list} - sum: {list_sum}")

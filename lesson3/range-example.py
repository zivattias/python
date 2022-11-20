grades = [95, 98, 97, 100, 95]
my_range = range(10)

print(type(my_range))
print(my_range)
print(5 in my_range)

for i in my_range:
    print(i)

my_range = range(-10, 0, 2)
print(0 in my_range)
print(-9 in my_range)
for i in my_range:
    print(i, end=" ")

for i in range(len(grades)-1, -1, -1):
    print(grades[i])

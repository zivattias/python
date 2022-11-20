l1 = []
g1 = int(input("g1: "))
g2 = int(input("g2: "))
l1.append(g1)
l1.append(g2)
print(l1)

# l1.pop(0) - remove value on given index
# print(l1)

# l1.remove(90)  # remove specific value, regardless of index
# print(l1)

l2 = [10, 20, 30, 50, 50]
print(l2)
l2.insert(3, 40)  # inserts a given value (40) into list in given index (3)
print(l2)

print(l2.count(50))  # count how many times value is present in list

various = ['AAA', [4, 5, 7], "5", 5,  3.0, True, 2654, -4, 0]
types_list = []

for x in range(len(various)):
    types_list.append(type(various[x]))
    print(various[x], types_list[x])

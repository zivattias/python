various = ['AAA', [4, 5, 7], "5", 5,  3.0, True, 2654, -4, 0]
pos_list = []

# expected output - [5, 2654]
for x in range(len(various)):
    if type(various[x]) == int:
        if various[x] <= 0:
            pass
        else:
            pos_list.append(various[x])
    elif type(various[x]) == list:
        for y in range(len(various[x])):
            if various[x][y] <= 0:
                pass
            else:
                pos_list.append(various[x][y])
    else:
        continue
print(pos_list)

my_list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
for x in range(len(my_list)):
    if my_list.index(my_list[x]) % 2 != 0:
        print(my_list[x])
    else:
        continue

original_list = [7, 4, 22, 1, 0]
print("List before reverse : ", original_list)
reversed_list = []
for value in original_list:
    # reversed_list.append(value)
    reversed_list = [value] + reversed_list
print("List after reverse : ", reversed_list)
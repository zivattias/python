# # List:
# # color_1 = ['red', 'white', 'blue','white', 'pink', 'purple', 'white']
# # colors_2 = ['red', 'White', 'BLUE','white & Red', 'sky blue', 'purple', 'orange with white straps']
# # Create a function that receives two lists and returns output (choose the right type)
# # that includes colors that exist in both lists
# # Case insensitive
#
# colors_1 = ['red', 'white', 'blue', 'white', 'pink', 'purple', 'white']
# colors_2 = ['red', 'White', 'BLUE', 'white & Red', 'sky blue', 'purple', 'orange with white straps']
#
# def intersection(l1: list[str], l2: list[str]) -> set[str]:
#     ret_val1 = set()
#     ret_val2 = set()
#     for color in l1:
#         ret_val1.add(color.lower())
#     for color in l2:
#         ret_val2.add(color.lower())
#     ret_val1.union(ret_val2)
#     return ret_val
#
# print(intersection(colors_1, colors_2))
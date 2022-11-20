# List:
# colors_2 = ['red', 'White', 'BLUE','white', 'Red', 'sky blue', 'purple', 'orange with white straps']
# Create a function that receives a list and returns output (choose the right type) with unique elements only
# No duplicated elements
# Case insensitive
# Expected result: red,white, blue, sky blue, purple, orange with white straps.

colors_1 = ['red', 'white', 'blue', 'white', 'pink', 'purple', 'white']
colors_2 = ['red', 'White', 'BLUE', 'white', 'Red', 'sky blue', 'purple', 'orange with white straps']

def unique_elements(l1: list[str]) -> set[str]:
    l2: list = []
    for color in l1:
        l2.append(color.lower())
    s1 = set(l2)
    return s1

print(unique_elements(colors_2))

# Valeria's solution:
# def unique_elements2(l3: list[str]) -> set[str]:
#     ret_val = set()
#     for color in l3:
#         ret_val.add(color.lower())
#     return ret_val
#
# print(unique_elements2(colors_2))

def color_intersection(colors1: list[str], colors2: list[str]):
    set1 = unique_elements(colors1)
    set2 = unique_elements(colors2)
    return set1.intersection(set2)

print(color_intersection(colors_2, colors_1))

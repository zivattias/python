# Write a Python function that takes a tuple and returns a new tuple with unique elements of the first list.
# Arguments types: tuple
# Return value type: tuple

# tup: tuple = (1, 4, 5, 6, 7, 6, 5, 3, 2)
tup1: tuple = (1, 4, 5, 6, 7, 6, 5, 3, 2, False, True, 'ss', 'ss', 'b1')

# def is_unique(t: tuple) -> tuple:
#     t1 = list()
#     for item in t:
#         if t.count(item) == 1:
#             t1.append(item)
#     t1 = tuple(t1)
#     return t1
#
# print(is_unique(tup))

def is_unique_by_set(t3: tuple) -> tuple:
    return tuple(set(t3))

print(is_unique_by_set(tup1))
# Write a function that receives a sequence of key-value pairs
# and creates a dictionary of lists (and returns it).
# For example:
# Original list:
# [('yellow', 1), ('blue', 2), ('yellow', 3), ('blue', 4), ('red', 1)]
# Grouping a sequence of key-value pairs into a dictionary of lists:
# {'yellow': [1, 3], 'blue': [2, 4], 'red': [1]}

_list: list = [('yellow', 1), ('blue', 2), ('yellow', 3), ('blue', 4), ('red', 1)]

def dic_creation(args: tuple[str, int]) -> dict[str | list]:
    d: dict[str, list] = dict()

    for item in args:
        if item[0] not in d.keys():
            d[item[0]] = [item[1]]
        else:
            d[item[0]].append(item[1])
    return d

print(dic_creation(_list))


# Implement a function that receives a list of strings and returns a dictionary that maps each string to its count received.
#
# 	For example, for the list:
# 	["sun", "water", "air", "water", "water", "apple", "air"]
# You should return:
#
# {"sun": 1,
# "water": 3,
# "air": 2,
# "apple": 1}

def dict_creator(elements: list) -> dict[str: int]:
    return {elem: elements.count(elem) for elem in elements}


elems = ["sun", "water", "air", "water", "water", "apple", "air"]
print(dict_creator(elems))

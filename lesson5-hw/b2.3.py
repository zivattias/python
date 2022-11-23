# Write a function that receives a dictionary of lists and splits it into a list of dictionaries.
# For example:
# Original dictionary of lists:
# {'Science': [88, 89, 62, 95], 'Language': [77, 78, 84, 80]}
# Split dictionary of lists into list of dictionaries:
# [{'Science': 88, 'Language': 77}, {'Science': 89, 'Language': 78},
# {'Science': 62, 'Language': 84}, {'Science': 95, 'Language': 80}]
d: dict = {'Science': [88, 89, 62, 95], 'Language': [77, 78, 84, 80]}

def transformation(_dict: dict[str | list]) -> list[dict]:
    # this list will hold dictionaries
    _list: list = list()
    # for loop to iterate through given dict keys
    for k in _dict:
        # for loop to iterate through index & values of key
        for i, v in enumerate(_dict.get(k)):
            # dict of key and value in index i
            new_dict: dict = {k: (_dict.get(k))[i]}
            # if length of list of dicts equals to length of values in original dict key:
            # update dict in new list, in index i
            if len(_list) == len(_dict.get(k)):
                _list[i].update(new_dict)
            # if not, append dict to list:
            else:
                _list.append(new_dict)
    return _list

print(transformation(d))

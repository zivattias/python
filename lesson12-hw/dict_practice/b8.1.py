# Write a function that receives 2 lists as parameters -
# the first list contains strings that represent vehicles (manufacturer + model),
# the second list contains strings of colors.

# Create a dictionary that maps vehicles to a list of colors. You can assume that the length of the lists is equal.
#  For example, for the input:
#
# ["Mazda 3",     "Toyota Yaris",     "Volvo S40",    "Mazda 2",  "Toyota Yaris", "Volvo S40"]
# ["red",         "white",            "red",          "blue",     "black",        "red"]
#
#
# Your function should return the following dictionary that represents colors for each vehicle:
#
# {"Mazda 3": ["red"],
# "Toyota Yaris": ["white", "black"],
# "Volvo S40": ["red"],
# "Mazda 2": ["blue"]}

def dict_creator(models: list, colors: list) -> dict[str: list[str]]:
    ret_val = dict()
    for model, color in zip(models, colors):
        if model not in ret_val:
            ret_val[model] = []
        if color in ret_val[model]:
            continue
        ret_val[model].append(color)
    return ret_val


models = ["Mazda 3", "Toyota Yaris", "Volvo S40", "Mazda 2", "Toyota Yaris", "Volvo S40"]
colors = ["red", "white", "red", "blue", "black", "red"]

print(dict_creator(models, colors))
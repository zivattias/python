# B5.4
# colors_0 = ['red', 'blue', 'Purple','white']
# colors_1 = ['orange red', 'blue navy', 'BLUE pure','snow white',
# 'sky blue', 'pure purple', 'white cream', 'Eggshell white',
# 'Orchid purple', 'Medium blue', 'Egyptian blue', 'Neon blue']
# colors_2 = ['red Crimson', 'Liberty blue', 'Purple pizzazz',
# 'white & Red', 'sky blue', 'Pale purple', 'Orchid purple', 'BLUE pure']
#
# Create a function that receives 3 lists and returns output (choose the right single type)
# that will indicate which colors are derived from basic colors.
# Basic colors are ones stored in colors_0. Others are derived colors.
# Case-insensitive
import pprint

col_0 = ['red', 'blue', 'Purple', 'white']
col_1 = ['orange red', 'blue navy', 'BLUE pure', 'snow white',
         'sky blue', 'pure purple', 'white cream', 'Eggshell white',
         'Orchid purple', 'Medium blue', 'Egyptian blue', 'Neon blue']
col_2 = ['red Crimson', 'Liberty blue', 'Purple pizzazz',
         'white & Red', 'sky blue', 'Pale purple', 'Orchid purple', 'BLUE pure']

# output example: {'red': [orange red, red crimson, white & red]}

def derived_colors(l1: list[str], l2: list[str], l3: list[str]) -> dict[str: str]:
    derived_dict: dict = dict()
    _l = l2 + l3
    for basic in l1:
        basic = basic.lower()
        derived_dict[basic] = list()
        for col1 in _l:
            col1 = col1.lower()
            if basic in col1.lower():
                derived_dict[basic].append(col1)
    pprint.pprint(derived_dict)

derived_colors(col_0, col_1, col_2)



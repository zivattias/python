# B5.7
# colors_1 = ['orange red', 'blue navy', 'BLUE pure','snow white',
#             'sky blue', 'pure purple', 'white cream', 'Eggshell white',
#             'Orchid purple', 'Medium blue', 'Egyptian blue', 'Neon blue']
# colors_2 = ['red Crimson', 'Liberty blue', 'Purple pizzazz',
#             'white & Red', 'sky blue', 'Pale purple', 'Orchid purple', 'BLUE pure']
#
#
# Create a function that receives 2 lists and returns output
# (choose the right single type) with unique elements from list #1 that are absent in list #2
# Case insensitive
import pprint

colors_1 = ['orange red', 'blue navy', 'BLUE pure','snow white',
            'sky blue', 'pure purple', 'white cream', 'Eggshell white',
            'Orchid purple', 'Medium blue', 'Egyptian blue', 'Neon blue']
colors_2 = ['red Crimson', 'Liberty blue', 'Purple pizzazz',
            'white & Red', 'sky blue', 'Pale purple', 'Orchid purple', 'BLUE pure']

def unique_elements(l1: list[str], l2: list[str]) -> set[str]:
    l1 = set(l1)
    l2 = set(l2)
    s = l1.difference(l2)
    return s

pprint.pprint(unique_elements(colors_1, colors_2))


# Lists:
# flowers = ['Rose','Lily','Tulip','Orchid','Carnation', 'Hyacinth', 'Rose']
# color = ['red', 'white', 'blue','white', 'pink', 'purple', 'white']
# Create a function that receives 2 lists and returns a dictionary, where
# keys are elements from the list #1 and values are elements from the list #2.
# Assume: number of elements in both lists are equal
# Don’t lose any information
import pprint

flowers = ['Rose', 'Lily', 'Tulip', 'Orchid', 'Carnation', 'Hyacinth', 'Rose']
colors = ['red', 'white', 'blue', 'white', 'pink', 'purple', 'white']
# keys are flowers, values are colors

def combined_dict(l1: list[str], l2: list[str]) -> dict[str: str]:
    d = dict()
    for flower in range(len(l1)):
        for color in l2:
            if l1[flower] in d.keys():
                d.update({l1[flower].replace(l1[flower], l1[flower] + '-2'): color})
            else:
                d.update({l1[flower]: color})
                flower += 1
        break
    return d

pprint.pprint(combined_dict(flowers, colors))


# Write a function to drop empty or None items from a given Dictionary. For example:
# Original Dictionary:
# {'c1': 'Red', 'c2': 'Green', 'c3': None, 'c4': [], 'c5': “”,}
# New Dictionary after dropping empty items:
# {'c1': 'Red', 'c2': 'Green'}

d1: dict = {'c1': 'Red', 'c2': 'Green', 'c3': None, 'c4': [], 'c5': ""}

def remove_empty(d: dict) -> None:
    pop_items = list()

    for k, v in d.items():
        if d.get(k) is None or len(d.get(k)) == 0:
            pop_items.append(k)

    for item in pop_items:
        d1.pop(item)
    return

print(d1)
print(remove_empty(d1))
print(d1)



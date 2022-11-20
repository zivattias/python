drinks = ['juice', 'wine', 'beer', 'coca-cola', 'sprite', 'martini', 'coffee', 'tea']
new_drinks = []

for drink in drinks:
    if 'i' not in drink:
        new_drinks.append(drink)
print(new_drinks)

# bad practice/code - not working - change list that's being iterated upon, it causes index bouncing

# for drink in drinks:
#     if 'i' in drink:
#         drinks.remove(drink)
# print(drinks)
# for i in range(len(drinks)):
#     if 'i' in drink:
#         drink.pop(i)

# good practice - iterate main list using values from other list
# option 1 - store indices to remove from main list:
drinks = ['juice', 'wine', 'beer', 'coca-cola', 'sprite', 'martini', 'coffee', 'tea']
indices_to_remove = []
for i, drink in enumerate(drinks):
    if 'i' in drink:
        indices_to_remove.append(i)

indices_to_remove.sort(reverse=True)
for i in indices_to_remove:
    drinks.pop(i)
print(drinks)

# option 2 - store values to remove from main list:
drinks = ['juice', 'wine', 'beer', 'coca-cola', 'sprite', 'martini', 'coffee', 'tea']
values_to_remove = []
for drink in drinks:
    if "i" in drink:
        values_to_remove.append(drink)

for val_to_remove in values_to_remove:
    drinks.remove(val_to_remove)
print(drinks)

# option 3 (shay) - iterate main list using indices in range IN REVERSE (end -> beginning)
drinks = ['juice', 'wine', 'beer', 'coca-cola', 'sprite', 'martini', 'coffee', 'tea']
drinks_len = len(drinks)
for i in range(drinks_len - 1, -1, -1):
    drink = drinks[i]
    if 'i' in drink:
        drinks.pop(i)
        # drinks.remove(drink)
print(drinks)

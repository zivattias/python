drinks = ['juice', 'wine', 'beer', 'coca-cola', 'sprite', 'martini', ['coffee', 'tea']]
drinks[2] = 'milk'
print(drinks[2])

drinks.insert(3, 'whisky')

fruits = ['apple', 'orange']
drinks.extend(fruits)
drinks.append(fruits)
print(drinks)


my_l = drinks + fruits  # creates a completely new list 'my_l'
print(my_l)

drinks.extend(fruits)  # adds list 'fruits' to current list 'drinks'

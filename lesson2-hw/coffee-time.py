# Provided coffee types
coffee_types: list = ['Espresso', 'Doppio', 'Lungo', 'Ristretto', 'Macchiato',
                      'Corretto', 'Con Panina', 'Romano', 'Cappuccino', 'Americano',
                      'Cafe Latte', 'Flat White', 'Marocchino', 'Mocha', 'Bicerin',
                      'Breve', 'Raf Coffee', 'Mead Raf', 'Vienna Coffee', 'Chocolate Milk',
                      'Latte Macchiato', 'Glace', 'Freddo', 'Irish Coffee', 'Frappe',
                      'Cappuccino Freddo', 'Caramel Frappe', 'Espresso Laccino']

# Input validation for 'time' hh:mm
hours, minutes = None, None
while True:
    time = input("Enter your coffee time (hh:mm): ")
    if time[2] != ':':
        print('Your time format is invalid. Use `:` to differ between hours and minutes and make sure - HH:MM.')
        continue
    time_slice = time.split(':')
    hours = time_slice[0]
    minutes = time_slice[1]
    if not (hours.isdigit() or minutes.isdigit()):
        print("Try again.")
        continue
    else:
        break

# Type ('int') casting for variables post-validation
hours: int = int(hours)
minutes: int = int(minutes)
time_sum: int = hours + minutes

# List of all coffees + 'friends' input
ordered_coffees: list = []
friends: int = int(input("How many people are you in total? "))

# Situation-based variables
new_minutes = time_sum % 28
new_start = 0

# Coffee types for Bonus #1
new_coffee_types = []

# While loop for bonus #1
flag = True
while flag:
    start_q = input("Would you like to skip a certain part of the coffee types? (Y/N): ").lower()
    if not (start_q == 'y' or start_q == 'n'):
        print("Try again. Please use 'Y' or 'N' as for Yes & No.")
        continue
    else:
        if start_q == 'y':
            while True:
                new_start = input('Enter coffee ID as new starting point: ')
                if not new_start.isdigit():
                    print('Try again. Use numbers please.')
                    continue
                else:
                    flag = False
                    new_start = int(new_start)
                    break
        else:
            break

# While loop for coffee excluding - Bonus #2
coffee_exclude_list: list = []
flag2 = True
while flag2:
    coffee_exclude_q: str = input("Would you like to exclude certain types of coffees (IDs) (Y/N): ").lower()
    if not (coffee_exclude_q == 'y' or coffee_exclude_q == 'n'):
        print("Try again. Please use 'Y' or 'N' as for Yes & No.")
        continue
    else:
        if coffee_exclude_q == 'y':
            while True:
                coffee_exclude_input: str = input('Enter coffee IDs to exclude, $ to stop: ')
                if coffee_exclude_input == '$':
                    print(f'Coffee IDs to exclude: {coffee_exclude_list}')
                    flag2 = False
                    break
                elif not coffee_exclude_input.isdigit():
                    print('Enter coffee IDs only, please. Use digits.')
                elif coffee_exclude_input != '$':
                    coffee_exclude_list.append(coffee_exclude_input)
        else:  # added after Valeria's comment
            flag2 = False

# Coffee list remake according to excluded coffees:
if len(coffee_exclude_list) != 0:
    for x in coffee_exclude_list:  # Iterates over list *values*, not indices
        x = int(x)
        coffee_types.pop(x)

# Coffee brewing!
for i in range(friends):
    if i == 0:  # first user only, i = 0
        ordered_coffees.append(coffee_types[hours + new_start - 1])
    else:
        if time_sum > 28:
            new_minutes += time_sum % 28
            if new_minutes > 28:
                new_minutes = new_minutes % 28
                ordered_coffees.append(coffee_types[new_minutes + new_start - 1])
            else:
                ordered_coffees.append(coffee_types[new_minutes + new_start - 1])
        else:
            ordered_coffees.append(coffee_types[(hours + minutes + new_start) - 1])
    i += 1

print(f'User coffee: {coffee_types[hours - 1]}\n'
      f'Friends coffee: {ordered_coffees[1::]}')

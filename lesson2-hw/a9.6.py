layout = input("Enter seats formation: ").strip().upper()
identifier = input("Enter your seat identifier: ").strip().upper()
location = None
# check for row number by seat number (row num is max 2 digits)
if len(identifier) > 2:
    row = identifier[0:2]
else:
    if len(identifier) == 2:
        row = identifier[0]
    else:
        print("Invalid seat identifier.")
# apply seat identifier by seat_combo
seat = identifier[-1]
# split layout to seat groups
groups = layout.split(' ')
if len(groups) == 1:
    if groups[0].index(seat) == 0 or -1:
        location = 'window'
    else:
        location = 'aisle'
if len(groups) == 2:
    if groups[0].index(seat) == 0 \
       or groups[1].index(seat) == -1:
        location = 'window'
    else:
        if groups[0].index(seat) == 2 \
           or groups[1].index(seat) == 0:
            location = 'aisle'
        else:
            location = 'middle'

print(f"Row: {row}, you sit at {location}")

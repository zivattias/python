array = []
indexes = []

for n in range(10**4):
    x = input("Enter a number to the array: ")
    if x.isnumeric():
        array.append(x)
        indexes.append(array.index(x))
    else:
        if x == '$':
            target = input("Enter a sum target: ")
            if target.isnumeric():
                for j, k in enumerate(indexes):
                    possible_i =
                    break
            else:
                print(f"Input {target} is not a valid target. Try again.")
                continue
        else:
            print(f"Input {x} is not a valid number. Try again.")
            continue


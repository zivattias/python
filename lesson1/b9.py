unit = float(input("Choose a storage unit to convert from:"
                   "\n1 - Byte\n2 - Kilobyte\n3 - Megabyte\n4 - Gigabyte\n5 - Terabyte\n"))
qty = float(input("Enter the storage amount: "))
conversion = float(input("Choose a storage unit to convert to:"
                         "\n1 - Byte\n2 - Kilobyte\n3 - Megabyte\n4 - Gigabyte\n5 - Terabyte\n"))
sub = unit - conversion

level = 1024

if unit == conversion or sub == 0:
    print("You're trying to convert into the same unit.")
else:
    if sub > 0:
        result = qty * (level ** sub)
        print(f"Your input '{qty, unit}' has been converted into '{result, conversion}'")
    elif sub < 0:
        result = qty / (level ** -sub)
        print(f"Your input '{qty, unit}' has been converted into '{result, conversion}'")

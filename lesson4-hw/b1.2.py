# Write a Python function to multiply all the numbers in a tuple.
# Arguments types: tuple
# Return value type: float

tup: tuple = (1, 2, 3)

def tup_x(tup_: tuple) -> float:
    multi: float = 1.0
    for i in tup_:
        multi *= i
    return multi

print(tup_x(tup))
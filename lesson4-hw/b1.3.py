# Write a Python function to find the Max of three numbers.
# The function receives 3 floats as parameters and returns a float.

def max_num(num1: float, num2: float, num3: float) -> float:
    if num1 > num2 and num1 > num3:
        maxi = num1
    elif num2 > num1 and num2 > num3:
        maxi = num2
    else:
        maxi = num3
    return maxi

print(max_num(5.1, 4.9, 0.8))



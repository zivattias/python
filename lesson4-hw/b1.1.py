# Write a function that receives a list of numbers as a parameter. The function returns the sum of numbers in the list.
# Arguments types: list
# Return value type: float


def parameter_sum(param: list) -> float:
    total_sum: float = 0.0
    for x in range(len(param)):
        if x == -1:
            break
        else:
            param[x] = int(param[x])
            total_sum += param[x]
    return total_sum


parameter: list = list(input('Enter a list of numbers: '))
print(parameter_sum(parameter))

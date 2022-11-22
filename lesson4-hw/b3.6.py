# Write a Python function to create and
# print a list where the values are square of numbers between 1 and 30 (both included)

def square_30() -> list:
    sq_list: list = []
    for squared in range(1, 31):
        sq_list.append(pow(squared, 2))
    return sq_list

print(square_30())
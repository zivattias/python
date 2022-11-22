# Write a Python program that prints the even numbers from a given list.

l1 = [2, 6, 4, 3, 8, 6, 9, 2, 1, 5, 7]

def print_even(a_list: list) -> list:
    b_list: list = []
    for item in a_list:
        if item % 2 == 0:
            b_list.append(item)
    return b_list

print(print_even(l1))
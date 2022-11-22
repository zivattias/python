# (Advanced) Write a Python function that takes a list and removes all the duplicate elements from the list.
# Note, you should mutate the list you received as an argument, not create a new one!

l1: list = ['car', 'house', 'white', 3, 'car', 3, True, False, True]

def remove_dups(a_list: list) -> list:
    for item in a_list:
        if a_list.count(item) > 1:
            a_list.remove(item)
    return a_list

print(remove_dups(l1))
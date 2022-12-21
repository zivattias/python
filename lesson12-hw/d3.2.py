# Write generator batches(n, my_list) that returns batches of length n of the given list

# when iterating it, the generator should yield sublist of length n from the original list my_list

my_list = [[1, 2, 3], [1, 2], [4, 5, 6], [7, 8], [9], [10], [], ['a', 'b', 'c'], [True, False, None]]

def batches(n: int, l: list):
    for sublist in l:
        if len(sublist) != n:
            continue
        yield sublist

for batch in batches(3, my_list):
    print(batch)
my_list = ['Apple is nice', 'baNana is yellow', 'ANANAS is Big']

strings = map(str.split, map(str.lower, my_list))

for string in strings:
    print(string)

print(list(strings))

def foo_sum(*args):
    return sum(args)


my_tuple1, my_tuple2 = (1, 2, 3, 4), (10, 20, 30, 40)

ret_val = map(foo_sum, my_tuple1, my_tuple2, [100, 200, 300, 400])
print(list(ret_val))
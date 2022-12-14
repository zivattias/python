def foo_squared(num):
    return num ** 2

my_list = [1, 3, 5, 6]

ret_val = map(foo_squared, my_list) # returns an iterable class ('map') object

print(type(ret_val))
print(ret_val)

ret_list = list(ret_val)

print(type(ret_list))
print(ret_list)

# Best Practice - transform map to an iterable (e.g. list()):

ret_val = list(map(foo_squared, my_list))

print(ret_val)


print(list(map(str.lower, ['Apple', 'BaNaNa', 'ANANAS'])))
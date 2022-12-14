# function as an object

def foo_power(num1, num2):
    return num1 ** num2


print(foo_power(3, 4))

print(foo_power)

my_func_var = foo_power

print(my_func_var)

print(type(foo_power))
print(type(my_func_var))

print(foo_power.__name__)
print(my_func_var(3, 4))


# ----------------------------------------------------------------

def foo_sum(num1, num2):
    return num1 + num2


def operation_on_nums(op: callable, num1, num2):
    return op(num1, num2)

print(operation_on_nums(foo_sum, 1, 2)) # 1 + 2 = 3


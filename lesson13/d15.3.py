# Implement a decorator @valid_param_types that receives as parameter allowed argument types and validates
# whether the argument passed to a function answers this requirement.
# If the validation fails, the decorator should raise an InvalidArgument exception.

class InvalidArgument(Exception):
    def __init__(self, t1: type, arg):
        super().__init__(f'Invalid argument type was given: {arg}: {t1}')


def valid_param_types(types: list):
    def wrapper(func):

        def decorated(*args, **kwargs):
            # if len(args) > 1 or len(kwargs) > 1:
            #     for arg, kwarg in zip(args, kwargs):
            #         if type(arg) not in types or type(kwarg) not in types:
            #             raise InvalidArgument(type(arg), arg)
            # if len(args) == 1 or len(kwargs) == 1:
            #     if type(args) not in types or type(kwargs) not in types:
            #         raise InvalidArgument(type(args), args)
            for arg in args:
                if type(arg) not in types:
                    raise InvalidArgument(type(arg), arg)
            for kwarg in kwargs.values():
                if type(kwargs) not in types:
                    raise InvalidArgument(type(kwarg), kwarg)

            return func(*args, *kwargs)

        return decorated

    return wrapper


@valid_param_types([int, float])
def sum_nums(n1: int, n2: int):
    return n1 + n2


@valid_param_types([str])
def my_print(string: str):
    return string


if __name__ == '__main__':
    try:
        print(sum_nums(2, 3))
        print(sum_nums(2, 3.5))
        print(my_print('hello'))
        print(my_print(2))
    except InvalidArgument as e:
        print(e)


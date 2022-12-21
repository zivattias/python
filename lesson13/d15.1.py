# Implement a decorator @single_str_arg that validates that function received exactly one argument
# and that the argument type is string. If the validation fails,
# the decorator should raise an InvalidArgument exception.

class TooManyArguments(Exception):
    def __init__(self):
        super().__init__('More than one argument was given')


class InvalidArgumentType(Exception):
    def __init__(self, arg):
        super().__init__(f'Invalid type was given: {type(arg)}, should be str')


def single_str_arg(func):
    def decorated_function(*args, **kwargs):

        if len(args) > 1 or len(kwargs) != 0:
            raise TooManyArguments()

        elif not isinstance(args[0], str):
            raise InvalidArgumentType(args[0])

        else:
            return func(*args, **kwargs)

    return decorated_function


@single_str_arg
def my_print(string: str):
    return string


if __name__ == '__main__':
    try:
        print(my_print('hello'))
        print(my_print('hello', 'world'))
    except (TooManyArguments, InvalidArgumentType) as e:
        print(e)

    try:
        print(my_print(2))

    except (TooManyArguments, InvalidArgumentType) as e:
        print(e)

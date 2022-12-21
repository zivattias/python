# Implement a decorator @numeric_params that validates that function received only numeric arguments (int, float).
# If the validation fails, the decorator should raise an InvalidArgument exception.

class InvalidArgument(Exception):
    def __init__(self, t1: type, arg):
        super().__init__(f'Invalid argument type for "{arg}" was given: '
                         f'{t1.__name__}, should be either int or float')


def valid_numeric_params(func):
    def decorated_func(*args, **kwargs):
        for arg in args:
            if not isinstance(arg, (int, float)):
                raise InvalidArgument(type(arg), arg)
        for kwarg in kwargs:
            if not isinstance(kwarg, (int, float)):
                raise InvalidArgument(type(kwarg), kwarg)

        return func(*args, *kwargs)

    return decorated_func


@valid_numeric_params
def sum_nums(n1: int | float, n2: int | float) -> int | float:
    return n1 + n2


if __name__ == '__main__':
    try:
        print(sum_nums(1, 2))
        print(sum_nums(2.3, 0.8))
        print(sum_nums('a', False))

    except InvalidArgument as e:
        print(e)

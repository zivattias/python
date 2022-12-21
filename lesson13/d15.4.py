# Implement a decorator @numeric_in_range that receives as parameters allowed range
# for numeric arguments (2 numbers - min and max) and validates that all the numerical arguments passed
# to the decorated function are in the range specified. If the validation fails,
# your decorator should raise an InvalidArgument exception.
class InvalidArgument(Exception):
    def __init__(self, min_num, max_num, arg):
        super().__init__(f'Invalid arg "{arg}" for given range ({min_num}, {max_num}) --> {min_num} <= arg <= {max_num}')


def numeric_in_range(min_num: int, max_num: int):
    def wrapper(func):

        def decorated(*args, **kwargs):
            for arg in args:
                if not min_num <= arg <= max_num:
                    raise InvalidArgument(min_num, max_num, arg)
            return func(*args, **kwargs)

        return decorated

    return wrapper


@numeric_in_range(1, 7)
def check_num(num: int):
    return f"num {num} in range!"

if __name__ == '__main__':
    try:
        print(check_num(4))
        print(check_num(1))
        print(check_num(7))
    except InvalidArgument as e:
        print(e)

    try:
        print(check_num(8))
    except InvalidArgument as e:
        print(e)

    try:
        print(check_num(-1))
    except InvalidArgument as e:
        print(e)

# Test comment

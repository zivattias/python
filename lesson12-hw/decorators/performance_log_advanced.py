import time


def performance_log(time_units: str = 's'):
    def wrapper(func):
        def decorated_func(*args, **kwargs):
            time_func = time.perf_counter if time_units != 'ns' else time.perf_counter_ns
            start = time_func()
            result = func(*args, **kwargs)
            end = time_func()
            print(f'Execution time: {end - start} {time_units}')

            return result

        return decorated_func

    return wrapper


@performance_log('ns')
def sum_and_diff(n1: int, n2: int, verbose=False):
    ret_val = n1 + n2, n1 - n2
    if verbose:
        print(f'n1: {n1}, n2: {n2}, ret_val: {ret_val}')
    return ret_val


if __name__ == '__main__':
    sum_and_diff(10, 11, verbose=True)
    sum_and_diff(10, 11)

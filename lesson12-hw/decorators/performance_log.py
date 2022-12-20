import time


def performance_log(func):
    def decorated_func(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        end = time.perf_counter()
        print(f'> Elapsed time since {func.__name__} execution: {end - start} seconds')

        return result

    return decorated_func


@performance_log
def long_running_function(num: int, iters: int):
    val = 1
    for i in range(iters):
        val *= num
    return val


if __name__ == '__main__':
    long_running_function(17, 100000)

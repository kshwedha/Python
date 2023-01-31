import numpy as np
import random
import functools
import time


def time_elapse(_func):
    functools.wraps(_func)

    def wrapper(**payload):
        start_time = time.time()
        # the below func is fruitful, can be printed.
        _func()
        end_time = time.time()
        delta = end_time-start_time
        return delta
    return wrapper


@time_elapse
def np_arr():
    return [~random.choice([j for j in np.arange(10000000)]) for i in range(10)]


@time_elapse
def memory_based():
    _list = [j for j in range(10000000)]
    return [~random.choice(_list) for i in range(10)]


@time_elapse
def normalised():
    return [~random.choice([j for j in range(10000000)]) for i in range(10)]


print(
    f"The time difference by numpy based number extraction method is - {np_arr()} secs.")
print(
    f"The time difference by equation based number extraction method is - {normalised()} secs.")
print(
    f"The time difference by memory based number extraction method is - {memory_based()} secs.")

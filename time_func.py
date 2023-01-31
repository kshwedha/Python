import functools
import time

"""
this is a time delta calculator decorator,
you can find the performance of your function
by decorating it with "time_elapse"
ex:

@time_elpase
def your_func():
    pass

"""


def time_elapse(_func):
    functools.wraps(_func)

    def wrapper(*payload):
        start_time = time.time()
        # if your func if fruitful, you can use print or
        # return the func_ value
        _func(*payload)
        end_time = time.time()
        delta = end_time-start_time
        return delta
    return wrapper

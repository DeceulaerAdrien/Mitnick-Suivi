def limit_execution(max_executions):
    def decorator(func):
        count = 0

        def wrapper(*args, **kwargs):
            nonlocal count
            if count >= max_executions:
                raise Exception("Function has been executed too many times")
            count += 1
            return func(*args, **kwargs)

        return wrapper

    return decorator


# Example usage
@limit_execution(3)
def my_function():
    print("Executing my_function")


# try:
#     my_function()
#     my_function()
#     my_function()
#     my_function()
# except Exception as e:
#     print(e)


# Exo 2

def restrict_return_type(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        if isinstance(result, (str, int)):
            raise TypeError("Function cannot return a string or an integer")
        return result

    return wrapper


@restrict_return_type
def my_function():
    return [1, 2, 3]


try:
    my_function()
except TypeError as e:
    print(e)


@restrict_return_type
def another_function():
    return {'key': 'value'}


# try:
#     another_function()
# except TypeError as e:
#     print(e)
#
#
# @restrict_return_type
# def yet_another_function():
#     return 123
#
#
# try:
#     yet_another_function()
# except TypeError as e:
#     print(e)


# Exo 3

import time


def timeit(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Function '{func.__name__}' took {end_time - start_time:.5f} seconds to run.")
        return result

    return wrapper


@timeit
def my_function():
    time.sleep(1)


try:
    my_function()
except TypeError as e:
    print(e)

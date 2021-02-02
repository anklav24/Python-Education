def debug(func=None):
    def wrapper(*args, **kwargs):
        try:
            function_name = func.__func__.__qualname__
        except:
            function_name = func.__qualname__
        return func(*args, **kwargs, function_name=function_name)

    return wrapper


@debug
def my_function_test(**kwargs):
    print(kwargs)


my_function_test()

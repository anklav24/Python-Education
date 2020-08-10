def func_1(x):
    """
    :param x:
    """
    return x


def func_2():
    """
    func_2
    """
    return "123"


arg = 1


# @func_2
@func_1(arg)
def func():
    """
    func
    """
    return "x"



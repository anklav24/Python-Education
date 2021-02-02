# https://www.youtube.com/watch?v=5SyA3lsO_hQ&list=PLlWXhlUMyooawilqK4lPXRvxtbYiw34S8&index=6&ab_channel=%D0%9E%D0%BB%D0%B5%D0%B3%D0%9C%D0%BE%D0%BB%D1%87%D0%B0%D0%BD%D0%BE%D0%B2


def coroutine(func):
    def inner(*args, **kwargs):
        g = func(*args, **kwargs)
        g.send(None)
        return g

    return inner


class BlaBlaException(Exception):
    pass

def subgen():
    while True:
        try:
            message = yield
        except StopIteration:
            print("Hoi!")
        else:
            print('.....', message)

@coroutine
def delegator(g):
    # while True:
    #     try:
    #         data = yield
    #         g.send(data)
    #     except BlaBlaException as e:
    #         g.throw(e)
    result = yield from g
    print(result)

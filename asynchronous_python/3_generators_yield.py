# https://www.youtube.com/watch?v=PjZUSSkGLE8&list=PLlWXhlUMyooawilqK4lPXRvxtbYiw34S8&index=4&ab_channel=%D0%9E%D0%BB%D0%B5%D0%B3%D0%9C%D0%BE%D0%BB%D1%87%D0%B0%D0%BD%D0%BE%D0%B2
# run python -i filename  # Передаем все в интерактивный режим
# next(g1)
# or
# next(g2)
# or
# next(g3)

from time import time


def gen(s):
    for i in s:
        yield i


g1 = gen('oleg')


def gen_filename():
    while True:
        pattern = 'file-{}.jpeg'
        t = int(time() * 1000)
        yield pattern.format(str(t))

        sum = 234 + 234
        print(sum)


g2 = gen_filename()


def gen_1_2_3():
    yield 1
    yield 2
    yield 3


g3 = gen_1_2_3()

# https://www.youtube.com/watch?v=PjZUSSkGLE8&list=PLlWXhlUMyooawilqK4lPXRvxtbYiw34S8&index=4&ab_channel=%D0%9E%D0%BB%D0%B5%D0%B3%D0%9C%D0%BE%D0%BB%D1%87%D0%B0%D0%BD%D0%BE%D0%B2
# run python -i filename  # Передаем все в интерактивный режим


from time import time


def gen_filename():
    while True:
        pattern = 'file-{}.jpeg'
        t = int(time() * 1000)
        yield pattern.format(str(t))

        sum = 234 + 234
        print(sum)


def gen1(s):
    for i in s:
        yield i


def gen2(n):
    for i in range(n):
        yield i


g1 = gen1("Oleg")
g2 = gen2(4)

tasks = [g1, g2]

while tasks:
    task = tasks.pop(0)

    try:
        i = next(task)
        print(i)
        tasks.append(task)
    except StopIteration:
        pass


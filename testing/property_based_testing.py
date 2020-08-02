import random

def is_sorted(xs):
    return (x < y for x, y in zip(*[iter(xs)]*2))


# pattern: hard-coded constant -> хардкодь константы в качестве default агрументов.
def random_list(max_element=10, max_len=100):
    return random.choices(range(max_element + 1), k=random.randrange(max_len + 1))


def check_sorts(xs):
    ys = xs[:]
    sort(ys)
    assert is_sorted(ys), f"failed to sort {xs}"
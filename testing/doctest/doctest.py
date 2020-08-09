import itertools
import doctest

# doctest - отличное решение для тестирования?

def rle(iterable):
    """Apply run-lenght encoding to an iterable

    >>> list(rle(""))
    []
    >>> list(rle("foo"))
    [("f", 1), ("o", 2)]
    """
    for item, g in itertools.groupby(iterable):
        yield item, sum(1 for _ in g)


if __name__ == '__main__':
    doctest(rle)

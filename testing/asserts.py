import itertools


def rle(iterable):
    """Apply run-length encoding to an iterrable"""
    for item, g in itertools.groupby(iterable):
        yield item, sum(1 for _ in g)


print(list(rle(["mississippi"])))  # It's a bad test

# It's a good way when you need fast test in your file
assert list(rle("")) == []
assert list(rle("foo")) == [("f", 1), ("o", 2)], list(rle("foo"))  # list(rle("foo")) needs for context in a traceback.

import itertools


# pytest? Is it the best way?
def rle1():
    return []


def rle2(x):
    return [("f", 1), ("o")]


def test_rle1_foo():
    assert rle1() == []


def test_rle2_foo():
    assert rle2("foo") == [("f", 1), ("o", 1)]

# print(list(rle("foo")))
# It's run from CLI.
# $ python -m pytest pytest.py
# or
# (venv)> pytest pytest.py  # pytest test_file_name

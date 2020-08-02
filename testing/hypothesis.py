"""Делаем не совсем случайные данные?"""
from itertools import chain, repeat, tee
from hypothesis import given, strategies as st


# @given(st.lists(st.integers()))
# def test_sorted(xs):
#     result = sorted(xs)
#     result[:2] = result[-2:]  # BUG!
#     assert all(xi <= xj for xi, xj in zip(result, result[1:]))

iterables = st.one_of(st.tuples(st.integers(0, 10),
                                st.lists(st.integers(0, 10),
                                st.text().map(iter))))


@given(iterables)
def test_rle(it):
    def encode_decode(it):
        return chain.from_iterable(repeat(item, count) for item, count in rle(it))

    it, copy = tee(it)
    expected = list(copy)
    assert list(encode_decode(it)) == expected
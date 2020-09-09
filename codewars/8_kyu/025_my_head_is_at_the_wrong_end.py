def fix_the_meerkat(arr: list) -> list:
    """Changes the element positions with logic - top, middle, bottom."""
    arr.reverse()  # fast and readable
    arr = arr[::-1]  # slower
    arr = list(reversed(arr))  # slowest
    return arr


print(fix_the_meerkat(["tail", "body", "head"]))
print(fix_the_meerkat(["tails", "heads", "body"]))
print(fix_the_meerkat(["bottom", "middle", "top"]))

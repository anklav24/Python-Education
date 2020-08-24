def invert(lst: list) -> list:
    """Each positive becomes negatives, and the negatives become positives."""
    invert_lst = []
    for i in lst:
        if i < 0:
            invert_lst.append(abs(i))
        elif i > 0:
            invert_lst.append(-i)
        else:
            invert_lst.append(i)
    if len(lst) == 0:
        return []
    elif len(lst) == 1:
        return [0]
    elif len(lst) > 1:
        return invert_lst


def invert(lst):
    return [-x for x in lst]


print(invert([1, -2, 3, -4, 5]))
print(invert([]))
print(invert([0]))


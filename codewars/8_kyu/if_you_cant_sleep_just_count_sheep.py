def count_sheep(n):
    """
    Given a non-negative integer,
    3 for example, return a string with a murmur:
    "1 sheep...2 sheep...3 sheep...".
    """
    string = ''
    for x in range(1, n + 1):
        string += f'{x} sheep...'
    return string


def count_sheep_community(n):
    """
    Given a non-negative integer,
    3 for example, return a string with a murmur:
    "1 sheep...2 sheep...3 sheep...".
    """
    return ''.join(f"{x} sheep..." for x in range(1, n + 1))


print(count_sheep(1))
print(count_sheep(2))
print(count_sheep(3))
print(count_sheep_community(1))
print(count_sheep_community(2))
print(count_sheep_community(3))

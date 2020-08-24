def find_average(lst: list) -> float:
    """Calculates average of numbers in given list."""
    return sum(lst) / len(lst)


def find_average_community_1(array: list) -> float:
    """Calculates average of numbers in given list."""
    return float(sum(array) / len(array)) if array else 0


def find_average_community_2(array: list) -> float:
    """Calculates average of numbers in given list."""
    try:
        return sum(array) / len(array)
    except ZeroDivisionError:
        return 0


print(find_average_community_1([5, 1, 3, 4, 5]))
print(find_average_community_1([0]))

print(find_average_community_2([5, 1, 3, 4, 5]))
print(find_average_community_2([0]))


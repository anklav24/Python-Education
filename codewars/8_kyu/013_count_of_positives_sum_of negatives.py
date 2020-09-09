def count_positives_sum_negatives(arr: list) -> list:
    """
    Return an array, where the first element is the count of positives numbers, and the second element is sum of
    negative numbers.
    """
    count_positives, sum_negatives = 0, 0

    for i in arr:
        if i > 0:
            count_positives += 1
        elif i < 0:
            sum_negatives += i

    if count_positives == 0 and sum_negatives == 0 and len(arr) == 0:
        return []
    else:
        return [count_positives, sum_negatives]


def count_positives_sum_negatives(arr: list) -> list:
    """
    Return an array, where the first element is the count of positives numbers, and the second element is sum of
    negative numbers.
    """
    pos = sum(1 for x in arr if x > 0)
    neg = sum(x for x in arr if x < 0)
    return [pos, neg] if len(arr) else []


print(count_positives_sum_negatives([1, 2, 3, 4, 0, 5, 6, 7, 8, 9, 10, -11, -12, -13, -14, -15]))
print(count_positives_sum_negatives([0, 0, 0, 0, 0]))
print(count_positives_sum_negatives([0, 0]))
print(count_positives_sum_negatives([]))

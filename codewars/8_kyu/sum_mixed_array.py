def sum_mix(arr: list) -> int:
    """Return the sum of the array values as if all were numbers."""
    sum = 0
    for x in arr:
        sum += int(x)
    return sum


def sum_mix_community_1(arr: list) -> int:
    """Return the sum of the array values as if all were numbers."""
    return sum(map(int, arr))


def sum_mix_community_2(arr: list) -> int:
    """Return the sum of the array values as if all were numbers."""
    return sum(int(n) for n in arr)


print(sum_mix([1, "2", 3, "4", 5]))
print(sum_mix_community_1([1, "2", 3, "4", 5]))
print(sum_mix_community_2([1, "2", 3, "4", 5]))

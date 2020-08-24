def sum_array_1(arr: list) -> int:
    """Sum without highest and lowest number"""
    if arr != None and len(arr) > 1:
        arr.remove(min(arr))
        arr.remove(max(arr))
        return sum(arr)
    else:
        return 0


def sum_array_2(arr: list) -> int:
    """Sum without highest and lowest number"""
    if arr and len(arr) > 1:
        return sum(arr) - min(arr) - max(arr)
    else:
        return 0


def sum_array_community_1(arr):
    if arr is None or len(arr) < 3:
        return 0
    return sum(arr) - max(arr) - min(arr)


def sum_array_community_2(arr):
    return sum(sorted(arr)[1:-1]) if arr and len(arr) > 1 else 0


print(sum_array_2(None))
print(sum_array_2([]))
print(sum_array_2([3]))
print(sum_array_2([3, 5]))
print(sum_array_2([1, 2, 3, 4, 5]))

arr = None
# arr = []
# arr = [1]
# arr = False
# arr = True
print(1 if arr else 0)

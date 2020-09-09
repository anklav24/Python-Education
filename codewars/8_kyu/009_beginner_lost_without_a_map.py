def maps(a):
    return [i * 2 for i in a]


print(maps([1, 2, 3]))


def maps_comm_1(a):
    return [x * 2 for x in a]


print(maps_comm_1([1, 2, 3]))


def maps_comm_2(a):
    return map(lambda x: x * 2, a)


print(maps_comm_2([1, 2, 3]))

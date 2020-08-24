def how_much_i_love_you_community_1(nb_petals: int) -> str:
    """Which phrase the girls would say for a flower of a given number of petals"""
    petal_list = ["I love you", "a little", "a lot", "passionately", "madly", "not at all"]
    return petal_list[nb_petals % 6 - 1]


def how_much_i_love_you_community_2(nb_petals: int) -> str:
    """Which phrase the girls would say for a flower of a given number of petals"""
    petal_list = ["I love you", "a little", "a lot", "passionately", "madly", "not at all"]
    return petal_list[nb_petals % 6 - 2]


nb_petals = 0
petal_list = ["I love you", "a little", "a lot", "passionately", "madly", "not at all"]
for nb_petals in range(1000):
    assert how_much_i_love_you_community_1(nb_petals) == petal_list[nb_petals % 6 - 1], \
        f'You receive: {nb_petals=}, {how_much_i_love_you_community_1(nb_petals)}' \
        f'. Should equal: {nb_petals=}, {petal_list[nb_petals % 6 - 1]}'

nb_petals = 0
petal_list = ["I love you", "a little", "a lot", "passionately", "madly", "not at all"]
for nb_petals in range(1000):
    assert how_much_i_love_you_community_2(nb_petals) == petal_list[nb_petals % 6 - 1], \
        f'You receive: {nb_petals=}, {how_much_i_love_you_community_2(nb_petals)}' \
        f'. Should equal: {nb_petals=}, {petal_list[nb_petals % 6 - 1]}'

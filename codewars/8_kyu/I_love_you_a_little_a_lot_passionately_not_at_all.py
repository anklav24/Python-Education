def how_much_i_love_you(nb_petals: int) -> str:
    """Which phrase the girls would say for a flower of a given number of petals"""
    petal_dict = {0: "I love you",
                  1: "I love you",
                  2: "a little",
                  3: "a lot",
                  4: "passionately",
                  5: "madly",
                  6: "not at all"
                  }
    return petal_dict[6 if nb_petals % 6 == 0 else nb_petals % 6]


assert how_much_i_love_you(7) == "I love you"
assert how_much_i_love_you(283) == "I love you"
assert how_much_i_love_you(3) == "a lot"
assert how_much_i_love_you(6) == "not at all"
assert how_much_i_love_you(454) == "passionately"


def how_much_i_love_you_community_1(nb_petals: int) -> str:
    """Which phrase the girls would say for a flower of a given number of petals"""
    petal_dict = {1: "I love you",
                  2: "a little",
                  3: "a lot",
                  4: "passionately",
                  5: "madly",
                  0: "not at all"
                  }
    return petal_dict[nb_petals % 6]


assert how_much_i_love_you_community_1(7) == "I love you"
assert how_much_i_love_you_community_1(283) == "I love you"
assert how_much_i_love_you_community_1(3) == "a lot"
assert how_much_i_love_you_community_1(6) == "not at all"
assert how_much_i_love_you_community_1(454) == "passionately"


def how_much_i_love_you_community_2(nb_petals: int) -> str:
    """Which phrase the girls would say for a flower of a given number of petals"""
    petal_list = ["I love you", "a little", "a lot", "passionately", "madly", "not at all"]
    return petal_list[nb_petals % 6 - 1]


for nb_petals in range(500):
    assert how_much_i_love_you_community_2(nb_petals) == \
           ["I love you", "a little", "a lot", "passionately", "madly", "not at all"][nb_petals % 6 - 1], \
           f'You receive "{how_much_i_love_you_community_2(nb_petals)}" should equal "{["I love you", "a little", "a lot", "passionately", "madly", "not at all"][nb_petals % 6 - 1]}"'

assert how_much_i_love_you_community_2(
    7) == "I love you", f"You receive '{how_much_i_love_you_community_2(7)}' should equal 'I love you'"
assert how_much_i_love_you_community_2(
    283) == "I love you", f"You receive '{how_much_i_love_you_community_2(283)}' should equal 'I love you'"
assert how_much_i_love_you_community_2(
    3) == "a lot", f"You receive '{how_much_i_love_you_community_2(3)}' should equal 'a lot'"
assert how_much_i_love_you_community_2(
    6) == "not at all", f"You receive '{how_much_i_love_you_community_2(6)}' should equal 'not at all'"
assert how_much_i_love_you_community_2(
    454) == "passionately", f"You receive '{how_much_i_love_you_community_2(454)}' should equal 'passionately'"

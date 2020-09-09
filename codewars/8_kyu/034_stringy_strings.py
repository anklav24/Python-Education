def stringy(size):
    string = ""
    if size % 2 == 0:
        return "10" * (int(size / 2))
    else:
        return str("10" * int(size / 2 + 1))[:-1]


def stringy_community(size):
    return "10" * (size // 2) + "1" * (size % 2)


def test_functions_stringy(name_of_test_func):
    assert name_of_test_func(2) == "10", f'{name_of_test_func}: {name_of_test_func(2)} should equal "10"'
    assert name_of_test_func(3) == "101", f'{name_of_test_func}: {name_of_test_func(3)} should equal "101"'
    assert name_of_test_func(4) == "1010", f'{name_of_test_func}: {name_of_test_func(4)} should equal "1010"'
    assert name_of_test_func(5) == "10101", f'{name_of_test_func}: {name_of_test_func(5)} should equal "10101"'

    assert name_of_test_func(10)[0] == '1', f'"Whoops your string doesnt start with a 1". You received {name_of_test_func(10)}'

    for i in range(1, 5):
        assert len(name_of_test_func(i)) == i, f"Make sure your string is the right length: {len(name_of_test_func(i))} should equal {i}."


test_functions_stringy(stringy)
test_functions_stringy(stringy_community)

# Let's see our results.
for i in range(6):
    print(f'{stringy(i)=}, {i=}')

for i in range(6):
    print(f'{stringy_community(i)=}, {i=}')

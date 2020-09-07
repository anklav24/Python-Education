def stringy(size):
    string = ""
    if size % 2 == 0:
        return "10" * (int(size / 2))
    else:
        return str("10" * int(size / 2 + 1))[:-1]


assert stringy(2) == "10", f'{stringy(2)} should equal "10"'
assert stringy(3) == "101", f'{stringy(3)} should equal "101"'
assert stringy(4) == "1010", f'{stringy(4)} should equal "1010"'
assert stringy(5) == "10101", f'{stringy(5)} should equal "10101"'

assert stringy(10)[0] == '1', f'"Whoops your string doesnt start with a 1". You received {stringy(10)}'

for i in range(1, 5):
    assert len(stringy(i)) == i, f"Make sure your string is the right length: {len(stringy(i))} should equal {i}."


def stringy_community(size):
    return "10" * (size // 2) + "1" * (size % 2)


assert stringy_community(2) == "10", f'{stringy_community(2)} should equal "10"'
assert stringy_community(3) == "101", f'{stringy_community(3)} should equal "101"'
assert stringy_community(4) == "1010", f'{stringy_community(4)} should equal "1010"'
assert stringy_community(5) == "10101", f'{stringy_community(5)} should equal "10101"'

assert stringy_community(10)[0] == '1', f'"Whoops your string doesnt start with a 1". You received {stringy_community(10)}'

for i in range(1, 5):
    assert len(stringy_community(i)) == i, f"Make sure your string is the right length: {len(stringy_community(i))} should equal {i}."

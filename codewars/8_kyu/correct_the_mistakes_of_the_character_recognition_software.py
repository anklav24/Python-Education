def correct(string: str) -> str:
    """It corrects the errors in the digitised text."""
    return string.replace("5", "S").replace("0", "O").replace("1", "I")


print(correct("L0ND0N"))
print(correct("DUBL1N"))
print(correct("51NGAP0RE"))
print(correct("BUDAPE5T"))


def correct_community(string: str) -> str:
    """It corrects the errors in the digitised text."""
    return string.translate(str.maketrans("501", "SOI"))


print(correct_community("L0ND0N"))
print(correct_community("DUBL1N"))
print(correct_community("51NGAP0RE"))
print(correct_community("BUDAPE5T"))

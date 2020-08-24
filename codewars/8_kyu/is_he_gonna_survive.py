def hero(bullets: int, dragons: int) -> int:
    """Is he gonna survive?"""
    return bullets >= dragons * 2


print(hero(2, 2))
print(hero(10, 5))

def abbrevName(name: str) -> str:
    """The function convert a name into initials."""
    first, last = name.upper().split()
    return f'{first[:1]}.{last[:1]}'


def abbrevName(name: str) -> str:
    """The function convert a name into initials"""

print(abbrevName('Lobanov Aleksander'))
print(abbrevName('Lobanov Aleksander'))
print(abbrevName('Lobanov Aleksander'.title()))

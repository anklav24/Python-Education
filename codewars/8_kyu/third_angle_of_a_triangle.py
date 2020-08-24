def other_angle(a: int, b: int) -> int:
    """Return the 3rd angle of a triangle."""
    return 180 - a - b


print(other_angle(30, 60))
print(other_angle(60, 60))
print(other_angle(43, 78))
print(other_angle(10, 20))


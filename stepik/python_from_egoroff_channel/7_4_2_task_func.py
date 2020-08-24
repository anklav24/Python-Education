MIN_DRIVING_AGE = 18


def allowed_driving(name: str, age: int) -> str:
    """It decides can you drive."""
    print(f"{name} может водить" if age >= MIN_DRIVING_AGE else f"{name} еще рано садиться за руль")


allowed_driving("Alex", 26)
allowed_driving("tim", 17)
allowed_driving("bob", 18)

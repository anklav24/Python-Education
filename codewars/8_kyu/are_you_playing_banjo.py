def areYouPlayingBanjo(name: str) -> str:
    """
    Answers the question "Are you playing banjo?"
    If your name starts with the letter "R" or lower case "r", you are playing banjo.
    """
    return f'{name} plays banjo' if name.lower()[0] == 'r' else f'{name} does not play banjo'


print(areYouPlayingBanjo('Rikke'))
print(areYouPlayingBanjo('Alex'))

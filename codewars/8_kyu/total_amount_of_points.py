def points(games: list) -> int:
    """Takes such collection adn counts the points of our team in the championship."""
    point = 0
    for x in range(len(games)):
        if int(games[x][0]) > int(games[x][-1]):
            point += 3
        elif int(games[x][0]) < int(games[x][-1]):
            point += 0
        elif int(games[x][0]) == int(games[x][-1]):
            point += 1
    return point


def points_community(games: list) -> int:
    """Takes such collection adn counts the points of our team in the championship."""
    count = 0
    for score in games:
        res = score.split(':')
        if res[0] > res[1]:
            count += 3
        elif res[0] == res[1]:
            count += 1
    return count


print(points(['1:0', '2:0', '3:0', '4:0', '2:1', '3:1', '4:1', '3:2', '4:2', '4:3']))
print(points_community(['1:0', '2:0', '3:0', '4:0', '2:1', '3:1', '4:1', '3:2', '4:2', '4:3']))

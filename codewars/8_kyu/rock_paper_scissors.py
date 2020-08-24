def rps(p1, p2):
    if p1 == p2:
        return 'Draw!'
    elif p1 == "scissors" and p2 == "paper":
        return "Player 1 won!"
    elif p1 == "paper" and p2 == "rock":
        return "Player 1 won!"
    elif p1 == "rock" and p2 == "scissors":
        return "Player 1 won!"
    else:
        return "Player 2 won!"


print(rps('rock', 'scissors'))
print(rps('scissors', 'rock'))
print()


def rps_community(p1, p2):
    beats = {'rock': 'scissors', 'scissors': 'paper', 'paper': 'rock'}
    if beats[p1] == p2:
        return 'Player 1 won!'
    if beats[p2] == p1:
        return 'Player 2 won!'
    return 'Draw!'


print(rps_community('rock', 'scissors'))
print(rps_community('scissors', 'rock'))
print(rps_community('paper', 'paper'))
print()


def rps_most_clever_community(p1, p2):
    hand = {'rock':0, 'paper':1, 'scissors':2}
    results = ['Draw!', 'Player 1 won!', 'Player 2 won!']
    return results[hand[p1] - hand[p2]]


print(rps_most_clever_community('rock', 'scissors'))
print(rps_most_clever_community('scissors', 'rock'))
print(rps_most_clever_community('paper', 'paper'))
print()

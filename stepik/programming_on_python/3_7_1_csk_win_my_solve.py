# https://stepik.org/lesson/3380/step/1?unit=963

# 3
# Зенит;3;Спартак;1
# Спартак;1;ЦСКА;1
# ЦСКА;0;Зенит;2
# n = 3
# [total_games, wins, draws, defeats, total_score]

n = int(input())
d = {}

for i in range(n):
    results = input().strip().split(';')

    if results[0] not in d:
        d[results[0]] = [0, 0, 0, 0, 0]
    if results[2] not in d:
        d[results[2]] = [0, 0, 0, 0, 0]

    if int(results[1]) > int(results[3]):
        d[results[0]][0] += 1  # total_games
        d[results[2]][0] += 1  # total_games
        d[results[0]][1] += 1  # win1
        d[results[2]][3] += 1  # defeats2
        d[results[0]][4] = int(d[results[0]][1]) * 3 + int(d[results[0]][2]) # total_score1
    elif int(results[1]) < int(results[3]):
        d[results[0]][0] += 1  # total_games
        d[results[2]][0] += 1  # total_games
        d[results[2]][1] += 1  # win2
        d[results[0]][3] += 1  # defeats1
        d[results[2]][4] = int(d[results[2]][1]) * 3 + int(d[results[2]][2]) # total_score2
    else:
        d[results[0]][0] += 1  # total_games
        d[results[2]][0] += 1  # total_games
        d[results[0]][2] += 1  # draws
        d[results[2]][2] += 1  # draws
        d[results[0]][4] = int(d[results[0]][2]) + int(d[results[0]][1]) * 3  # total_score1
        d[results[2]][4] = int(d[results[2]][2]) + int(d[results[2]][1]) * 3  # total_score2

for key, value in d.items():
    print(f'{key}:', *value)


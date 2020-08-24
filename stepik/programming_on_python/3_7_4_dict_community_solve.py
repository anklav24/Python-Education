lst = [input().split() for i in range(int(input()))]
destination = [[0], [0]]

for i in range(len(lst)):
    if lst[i][0] == 'север':
        destination[1][0] += int(lst[i][1])
    elif lst[i][0] == 'юг':
        destination[1][0] -= int(lst[i][1])
    elif lst[i][0] == 'запад':
        destination[0][0] -= int(lst[i][1])
    elif lst[i][0] == 'восток':
        destination[0][0] += int(lst[i][1])
    else:
        pass

for row in destination:
    print(' '.join([str(value) for value in row]), end=' ')


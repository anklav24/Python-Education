# https://stepik.org/lesson/3369/step/6?unit=952 объяснение преподавателя
# Игра сапер
# Вводные данные n = кол-во строк, m = столбцов, и k = количество мин
# также вводим позицию каждой мины
n, m, k = (int(i) for i in input().split())
a = [[0 for j in range(m)] for i in range(n)]  # Заполняем массив нулями
for i in range(k):
    # Вводим позиции мин в человеческом исчеслении и приводим с помощью -1 к отсчету от нуля в цикле
    # плюс записываем позиции мин в двумерный массив числом -1
    row, col = (int(i) - 1 for i in input().split())
    a[row][col] = -1

for i in range(n):
    for j in range(m):
        if a[i][j] != -1:  # Если текущая позиция не является позицией мины то проверяем массив вокруг нее.
            for di in range(-1, 2):
                for dj in range(-1, 2):
                    ai = i + di
                    aj = j + dj
                    if 0 <= ai < n and 0 <= aj < m and a[ai][aj] == -1:
                        a[i][j] += 1

for i in range(n):
    for j in range(m):
        if a[i][j] == -1:
            print('*', end='')
        elif a[i][j] == 0:
            print('0', end='')
        else:
            print(a[i][j], end='')
    print()

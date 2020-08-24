"""
Дополнительная
Выведите таблицу размером n×n, заполненную числами от 1 до n^2
  по спирали, выходящей из левого верхнего угла и закрученной по часовой стрелке, как показано в примере (здесь n=5n=5):

Sample Input:
5
Sample Output:
1 2 3 4 5
16 17 18 19 6
15 24 25 20 7
14 23 22 21 8
13 12 11 10 9

Тестируется через stdin → stdout
"""
n = 5
# n = int(input())
m = [[0 for j in range(n)] for i in range(n)]
count = 1
a = 0

for i in range(int(n / 2 + 1)):
    for j in range(a, n - a):
        # m[i][j] = count
        m[i][j] = "→"
        count += 1
    for i in range(a + 1, n - a):
        # m[i][j] = count
        m[i][j] = "↓"
        count += 1
    for j in range(-(2 + a), -(n + 1 - a), -1):
        # m[i][j] = count
        m[i][j] = "←"
        count += 1
    for i in range(-(2 + a), -(n - a), -1):
        # m[i][j] = count
        m[i][j] = "↑"
        count += 1
    a += 1

for i in range(n):
    print(*m[i])  # тут * значит распоковать значения массива

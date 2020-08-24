"""Напишите программу, на вход которой подаётся прямоугольная матрица в виде последовательности строк,
заканчивающихся строкой, содержащей только строку "end" (без кавычек) Программа должна вывести матрицу того же
размера, у которой каждый элемент в позиции i, j равен сумме элементов первой матрицы на позициях (i-1, j), (i+1, j),
(i, j-1), (i, j+1). У крайних символов соседний элемент находится с противоположной стороны матрицы. В случае одной
строки/столбца элемент сам себе является соседом по соответствующему направлению.

Sample Input 1:
9 5 3
0 7 -1
-5 2 9
end

Sample Output 1:
3 21 22
10 6 19
20 16 -1


Sample Input 2:
1
end

Sample Output 2:
4

Напишите программу. Тестируется через stdin → stdout"""
matrix = []
end = ''
while not end:
    matrix += [[i for i in input().split()]]
    if matrix[-1][-1] == 'end':
        end = True
        del matrix[-1]
        matrix = [[int(values) for values in lists] for lists in matrix]
new_matrix = [[0 for j in range(len(matrix[i]))] for i in range(len(matrix))]

for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        if i == len(matrix) - 1 and j == len(matrix[i]) - 1:
            new_matrix[i][j] = matrix[i-1][j] + matrix[i][-len(matrix[i])] + matrix[-len(matrix)][j] + matrix[i][j - 1]
        elif j == len(matrix[i]) - 1:
            new_matrix[i][j] = matrix[i-1][j] + matrix[i][-len(matrix[i])] + matrix[i+1][j] + matrix[i][j-1]
        elif i == len(matrix) - 1:
            new_matrix[i][j] = matrix[i-1][j] + matrix[i][j+1] + matrix[-len(matrix)][j] + matrix[i][j-1]
        else:
            new_matrix[i][j] = matrix[i-1][j] + matrix[i][j+1] + matrix[i+1][j] + matrix[i][j-1]

for i in range(len(new_matrix)):
    for j in range(len(new_matrix[i])):
        print(new_matrix[i][j], end=' ')
    print()

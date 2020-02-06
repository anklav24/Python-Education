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
# matrix = []
# end = ''
# while not end:
#     matrix += [[i for i in input().split()]]
#     if matrix[-1][-1] == 'end':
#         end = True
#         del matrix[-1]
#         matrix = [[int(values) for values in lists] for lists in matrix]
# print(matrix)
matrix = [[9, 5, 3], [0, 7, -1], [-5, 2, 9]]
print(matrix)

new_matrix = []
for i in range(len(matrix)):
    for j in matrix[i]:
        for di in range(-1, 2):
            for dj in range(-1, 2):
                ai = i + di
                aj = j + dj
                if 0 <= ai < len(matrix) and 0 <= aj < len(matrix[i]):
                    new_matrix[i][j] += 1

for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        print(new_matrix[i][j], end='')

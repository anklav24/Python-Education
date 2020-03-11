import os

dataset = os.path.join('C:\\', 'Users', 'Admin', 'Downloads', 'dataset_3363_4 ' + '(7)' + '.txt')
print(dataset)
answer = os.path.join('C:\\', 'Users', 'Admin', 'Downloads', 'answer.txt')
print(answer)
first_sum, second_sum, third_sum, count = 0, 0, 0, 0

with open(dataset) as inf, open(answer, 'w') as ouf:
    for string in inf:
        student = string.strip().split(sep=';')
        average = (int(student[1]) + int(student[2]) + int(student[3]))/3
        ouf.write(str(round(average, 9)) + '\n')
        first_sum += int(student[1])
        second_sum += int(student[2])
        third_sum += int(student[3])
        count += 1

with open(answer, 'a') as ouf:
    ouf.write(str(round(first_sum / count, 9)) + ' ' + str(round(second_sum / count, 9)) + ' ' + str(round(third_sum / count, 9)) + '\n')
    ouf.write(f'Count: {count}\n')  # Запись в файл с помощью f строк.
    ouf.write(f'{first_sum / count}\n')
    ouf.write('{}, {}\n'.format(first_sum / count, count))
    ouf.write('test')

with open(answer) as inf:
    for string in inf:
        print(string.strip())

# Делаем словарь {1:[0,0], 2:[0,0]... 11:[0,0]}, где [0:0] = [сумма ростов : кол-во учеников]
tab = {i: [0, 0] for i in range(1, 12)}

with open('dataset_3380_5.txt') as inf:
    # Заполняем словарь:
    for i in inf:
        line = i.strip().split('\t')
        tab[int(line[0])][0] += int(line[2])  # tab[класс][0] += рост ученика
        tab[int(line[0])][1] += 1  # tab[класс][1] += 1 (счетчик учеников в классе)

    # Распечатка:
    for i in tab.keys():
        if tab[i][1] == 0:
            print(i, '-')  # распечатываем класс, в котором нет учеников
        else:
            # считаем и распечатываем средний рост для i-го класса:
            print(i, (tab[i][0] / tab[i][1]))

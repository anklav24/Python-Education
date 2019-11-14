import time

try:
    f = open('poem.txt')
    while True:  # Наш обычный способ читать файлы.
        line = f.readline()
        if len(line) == 0:
            break
        print(line, end='')
        time.sleep(2)  # Пусть подождёт некоторое время.
except KeyboardInterrupt:
    print('!! You canceled reading a file.')
finally:
    f.close()
    print('(Cleaning: Closing a file)')

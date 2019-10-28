# https://www.youtube.com/watch?v=fp5-XQFr_nk
print("Простой калькулятор\n\"ver. 0.2\"")

# Подключаем пакет Colorama
from colorama import init
from colorama import Fore, Back, Style
# Use Colorama to make Termcolor work on Windows too
init()

print(Fore.BLACK)
# Выбираем цвет фона и возможные математические действия
print(Back.CYAN)
what=input("Что делаем? (+,-): ")

# Выбираем цвет фона и просим ввести пользователя первое число
print(Back.YELLOW)
a=float(input("Введи первое число: "))

# Выбираем цвет фона и просим ввести пользователя второе число
print(Back.MAGENTA)
b=float(input("Введи второе число: "))

if what == "+":
    c=a+b
    print(Back.GREEN)
    print("Результат: " + str(c))
elif what == "-":
    c=a-b
    print(Back.GREEN)
    print("Результат: " + str(c))
else:
    print(Back.RED)
    print("Выбрана неверная операция!")
input()
# После можно скомпилить в .exe при помощи запуска в CMD из папки проекта пакета pyinstaller
# Устанавливаем pyinstaller введя в CMD "pip install pyinstaller"
# Переходим в папку проекта "cd путькпапкеспроектом"
# Выполняем "pyinstaller -F имяфайла.py"
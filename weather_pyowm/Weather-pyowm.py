# https://github.com/csparpa/pyowm
# Импортируем пакет с помощью которого мы узнаем погоду
import pyowm
# Регистрируемся на их сайте получаем ключ API
owm = pyowm.OWM('Your Token', language='ru')

# Бесконеный цикл (пока 1 не равно 1)
while True:
    # Вложенный цикл для того что при вводе неправильного города программа не вылетала
    while True:
        # Просим ввести пользователя свой город
        question = input("Хотите узнать погоду в каком нибудь городе? (Да/Нет): ")
        if question == 'Да':
            place = input("Введи название города: ")
        elif question == 'да':
            place = input("Введи название города: ")
        else:
            print("Всего доброго!")
            print()
            break
        # С помощью try заставляю пройти код, если выводит ошибку то происходит переход к except
        try:
            # Search for current weather in London (Great Britain)
            observation = owm.weather_at_place(place)
            w = observation.get_weather()

            # Присваиваем переменной значение температуры из таблицы
            temp = w.get_temperature('celsius')["temp"]

            # Выводим полученные данные на экран
            print("В городе " + place + " сейчас " + w.get_detailed_status() + ".")
            print("Температура " + str(temp) + " градусов цельсия."),
            if temp < 10:
                print("Пи**ц как холодно, одевайся как танк!")
            elif temp < 20:
                print("Холодно, одевайся теплее.")
            elif temp > 25:
                print("Жарень.")
            else:
                print("На улице вроде норм.")
            print()
        except:
            print("Не найден город, попробуйте ввести название снова.")
            print()



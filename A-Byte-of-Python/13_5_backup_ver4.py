import os
import time

# 1. Файлы и каталоги, которые необходимо скопировать, собираются в список.
source = ['C:\\test01', '"C:\\test 02']
# Заметьте, что для имён, содержащих пробелы, необходимо использовать
# двойные кавычки внутри строки.

# 2. Резервные копии должны храниться в основном каталоге резерва.
target_dir = 'C:\\Backup'  # Подставьте тот путь, который вы будете использовать.

# 3. Файлы помещаются в zip-архив.
# 4. Текущая дата служит именем подкаталога в основном каталоге.
today = target_dir + os.sep + time.strftime('%Y%m%d')
now = time.strftime('%Y%m%d-%H%M%S')

# Запрашиваем комментарий пользователя для имени файла
comment = input('Введите комментарий --> ')
if len(comment) == 0:  # проверяем, введён ли комментарий
    target = today + os.sep + now + '.zip'
else:
    target = today + os.sep + now + '_' + comment.replace(' ', '_') + '.zip'

# Создаем каталог, если его еще нет.
if not os.path.exists(target_dir):
    os.mkdir(target_dir)
    print('Create a directory: {}'.format(target_dir))
if not os.path.exists(today):
    os.mkdir(today)  # Создание каталога
    print('Create a directory: {}'.format(today))

# 5. Используем команду "zip" для помещения файлов в zip-архив.
zip_command = "zip -qr {} {}".format(target, ' '.join(source))

# Запускаем создание резервной копии.
if os.system(zip_command) == 0:
    print('Резервная копия успешно создана в', target)
else:
    print('Создание резервной копии не удалось')

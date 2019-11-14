import pickle


# Имя файла, в котором мы сохраним объект.
shoplistfile = 'shoplist.data'
# Список покупок
shoplist = ['apples', 'mangoes', 'carrots']

# Write in a file.
f = open(shoplistfile, 'wb')
pickle.dump(shoplist, f)  # Помещаем объект в файл.
f.close()

del shoplist  # Уничтожаем переменную shoplist

# Считываем из хранилища.
f = open(shoplistfile, 'rb')
storedlist = pickle.load(f)  # Загружаем объект из файла
print(storedlist)

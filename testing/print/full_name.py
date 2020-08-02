def full_name(first, last, middle=''):
    """Отдает полное имя пользователя"""
    if middle:
        full = f"{first} {last} {middle}"
    else:
        full = f"{first} {last}"
    return full.title()


print(full_name("Alex", "Nofam"))

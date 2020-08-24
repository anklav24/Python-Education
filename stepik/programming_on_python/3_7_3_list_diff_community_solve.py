"""
мой вариант решения: 1) заполняем словарь; 2) преобразуем текст в множество слов; 3) печатаем разность двух множеств
Sample Input:

4
champions
we
are
Stepik
3
We are the champignons
We Are The Champions
Stepic
Sample Output:

stepic
champignons
the
"""

words = set(input().lower() for i in range(int(input())))
text = set(('\n'.join(input().lower() for i in range(int(input())))).split())
print('\n'.join(text - words))


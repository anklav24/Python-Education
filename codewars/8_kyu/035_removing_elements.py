def remove_every_other(my_list: list) -> list:
    """
    Take an array and remove every second element from the array.
    Always keep the first element and start removing with the next element.
    """
    new_list = []
    for i in range(len(my_list)):
        if i % 2 == 0:
            new_list.append(my_list[i])
    return new_list


def test_remove_every_other(name_of_test_func):
    assert name_of_test_func(['Hello', 'Goodbye', 'Hello Again']) == ['Hello', 'Hello Again'], f"{name_of_test_func}: {['Hello', 'Goodbye', 'Hello Again']} should equal '['Hello', 'Hello Again']'"
    assert name_of_test_func([['Goodbye'], {'Great': 'Job'}]) == [['Goodbye']]
    assert name_of_test_func([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]) == [1, 3, 5, 7, 9, 11, 13, 15]


print(remove_every_other([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]))
print(remove_every_other([['No'], {8: 'Yes'}, 0, ['Hello'], [False], False, 'Hello', {True: 32}, [True], {9: 5}, 44, ['Hello'], [False], 43, {56.0: 'No'}, [75.25]]))
print(remove_every_other(['Hello', 'Goodbye', 'Hello Again']))
print(remove_every_other([['Goodbye'], {'Great': 'Job'}]))
print(remove_every_other([[1, 2]]))
test_remove_every_other(remove_every_other)


# BEST PRACTICE SOLVED SO EASY. Oh, gosh! I spent over two days on this task.


def remove_every_other(my_list: list) -> list:
    return my_list[::2]


print(remove_every_other([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]))
print(remove_every_other([['No'], {8: 'Yes'}, 0, ['Hello'], [False], False, 'Hello', {True: 32}, [True], {9: 5}, 44, ['Hello'], [False], 43, {56.0: 'No'}, [75.25]]))
print(remove_every_other(['Hello', 'Goodbye', 'Hello Again']))
print(remove_every_other([['Goodbye'], {'Great': 'Job'}]))
print(remove_every_other([[1, 2]]))
test_remove_every_other(remove_every_other)

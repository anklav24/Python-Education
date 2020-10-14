# It doesn't work.
# It isn't working.

def remove_every_other(my_list: list) -> list:
    """
    Take an array and remove every second element from the array.
    Always keep the first element and start removing with the next element.
    """
    for element in my_list:
        print(my_list.index(element))
        if my_list[:].index(element) % 2 != 0:
            my_list.remove(element)
    return my_list


def test_remove_every_other(name_of_test_func):
    assert name_of_test_func(['Hello', 'Goodbye', 'Hello Again']) == ['Hello', 'Hello Again'], f"{name_of_test_func}: {['Hello', 'Goodbye', 'Hello Again']} should equal '['Hello', 'Hello Again']'"
    assert name_of_test_func(['Yes', 'Yes', 'No', 'Yes', 'No']) == ['Yes', 'Yes', 'Yes']


print(remove_every_other(['Hello', 'Goodbye', 'Hello Again']))
test_remove_every_other(remove_every_other)

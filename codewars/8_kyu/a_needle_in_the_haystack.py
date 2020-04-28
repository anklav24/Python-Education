def find_needle_my(haystack):
    for i in range(len(haystack)):
        if haystack[i] == 'needle':
            return f"found the needle at position {i}"

def find_needle_community(haystack):
    return f'found the needle at position {haystack.index("needle")}'

print(find_needle_my(['3', '123124234', None, 'needle', 'world', 'hay', 2, '3', True, False]))
print(find_needle_community(['3', '123124234', None, 'needle', 'world', 'hay', 2, '3', True, False]))

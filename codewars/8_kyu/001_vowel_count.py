def getCount(inputStr):
    vowels, num_vowels = ['a', 'e', 'i', 'o', 'u'], 0
    for i in vowels:
        num_vowels += inputStr.count(i)
    return num_vowels


print(getCount('abracadabra'))



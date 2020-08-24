"""
abcd
*d%#
abacabadaba
#*%*d*%
"""
# alphabet = 'abcd'
# key = '*d%#'
# origin_text = 'abacabadaba'
# ciphertext = '#*%*d*%'

alphabet = input()
key = input()
origin_text = input()
ciphertext = input()

for letter in origin_text:
    for j in range(len(alphabet)):
        if letter == alphabet[j]:
            cipher_letter = key[j]
            print(cipher_letter, end='')
        elif letter not in alphabet:
            print(letter, end='')
print()

for letter in ciphertext:
    for j in range(len(key)):
        if letter == key[j]:
            origin_letter = alphabet[j]
            print(origin_letter, end='')
        elif letter not in ciphertext:
            print(letter, end='')

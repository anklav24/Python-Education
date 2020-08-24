# crypted_string = input()
# crypted_string = 'a3b3c2'
crypted_string = 'E14e6L10F10E3F4W3Y18S10M2O13g18B5y17s16o9Z8o12L19r8o12q20s20C12u4x19S20n1d13O20w5V8x16k20i11y18r19a13x14L9q12A18D7J3M4g3B17G16'
alphabet = 'qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'
numbers = '1234567890'
prev_letter = ''

for i in range(len(crypted_string)):
    if crypted_string[i] in numbers and crypted_string[i + 1 - len(crypted_string)] in numbers:
        print(crypted_string[i - 1] * int(crypted_string[i] + crypted_string[i + 1]), end='')
    elif crypted_string[i] in alphabet and crypted_string[i + 1 - len(crypted_string)] in alphabet:
        print(crypted_string[i], end='')
    elif crypted_string[i] in alphabet and crypted_string[i + 1 - len(crypted_string)] in numbers and crypted_string[i + 2 - len(crypted_string)] not in numbers:
        print(crypted_string[i] * int(crypted_string[i + 1]), end='')

def modify_list(l):
    i = 0
    while i < len(l):
        if l[i] % 2 == 0:
            l[i] //= 2
            i += 1
        elif l[i] % 2 != 0:
            del l[i]

lst = [2, 2, 4, 4, 5, 6]

print(modify_list(lst))
print(lst)
print()

lst = [1, 2, 3, 4, 5, 6]

print(modify_list(lst))
print(lst)
print()

print(modify_list(lst))
print(lst)
print()

lst = [10, 5, 8, 3]
print(modify_list(lst))
print(lst)
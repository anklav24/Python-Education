def modify_list(l):
    l[:] = [i//2 for i in l if not i % 2]


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
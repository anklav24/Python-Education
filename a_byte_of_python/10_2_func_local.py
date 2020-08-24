x = 50


# shadows name from outer scope
def func(x):
    print('x equals', x)
    x = 2
    print('Change local x to', x)


func(x)
print('x по прежнему', x)
print()

x = input('Input x = ')
func(x)
print('Now x equals', x)

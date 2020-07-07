x = 50


# shadows name from outer scope
def func():
    global x
    print('x equals', x)
    x = 2
    print('Change global value x to', x)


func()
print('x equals ', x)

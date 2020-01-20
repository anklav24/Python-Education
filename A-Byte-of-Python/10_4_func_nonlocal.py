def func_outer():
    x = 2
    print('x equals', x)

    def func_inner():
        # Select one from three count and see for result
        # nonlocal x
        # global x
        #
        x = 5

    func_inner()

    print('Local x changed to', x)


func_outer()

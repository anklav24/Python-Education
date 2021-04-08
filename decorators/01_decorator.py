def start_stop(func):
    def wrapper():
        print("||||||START||||||")
        func()
        print("||||||STOP||||||")

    return wrapper()


@start_stop
def foo():
    print("Hello, world!")


foo()

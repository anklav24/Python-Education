def rec(x):
    print(x)
    rec(x + 1)


if __name__ == "__main__":
    rec(1)

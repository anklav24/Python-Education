import sys


def foo():
    if len(sys.argv) < 2:
        print("Missing command-line argument.")
        sys.exit(1)
    else:
        print(f"Hello, {sys.argv[1]}")


foo()

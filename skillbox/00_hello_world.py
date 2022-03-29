def main() -> object:
    return "Hello, world!"


if __name__ == '__main__':
    for i in range(3):
        assert "Hello, world!" == main()
        print(main())

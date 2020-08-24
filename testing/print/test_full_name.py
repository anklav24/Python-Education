from testing.full_name import full_name

print("Quit 'Q'")

while True:
    first = input("\nInput your name: ")
    if first == "Q":
        break

    last = input("\nInput your last name: ")
    if last == "Q":
        break

    format_name = full_name(first, last)
    print("\tformating the name: " + format_name)

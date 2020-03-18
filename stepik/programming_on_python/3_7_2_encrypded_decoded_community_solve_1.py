source, dest = input(), input()
decoded = input()
encoded = input()

print(decoded.translate(str.maketrans(source, dest)))
print(encoded.translate(str.maketrans(dest, source)))
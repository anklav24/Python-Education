string = input().lower().split()
for word in set(string):
    print(word, string.count(word))

st = ""
while True:
    i = int(input())
    if i < 10:
        continue
    elif i > 100:
        break
    else:
        st += str(i) + "\n"
print(st)

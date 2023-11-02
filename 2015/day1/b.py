floor = 0

f = open('input.txt', 'r')
lines = f.read()
f.close()
for index, n in enumerate(lines, start=1):
    if n == "(":
        floor += 1
        if floor == -1:
            print(index, n)
            break
    else:
        floor -= 1
        if floor == -1:
            print(index, n)
print(floor)
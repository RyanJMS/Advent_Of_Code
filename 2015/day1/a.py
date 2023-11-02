floor = 0

f = open('input.txt', 'r')
lines = f.read()
f.close()
for n in lines:
    if n == "(":
        floor += 1
    else:
        floor -= 1
print(floor)
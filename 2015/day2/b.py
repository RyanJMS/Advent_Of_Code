import math

present = "2x3x4"
d = present.split("x")
l = int(d[0])
w = int(d[1])
h = int(d[2])
sq = (2*l*w) + (2*w*h) + (2*h*l)

f = open('input.txt', 'r')
lines = f.read()
f.close()

sep = lines.split("\n")

def calc_w_p(dimensions):
    total_paper = 0
    for dim in dimensions:
        parts = dim.split('x')
        if len(parts) != 3:
            continue  # Skip invalid dimension
        try:
            l, w, h = map(int, parts)
        except ValueError:
            continue  # Skip invalid dimension
        surface_area = 2*l*w + 2*w*h + 2*h*l
        slack = min(l*w, w*h, h*l)
        total_paper += surface_area + slack
    return total_paper

def calc_ribbon(dimensions):
    total_ribbon = 0
    for dim in dimensions:
        parts = dim.split('x')
        if len(parts) != 3:
            continue  # Skip invalid dimension
        parts_map = map(int, parts)
        parts_sorted = sorted(parts_map)
        print(parts_sorted)
        try:
            l, w, h = map(int, sorted(parts_sorted))
        except ValueError:
            continue  # Skip invalid dimension
        total_ribbon += (l + l + w + w) + (l * w * h)
        print(total_ribbon)
    return total_ribbon


ribbon = calc_ribbon(sep)
print(ribbon)

test = calc_ribbon("2x3x4")
print(test)


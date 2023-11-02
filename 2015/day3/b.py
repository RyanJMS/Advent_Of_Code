import numpy as np
from collections import Counter
f = open('input.txt')
puzzle = f.read()
f.close()

def calc_houses(input):
    visited_houses = set()
    sx, sy = 0,0
    rx, ry = 0,0
    visited_houses.add((sx, sy))

    is_santa_turn = True
    for i in input:
        if is_santa_turn:
            if i == "<":
                sx -= 1
            if i == ">":
                sx += 1
            if i == "^":
                sy += 1
            if i == "v":
                sy -= 1
            visited_houses.add((sx, sy))
        else:
            if i == "<":
                rx -= 1
            if i == ">":
                rx += 1
            if i == "^":
                ry += 1
            if i == "v":
                ry -= 1
            visited_houses.add((rx, ry))
        is_santa_turn = not is_santa_turn

    print(len(visited_houses))
    
        
calc_houses(puzzle)